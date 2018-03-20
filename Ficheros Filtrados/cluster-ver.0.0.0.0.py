import pandas as pd
df = pd.read_csv('ini.csv')
di = pd.read_csv('ini.csv')
dn = pd.read_csv('noini.csv')
ds = pd.read_csv('sele.csv')
d = pd.merge(pd.merge(di,ds, on = 'CODEX'),dn, how='outer')

#d[d.CODASS == 240011] comprovacio que agafa assig del q1
#d[d.CODASS == 240131] comprovacio que agafa assig > 1r

def crea_dict():
    #faltar ampliar el d = d[..|..|] amb les assignatures input ! i
    # i el dataframe "d" ha de ser el merge ben fet!
    dic={} 
    d = pd.read_csv('ini.csv')
    dn = pd.read_csv('noini.csv')
    ds = pd.read_csv('sele.csv')
    #d = pd.merge(pd.merge(di,ds, on = 'CODEX'),dn, how='outer')
    d = d[(d['CODASS']==240011)|(d['CODASS']==240012)|(d['CODASS']==240013) \
          |(d['CODASS']==240014)|(d['CODASS']==240015)|(d['CODASS']==240021)\
          |(d['CODASS']==240022)|(d['CODASS']==240023)|(d['CODASS']==240024)\
          |(d['CODASS']==240025)]
    for e in d.CODEX:
        keyslist = d[d['CODEX']==e]['CODASS']
        valueslist=d[d['CODEX']==e]['NF']
        table = dict(zip(keyslist,valueslist))
        if len(table)==10:#atencio que aquest valor canvia segons el nº d'assigantures
            dic[e]=table
    return dic

dic = crea_dict()
dic[245218]#exemple
#out
#{240011: 7.0,
# 240012: 7.0,
# 240013: 6.5,
# 240014: 6.0,
# 240015: 7.6,
# 240021: 7.6,
# 240022: 7.5,
# 240023: 7.7,
# 240024: 6.6,
# 240025: 6.0}

def sim_distance(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0: 
        return 0
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])   
    return sum_of_squares

scores=[(sim_distance(dic,245218,other),other) for other in dic if other !=0]
scores.sort()
scores[0:4]#4 veins
#out
#[(0.0, 245218),
# (2.1900000000000004, 244005),
# (3.0600000000000005, 243582),
# (3.17, 244406)]
