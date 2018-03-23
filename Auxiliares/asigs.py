# Guardar créditos de las asignaturas de la fase no inicial.

import pandas as pd

# Leer archivo con asignaturas (CODASS y CR).
dani = pd.read_csv('asigsnoini.csv')

# Leer archivo con todas las asignaturas (CODASS y NOMBRE).
da = pd.read_csv('asignaturas.csv')

# Eliminar duplicados.
dani = dani.drop_duplicates(['CODASS'])
dani = dani.reset_index(drop=True)

# Eliminar asignaturas con códigos con letras.
dani = dani[dani.CODASS.str.contains("A") == False]
dani = dani[dani.CODASS.str.contains("E") == False]
dani = dani.reset_index(drop=True)

# Poner el número de créditos en fichero con nombre de asignaturas.
da = pd.merge(da, dani, on = 'CODASS', how = 'left')

# Ordenar por CODASS.
da = da.sort_values(by = ['CODASS'])

# Guardar archivo.
da.to_csv('asignaturas.csv', encoding='UTF-8', index=False)
