import pandas as pd
from app.scripts import codificador as cd
from app.scripts import predictor as pr
from app.scripts import horas as hr
from app.scripts import generador as gn
from app.scripts import rendimiento as rd
from app.scripts import terminal as ter


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


def main(notas_curs_todas, rend, nombres_des, notas_des, horario):
    # Convertir input de la web en input válido para el programa.
    sele, l_curs, l_des, nombres_des, notas_des, codas, nombres, notas, k, \
        horario, rend, notas_curs, l_horario = \
        convert_input(notas_curs_todas, nombres_des, rend, notas_des, horario)

    # Predecir notas.
    grades, nearest_form, diff = pr.predictor_main(codas, notas, k, l_curs, sele)
    notas_esp = []
    for i in range(0, l_des):
        pos = nombres.index(nombres_des[i])
        notas_esp.append(grades[pos])

    # Crear vector de medias y de creditos para asignaturas deseadas.
    df = pd.read_csv('app/databases/asignaturas.csv')
    df = df[df['NOMBRE'].isin(nombres_des)]
    df = df.reset_index(drop = True)
    notas_med = []
    creds = []
    for i in range(0, len(nombres_des)):
        notas_med += df[df['NOMBRE'] == nombres_des[i]]['NM'].values.tolist()
        creds += df[df['NOMBRE'] == nombres_des[i]]['CR'].values.tolist()

    # Obtener horas deseadas según rendimiento.
    notas_des = rd.rend_main(rend, l_des, notas_des, notas_curs, l_curs)

    # Obtener horas de estudio.
    horas = hr.hours_main(notas_des, notas_esp, notas_med, l_des, creds)

    # Generar horario.
    finde_des = gn.generator_main(horas, nombres_des, horario)

    # Devolver resultados. Falta.
    # Generar output.
    ter.print_results(nombres_des, notas_des, l_des, notas_esp, nombres, \
                      nearest_form, notas, diff, horas, horario, finde_des, \
                      sele, notas_med, creds, rend)
