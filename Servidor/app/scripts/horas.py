def hours_main(notas_des, notas_esp, notas_med, l_des, creds):
    hours = [0]*l_des
    for i in range(0, l_des):
        hours[i] = creds[i]*0.8*pow(1.1, -notas_des[i] - notas_esp[i])
    for i in range(0, l_des):
        hours[i] = int(round(hours[i], 0))
    return hours

    
# Falta programa, versión de prueba.
# def hours_main(notas_des, notas_esp, notas_med, l_des, creds):
#     hours = [5, 4, 3, 5, 4, 7, 7, 4, 5, 4, 5, 5, 4, 5, 4]
#     return hours[0:l_des]
