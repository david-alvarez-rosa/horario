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


# Retorna vector con las filas (en la matriz) de los k vecinos más cercanos.
# Ahora retorna todas las distancias, falta implementar la k.
# Funciona bien porque los CODASS de fase inicial son los más pequeños.
# Si en el input hubiera una asignatura de la fase no inicial, no funcionará bien.
def k_nearest_neighboors(k, matrix, notas):
    nearest = []
    for i in range(1, len(matrix)):
        nearest.append([distance(i, notas, matrix), i])
    nearest.sort()
    return nearest


# # Asignaturas con la notas que el usuario introduce como input.
# asigs1 = [240011, 240012, 240013, 240014, 240015, 240021, 240022, 240023, 240024, 240025]
# notas = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

# # Asignaturas que el usuario se va a matricular (de las que quiere el horario).
# asigs2 = [240033, 240041, 240042, 240053]

# # Abrir fichero con todos los datos (está ordenado).
# df = pd.read_csv('Ficheros/data.csv')

# # Crear la matriz.
# matrix = create_matrix(df, asigs1, asigs2)

# # Vector con todas las distancias.
# nearest = k_nearest_neighboors(15, matrix, notas)


# # Imprimir por pantalla resultados.
# print(nearest[0:15])


# print()
# s = [[str(e) for e in row] for row in matrix]
# lens = [max(map(len, col)) for col in zip(*s)]
# fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
# table = [fmt.format(*row) for row in s]
# print ('\n'.join(table))




