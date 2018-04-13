# Calcula distancia entre usuario y alumno (dada su fila en matriz).
def distance(row, notas, matrix):
    distance = 0
    for j in range(0, len(notas)):
        distance += pow(notas[j] - matrix[row][j + 1], 2) # La primera columna tiene el CODEX.
    return distance


# Calculo de la media de diferencias de notas (con signo) entre usuario y vecinos.
def differences(notas, nearest, k, matrix):
    if len(notas) == 0: return 0 # Caso especial si ninguna nota se introduce.
    diff_tot = 0
    for i in range(0, k):
        row = nearest[i][1]
        diff = 0
        for j in range(1, len(notas)):
            diff += notas[j] - matrix[row][j + 1]
        diff_tot += diff/len(notas)
    return diff_tot/k


# Retorna vector con las filas (en la matriz) de los k vecinos más cercanos.
# Precondición: todas las asignaturas del input son un subconjunto de las de la fase inicial.
# Funciona bien porque los CODASS de fase inicial son los más pequeños.
def k_nearest_neighbors(k, matrix, notas):
    nearest = []
    for i in range(1, len(matrix)):
        nearest.append([distance(i, notas, matrix), i])
    nearest.sort()
    nearest = nearest[0:k]
    nearest[0][0] = differences(notas, nearest, k, matrix) # Me lo guardo en la distancia.
    return nearest
