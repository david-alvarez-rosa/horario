import pandas as pd
d = pd.read_csv('ini.csv')
dn = pd.read_csv('noini.csv')
ds = pd.read_csv('sele.csv')
#d = pd.merge(pd.merge(d,ds, on = 'CODEX'),dn, how='outer')

def KMeans(k, a1, nota_a1, a2 = 0, nota_a2 = 0, a3 = 0, nota_a3 = 0, a4 = 0, nota_a4 = 0, a5 = 0, nota_a5 = 0, a6 = 0, nota_a6 = 0, a7 = 0, nota_a7 = 0, a8 = 0, nota_a8 = 0):
    dic = genera_dic(a1, a2, a3, a4, a5, a6, a7, a8)
    afegeix_al_dic(dic,a1, nota_a1, a2, nota_a2, a3, nota_a3, a4, nota_a4, a5, nota_a5, a6, nota_a6, a7, nota_a7, a8, nota_a8)
    for codex in dic:
        for codass in dic[codex]:
            if codass == 0: dic.pop(codex,None)
    scores=[(sim_distance(dic,'client',other),other) for other in dic if other !=0]
    scores.sort()
    return scores[0:k]

def genera_dic(a1, a2=0, a3=0, a4=0, a5=0, a6=0, a7=0, a8=0):
    n = 0
    llista_as = [a1, a2, a3, a4, a5, a6, a7, a8]
    for a in llista_as:
        if a != 0: n += 1
    if n == 1: dic = crea_dict1(a1)
    elif n == 2: dic = crea_dict2(a1, a2)
    elif n == 3: dic = crea_dict3(a1, a2, a3)
    elif n == 4: dic = crea_dict4(a1, a2, a3, a4)
    elif n == 5: dic = crea_dict5(a1, a2, a3, a4, a5)
    elif n == 6: dic = crea_dict6(a1, a2, a3, a4, a5, a6)
    elif n == 7: dic = crea_dict7(a1, a2, a3, a4, a5, a6, a7)
    elif n == 8: dic = crea_dict8(a1, a2, a3, a4, a5, a6, a7, a8)
    return dic
        
def afegeix_al_dic(dic,a1, nota_a1, a2, nota_a2, a3, nota_a3, a4, nota_a4, a5, nota_a5, a6, nota_a6, a7, nota_a7, a8, nota_a8):
    dic['client'] = {a1:nota_a1, a2:nota_a2, a3:nota_a3, a4:nota_a4, a5:nota_a5, a6:nota_a6, a7:nota_a7, a8:nota_a8}  

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



    
    

