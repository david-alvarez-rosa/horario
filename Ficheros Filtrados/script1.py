import pandas as pd

dsele = pd.read_csv('sele1.csv')
dini = pd.read_csv('ini1.csv')
dnoini = pd.read_csv('noini1.csv')

dsele = dsele.drop_duplicates(['CODEX'],keep='last')
dsele = dsele.reset_index(drop=True)

dini = dini[dini['CODEX'].isin(dnoini.CODEX)]
dini = dini.reset_index(drop=True)
dnoini = dnoini[dnoini['CODEX'].isin(dini.CODEX)]
dnoini = dnoini.drop_duplicates(subset=['CODEX','CODASS'],keep = 'first')
dnoini = dnoini.reset_index(drop=True)



dsele.to_csv('sele2.csv',encoding='UTF-8',index=False)
dini.to_csv('ini2.csv',encoding='UTF-8',index=False)
dnoini.to_csv('noini2.csv',encoding='UTF-8',index=False)
    
