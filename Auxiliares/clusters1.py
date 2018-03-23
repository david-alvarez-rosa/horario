import pandas as pd

def cluster(codass, nota):
    #di = pd.read_csv('ini1.csv')
    llista = []
    a = di.loc[(di.CODASS==codass) & (di.NF < nota + 0.5),['CODEX','NF']]
    b = a.loc[a.NF > nota - 0.5,['CODEX','NF']]
    for codex in b.CODEX:
        llista += [codex]
    return llista
        
    
    
    
