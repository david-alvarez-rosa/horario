#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


using VI = vector<int>;
using VVI = vector<VI>;
using VS = vector<string>;


// Using latex.
void convert_to_pdf(VVI horario, VS asigs, VI finde) {
  int n = horario.size();
  
  ofstream fileOut;
  fileOut.open("horario.tex", ofstream::out);
  fileOut << "\\documentclass{article}\n\n\\usepackage[landscape]{geometry}\n\n\n\\begin{document}\n\n\t\\begin{center}\n\t\t\\begin{tabular}{|c|c|c|c|c|}\n";
  fileOut << "\t\t\t\\hline\n\t\t\t\\textbf{LUNES}\t&\t\\textbf{MARTES}\t&\t\\textbf{MIERCOLES}\t&\t\\textbf{JUEVES}\t&\t\\textbf{VIERNES}\t\\\\\n";
  for (int i = 0; i < n; ++i) {
    fileOut << "\t\t\t" << "\\hline" << endl;
    for (int j = 0; j < 5; ++j) {
      fileOut << "\t\t\t" << (j ? "&\t" : "");
      if (horario[i][j] >= 0) fileOut << asigs[horario[i][j]];
      if (horario[i][j] == -1) fileOut << -1;
      fileOut << '\t';
      if (j == 4) fileOut << "\\\\" << endl; 
    }
  }
  fileOut << "\t\t\t" << "\\hline" << endl;
  fileOut << "\t\t\\end{tabular}\n\t\\end{center}\n\n" << endl;

  fileOut << "\t\\vspace{2cm}\n\t\\textbf{Fin de semana:}\n\n\t\\begin{center}\n\t\t\\begin{tabular}{|c|c|}\n";
  fileOut << "\t\t\t\\hline\n\t\t\t\\textbf{ASIGNATURA}\t&\t\\textbf{HORAS}\\\\\n";
  int m = asigs.size();
  for (int i = 0; i < m; ++i)
    if (finde[i] != 0) {
      fileOut << "\t\t\t" << "\\hline" << endl;      
      fileOut << "\t\t\t" << asigs[i] << "\t&\t" << finde[i] << "\\\\" << endl; 
    }
  fileOut << "\t\t\t" << "\\hline" << endl;
  fileOut << "\t\t\\end{tabular}\n\t\\end{center}\n\n\\end{document}";
  
  system("pdflatex horario.tex && okular horario.pdf &");
}


void print(VI v) {
  int n = v.size();
  for (int i = 0; i < n; ++i) cout << v[i] << '\t';
  cout << endl;
}


void print(VS v) {
  int n = v.size();
  for (int i = 0; i < n; ++i) cout << v[i] << '\t';
  cout << endl;
}


void swap(int& a, int& b) {
  int c = a;
  a = b;
  b = c;
}


void swap(string& a, string& b) {
  string c = a;
  a = b;
  b = c;
}


// Comparison function for selection sort.
bool comp(int a, int b) {
  if (a%2 == 0) {
    if (b%2 == 0) return a <= b;
    else return true;
  }
  else {
    if (b%2 == 0) return false;
    return a < b;
  }
}


// Selection sort.
void sort(VI& v, VS& w) {
  int n = v.size();
  for (int i = 0; i < n; ++i) {
    int min = v[i];
    int posMin = i;
    for (int j = i + 1; j < n; ++j)
      if (comp(v[j], min)) {
	min = v[j];
	posMin = j;
      }
    swap(v[i], v[posMin]);
    swap(w[i], w[posMin]);
  }
}


// Primera asignación de horas al fin de semana.
VI update_finde(VI& horas) {
  int n = horas.size();
  VI finde(n, 0);
  
  int ht = 0;
  for (int i = 0; i < n; ++i) ht += horas[i];
  int hf = (ht*2)/7;

  if (hf%2 != 0) --hf;
    
  int i = n - 1;
  while (hf > 0) {
    hf -= 2;
    horas[i] -= 2;
    finde[i] += 2;
    --i;
  }

  return finde;
}


// Añadir 1 horas de estudio de asig en day.
bool put1(int asig, int day, VVI& horario) {
  for (int i = 0; i < int(horario.size()); ++i)
    if (horario[i][day] == -2) {
      horario[i][day] = asig;
      return true;
    }
  return false;
}


// Añadir 2 horas de estudio de asig en day.
bool put2(int asig, int day, VVI& horario) {
  for (int i = 0; i < int(horario.size()) - 1; ++i)
    if (horario[i][day] == -2 and horario[i + 1][day] == -2) {
      horario[i][day] = horario[i + 1][day] = asig;
      return true;
    }
  return false;
}


// Retorna verdadero si un día está completo.
int complete(VVI horario, int day) {
  int n = horario.size();
  for (int i = 0; i < n; ++i)
    if (horario[i][day] == -2) return false;
  return true;
}


// Devuelve el día con menos horas de estudio no completo.
int next_minimum_uncomplete(VVI horario, VI hras_est_dia) {
  int minDay = -1;
  for (int day = 0; day < 5; ++day)
    if (not complete(horario, day) and (minDay == -1 or hras_est_dia[day] < hras_est_dia[minDay]))
      minDay = day;

  return minDay;
}


void distribute(VI& horas, VVI& horario, VI& finde) {
  VI hras_est_dia(5, 0);
  int n = horas.size(); // Número de asignaturas.
  
  // En grupos de 2 horas.
  // Secuencia: Lunes, Miércoles, Viernes, Martes, Jueves.
  VI sec = {0, 2, 4, 1, 3};
  int j = 0;  // Iterador para la secuencia de días.  
  for (int asig = 0; asig < n; ++asig) {
    int exit = 0;
    while (horas[asig] > 1 and exit < 5) {
      if (j > 4) j = 0;
      if (put2(asig, sec[j], horario)) {
	horas[asig] -= 2;
	hras_est_dia[sec[j]] += 2;
      }
      else ++exit;
      ++j;
    }
  }

  // Para que no se quede una asignatura con más de 4 horas para el fin de semana.
  for (int asig = 0; asig < n; ++asig) {
    while (horas[asig] + finde[asig] > 4) {
      int day = next_minimum_uncomplete(horario, hras_est_dia);
      if (put1(asig, day, horario)) {
	--horas[asig];
	++hras_est_dia[day];
      }
    }
  }
  
  // De 1 hora en 1 hora. Comenzando por los días con menos horas de estudio y sin importar orden de asignaturas.
  for (int asig = 0; asig < n; ++asig) {
    bool finished = false;
    while (horas[asig] > 0 and not finished) {
      int day = next_minimum_uncomplete(horario, hras_est_dia);
      if (day == -1) finished = true;
      else if (put1(asig, day, horario)) {
	--horas[asig];
	++hras_est_dia[day];
      }
    }
  }

  // Guardando las horas no asignadas en vector fin de semana.
  for (int i = 0; i < n; ++i) {
    finde[i] += horas[i];
    horas[i] = 0;
  }
}


VI distribute_main(VI& horas, VS& asigs, VVI& horario) {
  sort(horas, asigs);
  VI finde = update_finde(horas);
  sort(horas, asigs);
  distribute(horas, horario, finde);
  
  return finde;
}


int main() {
  // Input
  VI horas = {3, 5, 4, 5, 4, 4, 2};
  VS asigs = {"DINAMICA", "ANALISIS REAL", "MECANICA", "TOPOLOGIA", "ECONOMIA", "ELECTROMAGNETISMO", "PROYECTO"};
  VVI horario = {
    {-1, -2, -2, -2, -2},
    {-2, -2, -1, -2, -2},
    {-2, -1, -1, -2, -2},
    {-1, -1, -2, -2, -2},
    {-1, -1, -2, -2, -1},
    {-1, -2, -2, -1, -1}
  };

  // Programa
  VI finde = distribute_main(horas, asigs, horario);

  // Output en pdf
  convert_to_pdf(horario, asigs, finde);
}
