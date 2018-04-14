import pandas as pd
import codificador as cd


# Imprimir por pantalla bien una matriz (de Stack Overflow).
def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))

    
# Imprimir por pantalla bien una matriz (de Stack Overflow).
def print_matrix_small(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))


# Programa para leer el input desde input_file.txt
def read(name):
    # Abrir fichero.
    input_file = open(name, 'r')

    # Leer todas las líneas del fichero como string.
    lines = input_file.readlines()

    # Guardar la nota de selectividad.
    sele = float(lines[18])

    # Guardar en vector asignaturas ya cursadas con notas.
    nombres_obt = []
    notas_obt = []
    # Diferencio entre el número de asignaturas cursadas introducido y el real.
    l_obt_int = int(lines[21])
    l_obt = l_obt_int
    for i in range(0, l_obt):
        nombre = lines[23 + 2*i]
        nota = float(lines[24 + 2*i])
        if nota != -1:
            nombre = nombre[0:len(nombre) - 1]
            nombres_obt.append(nombre)
            notas_obt.append(nota)
        else: l_obt -= 1
        codas_obt = cd.encoder(nombres_obt)

    # Guardar en vector asignaturas para hacer horario con nota deseada.
    l_des = int(lines[25 + 2*l_obt_int])
    nombres_des = []
    notas_des = []
    for i in range(0, l_des):
        nombre = lines[27 + 2*l_obt_int + 2*i]
        nombre = nombre[0:len(nombre) - 1]
        nombres_des.append(nombre)
        nota = float(lines[28 + 2*l_obt_int + 2*i])
        notas_des.append(nota)
        codas_des = cd.encoder(nombres_des)
        
    # Número de vecinos más cercanos.
    k = int(lines[27 + 2*l_des + 2*l_obt_int + 2])
            
    # Restricciones de horario.
    l = int(lines[32 + 2*l_des + 2*l_obt_int])
    horario = []
    for i in range(0, l):
        aux = [0, 0, 0, 0, 0]
        for j in range(0, 5):
            aux[j] = int(lines[34 + 2*l_des + 2*l_obt_int + i][3*j:3*j + 2])
        horario.append(aux)
        
    # Unir todo el input y ordenarlo simultáneamente por CODASS.
    codas = codas_obt + codas_des
    # Guardar las notas deseadas negativas (para identificarlas después).
    for i in range(0, len(notas_des)):
        notas_des[i] *= -1
        if notas_des[i] == 0: notas_des[i] = -11 # Para no tener problemas con el 0.
    notas = notas_obt + notas_des
    nombres = nombres_obt + nombres_des
    if len(codas) > 0:
        codas, notas, nombres = (list(t) for t in zip(*sorted(zip(codas, notas, nombres))))

    # Retornar todo lo necesario.
    return sele, l_obt, l_des, nombres_des, notas_des, codas, nombres, notas, \
        k, horario
        

# Programa que genera el output del programa.
def print_data(nombres_des, notas_des, l_des, notas_esp, nombres, \
               nearest_form, notas, diff, horas, horario, finde_des, sele):
    # Imprimir por pantalla los vecinos más cercanos.
    print('\n', '\t'*6, 'VECINOS MÁS CERCANOS', '\n'*2)
    if sele < 0:
        nearest_form = [['CODEX'] + nombres + ['DISTANCIA'], ['']*(len(nombres) + 2)] \
                       + [['TÚ'] + notas + ['diff = ' + str(round(diff, 2))]] \
                       + [['']*(len(nombres) + 2)] + nearest_form
    else:
        nearest_form = [['CODEX'] + nombres + ['SELE'] + ['DISTANCIA'], ['']*(len(nombres) + 3)] \
                       + [['TÚ'] + notas + [sele] + ['diff = ' + str(round(diff, 2))]] \
                       + [['']*(len(nombres) + 3)] + nearest_form
    # Acortar nombres para que entren en pantalla.
    for j in range(0, len(nearest_form[0])):
        nearest_form[0][j] = nearest_form[0][j][0:5]
    print_matrix_small(nearest_form)

    # Imprimir por pantalla tabla con datos diversos.
    df = pd.read_csv('Ficheros/asignaturas.csv')
    df = df[df['NOMBRE'].isin(nombres_des)]
    df = df.reset_index(drop = True)
    means = []
    for i in range(0, len(nombres_des)):
        means += df[df['NOMBRE'] == nombres_des[i]]['NM'].values.tolist()
    print('\n'*3, '\t'*6, 'EJECUCIÓN DEL PROGRAMA', '\n'*2)
    aux2 = [['ASIGNATURA', 'NOTA ESPERADA', 'NOTA DESEADA', 'NOTA MEDIA', 'HORAS (INVENTADAS)'], \
                ['', '', '', '', '']]
    for i in range(0, l_des):
        aux2.append([nombres_des[i], round(notas_esp[i], 2), -notas_des[i], \
                     round(means[i], 2), horas[i]])
    print_matrix(aux2)

    # Imprimir por pantalla el horario en tabla.
    print('\n'*3, '\t'*6, 'HORARIO DE ESTUDIO', '\n\n')
    horario = [['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES'], \
               ['', '', '', '', '']] + horario
    print_matrix(horario)

    # Vector con las horas del fin de semana.
    print('\n'*3, '\t'*6, 'FIN DE SEMANA: ', '\n'*2)
    aux3 = [['ASIGNATURA', 'HORAS'],['', '']]
    for i in range(0, l_des):
        aux3.append([nombres_des[i], finde_des[i]])
    print_matrix(aux3)
    print()
