import predictor


# Abrir fichero de input.
input_file = open('input_file.txt', 'r')

# Leer todas las líneas del fichero como string.
lines = input_file.readlines()

# Pasar los datos a los vectores.
asigs1 = [0]*10
notas = [0]*10
for i in range(0, 10):
    asigs1[i] = int(lines[10 + 2*i])
    notas[i] = int(lines[11 + 2*i])

n = int(lines[31])
asigs2 = [0]*n
for i in range(0, n):
    asigs2[i] = int(lines[32 + i])


# Número de vecinos más cercanos.
k = int(lines[32 + n + 1])

grades = predictor.predict_main(asigs1, notas, asigs2, k)

print(grades)
