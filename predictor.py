import pandas as pd
import vecinos as vc


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
    df.reset_index(drop = True)

    pos = 0
    matrix = [['CODEX/CODASS'] + asigs]
    while True:
        npos = next(pos, df)
        if npos == -1: return matrix
        notas = df[pos:npos]['NF'].values.tolist() # Optimización usando que df está ordenado.
        if len(notas) == len(asigs):
            codex = []
            codex.append(df['CODEX'].iloc[pos])
            matrix.append(codex + notas)
        pos = npos


# Retorna vector con las notas predichas para las asignaturas de asigs2.
def predict_grades(nearest, asigs2, matrix, k, n):
    if len(nearest) < k: k = len(nearest) # Posible error por falta de alumnos 'compatibles'.
    m = len(asigs2)
    grades = [0]*m
    for i in range(0, k):
        print(matrix[nearest[i][1]])
        for j in range(0, m):
            grades[j] += matrix[nearest[i][1]][n + 1 + j]
    for j in range(0, m):
        grades[j] /= k
        grades[j] += nearest[0][0] # Añado la diferencia.
        if grades[j] < 0: grades[j] = 0 # No permitir notas negativas.
        if grades[j] > 10: grades[j] = 10 # No permitir notas mayores que 10.
    return grades


# Precondición: asigs2 está ordenado de manera creciente (mismo orden que matriz).
def predictor_main(asigs1, notas, asigs2, k):
    # Abrir fichero con todos los datos (está ordenado).
    df = pd.read_csv('Ficheros/data.csv')

    # Crear la matriz.
    matrix = create_matrix(df, asigs1, asigs2)

    # Vector con los k vecinos más cercanos.
    nearest = vc.k_nearest_neighbors(k, matrix, notas)

    # Predecir notas.
    grades = predict_grades(nearest, asigs2, matrix, k, len(asigs1))

    return grades
