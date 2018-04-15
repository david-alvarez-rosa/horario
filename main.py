import pandas as pd
import predictor as pr
import horas as hr
import generador as gn
import rendimiento as rd
import terminal as ter


# Leer fichero de input.
sele, l_curs, l_des, nombres_des, notas_des, codas, nombres, notas, k, \
    horario, rend, notas_curs, l_horario = ter.read('input_file.txt')

# Predecir notas.
grades, nearest_form, diff = pr.predictor_main(codas, notas, k, l_curs, sele)
notas_esp = []
for i in range(0, l_des):
    pos = nombres.index(nombres_des[i])
    notas_esp.append(grades[pos])

# Crear vector de medias y de creditos para asignaturas deseadas.
df = pd.read_csv('Ficheros/asignaturas.csv')
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

# Generar output.
ter.print_results(nombres_des, notas_des, l_des, notas_esp, nombres, \
               nearest_form, notas, diff, horas, horario, finde_des, \
               sele, notas_med, creds, rend)
