#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


using VI = vector<int>;
using VVI = vector<VI>;
using VS = vector<string>;


// Using latex.
void convert_to_pdf(VVI horario, VS asigs) {
  int n = horario.size();
  
  ofstream fileOut;
  fileOut.open("horario.tex", ofstream::out);
  fileOut << "\\documentclass{article}\n\n\\usepackage[landscape]{geometry}\n\n\n\\begin{document}\n\n\t\\begin{center}\n\t\t\\begin{tabular}{|c|c|c|c|c|}\n";
  fileOut << "\t\t\t\\hline\n\t\t\t\\textbf{LUNES}\t&\t\\textbf{MARTES}\t&\t\\textbf{MIERCOLES}\t&\t\\textbf{JUEVES}\t&\t\\textbf{VIERNES}\t\\\\\n";
  for (int i = 0; i < n; ++i) {
    fileOut << "\t\t\t" << "\\hline" << endl;
    for (int j = 0; j < 5; ++j) {
      fileOut << "\t\t\t" << (j ? "& \t" : "");
      if (horario[i][j] >= 0) fileOut << asigs[horario[i][j]];
      if (horario[i][j] == -1) fileOut << -1;
      fileOut << '\t';
      if (j == 4) fileOut << "\\\\" << endl;
    }
  }
  fileOut << "\t\t\t" << "\\hline" << endl;
  
  fileOut << "\t\t\\end{tabular}\n\t\\end{center}\n\n\\end{document}" << endl;

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


VI update_finde(VI& horas) {
  int n = horas.size();
  VI finde(n, 0);
  
  int ht = 0;
  for (int i = 0; i < n; ++i) ht += horas[i];
  int hf = (ht*2)/7;

  if (hf%2 == 1) {
    --hf;
    --horas[n - 1];
    ++finde[n - 1];
  }
  int i = n - 1;
  while (hf > 0) {
    hf -= 2;
    horas[i] -= 2;
    finde[i] += 2;
    --i;
  }

  return finde;
}


bool put(int asig, int day, VVI& horario) {
  for (int i = 0; i < int(horario.size()) - 1; ++i)
    if (horario[i][day] == -2 and horario[i + 1][day] == -2) {
      horario[i][day] = horario[i + 1][day] = asig;
      return true;
    }
  return false;
}


void distribute(VI& horas, VVI& horario) {
  // Secuencia: Lunes, Miércoles, Viernes, Martes, Jueves.
  VI sec = {0, 2, 4, 1, 3};
  
  int n = horas.size();
  int j = 0;  
  for (int asig = 0; asig < n; ++asig) {
    int exit = 0;
    while (horas[asig] > 1 and exit < 5) {
      if (j > 4) j = 0;
      if (put(asig, sec[j], horario)) horas[asig] -= 2;
      else ++exit;
      ++j;
    }
  }
}


int main() {
  // Input
  VI horas = {3, 5, 4, 5, 4, 4, 2};
  VS asigs = {"DINAMICA", "ANALISIS REAL", "MECANICA", "TOPOLOGIA", "ECONOMIA", "ELECTROMAGNETISMO", "PROYECTO"};
  VVI horario = {
    {-1, -2, -2, -2, -2},
    {-2, -2, -1, -2, -2},
    {-2, -2, -1, -2, -2},
    {-2, -2, -2, -2, -2},
    {-2, -1, -2, -2, -1},
    {-2, -2, -2, -1, -1}
  };
  
  // cout << endl << "INPUT INICIAL" << endl;
  // cout << "horas: ";
  // print(horas);
  // cout << "asigs: ";
  // print(asigs);
  
  sort(horas, asigs);
  VI finde = update_finde(horas);
  
  // cout << endl << "ESTADO INTERMEDIO" << endl;
  // cout << "horas: ";
  // print(horas);
  // cout << "finde: ";
  // print(finde);
  // cout << "asigs: ";
  // print(asigs);

  // sort(horas, asigs);
  distribute(horas, horario);
  
  // cout << endl << "ESTADO FINAL" << endl;
  // cout << "horas: ";
  // print(horas);
  // cout << "finde: ";
  // print(finde);
  // cout << "asigs: ";
  // print(asigs);
  
  // convert_to_pdf(horario, asigs);
}
