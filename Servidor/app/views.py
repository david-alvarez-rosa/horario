from flask import render_template, request
from app import app
from app.scripts import entrada, main


@app.route('/')
@app.route('/index')
@app.route('/horario')
def horario():
    return render_template('horario.html', title = 'Home')


@app.route('/documentacion')
def documentacion():
    return render_template('documentacion.html', title = 'Documentacion')


@app.route('/deseadas', methods = ['POST'])
def deseadas():
    # Leer horas ocupadas del horario.
    horario = request.form.getlist('horario')
    # Guardar el horario en fichero.
    horario_file = open('app/tmp/horario_file.txt', 'w')
    for i in range(0, len(horario)):
        for j in range(0, len(horario[0])):
            horario_file.write(str(horario[i][j]))
        horario_file.write('\n')
    
    return render_template('deseadas.html', vacio = False,
                           title='Deseadas')


@app.route('/cursadas', methods = ['POST'])
def cursadas():
    # Leer rendimiento.
    rend = request.form['rend']
    # Guardarlo en fichero.
    rend_file = open('app/tmp/rend_file.txt', 'w')
    rend_file.write(rend)
    
    # Leer nombres de las asignaturas deseadas para hacer horario.
    nombres_des = request.form.getlist('check_list[]')
    # Comprobar que el usuario ha introducido al menos una asignatura.
    if len(nombres_des) == 0:
        return render_template('deseadas.html', vacio = True, \
                               title='Deseadas')
    # Guardarlos en un fichero por filas.
    nombres_des_file = open('app/tmp/nombres_des_file.txt', 'w')
    for i in range(0, len(nombres_des)):
        nombres_des_file.write(nombres_des[i] + '\n')

    if rend == 'man':
        return render_template('cursadas_man.html', nombres_des = nombres_des, \
                               l_des = len(nombres_des), error = False, \
                               title = 'Cursadas')

    return render_template('cursadas.html', vacio = False, \
                           title = 'Cursadas')


@app.route('/resultados', methods = ['POST'])
def resultados():
    # Leer notas cursadas desde la web.
    notas_curs_todas = entrada.leer_cursadas()

    # Leer rendimiento desde fichero.
    rend_file = open('app/tmp/rend_file.txt', 'r')
    rend = rend_file.readlines()
    rend = str(rend[0])

    # Si el rendimiento no es manual, comprobar que el formulario no
    # se ha dejado vac??o.
    if rend !=  'man' and notas_curs_todas == [-1]*11:
        return render_template('cursadas.html', vacio = True, \
                               title = 'Cursadas')

    # Leer nombres asignaturas deseadas desde fichero.
    nombres_des_file = open('app/tmp/nombres_des_file.txt', 'r')
    lines = nombres_des_file.readlines()

    # Guardar nombres en lista.
    nombres_des = []
    for i in range(0, len(lines)):
        nombre = lines[i]
        nombre = nombre[0:len(nombre) - 1]
        nombres_des.append(nombre)

    # Leer notas deseadas si el rendimiento es manual.
    notas_des = []
    if rend == 'man':
        for i in range(0, len(nombres_des)):
            nota = request.form[nombres_des[i]]
            notas_des.append(float(nota))
    else: notas_des = [20]*len(nombres_des)

    # Leer horario desde fichero.
    horario_file = open('app/tmp/horario_file.txt', 'r')
    lines = horario_file.readlines()
    horario = []
    for i in range(0, 15):
        aux = [-2]*5
        horario.append(aux)
    for k in range(0, len(lines) - 1):
        ia = int(lines[k][1:3]) - 9
        ja = int(lines[k][0]) - 1
        horario[ia][ja] = -1

    # Ejecutar el programa.
    horario, hora_ini, nombres_hor, vecinos_curs, vecinos_des, notas_esp, \
        nombres_des, finde, notas_des, \
        notas_med, horas, creds = main.main(notas_curs_todas, rend, nombres_des, \
                              notas_des, horario)

    # Si ha habido alg??n error, volver a la p??gina anterior y avisar de error.
    if horario == -1:
        # Volver a leer nombres deseados del fichero.
        nombres_des_file = open('app/tmp/nombres_des_file.txt', 'r')        
        lines = nombres_des_file.readlines()
        nombres_des = []
        for i in range(0, len(lines)):
            nombre = lines[i]
            nombre = nombre[0:len(nombre) - 1]
            nombres_des.append(nombre)
        # Devolver la p??gina con el mensaje de error.
        return render_template('cursadas_man.html', nombres_des = nombres_des, \
                               l_des = len(nombres_des), error = True, \
                               title = 'Cursadas')

    # Variables necesarias para crear el output en web.
    dias = ['Lunes', 'Martes', 'Mi??rcoles', 'Jueves', 'Viernes']
    l_vecinos_curs_i = len(vecinos_curs)
    l_vecinos_curs_j = len(vecinos_curs[0])
    l_vecinos_des_i = len(vecinos_des)
    l_vecinos_des_j = len(vecinos_des[0])
    l_des = len(notas_des)
    if len(horario) > 9:
        large_horario = True
    else:
        large_horario = False

    # Redondear las notas medias y las deseadas.
    for i in range(0, l_des):
        notas_med[i] = round(notas_med[i], 2)
        notas_des[i] = round(notas_des[i], 2)
    
    return render_template('resultados.html', horario = horario, dias = dias, \
                           l_horario = len(horario), nombres = nombres_hor, \
                           large_horario = large_horario, \
                           ini = hora_ini, title = 'Resultados', \
                           vecinos_curs = vecinos_curs, \
                           l_vecinos_curs_i = l_vecinos_curs_i, \
                           l_vecinos_curs_j = l_vecinos_curs_j, \
                           vecinos_des = vecinos_des, \
                           l_vecinos_des_i = l_vecinos_des_i, \
                           l_vecinos_des_j = l_vecinos_des_j, \
                           notas_esp = notas_esp, \
                           notas_med = notas_med, \
                           nombres_des = nombres_des, l_des = l_des, \
                           notas_des = notas_des, \
                           finde = finde, l_finde = len(finde),
                           horas = horas, creds = creds)
