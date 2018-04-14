import predictor as pr
import horas as hr
import generador as gn
import terminal as ter


# Leer fichero de input.
sele, l_obt, l_des, nombres_des, notas_des, codas, nombres, notas, k, \
    horario = ter.read('input_file.txt')

# Predecir notas.
grades, nearest_form, diff = pr.predictor_main(codas, notas, k, l_obt, sele)
notas_esp = []
for i in range(0, l_des):
    pos = nombres.index(nombres_des[i])
    notas_esp.append(grades[pos])

# Obtener horas de estudio.
horas = hr.hours_main(l_des)

# Generar horario.
finde_des = gn.generator_main(horas, nombres_des, horario)

# Generar output.
ter.print_data(nombres_des, notas_des, l_des, notas_esp, nombres, \
               nearest_form, notas, diff, horas, horario, finde_des, sele)
