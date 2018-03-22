import pandas as pd
d = pd.read_csv('ini.csv')
dn = pd.read_csv('noini.csv')
ds = pd.read_csv('sele.csv')
#d = pd.merge(pd.merge(d,ds, on = 'CODEX'),dn, how='outer')


listAss=['Algebra','Calcul1','MecFon','Quim1','Info1',
     'Geom','Calcul2','TermoFon','Quim2','Expre']

Ass={'Algebra':240011,'Calcul1':240012,'MecFon':240013,'Quim1':240014,'Info1':240015,
     'Geom':240021,'Calcul2':240022,'TermoFon':240023,'Quim2':240024,'Expre':240025}


def KMeans(k, n_alg, n_calc1, n_mecfon, n_quim1, n_info1, n_geo, n_calc2, n_termo, n_quim2, n_expre, a1=0, a2 = 0, a3 = 0, a4 = 0, a5 = 0, a6 = 0, a7 = 0, a8 = 0):
    #a1,a2,a3.. son codis de assignatures matriculades
    dic = genera_dic(a1, a2, a3, a4, a5, a6, a7, a8)
    dic[0] = {'240011':n_alg, '240012':n_calc1, '240013':n_mecfon, '240014':n_quim1, '240015':n_info1, '240021':n_geo, '240022':n_calc2, '240023':n_termo, '240024':n_quim2, '240025':n_expre}
    scores=[(sim_distance(dic,0,other),other) for other in dic if other !=0]
    scores.sort()
    return scores[0:k]

def genera_dic(a1, a2, a3, a4, a5, a6, a7, a8):
    n = 0
    llista_as = [a1, a2, a3, a4, a5, a6, a7, a8]
    for a in llista_as:
        if a != 0: n += 1
    if n == 0: dic = crea_dict()
    elif n == 1: dic = crea_dict1(a1)
    elif n == 2: dic = crea_dict2(a1, a2)
    elif n == 3: dic = crea_dict3(a1, a2, a3)
    elif n == 4: dic = crea_dict4(a1, a2, a3, a4)
    elif n == 5: dic = crea_dict5(a1, a2, a3, a4, a5)
    elif n == 6: dic = crea_dict6(a1, a2, a3, a4, a5, a6)
    elif n == 7: dic = crea_dict7(a1, a2, a3, a4, a5, a6, a7)
    elif n == 8: dic = crea_dict8(a1, a2, a3, a4, a5, a6, a7, a8)
    return dic

def sim_distance(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0: 
        return 0
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])   
    return sum_of_squares

####################################################################################################################################
########## 1 assignatura com input ###############
def crea_dict1(a1):
    #faltar ampliar el d = d[..|..|] amb les assignatures input ! i d ha de ser el merge!
    d = pd.read_csv('ini.csv')
    dic={} 
    d = d[(d['CODASS']==240011)|(d['CODASS']==240012)|(d['CODASS']==240013) \
          |(d['CODASS']==240014)|(d['CODASS']==240015)|(d['CODASS']==240021)\
          |(d['CODASS']==240022)|(d['CODASS']==240023)|(d['CODASS']==240024)\
          |(d['CODASS']==240025)|(d['CODASS']==a1)]
    for e in d.CODEX:
        keyslist = d[d['CODEX']==e]['CODASS']
        valueslist=d[d['CODEX']==e]['NF']
        table = dict(zip(keyslist,valueslist))
        if len(table)==11:
            dic[e]=table
    return dic

########## 2 assignatures com input ###############
def crea_dict2(a1, a2):
    #faltar ampliar el d = d[..|..|] amb les assignatures input ! i d ha de ser el merge!
    d = pd.read_csv('ini.csv')
    dic={} 
    d = d[(d['CODASS']==240011)|(d['CODASS']==240012)|(d['CODASS']==240013) \
          |(d['CODASS']==240014)|(d['CODASS']==240015)|(d['CODASS']==240021)\
          |(d['CODASS']==240022)|(d['CODASS']==240023)|(d['CODASS']==240024)\
          |(d['CODASS']==240025)|(d['CODASS']==a1)|(d['CODASS']==a2)]
    for e in d.CODEX:
        keyslist = d[d['CODEX']==e]['CODASS']
        valueslist=d[d['CODEX']==e]['NF']
        table = dict(zip(keyslist,valueslist))
        if len(table)==12:
            dic[e]=table
    return dic

########## 3 assignatures com input ###############
def crea_dict3(a1, a2, a3):
    #faltar ampliar el d = d[..|..|] amb les assignatures input ! i d ha de ser el merge!
    d = pd.read_csv('ini.csv')
    dic={} 
    d = d[(d['CODASS']==240011)|(d['CODASS']==240012)|(d['CODASS']==240013) \
          |(d['CODASS']==240014)|(d['CODASS']==240015)|(d['CODASS']==240021)\
          |(d['CODASS']==240022)|(d['CODASS']==240023)|(d['CODASS']==240024)\
          |(d['CODASS']==240025)|(d['CODASS']==a1)|(d['CODASS']==a2)|(d['CODASS']==a3)]
    for e in d.CODEX:
        keyslist = d[d['CODEX']==e]['CODASS']
        valueslist=d[d['CODEX']==e]['NF']
        table = dict(zip(keyslist,valueslist))
        if len(table)==13:
            dic[e]=table
    return dic

########## 4 assignatures com input ###############
def crea_dict4(a1, a2, a3, a4):
    #faltar ampliar el d = d[..|..|] amb les assignatures input ! i d ha de ser el merge!
    d = pd.read_csv('ini.csv')
    dic={} 
    d = d[(d['CODASS']==240011)|(d['CODASS']==240012)|(d['CODASS']==240013) \
          |(d['CODASS']==240014)|(d['CODASS']==240015)|(d['CODASS']==240021)\
          |(d['CODASS']==240022)|(d['CODASS']==240023)|(d['CODASS']==240024)\
          |(d['CODASS']==240025)|(d['CODASS']==a1)|(d['CODASS']==a2)|(d['CODASS']==a3)|(d['CODASS']==a4)]
    for e in d.CODEX:
        keyslist = d[d['CODEX']==e]['CODASS']
        valueslist=d[d['CODEX']==e]['NF']
        table = dict(zip(keyslist,valueslist))
        if len(table)==14:
            dic[e]=table
    return dic

########## 5 assignatures com input ###############
def crea_dict5(a1, a2, a3, a4, a5):
    #faltar ampliar el d = d[..|..|] amb les assignatures input ! i d ha de ser el merge!
    d = pd.read_csv('ini.csv')
    dic={} 
    d = d[(d['CODASS']==240011)|(d['CODASS']==240012)|(d['CODASS']==240013) \
          |(d['CODASS']==240014)|(d['CODASS']==240015)|(d['CODASS']==240021)\
          |(d['CODASS']==240022)|(d['CODASS']==240023)|(d['CODASS']==240024)\
          |(d['CODASS']==240025)|(d['CODASS']==a1)|(d['CODASS']==a2)|(d['CODASS']==a3)\
          |(d['CODASS']==a4)|(d['CODASS']==a5)]
    for e in d.CODEX:
        keyslist = d[d['CODEX']==e]['CODASS']
        valueslist=d[d['CODEX']==e]['NF']
        table = dict(zip(keyslist,valueslist))
        if len(table)==15:
            dic[e]=table
    return dic

########## 6 assignatures coo input ###############
def crea_dict6(a1, a2, a3, a4, a5, a6):
    #faltar ampliar el d = d[..|..|] amb les assignatures input ! i d ha de ser el merge!
    d = pd.read_csv('ini.csv')
    dic={} 
    d = d[(d['CODASS']==240011)|(d['CODASS']==240012)|(d['CODASS']==240013) \
          |(d['CODASS']==240014)|(d['CODASS']==240015)|(d['CODASS']==240021)\
          |(d['CODASS']==240022)|(d['CODASS']==240023)|(d['CODASS']==240024)\
          |(d['CODASS']==240025)|(d['CODASS']==a1)|(d['CODASS']==a2)|(d['CODASS']==a3)\
          |(d['CODASS']==a4)|(d['CODASS']==a5)|(d['CODASS']==a6)]
    for e in d.CODEX:
        keyslist = d[d['CODEX']==e]['CODASS']
        valueslist=d[d['CODEX']==e]['NF']
        table = dict(zip(keyslist,valueslist))
        if len(table)==16:
            dic[e]=table
    return dic

########## 7 assignatures com input ###############
def crea_dict7(a1, a2, a3, a4, a5, a6, a7):
    #faltar ampliar el d = d[..|..|] amb les assignatures input ! i d ha de ser el merge!
    d = pd.read_csv('ini.csv')
    dic={} 
    d = d[(d['CODASS']==240011)|(d['CODASS']==240012)|(d['CODASS']==240013) \
          |(d['CODASS']==240014)|(d['CODASS']==240015)|(d['CODASS']==240021)\
          |(d['CODASS']==240022)|(d['CODASS']==240023)|(d['CODASS']==240024)\
          |(d['CODASS']==240025)|(d['CODASS']==a1)|(d['CODASS']==a2)|(d['CODASS']==a3)\
          |(d['CODASS']==a4)|(d['CODASS']==a5)|(d['CODASS']==a6)|(d['CODASS']==a7)]
    for e in d.CODEX:
        keyslist = d[d['CODEX']==e]['CODASS']
        valueslist=d[d['CODEX']==e]['NF']
        table = dict(zip(keyslist,valueslist))
        if len(table)==17:
            dic[e]=table
    return dic

########## 8 assignatures com input ###############
def crea_dict8(a1, a2, a3, a4, a5, a6, a7, a8):
    #faltar ampliar el d = d[..|..|] amb les assignatures input ! i d ha de ser el merge!
    d = pd.read_csv('ini.csv')
    dic={} 
    d = d[(d['CODASS']==240011)|(d['CODASS']==240012)|(d['CODASS']==240013) \
          |(d['CODASS']==240014)|(d['CODASS']==240015)|(d['CODASS']==240021)\
          |(d['CODASS']==240022)|(d['CODASS']==240023)|(d['CODASS']==240024)\
          |(d['CODASS']==240025)|(d['CODASS']==a1)|(d['CODASS']==a2)|(d['CODASS']==a3)\
          |(d['CODASS']==a4)|(d['CODASS']==a5)|(d['CODASS']==a6)|(d['CODASS']==a7)|(d['CODASS']==a8)]
    for e in d.CODEX:
        keyslist = d[d['CODEX']==e]['CODASS']
        valueslist=d[d['CODEX']==e]['NF']
        table = dict(zip(keyslist,valueslist))
        if len(table)==18:
            dic[e]=table
    return dic

########## 0 assignatura com input ###############
def crea_dict():
    #faltar ampliar el d = d[..|..|] amb les assignatures input ! i d ha de ser el merge!
    d = pd.read_csv('ini.csv')
    dic={} 
    d = d[(d['CODASS']==240011)|(d['CODASS']==240012)|(d['CODASS']==240013) \
          |(d['CODASS']==240014)|(d['CODASS']==240015)|(d['CODASS']==240021)\
          |(d['CODASS']==240022)|(d['CODASS']==240023)|(d['CODASS']==240024)\
          |(d['CODASS']==240025)]
    for e in d.CODEX:
        keyslist = d[d['CODEX']==e]['CODASS']
        valueslist=d[d['CODEX']==e]['NF']
        table = dict(zip(keyslist,valueslist))
        if len(table)==10:
            dic[e]=table
    return dic



    
    

