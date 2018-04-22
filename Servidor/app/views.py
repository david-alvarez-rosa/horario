from flask import render_template, g
from app import app
from flask import request


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
    a = request.form.getlist("check_list[]")
    print(a)
    return render_template('cursadas.html', title='cursadas')


@app.route('/resultados', methods = ['POST'])
def resultados():
    sele = request.form['input_sele']
    algebra = request.form['input_algebra']
    calcul1 = request.form['input_calcul1']
    info1 = request.form['input_info1']
    quim1 = request.form['input_quim1']
    mec_fon = request.form['input_MecFon']
    quim2 = request.form['input_quim2']
    calc2 = request.form['input_calcul2']
    expre = request.form['input_expre']
    geo = request.form['input_geo']
    rend = request.form['rend']
    
    print(str(rend))
    notas = [float(sele),float(algebra),float(calcul1),float(info1),float(quim1),
             float(mec_fon),float(quim2),float(calc2),float(expre),float(geo)]
    print(notas)
    

    # en el return tornem les variables per separat, però es pot tornar un dict
    # amb els valors a tornar {'id':'valor'}
    return render_template('notes.html',
                           title = 'Notes',
                           sele = float(sele),
                           algebra = float(algebra),
                           calcul1=float(calcul1),
                           info1 = float(info1),
                           quim1 = float(quim1),
                           mec_fon = float(mec_fon),
                           quim2 = float(quim2),
                           calc2 = float(calc2),
                           expre = float(expre),
                           geo=float(geo),
                           rend = str(rend))
