from flask import render_template, g
from app import app
from flask import request

#from app.scripts import calculs as cal

#from app.scripts.calculs import sumainterval
#from .scripts.predictor import *
a = 'aaa'
a2 = ''
a3 = ''
a4 = ''
a5 = ''
a6 = ''
a7 = ''
a8 = ''
a9 = ''
a10 = ''
a11 = ''
a12 = ''
a13= ''
a14 = ''
a15 = ''
a16 = ''
a17 = ''
a18 = ''
a19 = ''
a20 = ''


@app.route('/')
@app.route('/index')
def index():
    return render_template('p1.html', title = 'Home')


@app.route('/pagina2')
def next1():
    return render_template('p2.html', title='pagina2')


@app.route('/notes', methods=['POST'])
def notes():
    a = request.form.getlist("check_list[]")
    print(a)
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
