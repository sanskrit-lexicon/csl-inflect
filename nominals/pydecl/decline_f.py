""" decline_f.py
"""
import sys,re
from declension_join_simple import declension_join_simple

def agent_relation(pada2):
 """ should be consistent with agent_relation function in
     inputs/nominals/analyze_f.py
 """
 relations = [
  ##  masculine
  # Deshpande
  'pitf','BrAtf','jAmAtf',
  'nf', # 6p: nfRAm/nFRAm
  # Kale additionally
  'devf', # husband's brother
  'SaMstf', # one who praises
  'savyezWf', # a charioteer   Kale spells as ..wf; 
             # AP has both, and also savyezWAtf, savyezWa
  ## feminine
  # Deshpande
  'mAtf','duhitf','nanAndf',
  # Kale
  'nanandf',
  'yAtf',  # a husband's brother's wife
  ]
 agent_relations = [
  ### relation nouns that are declined like agent nouns
  ## masculine
  'naptf','Bartf',
  ## feminine
  'svasf', # 2p = svasFH
 ]

 if pada2 in relations:
  return 'R'
 elif pada2 in agent_relations:
  return 'RA'
 else:
  return 'A'

class Decline_m_f(object):
 """ declension table for masculine nouns ending in 'f'
     
sup-m-f-A=A:ArO:AraH:Aram:ArO:Fn:rA:fByAm:fBiH:re:fByAm:fByaH:uH:fByAm:fByaH:uH:roH:FRAm:ari:roH:fzu:ar:ArO:AraH
     or nouns of relation.
sup-m-f-r=A:arO:araH:aram:arO:Fn:rA:fByAm:fBiH:re:fByAm:fByaH:uH:fByAm:fByaH:uH:roH:FRAm:ari:roH:fzu:ar:arO:araH
  These have no alternate sups.
  I find no clear guidance regarding Acc. pl. of feminine action nouns ending
  in 'f'.  Is the ending 'Fn' or 'FH' as shown for feminine nouns of relation.
 
  Since Huet shows 'FH' (netf, f), I'll go with that.

 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  head,base = self.splitkey2()
  # determine sup (agent or relation) using last pada (base)
  # Returned type will be 'R','RA', or 'A'
  # 'RA' and 'A' are to decline like agent
  agent_relation_type = agent_relation(base)
  if agent_relation_type == 'R': #relation
   self.sup = 'A:arO:araH:aram:arO:Fn:rA:fByAm:fBiH:re:fByAm:fByaH:uH:fByAm:fByaH:uH:roH:FRAm:ari:roH:fzu:ar:arO:araH' 
  else: # RA, A  agent
   self.sup = 'A:ArO:AraH:Aram:ArO:Fn:rA:fByAm:fBiH:re:fByAm:fByaH:uH:fByAm:fByaH:uH:roH:FRAm:ari:roH:fzu:ar:ArO:AraH'
  sups = self.getsups()

  base1 = base[0:-1]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  # make a few adjustments for irregularities
  self.irregularities(base,base_infls)
  # construct list, or list of lists by prepending head 
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def irregularities(self,base,infls):
  # adjusts one or more entries in infls list
  if base == 'nf': 
   # Deshpande, p. 107
   infls[17] = ['nFRAm','nfRAm']  # genitive pl.
  return infls

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def declension_join_altsup(self,base,supstr):
   sups = supstr.split('/')
   return [declension_join(base,sup) for sup in sups]
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_f_f(object):
 """ declension table for feminine nouns ending in 'f'
     
sup-f-f-A=A:ArO:AraH:Aram:ArO:FH:rA:fByAm:fBiH:re:fByAm:fByaH:uH:fByAm:fByaH:uH:roH:FRAm:ari:roH:fzu:ar:ArO:AraH
     or nouns of relation.
sup-f-f-r=A:arO:araH:aram:arO:FH:rA:fByAm:fBiH:re:fByAm:fByaH:uH:fByAm:fByaH:uH:roH:FRAm:ari:roH:fzu:ar:arO:araH
  These have no alternate sups.
  I find no clear guidance regarding Acc. pl. of feminine action nouns ending
  in 'f'.  Is the ending 'Fn' or 'FH' as shown for feminine nouns of relation.
 
  Since Huet shows 'FH' (netf, f), I'll go with that.

 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  head,base = self.splitkey2()
  # determine sup (agent or relation) using last pada (base)
  # Returned type will be 'R','RA', or 'A'
  # 'RA' and 'A' are to decline like agent
  agent_relation_type = agent_relation(base)
  if agent_relation_type == 'R': #relation
   self.sup = 'A:arO:araH:aram:arO:FH:rA:fByAm:fBiH:re:fByAm:fByaH:uH:fByAm:fByaH:uH:roH:FRAm:ari:roH:fzu:ar:arO:araH' 
  else: # RA, A  agent
   self.sup = 'A:ArO:AraH:Aram:ArO:FH:rA:fByAm:fBiH:re:fByAm:fByaH:uH:fByAm:fByaH:uH:roH:FRAm:ari:roH:fzu:ar:ArO:AraH'
  sups = self.getsups()

  base1 = base[0:-1]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  # make a few adjustments for irregularities
  self.irregularities(base,base_infls)
  # construct list, or list of lists by prepending head 
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def irregularities(self,base,infls):
  # adjusts one or more entries in infls list
  if base == 'nf': 
   # Deshpande, p. 107
   infls[17] = ['nFRAm','nfRAm']  # genitive pl.
  return infls

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def declension_join_altsup(self,base,supstr):
   sups = supstr.split('/')
   return [declension_join(base,sup) for sup in sups]
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b


class Decline_n_f(object):
 """ declension table for neuter nouns ending in 'f'
sup-n-f=f:fRI:FRi:f:fRI:FRi:fRA:fByAm:fBiH:fRe:fByAm:fByaH:fRaH:fByAm:fByaH:fRaH:fRoH:FRAm:fRi:fRoH:fzu:f,ar:fRI:FRi
  Note alternate sups
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'f:fRI:FRi:f:fRI:FRi:fRA:fByAm:fBiH:fRe:fByAm:fByaH:fRaH:fByAm:fByaH:fRaH:fRoH:FRAm:fRi:fRoH:fzu:f/ar:fRI:FRi' 
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  # construct list, or list of lists by prepending head 
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def declension_join_altsup(self,base,supstr):
   sups = supstr.split('/')
   return [declension_join(base,sup) for sup in sups]
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b
