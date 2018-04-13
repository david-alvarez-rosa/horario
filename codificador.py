import pandas as pd


# Dado un vector de CODASS, devuelve un vector con los nombres de las asignaturas.
# Precondición: el vector de CODASS tiene que estar ordenado.
def decoder(codass):
    df = pd.read_csv('Ficheros/asignaturas.csv')
    df = df[df['CODASS'].isin(codass)]
    df = df.reset_index(drop = True)
    names = []
    for i in range(0, len(df)):
        names.append(df['NOMBRE'].iloc[i])
    return names


# Dado un vector de nombres de asignaturas, devuelve un vector con los CODASS.
def encoder(names):
    df = pd.read_csv('Ficheros/asignaturas.csv')
    df = df[df['NOMBRE'].isin(names)]
    df = df.reset_index(drop = True)
    codass = []
    for i in range(0, len(df)):
        codass += df[df['NOMBRE'] == names[i]]['CODASS'].values.tolist()
    return codass
