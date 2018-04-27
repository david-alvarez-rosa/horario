# Crea matriz de vecinos más cercanos para sacarla en la web.
def vecinos_matrix(nearest_form, nombres, notas, sele, diff):
    for i in range(0, len(notas)):
        if notas[i] < 0:
            notas[i] = ''
            
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
