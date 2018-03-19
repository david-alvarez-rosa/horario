# Función de comparación para el ordenamiento por selección.
def comp(a, b):
    if a%2 == 0:
        if b%2 == 0:
            if a <= b: return True
            return False
        return True
    else:
        if b%2 == 0: return False
        if a <= b: return True

        
# Ordenamiento por selección.
def sort(v, w):
    n = len(v)
    for i in range(0, n):
        min = v[i]
        posMin = i
        for j in range(i + 1, n):
            if comp(v[j], min):
                min = v[j]
                posMin = j
        v[i], v[posMin] = v[posMin], v[i]
        w[i], w[posMin] = w[posMin], w[i]

        
# Primera asignación de horas al fin de semana.
def update_finde(horas):
    n = len(horas)
    finde = [0]*n
  
    ht = 0
    for i in range (0, n): ht += horas[i]
    hf = int((ht*2)/7)

    if hf%2 != 0: hf -= 1
    
    i = n - 1
    while hf > 0:
        hf -= 2
        horas[i] -= 2
        finde[i] += 2
        i -= 1

    return finde
        

# Añadir 1 horas de estudio de asig en day.
def put1(asig, day, horario):
    for i in range(0, len(horario)):
        if horario[i][day] == -2:
            horario[i][day] = asig
            return True
                   
    return False


# Añadir 2 horas de estudio de asig en day.
def put2(asig, day, horario):
    for i in range(0, len(horario) - 1):
        if horario[i][day] == -2 and horario[i + 1][day] == -2:
            horario[i][day] = horario[i + 1][day] = asig
            return True
  
    return False;


# Retorna verdadero si un día está completo.
def complete(horario, day):
    n = len(horario)
    for i in range(0, n):
        if horario[i][day] == -2: return False
    return True


# Devuelve el día con menos horas de estudio no completo.
def next_minimum_uncomplete(horario, hras_est_dia):
    minDay = -1
    for day in range(0, 5):
        if not complete(horario, day) and (minDay == -1 or hras_est_dia[day] < hras_est_dia[minDay]):
            minDay = day

    return minDay


def distribute(horas, horario, finde):
    hras_est_dia = [0]*5
    n = len(horas) # Número de asignaturas.
  
    # En grupos de 2 horas.
    # Secuencia: Lunes, Miércoles, Viernes, Martes, Jueves.
    sec = [0, 2, 4, 1, 3]
    j = 0  # Iterador para la secuencia de días.
    for asig in range(0, n):
        exit = 0
        while horas[asig] > 1 and exit < 5:
            if j > 4: j = 0
            if put2(asig, sec[j], horario):
                horas[asig] -= 2
                hras_est_dia[sec[j]] += 2
            else: exit += 1
            j += 1

    # Para que no se quede una asignatura con más de 4 horas para el fin de semana.
    for asig in range(0, n):
        bug = 0 # Para evitar bucle infinito.
        while horas[asig] + finde[asig] > 4 and bug < 3:
            bug += 1
            day = next_minimum_uncomplete(horario, hras_est_dia)
            if day != -1 and put1(asig, day, horario):
                horas[asig] -= 1
                hras_est_dia[day] += 1

    # De 1 hora en 1 hora. Comenzando por los días con menos horas de estudio.
    for asig in range (0, n):
        finished = False
        while horas[asig] > 0 and not finished:
            day = next_minimum_uncomplete(horario, hras_est_dia)
            if day == -1: finished = True
            elif put1(asig, day, horario):
                horas[asig] -= 1
                hras_est_dia[day] += 1

    # Guardando las horas no asignadas en vector fin de semana.
    for i in range (0, n):
        finde[i] += horas[i]
        horas[i] = 0

        
def distribute_main(horas, asigs, horario):
    sort(horas, asigs)
    finde = update_finde(horas)
    sort(horas, asigs)
    distribute(horas, horario, finde)
    
    return finde;


# Input.
horas = [3, 5, 4, 5, 4, 4, 2]
asigs = ["DINAMICA", "ANALISIS REAL", "MECANICA", "TOPOLOGIA", "ECONOMIA", "ELECTROMAGNETISMO", "PROYECTO"]
horario = [
    [-1, -2, -1, -2, -1],
    [-2, -1, -2, -2, -2],
    [-1, -1, -2, -2, -1],
    [-1, -1, -1, -2, -1],
    [-1, -1, -1, -1, -2],
    [-2, -2, -2, -2, -2]
]

# Programa.
finde = distribute_main(horas, asigs, horario)

# Output codificado.
print("asigs: ", asigs)
print("finde: ", finde)
print("horario: ", horario)

# Output en tabla con nombre asignaturas.
matrix = horario
for i in range (0, len(horario)):
    for j in range(0, 5):
        k = horario[i][j]
        if k >= 0: matrix[i][j] = asigs[k]
        else: matrix[i][j] = k

print()
s = [[str(e) for e in row] for row in matrix]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print ('\n'.join(table))
