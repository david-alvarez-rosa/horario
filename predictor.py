import pandas as pd
import neighboors


# Retorna vector con las notas predecidas para las asignaturas de asigs2.
def predict_grades(nearest, asigs2, matrix, k, n):
    m = len(asigs2)
    grades = [0]*m
    for i in range(0, k):
        for j in range(0, m):
            grades[j] += matrix[nearest[i][1]][n + j]
    for j in range(0, m):
        grades[j] /= k
    return grades


def predict_main(asigs1, notas, asigs2):
    # Abrir fichero con todos los datos (está ordenado).
    df = pd.read_csv('Ficheros/data.csv')
    
    asigs2.sort() # Mismo orden que data.csv y que matriz.
    # Crear la matriz.
    matrix = neighboors.create_matrix(df, asigs1, asigs2)

    # Vector con todas las distancias.
    nearest = neighboors.k_nearest_neighboors(15, matrix, notas)

    # Predecir notas.
    grades = predict_grades(nearest, asigs2, matrix, 15, len(asigs1))

    return grades
