import pandas as pd

# Abrir ficheros a unir.
dsele = pd.read_csv('sele.csv')
dini = pd.read_csv('ini.csv')
dnoini = pd.read_csv('noini.csv')

# Eliminar asignaturas con CODASS con letras.
dnoini = dnoini[dnoini.CODASS.str.contains("A") == False]
dnoini = dnoini[dnoini.CODASS.str.contains("E") == False]
dnoini = dnoini.reset_index(drop=True)

# Merge en dos pasos.
dfm = pd.merge(dini, dnoini, how = 'outer')
dfm = pd.merge(dsele, dfm, on = 'CODEX')

# Ordenar archivo unido por CODEX y cuando coincida por CODASS.
dfm = dfm.sort_values(by = ['CODEX', 'CODASS'])

# Guardar archivo unido.
dfm.to_csv('data.csv', encoding='UTF-8', index=False)
