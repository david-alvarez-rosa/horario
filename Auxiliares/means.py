import pandas as pd


# Abrir fichero de asignaturas y datos.
dfdata = pd.read_csv('data.csv')
dfasigs = pd.read_csv('asignaturas.csv')

# Para cada asignatura, calcular la media y guardarla en vector de medias.
mean = []
for codass in dfasigs['CODASS']:
    mean_codass = dfdata[dfdata['CODASS'] == codass]['NF'].mean()    
    mean.append(mean_codass)

# Añadir vector de medias como columna de Nota Media (NM) en fichero de asignaturas.
dfasigs['NM'] = mean

# Guardar archivo.
dfasigs.to_csv('asignaturas.csv', encoding='UTF-8', index=False)
