from app.scripts import codificador as cd


# Convertir input de la web en input válido para el programa.
def convert_input(notas_curs_todas, nombres_des, rend, notas_des, horario):
    # Variables puestas como 'default'.
    nombres_curs_todas = ['Álgebra Lineal', 'Cálculo I', 'Mecánica Fundamental', 
                          'Química I', 'Fundamentos de Informática', 'Cálculo II',
                          'Geometría','Termodinámica Fundamental', 'Química II',
                          'Expresión Gráfica']
    k = 12
    l_horario = 15

    # Notas introducidas por el usuario.
    sele = notas_curs_todas[0]
    l_curs = 0
    notas_curs = []
    nombres_curs = []
    for i in range(1, len(notas_curs_todas)):
        if notas_curs_todas[i] >= 0:
            notas_curs.append(notas_curs_todas[i])
            nombres_curs.append(nombres_curs_todas[i - 1])
            l_curs += 1
    codas_curs = cd.encoder(nombres_curs)

    # Asignaturas para hacer horario.
    l_des = len(nombres_des)
    codas_des = cd.encoder(nombres_des)

    # Rendimiento.
    if rend == 'Min':
        rend = 0
    elif rend == 'Med':
        rend = 1
    elif rend == 'Max':
        rend = 2
    else: rend  = -1

    # Unir todo el input y ordenarlo simultáneamente por CODASS.
    codas = codas_curs + codas_des
    # Guardar las notas deseadas negativas (para identificarlas después).
    for i in range(0, len(notas_des)):
        notas_des[i] *= -1
        # Para no tener problemas con el 0 lo guardo como -11.
        if notas_des[i] == 0: notas_des[i] = -11 
        notas = notas_curs + notas_des
        nombres = nombres_curs + nombres_des
    if len(codas) > 0:
        codas, notas, nombres = (list(t) for t in \
                                 zip(*sorted(zip(codas, notas, nombres))))

    # Retornar todo lo necesario.
    return sele, l_curs, l_des, nombres_des, notas_des, codas, nombres, notas, \
        k, horario, rend, notas_curs, l_horario


# Escribir tabla en html dado una matriz de Python.
def print_table_html(matrix, resultados):
    resultados.write('<table>' + '\n')
    for i in range(0, len(matrix)):
        resultados.write('<tr>' + '\n')
        for j in range(0, len(matrix[0])):
            resultados.write('<th>' + str(matrix[i][j]) + ' </th>' + '\n')
        resultados.write('</tr>' + '\n')
    resultados.write('</table>')


# Programa que genera el output del programa.
def print_results_html(nombres_des, notas_des, l_des, notas_esp, nombres, \
               nearest_form, notas, diff, horas, horario, finde_des, \
               sele, notas_med, creds, rend):

    # Crear la página de resultados.
    resultados = open('app/templates/resultados.html', 'w')

    resultados.write('<!DOCTYPE html>' + '\n')
    resultados.write('<html>' + '\n')
    resultados.write('  <head>' + '\n')
    resultados.write('    <title>Proyecto I - Horario</title>' + '\n')
    resultados.write('    <p class = title1>Smart_hours.</p>' + '\n')
    resultados.write('    <meta charset="utf-8">' + '\n')
    resultados.write('    <meta name="viewport" content="width=device-width, initial-scale=1">' + '\n')
    resultados.write('    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">' + '\n')
    resultados.write('    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">' + '\n')
    resultados.write('    <link rel = "stylesheet" type = "text/css" href = "../static/style.css" />' + '\n')
    resultados.write('  </head>' + '\n')
    resultados.write('<body bgcolor = #F3CA24>' + '\n')

    # Imprimir por pantalla los vecinos más cercanos.
    resultados.write('\n' + '\t'*7 + 'VECINOS MÁS CERCANOS' + '\n'*2)
    if sele < 0:
        nearest_form = [['CODEX'] + nombres + ['DISTANCIA'], \
                        ['']*(len(nombres) + 2)] + [['TÚ'] + notas + \
                        ['diff = ' + str(round(diff, 2))]] \
                       + [['']*(len(nombres) + 2)] + nearest_form
    else:
        nearest_form = [['CODEX'] + nombres + ['SELE'] + ['DISTANCIA'], \
                        ['']*(len(nombres) + 3)] + [['TÚ'] + notas + [sele] + \
                        ['diff = ' + str(round(diff, 2))]] \
                       + [['']*(len(nombres) + 3)] + nearest_form
    # Acortar nombres para que entren en pantalla.
    for j in range(0, len(nearest_form[0])):
        nearest_form[0][j] = nearest_form[0][j][0:5]
    print_table_html(nearest_form, resultados)

    # Imprimir por pantalla tabla con datos diversos.
    resultados.write('\n'*3 + '\t'*7 + 'EJECUCIÓN DEL PROGRAMA' + '\n'*2)
    aux2 = [['ASIGNATURA', 'NOTA ESPERADA', 'NOTA DESEADA', 'NOTA MEDIA', \
             'CRÉDITOS', 'HORAS'], \
                ['', '', 'rend = ' + str(rend), '', '', '']]
    for i in range(0, l_des):
        aux2.append([nombres_des[i], round(notas_esp[i], 2), \
                     -round(notas_des[i], 2), round(notas_med[i], 2), \
                     creds[i], horas[i]])
    print_table_html(aux2, resultados)

    # Imprimir por pantalla el horario en tabla.
    resultados.write('\n'*3 + '\t'*7 + 'HORARIO DE ESTUDIO' + '\n\n')
    horario = [['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES'], \
               ['', '', '', '', '']] + horario
    print_table_html(horario, resultados)

    # Vector con las horas del fin de semana.
    resultados.write('\n'*3 + '\t'*7 + 'FIN DE SEMANA: ' + '\n'*2)
    aux3 = [['ASIGNATURA', 'HORAS'],['', '']]
    for i in range(0, l_des):
        aux3.append([nombres_des[i], finde_des[i]])
    print_table_html(aux3, resultados)

    # Imprimir distribución de horas.
    resultados.write('\n'*2)
    horas_total = 0
    for i in range(0, l_des):
        horas_total += horas[i]
    horas_finde = 0
    for i in range(0, l_des):    
        horas_finde += finde_des[i]
    horas_semana = horas_total - horas_finde
    aux4 = [['DISTRIBUCIÓN DE HORAS:', ''], ['', ''], ['Semana:', horas_semana], \
            ['Fin de semana:', horas_finde], ['Total:', horas_total]]
    print_table_html(aux4, resultados)

    resultados.write('\</body>')
