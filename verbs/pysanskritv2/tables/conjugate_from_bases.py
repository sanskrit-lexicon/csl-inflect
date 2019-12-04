""" conjugate_from_bases.py
"""
import sys
sys.path.append('../bases')
import benedictive

from conjugation_join_simple import conjugation_join_simple
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
  if self.tense in special_tenses:
   self.inflect_special_tense()
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
 def inflect_special_tense(self):
  """ tense pre, ipf, ipv, opt
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
  (self.theclass,self.voice,self.tense) = self.model.split(',')

def init_baserecs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [BaseRec(line) for line in f if not line.startswith(';')]
 return recs

def conjtab(rec):
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

