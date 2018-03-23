import pandas as pd


# Dada una posición, devuelve el inicio del siguiente alumno (con CODEX distinto).
# Devuelve -1 si no quedan más alumnos.
def next(pos, df):
    aux = pos # Para no modificar pos.
    codex = df['CODEX'].iloc[aux]
    while aux < len(df):
        if df['CODEX'].iloc[aux] != codex: return aux
        aux += 1
    return -1


# Crea una matriz con todos los alumnos que tienen nota en asigs1 y asigs2.
# La matrix tiene la forma (con primer fila de cabecera):
# | CODEX/CODASS | CODASS1 | CODASS2 | ... | CODASSN |
# |    CODEX     |   NF1   |   NF2   | ... |   NFN   |
# Donde CODASS1...CODASSN son los códigos de asigs1, asigs2.
def create_matrix(df, asigs1, asigs2):
    asigs = asigs1 + asigs2
    df = df[df['CODASS'].isin(asigs)] # Primer filtrado.
    df.reset_index(drop=True)
    
    pos = 0
    filtered_data = [["CODEX/CODASS"] + asigs]
    while True:
        npos = next(pos, df)
        if npos == -1: return filtered_data
        notas = df[pos:npos]['NF'].values.tolist() # Optimización usando que df está ordenado.        
        if len(notas) == len(asigs):
            codex = []
            codex.append(df['CODEX'].iloc[pos])
            filtered_data.append(codex + notas)
        pos = npos


# Calcula distancia entre usuario y alumno (dada su fila en matriz).
def distance(row, notas, matrix):
    distance = 0
    for j in range(0, len(notas)):
        distance += pow(notas[j] - matrix[row][j + 1], 2) # La primera columna tiene el CODEX.
    return distance


# Va actualizando el vector nearest para solo quedarse con los k primeros.
# Es una modificación del ordenamiento por selección.
def update(nearest, k):
    if len(nearest) <= k:
        nearest.sort()
        return
    it = k
    while k > 0:
        k -= 1
        if nearest[k][0] > nearest[k + 1][0]:
            nearest[k], nearest[k + 1] = nearest[k + 1], nearest[k] # Swap.
        else:
            nearest.pop()
            return

        
# Retorna vector con las filas (en la matriz) de los k vecinos más cercanos.
# Precondición: todas las asignaturas del input son de la fase inicial.
# Funciona bien porque los CODASS de fase inicial son los más pequeños.
def k_nearest_neighboors(k, matrix, notas):
    nearest = []
    for i in range(1, len(matrix)):
        nearest.append([distance(i, notas, matrix), i])
        update(nearest, k)
    return nearest
