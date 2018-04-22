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
    nombres_des = request.form.getlist("check_list[]")
    nombres_des_file = open('nombres_des_file.txt', 'w')
    for i in range(0, len(nombres_des)):
        nombres_des_file.write(nombres_des[i] + '\n')
    return render_template('cursadas.html', title='cursadas')


@app.route('/resultados', methods = ['POST'])
def resultados():
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
    rend = request.form['rend']

    rend = str(rend)
    notas = [float(sele), float(algebra), float(calcul1), float(info1),
             float(mec_fon), float(quim1), float(calc2), float(expre),
             float(geo), float(quim2), float(termo)]
    nombres_des_file = open('nombres_des_file.txt', 'r')
    lines = nombres_des_file.readlines()
    nombres_des = []
    for i in range(0, len(lines)):
        nombre = lines[i]
        nombre = nombre[0:len(nombre) - 1]
        nombres_des.append(nombre)
            
    # Para probrarlo.
    notas_des = 6*[5]
    rend = -1
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

notas = []
print(notas)
