from flask import render_template, request
from app import app
from app.scripts import main


@app.route('/')
@app.route('/index')
@app.route('/horario')
def horario():
    return render_template('horario.html', title = 'Home')


@app.route('/deseadas')
def deseadas():
    # Leer horas ocupadas del horario.
    horario = request.form.getlist('horario')
    # Guardar el horario en fichero.
    horario_file = open('app/tmp/horario_file.txt', 'w')
    for i in range(0, len(horario)):
        for j in range(0, len(horario[0])):
            horario_file.write(str(horario[i][j]))
        horario_file.write('\n')
    
    return render_template('deseadas.html', title='deseadas')


@app.route('/cursadas', methods = ['POST'])
def cursadas():
    # Leer rendimiento.
    rend = request.form['rend']
    # Guardarlo en fichero.
    rend_file = open('app/tmp/rend_file.txt', 'w')
    rend_file.write(rend)
    
    # Leer nombres de las asignaturas deseadas para hacer horario.
    nombres_des = request.form.getlist('check_list[]')
    # Guardarlos en un fichero por filas.
    nombres_des_file = open('app/tmp/nombres_des_file.txt', 'w')
    for i in range(0, len(nombres_des)):
        nombres_des_file.write(nombres_des[i] + '\n')

    if rend == 'man':
        return render_template('cursadas_man.html', nombres_des = nombres_des,
                               l_des = len(nombres_des), title='cursadas')

    return render_template('cursadas.html', title='cursadas')


@app.route('/resultados', methods = ['POST'])
def resultados():
    # Notas cursadas.
    sele = request.form['input_sele']
    algebra = request.form['input_algebra']
    calcul1 = request.form['input_calcul1']
    info1 = request.form['input_info1']
    mec_fon = request.form['input_MecFon']
    quim1 = request.form['input_quim1']
    calc2 = request.form['input_calcul2']    
    expre = request.form['input_expre']
    geo = request.form['input_geo']
    quim2 = request.form['input_quim2']
    termo = request.form['input_termo']

    # Convertir notas a lista.
    notas = [sele, algebra, calcul1, info1, mec_fon, quim1, calc2, expre,
             geo, quim2, termo]
    for i in range(0, len(notas)):
        if notas[i] == '':
            notas[i] = -1
        notas[i] = float(notas[i])

    # Leer rendimiento desde fichero.
    rend_file = open('app/tmp/rend_file.txt', 'r')
    rend = rend_file.readlines()
    rend = str(rend[0])

    print('rendimiento: ', rend)

    # Leer nombres asignaturas deseadas desde fichero.
    nombres_des_file = open('app/tmp/nombres_des_file.txt', 'r')
    lines = nombres_des_file.readlines()
    # Guardar nombres en lista.
    nombres_des = []
    for i in range(0, len(lines)):
        nombre = lines[i]
        nombre = nombre[0:len(nombre) - 1]
        nombres_des.append(nombre)
            
    # Para probrarlo.
    notas_des = [7.5]*len(nombres_des)
    horario = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-2, -2, -2, -2, -1],
        [-1, -2, -1, -2, -2],
        [-2, -2, -1, -1, -2],
        [-2, -2, -2, -2, -2],
        [-1, -2, -1, -1, -1],
        [-2, -2, -2, -2, -2],
        [-2, -1, -2, -2, -1],
        [-1, -1, -1, -2, -1],
        [-2, -1, -1, -1, -2],
        [-2, -2, -2, -2, -2],
        [-1, -2, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1]
    ]

    # Ejecutar el programa.
    horario, hora_ini, nombres_hor = main.main(notas, rend, nombres_des,
                                               notas_des, horario)

    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    
    return render_template('resultados.html', horario = horario, dias = dias,
                           l_horario = len(horario), nombres = nombres_hor,
                           ini = hora_ini, title = 'resultados')
