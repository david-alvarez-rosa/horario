import pandas as pd

dsele = pd.read_csv('sele.csv')
dini = pd.read_csv('ini.csv')
dnoini = pd.read_csv('noini.csv')

dsele = dsele.drop_duplicates(['CODEX'],keep='last')
dsele = dsele.reset_index(drop=True)

dini = dini[dini['CODEX'].isin(dnoini.CODEX)]
dini = dini.drop_duplicates(subset=['CODEX','CODASS'],keep = 'first')
dini = dini.reset_index(drop=True)
dnoini = dnoini[dnoini['CODEX'].isin(dini.CODEX)]
dnoini = dnoini.drop_duplicates(subset=['CODEX','CODASS'],keep = 'first')
dnoini = dnoini.reset_index(drop=True)



dsele.to_csv('sele.csv',encoding='UTF-8',index=False)
dini.to_csv('ini.csv',encoding='UTF-8',index=False)
dnoini.to_csv('noini.csv',encoding='UTF-8',index=False)

d1 = pd.merge(di,ds, on='CODEX')
d2 = pd.merge(d1,dn,how = "outer")
d2.to_csv('merged_files.csv',encoding='UTF-8',index=False)
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
    >>> d1 = pd.merge(di,ds, on='CODEX')
    >>> d2 = pd.merge(d1,dn,how = "outer")
    >>> d2.to_csv('merged_files.csv',encoding='UTF-8',index=False)


dini.loc[dini.CODASS==240012,['CODEX','NF']] #mirar assignatura 240012
	CODEX	NF
0	247426	4.0
1	244339	5.5
2	245218	7.0
3	245516	5.9
4	246370	7.2
5	246767	5.0
6	243050	7.2

di.loc[(di.CODASS==240012) & (di.NF == 7.0),['CODEX','NF']]
        CODEX	NF
2	245218	7.0
17	245344	7.0
18	247256	7.0
43	248338	7.0
61	244533	7.0
428	261169	7.0


a = di.loc[(di.CODASS==240012) & (di.NF < 7.0),['CODEX','NF']] #entre 6 i 7
a.loc[a.NF > 6.0,['CODEX','NF']]
    CODEX	NF
31	245418	6.1
32	244458	6.6
67	245377	6.6
68	244905	6.8
100	245181	6.3
101	244060	6.5
363	261734	6.6
378	259899	6.5

####### CLUSTER PER UNA ASSIGNATURA #########
--------retorna llista de codex de gent de la assignatura
        amb nota +- 0.5 de la nota entrada --------------
def cluster(codass, nota):
    #di = pd.read_csv('ini1.csv')
    llista = []
    a = di.loc[(di.CODASS==codass) & (di.NF < nota + 0.5),['CODEX','NF']]
    b = a.loc[a.NF > nota - 0.5,['CODEX','NF']]
    for codex in b.CODEX:
        llista += [codex]
    return llista
########################## FER TAULA ##########
df = pd.read_csv('ini.csv')
#df = df.drop_duplicates(subset=['CODEX','CODASS'],keep = 'first')
df = df.pivot(index="CODEX",columns="CODASS",values="NF")

CODASS	240011	240012	240013	240014	240015	240021	240022	240023	240024	240025
CODEX										
226431	NaN	NaN	NaN	NaN	NaN	5.0	NaN	3.0	NaN	8.0
226464	NaN	NaN	7.0	NaN	NaN	5.3	NaN	5.1	NaN	NaN
226467	7.1	NaN	5.0	NaN	NaN	2.5	7.2	0.8	4.7	NaN
226494	NaN	NaN	NaN	NaN	7.3	NaN	NaN	NaN	NaN	5.2
226495	NaN	NaN	NaN	NaN	7.3	NaN	NaN	NaN

#df = df.pivot_table(values ='NF', index='CODEX',columns='CODASS',fill_value=0)
    
'''
