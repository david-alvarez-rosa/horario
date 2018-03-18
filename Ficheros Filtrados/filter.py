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
'''
comprovació:
    a = 0
    b = 3
    for e in dnoini.CODEX:
        if a == b:
            break
        else:
            a += 1
            print(dnoini[dnoini.CODEX == e])

merge dels 3 fitxers:
    >>> import pandas as pd
    >>> di = pd.read_csv('ini.csv')
    >>> dn = pd.read_csv('noini.csv')
    >>> ds = pd.read_csv('sele.csv')
    >>> d1 = pd.merge(di,dn, on=['CODEX','CODASS','NF'])
    >>> d2 = pd.merge(d1,dn,how = "outer")
'''
