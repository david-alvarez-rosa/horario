import codificador as cd
import predictor as pr
import horas as hr
import generador as gn
import pandas as pd


# Imprimir por pantalla bien una matriz (de Stack Overflow).
def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))


# Lectura del input.
# Abrir fichero.
input_file = open('input_file.txt', 'r')

# Leer todas las líneas del fichero como string.
lines = input_file.readlines()

# Guardar en vector asignaturas ya cursadas con notas.
asigs1 = []
notas1 = []
# sele = float(lines[17])
# if sele != -1:
#     notas1.append(sele)
for i in range(0, 10):
    nota1 = float(lines[20 + 2*i])
    if nota1 != -1:
        asigs1.append(lines[19 + 2*i])
        asigs1[len(asigs1) - 1] = asigs1[len(asigs1) - 1][0:(len(asigs1[len(asigs1) - 1]) - 1)]
        notas1.append(nota1)
asigs1 = cd.encoder(asigs1)

# Guardar en vector asignaturas para hacer horario con nota deseada.
n = int(lines[41])
asigs2 = [0]*n
notas2 = [0]*n
for i in range(0, n):
    asigs2[i] = lines[43 + 2*i]
    asigs2[i] = asigs2[i][0:(len(asigs2[i]) - 1)]
    notas2[i] = float(lines[44 + 2*i])
asigs2 = cd.encoder(asigs2)
if len(asigs2) > 0:
    asigs2, notas2 = zip(*sorted(zip(asigs2, notas2))) # Ordenar simultaneamente.
    asigs2, notas2 = (list(t) for t in zip(*sorted(zip(asigs2, notas2)))) # Volver a convertir en lista.

# Número de vecinos más cercanos.
k = int(lines[43 + 2*n + 2])

# Restricciones de horario.
l = int(lines[48 + 2*n])
horario = []
for i in range(0, l):
    aux = [0, 0, 0, 0, 0]
    for j in range(0, 5):
        aux[j] = int(lines[50 + 2*n + i][3*j:3*j + 2])
    horario.append(aux)


# Ejecución del programa.
# Predecir notas.
grades = pr.predictor_main(asigs1, notas1, asigs2, k)

# Obtener horas de estudio.
hours = hr.hours_main(n)

# Generar horario.
names = cd.decoder(asigs2)
finde = gn.generator_main(hours, names, horario)


# Output.
# Imprimir por pantalla tabla con datos diversos.
df = pd.read_csv('Ficheros/asignaturas.csv')
df = df[df['NOMBRE'].isin(names)]
df = df.reset_index(drop = True)
means = []
for i in range(0, len(df)):
    means += df[df['NOMBRE'] == names[i]]['NM'].values.tolist()    
print('\n'*4, '\t'*6, 'EJECUCIÓN DEL PROGRAMA', '\n'*3)
aux2 = [['ASIGNATURA', 'NOTA ESPERADA', 'NOTA DESEADA', 'NOTA MEDIA', 'HORAS (INVENTADAS)'], ['', '', '', '', '']]
for i in range(0, n):
    aux2.append([names[i], round(grades[i], 2), notas2[i], round(means[i], 2), hours[i]])

print_matrix(aux2)

# Imprimir por pantalla el horario en tabla.
print('\n'*3, '\t'*6, 'HORARIO DE ESTUDIO', '\n\n')
horario = [['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES'], ['', '', '', '', '']] + horario
print_matrix(horario)

# Vector con las horas del fin de semana.
print('\n'*3, '\t'*6, 'FIN DE SEMANA: ', '\n'*2)
finde = [['ASIGNATURA', 'HORAS'],['', '']] + finde
print_matrix(finde)
print()
