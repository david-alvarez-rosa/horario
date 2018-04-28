# Crea matriz de vecinos más cercanos para sacarla en la web.
def vecinos_matrix(nearest_form, nombres, notas, sele, diff):
    # Quitar las notas deseadas.
    # for i in range(0, len(notas)):
    #     if notas[i] < 0:
    #         notas[i] = ''
            
    if sele < 0:
        nearest_form = [['CODEX'] + nombres + ['DISTANCIA']] + \
                       [['Tú'] + notas + \
                        ['diff = ' + str(round(diff, 2))]] + \
                        nearest_form
    else:
        nearest_form = [['CODEX'] + nombres + ['Selectividad'] + ['DISTANCIA']] + \
                       [['Tú'] + notas + [sele] + \
                        ['diff = ' + str(round(diff, 2))]] + \
                        nearest_form

    return nearest_form


# Reordenar las notas esperadas como las introdujo el usuario y redondear
# a dos decimales.
def format_notas_esp(nombres_des, l_des, grades, nombres):
    notas_esp = []
    for i in range(0, l_des):
        pos = nombres.index(nombres_des[i])
        notas_esp.append(grades[pos])
        notas_esp[i] = round(notas_esp[i], 2)
    return notas_esp
