""" conjugate_from_bases.py
"""
import sys
sys.path.append('../bases')
import benedictive
import perfect_join
from perfect_3p import perfect_3p_dict
from conjugation_join_simple import conjugation_join_simple
import class_2_special
import class_3_special
import class_5_special
special_tenses = ['pre','ipf','ipv','opt']   
general_tenses = ['ppf','prf','fut','con','pft','ben']
all_tenses = special_tenses + general_tenses
tenses_sl_test2 =  {
  "pre":"law",
  "ipf":"laN",
  "ipv":"low",
  "opt":"viDiliN",
  "ppf":"liw-p",
  "prf":"liw-r",
  "fut":"lfw",
  "con":"lfN",
  "pft":"luw",
  "ben":"ASIrliN",
  "aor1":"luN1",
  "aor2":"luN2",
  "aor3":"luN3",
  "aor4":"luN4",
  "aor5":"luN5",
  "aor6":"luN6",
  "aor7":"luN7"
 }
class ConjTable(object):
 def __init__(self,root,theclass,amp_voice,tense,base,dbg=False,upasargas=[]):
  """  root : string, MW spelling
       theclass: string, '1' to '10'
       amp_voice: string 
          'a' : active voice (Parasmaipada)
          'm' : middle voice (Atmanepada)
          'p' : passive voice
       tense: string - one of the keys of all_tenses
       upasargas:  a list of upasargas (e.g. ['pra','vi']).
                   There are a few situations (e.g. in passive) where
                   the base varies if there are upasargas present.
                   This situation needs to be further explored (11-20-2019)
  """
  self.root = root
  self.theclass = theclass
  self.amp_voice = amp_voice
  self.tense = tense
  self.base = base
  self.dbg = dbg
  self.status = True
  # Each table is a list of strings; 
  self.table = []
  if (self.tense in special_tenses):
   if self.amp_voice == 'p':
    self.inflect_special_tense()
   elif self.theclass in ['1','4','6','10']:
    # same routine name as above
    self.inflect_special_tense()
   elif self.theclass == '2':
    self.inflect_special_tense_2()
   elif self.theclass == '3':
    self.inflect_special_tense_3()
   elif self.theclass == '5':
    self.inflect_special_tense_5()
   else:
    # can't do other classes yet
    self.status = False
  elif self.tense == 'fut':
   self.inflect_future()
  elif self.tense == 'pft':
   self.inflect_pft()
  elif self.tense == 'con':
   self.inflect_con()
  elif self.tense == 'ben':
   self.inflect_ben()
   #if True:
   # print(self.root,self.amp_voice,self.table[0])
  elif self.tense == 'ppf':
   self.inflect_ppf()
  elif self.tense == 'prf':
   self.inflect_prf()

 def inflect_special_tense_2(self):
  """ Use precomputed values
  """
  d = class_2_special.d
  model = ','.join([self.theclass,self.amp_voice,self.tense])
  key = (model,self.root)
  if key in d:
   tables = d[key]
   # tables is a list of conjugation tables.
   # We don't know how to handle more than 1!
   if len(tables) == 0:
    print('WARNING: conjugate_from_bases.inflect_special_tense_2: No table.',   key)
    self.status = False
    return
   if len(tables) > 1:
    print('WARNING: conjugate_from_bases.inflect_special_tense_2: multiple tables',   key)
   # use only the 1st table (assume tables not empty list!)
   self.table = tables[0]

 def inflect_special_tense_3(self):
  """ Use precomputed values; a close variant of inflect_special_tense_2
  """
  d = class_3_special.d
  model = ','.join([self.theclass,self.amp_voice,self.tense])
  key = (model,self.root)
  if key in d:
   tables = d[key]
   # tables is a list of conjugation tables.
   # We don't know how to handle more than 1!
   if len(tables) == 0:
    print('WARNING: conjugate_from_bases.inflect_special_tense_3: No table.',   key)
    self.status = False
    return
   if len(tables) > 1:
    print('WARNING: conjugate_from_bases.inflect_special_tense_3: multiple tables',   key)
   # use only the 1st table (assume tables not empty list!)
   self.table = tables[0]

 def inflect_special_tense_5(self):
  """ Use precomputed values; a close variant of inflect_special_tense_2
  """
  d = class_5_special.d
  model = ','.join([self.theclass,self.amp_voice,self.tense])
  key = (model,self.root)
  if key in d:
   tables = d[key]
   # tables is a list of conjugation tables.
   # We don't know how to handle more than 1!
   if len(tables) == 0:
    print('WARNING: conjugate_from_bases.inflect_special_tense_5: No table.',   key)
    self.status = False
    return
   if len(tables) > 1:
    print('WARNING: conjugate_from_bases.inflect_special_tense_5: multiple tables',   key)
   # use only the 1st table (assume tables not empty list!)
   self.table = tables[0]

 def inflect_special_tense(self):
  """ tense pre, ipf, ipv, opt  only for class 2
  """
  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   'pre-a': 'ati:ataH:anti:asi:aTaH:aTa:Ami:AvaH:AmaH',
   'pre-m':'ate:ete:ante:ase:eTe:aDve:e:Avahe:Amahe',
   'ipf-a':'at:atAm:an:aH:atam:ata:am:Ava:Ama',
   'ipf-m':'ata:etAm:anta:aTAH:eTAm:aDvam:e:Avahi:Amahi',
   'ipv-a':'atu:atAm:antu:a:atam:ata:Ani:Ava:Ama',
   'ipv-m':'atAm:etAm:antAm:asva:eTAm:aDvam:E:AvahE:AmahE',
   'opt-a':'et:etAm:eyuH:eH:etam:eta:eyam:eva:ema',
   'opt-m':'eta:eyAtAm:eran:eTAH:eyATAm:eDvam:eya:evahi:emahi'
  }
  if self.amp_voice == 'p': # passive
   # use endings of class 4, m (middle) voice
   self.sup = supdict[self.tense + '-' + 'm']
  else:
   try:
    self.sup = supdict[self.tense + '-' + self.amp_voice]
   except:
    self.sup = ''
  if self.sup != '':
   sups = self.getsups()
   self.table = [conjugation_join_simple(self.base,sup) for sup in sups]

 def unused_inflect_special_tense_2(self):
  """ tense pre, ipf, ipv, opt
   get values from a file
  """

  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   'pre-a':'ti:taH:anti:si:TaH:Ta:mi:vaH:maH',
   'pre-m':'te:Ate:ate:se:ATe:Dve:e:vahe:mahe',
   'ipf-a':'t:tAm:an:s:tam:ta:am:va:ma',
   'ipf-m':'ta:AtAm:ata:TAH:ATAm:Dvam:i:vahi:mahi',
   'ipv-a':'tu:tAm:antu:hi:tam:ta:Ani:Ava:Ama',
   'ipv-m':'Am:AtAm:atAm:sva:ATAm:Dvam:E:AvahE:AmahE',
   'opt-a':'yAt:yAtAm:yuH:yAH:yAtam:yAta:yAm:yAva:yAma',
   'opt-m':'Ita:IyAtAm:Iran:ITAH:IyATAm:IDvam:Iya:Ivahi:Imahi'
  }
  strengthdict = {
   'pre-a':'S:W:W:S:W:W:S:W:W',
   'pre-m':'W:W:W:W:W:W:W:W:W',
   'ipf-a':'S:W:W:S:W:W:S:W:W',
   'ipf-m':'W:W:W:W:W:W:W:W:W',
   'ipv-a':'S:W:W:W:W:W:S:S:S',
   'ipv-m':'W:W:W:W:W:W:S:S:S',
   'opt-a':'W:W:W:W:W:W:W:W:W',
   'opt-m':'W:W:W:W:W:W:W:W:W'
  }
  self.sup = supdict[self.tense + '-' + self.amp_voice]
  sups = self.getsups()
  self.strength = strengthdict[self.tense + '-' + self.amp_voice]
  strengths = self.strength.split(':') 
  for isup,sup in enumerate(sups):
   strength = strengths[isup]
   infl = conjugation_join_2(self.root,sup,strength,isup,self.amp_voice,self.tense)
   self.table.append(infl)
  self.table = [conjugation_join_simple(self.base,sup) for sup in sups]

 def inflect_future(self):
  """ tense fut
  """ 
  # from init.py
  #lfw-1-p=syati:syataH:syanti:syasi:syaTaH:syaTa:syAmi:syAvaH:syAmaH
  #lfw-1-p-strengths=S:S:S:S:S:S:S:S:S
  #lfw-1-a=syate:syete:syante:syase:syeTe:syaDve:sye:syAvahe:syAmahe
  #lfw-1-a-strengths=S:S:S:S:S:S:S:S:S
  # all strengths are 'S' (strong)
  """
  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   'fut-a':'syati:syataH:syanti:syasi:syaTaH:syaTa:syAmi:syAvaH:syAmaH',
   'fut-m':'syate:syete:syante:syase:syeTe:syaDve:sye:syAvahe:syAmahe'
  }
  """
  """ change so that 'sy' is part of the base"""
  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   'fut-a':'ati:ataH:anti:asi:aTaH:aTa:Ami:AvaH:AmaH',
   'fut-m':'ate:ete:ante:ase:eTe:aDve:e:Avahe:Amahe'
  }
  self.sup = supdict[self.tense + '-' + self.amp_voice]
  sups = self.getsups()
  tab = []
  for sup in sups:
   t = self.base + sup  #self.future_join(self.base,sup)
   tab.append(t)
  self.table = tab

 def inflect_pft(self):
  """ tense pft (periphrastic future)
  """ 
  # from init.py
  #luw-1-p=tA:tArO:tAraH:tAsi:tAsTaH:tAsTa:tAsmi:tAsvaH:tAsmaH
  #luw-1-a=tA:tArO:tAraH:tAse:tAsATe:tADve:tAhe:tAsvahe:tAsmahe
  # all strengths are 'S' (strong)
  #Since all ending start with 't', and we are using for a base
  #the infinitive minus ending 'um' (i.e., the 't' is already in the base),
  # we drop the initial 't' in our endings
  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   'pft-a':'A:ArO:AraH:Asi:AsTaH:AsTa:Asmi:AsvaH:AsmaH',
   'pft-m':'A:ArO:AraH:Ase:AsATe:ADve:Ahe:Asvahe:Asmahe'
  }
  self.sup = supdict[self.tense + '-' + self.amp_voice]
  sups = self.getsups()
  tab = []
  for sup in sups:
   t = self.base + sup 
   tab.append(t)
  self.table = tab

 def inflect_con(self):
  """ tense con (conditional mood).
      Use endings of imperfect tense. Per Deshpande p. 327
  """ 
  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   'con-a':'at:atAm:an:aH:atam:ata:am:Ava:Ama',
   'con-m':'ata:etAm:anta:aTAH:eTAm:aDvam:e:Avahi:Amahi',
  }
  self.sup = supdict[self.tense + '-' + self.amp_voice]
  sups = self.getsups()
  tab = []
  for sup in sups:
   t = self.base + sup 
   tab.append(t)
  self.table = tab

 def inflect_ben(self):
  """ tense ben (benedictive mood).
      Use endings of imperfect tense. Per Deshpande p. 327
  """ 
  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   'ben-a':'yAt:yAstAm:yAsuH:yAH:yAstam:yAsta:yAsam:yAsva:yAsma',
   'ben-m':'sIzwa:sIyAstAm:sIran:sIzWAH:sIyAsTAm:sIDvam:sIya:sIvahi:sImahi',
  }
  self.sup = supdict[self.tense + '-' + self.amp_voice]
  sups = self.getsups()
  if (self.amp_voice == 'm'):
   # sometimes, the initial 's' of the ben-m endings becomes 'z'
   # This information is in the benedictive database
   # and we adjust the 'sups' array accordingly
   d = benedictive.d
   key = (self.root,self.amp_voice)
   if key not in d:
    # We don't know anything of this
    return
   rec = d[key]
   knownbases = rec.bases
   ibase = -1
   for ib,b in enumerate(knownbases):
    if b == self.base:
     ibase = ib
     break
   if ibase == -1:
    # we don't know anything about this 
    return
   sup0 = rec.zs[ibase] 
   sups = [sup0 + sup[1:] for sup in sups]
  # now join base to sups
  tab = []
  for sup in sups:
   t = self.base + sup 
   tab.append(t)
  self.table = tab

 def inflect_ppf(self):
  """ tense ppf (periphrastic perfect).
      Our base is the periphrastic action noun, e.g. arTayAm, IkzAm, etc.
      The conjugation table joins this to the reduplicated perfect of
      either the root kf, as, or BU.  
      The following code uses only the reduplicated perfect of 'kf'.
  """ 
  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   'ppf-a':'cakAra:cakratuH:cakruH:cakarTa:cakraTuH:cakra:cakara:cakfva:cakfma',
   'ppf-m':'cakre:cakrAte:cakrire:cakfze:cakrATe:cakfQve:cakre:cakfvahe:cakfmahe',
  }
  self.sup = supdict[self.tense + '-' + self.amp_voice]
  sups = self.getsups()
  tab = []
  for sup in sups:
   # base (periphrastic action noun) ends in 'm'
   # join to sup using homorganic nasal
   if self.base.endswith('m') and sup.startswith('c'):
    t = self.base[0:-1] + 'Y' + sup 
    tab.append(t)
   else:  
    print('conjugate_from_bases ERROR:',self.base,self.voice,sup)
    self.table = []
    return
  self.table = tab
  #if True:
  # model = ','.join([self.theclass,self.amp_voice,self.tense])
  # print(model,self.root,self.table[0]) #self.table[1],self.table[2])

 def inflect_prf(self):
  """ tense prf (reduplicative perfect).
      Our 'base' contains 4 elements, as generated by active_prf in
      bases/bases_test2.py
   - bs: the reduplicated base to be used before strong endings
      namely, the singular parasmaipada (active voice) endings
      (i.e., sup index is 0,3,6 : see supdict below)
   - bw: the reduplicated base to be used before weak endings 
      namely, all the other endings
   - sc1: The 'sew_code' relevant for all endings EXCEPT the ending 'Ta' of
     the 2nd person singular active voice ending
   - sc2: The 'sew_code' relevant for all other endings.

  """ 
  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   'prf-a':'a:atuH:uH:Ta:aTuH:a:a:va:ma',
   'prf-m':'e:Ate:ire:se:ATe:Dve:e:vahe:mahe',
  }
  self.sup = supdict[self.tense + '-' + self.amp_voice]
  sups = self.getsups()
  tab = []
  
  bs,bw,sc1,sc2 = self.base.split(',')
  v = self.amp_voice
  for isup,sup in enumerate(sups):
   if (v == 'a') and (isup in [0,3,6]):
    b = bs
    strong = True
   else:
    b = bw
    strong = False
   if (v == 'a') and (isup == 3):
    # active voice, 2nd person singular
    sc = sc2
   else:
    sc = sc1
   tarr = perfect_join.perfect_join(self.root,isup,b,sc,sup,strong) 
   try:
    t = '/'.join(tarr)
   except:
    print('tarr = ',tarr)
    exit(1)
   tab.append(t)
  self.table = tab
  if True:
   model = ','.join([self.theclass,self.amp_voice,self.tense])  
   key = '%s %s' % (model,self.root)
   p3vals = ' '.join([self.table[0],self.table[1],self.table[2]])
   status = self.get_prf_p3_status(key,p3vals)
   if status != 'OK':
    print('conjugate_from_bases. Perfect tense Warning:',key,p3vals,'   %s   '%status,self.base) 


 def get_prf_p3_status(self,key,p3vals):
  known_prf_p3 = perfect_3p_dict
  if (key in known_prf_p3):
   value_list = known_prf_p3[key]  # a list of strings
   if p3vals in value_list:
    status = 'OK'
   else:
    status = 'DIFF: %s' % value_list
  else:
   status = 'UNKNOWN'
  return status

 def unused_future_join(self,b,e):
  """ static method """
  if b.endswith('i'):
   # e starts with 's', which becomes 'z' after 'i'
   return b + 'z' + e[1:]
  if b.endswith(('e','o')):
   # e starts with 's', which becomes 'z' after 'e', 'o'
   return b + 'z' + e[1:]  
  if b.endswith(('d','D')):
   # switch to hard consonant before initial 's' of 'e'
   return b[0:-1]+'t'+e
  if b.endswith(('S','z')):
   # change final sibilant to 'k' and replace initial 's' with z'
   return b[0:-1]+'kz'+e[1:]
  # default
  return b+e

 def getsups(self):
  return self.sup.split(':') 

import sys,re,codecs

class BaseRec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.model,self.root,self.Lrefs,self.base) = line.split('\t')
  if self.model == 'ind_ppfactn':
   (self.theclass,self.voice,self.tense) = (None,None,None)
  else:
   (self.theclass,self.voice,self.tense) = self.model.split(',')

def init_baserecs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [BaseRec(line) for line in f if not line.startswith(';')]
 return recs

def conjtab(rec):
 conj = ConjTable(rec.root,rec.theclass,rec.voice,rec.tense,rec.base)
 return conj.table

def unused_conjtab(rec):
 if rec.model == 'ind_ppfactn':
   return [rec.base]
 else:
  conj = ConjTable(rec.root,rec.theclass,rec.voice,rec.tense,rec.base)
  return conj.table

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 baserecs = init_baserecs(filein)
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in baserecs:
   tab = conjtab(rec)
   tabstr = ':'.join(tab)
   out = rec.line + '\t' + tabstr
   f.write(out + '\n')
   #print rec.line
   #print tab
   #print

