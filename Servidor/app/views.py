from flask import render_template, g
from app import app
from flask import request
from app.scripts import main


@app.route('/')
@app.route('/index')
@app.route('/horario')
def horario():
    return render_template('horario.html', title = 'Home')


@app.route('/deseadas')
def deseadas():
    return render_template('deseadas.html', title='deseadas')


@app.route('/cursadas', methods = ['POST'])
def cursadas():
    # Leer nombres de las asignaturas deseadas para hacer horario.
    nombres_des = request.form.getlist("check_list[]")
    # Guardarlos en un fichero por filas.
    nombres_des_file = open('app/tmp/nombres_des_file.txt', 'w')
    for i in range(0, len(nombres_des)):
        nombres_des_file.write(nombres_des[i] + '\n')
        
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
    notas = [float(sele), float(algebra), float(calcul1), float(info1),
             float(mec_fon), float(quim1), float(calc2), float(expre),
             float(geo), float(quim2), float(termo)]

    # Leer rendimiento como string.
    rend = request.form['rend']
    rend = str(rend)

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
    notas_des = [5]*len(nombres_des)
    horario = [
        [-1, -2, -1, -1, -1],
        [-2, -2, -2, -2, -2],
        [-2, -1, -2, -2, -1],
        [-1, -1, -1, -2, -1],
        [-2, -1, -1, -1, -2],
        [-2, -2, -2, -2, -2],
        [-1, -2, -1, -1, -1],
        [-2, -2, -2, -2, -2],
        [-2, -1, -2, -2, -1],
        [-1, -1, -1, -2, -1],
        [-2, -1, -1, -1, -2],
        [-2, -2, -2, -2, -2],
        [-1, -2, -1, -1, -1],
        [-2, -2, -2, -2, -2],
        [-2, -1, -2, -2, -1]
    ]

    # Ejecutar el programa.
    main.main(notas, rend , nombres_des, notas_des, horario)

    return render_template('resultados.html')
    

    # en el return tornem les variables per separat, però es pot tornar un dict
    # amb els valors a tornar {'id':'valor'}
    # return render_template('notes.html',
    #                        title = 'Notes',
    #                        sele = float(sele),
    #                        algebra = float(algebra),
    #                        calcul1=float(calcul1),
    #                        info1 = float(info1),
    #                        quim1 = float(quim1),
    #                        mec_fon = float(mec_fon),
    #                        quim2 = float(quim2),
    #                        calc2 = float(calc2),
    #                        expre = float(expre),
    #                        geo=float(geo),
    #                        rend = str(rend))
