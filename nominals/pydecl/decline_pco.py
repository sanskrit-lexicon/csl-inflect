""" decline_pco.py
  Declensions of pronouns, cardinals
  Rather than orchestrating an algorithm joining of bases and suffixes,
  these classes read information from data files:
  decline_pron_data.txt, decline_card_data.txt
"""
import sys,re
import codecs

class PcoData(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  key,self.inflectionstr = line.split('\t')
  self.key = key
  m = re.search(r'^(.*?),([mfn])_(.*)$',key)
  self.headword = m.group(1)
  self.gender = m.group(2)
  self.lexid = m.group(3)
  # deserialize
  a = self.inflectionstr.split(':')
  assert len(a)==24
  b = []
  for x in a:
   y = x.split('/')
   if len(y) == 1:
    b.append(x)
   else:
    b.append(y)
  self.inflections = b

def init_pron_data(filein):
 import os 
 dir_path = os.path.dirname(os.path.realpath(__file__))
 pathin = '%s/%s' % (dir_path,filein)
 with codecs.open(pathin,"r","utf-8") as f:
  recs = [PcoData(x) for x in f if not x.startswith(';')]
 d = {}
 for rec in recs:
  d[rec.key] = rec
 return d 

from declension_join_simple import declension_join_simple
class Decline_pron_1(object):
 """ For pronominal adjectives declined 'like' yad (Kale section 147)
 """
 def __init__(self,gender,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  if gender == 'm':
   self.sup = 'aH:O:e:am:O:An:ena:AByAm:EH:asmE:AByAm:eByaH:asmAt:AByAm:eByaH:asya:ayoH:ezAm:asmin:ayoH:ezu:a:O:e' 
  elif gender == 'n':
   self.sup = 'at:e:Ani:at:e:Ani:ena:AByAm:EH:asmE:AByAm:eByaH:asmAt:AByAm:eByaH:asya:ayoH:ezAm:asmin:ayoH:ezu:at:e:Ani'
  elif gender == 'f':
   self.sup = 'A:e:AH:Am:e:AH:ayA:AByAm:ABiH:asyE:AByAm:AByaH:asyAH:AByAm:AByaH:asyAH:ayoH:AsAm:asyAm:ayoH:Asu:e:e:AH'
  else:
   print('Decline_pron_1 ERROR. Unknown gender:',gender,key1)
   self.status = False
   self.table = []
   return
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1] # drop final 'a'
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
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

import re
class Decline_pron_2(object):
 """ For pronominal adjectives declined 'like' sarva (Kale section 148)
   Use Decline_pron_1  (declension 'like' yad) BUT
   for neuter gender, Nom. and Acc. singular, change ending 'at' to 'am';
   this is according to Kale.  
   For neuter Voc. Sing., we use ending 'a' instead of 'at' -- This
   agrees with Bucknell.
 """
 def __init__(self,gender,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  decl = Decline_pron_1(gender,key1,key2)
  self.status = decl.status
  self.table = decl.table
  if gender == 'n':
   # adjust Nom., Acc. and Voc. singular
   # indices 0,3, 21
   for i in [0,3,21]:
    x = self.table[i]
    if x.endswith('at'): # it should so end
     if i in [0,3]:  
      # nom and accusative singular, replace final 't' with 'm'
      self.table[i] = x[0:-1] + 'm'  
     else:
      # vocative singular, drop final 't'
      self.table[i] = x[0:-1]

class Decline_pron_3(object):
 """ For pronominal adjectives declined 'like' sarva (Kale section 148)
   BUT with optional forms in some of m1p, m5s, and m6s
 """
 def __init__(self,gender,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  # first, decline like sarva
  decl = Decline_pron_2(gender,key1,key2)
  self.status = decl.status
  self.table = decl.table
  if gender == 'm':
   # optional forms in  some of Nom. pl., Ablative sing., Locative sing.
   # indices 2,12,15. These are like 'rAma'
   # so Xe -> XAH, Xasmat -> XAt, Xasmin -> Xa ,
   # where X = 'sarv' if key1 were 'sarva'
   base = key1[0:-1] # remove final a
   suffixes = {2:'AH', 12:'At', 18:'e'}
   # It depends on the pronoun as to which of these optional forms apply
   if key1 in ['sva','antara']:
    indices = [2,12,18]   # m1p, m5s, m7s
   elif key1 in ['nema']:
    indices = [2]  # m1p
   elif key1 in ['pUrva','avara','dakziRa','uttara','apara','aDara']:
    # MW under says also m5s for: pUrva, dakziRa 
    indices = [2,18] # m1p, m72 (Kale)
   elif key1 in ['para','paraspara']:
    # No special mention in Kale. MW provides m1p, m5s, m7s
    # and also an additional 'parAsaH' for m1p (Not included here)
    indices = [2,12,18]   # m1p, m5s, m7s
   else: 
    # internal error
    print('Decline_pron_3 internal error',key1)
    exit(1)
   for i in indices:
    x = self.table[i]
    y = base + suffixes[i]
    self.table[i] = [x,y]  # optional form, as list


class Decline_pron(object):
 """ declension table for all pronouns .
  Some are determined by file decline_pron_data.txt, and
  some are determined algorithmically
 """
 # class variable
 d = init_pron_data('decline_pron_data.txt')
 def __init__(self,gender,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  if key2.endswith('-Bavat'):
   # it's a compound of Bavat
   # 0) get the prefix and base(logic of splitkey2 method used in decline.py)
   parts = self.key2.split('-')
   base = parts[-1] # == 'Bavat'
   head = ''.join(parts[0:-1])
   # 1) get the predeclined form for Bavat
   datakey = '%s,%s_pron' %(base,gender)
   d = Decline_pron.d
   rec = d[datakey] # assume predeclined forms present
   table = rec.inflections # list form for Bavat
   # 2) prepend the prefix. There are no alternate forms in 'table'
   self.table = [head + x for x in table]
   self.status = True
   return
   
  # not a compound of Bavat
  # try the predeclined forms first
  datakey = '%s,%s_pron' %(self.key2,gender)
  d = Decline_pron.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections # list form
   return
  # otherwise, use one of the algorithms, according to 'key1'
  if key1 in ['anya','anyatara','itara',
     'ekatama','katara','katama','yatara','yatama','tatara','tatama',
     'anyonya', 'itaretara',
     'ananya','tadanya','tvadanya','dvyanya','Bavadanya',
     ]:
   # the 'yad-like' group
   decl = Decline_pron_1(gender,key1,key2)
   self.table = decl.table
   self.status = decl.status
  elif key1 in ['sarva','viSva',
   'sama', 
   'sima','uBa','uBaya',
   # the 'sarva' group
   # itara --  Kale has it here and in the 'anya' group
   'ekatara',
   'tva', # Kale section 149
   'atisarva','asarva','jagatsarva','susarva','svasarva',
   'ativiSva','anuviSva','aviSva','prativiSva','viSvaviSva','sarvaviSva',
   ]:
   # the sarva group
   decl = Decline_pron_2(gender,key1,key2)
   self.table = decl.table
   self.status = decl.status
  elif key1 in ['sva','antara','nema',
     'pUrva','avara','dakziRa','uttara','apara','aDara',
     'para',  # declension not mentioned specifically by Kale
     'paraspara',
     ]:
   # the 'sva' group:
   decl = Decline_pron_3(gender,key1,key2)
   self.table = decl.table
   self.status = decl.status
  else:
   self.status = False
   self.table = None

class Decline_m_pron(object):
 """ declension table for pronouns in masculine gender
 """
 def __init__(self,key1,key2=None):
  decl = Decline_pron('m',key1,key2)
  self.status = decl.status
  self.table = decl.table

class Decline_f_pron(object):
 """ declension table for pronouns in feminine gender
 """
 def __init__(self,key1,key2=None):
  decl = Decline_pron('f',key1,key2)
  self.status = decl.status
  self.table = decl.table

class Decline_n_pron(object):
 """ declension table for pronouns in neuter gender
 """
 def __init__(self,key1,key2=None):
  decl = Decline_pron('n',key1,key2)
  self.status = decl.status
  self.table = decl.table

def unused_check_pron(gender,key1,key2,table):
 """ alternate derivation for some values of key1"""
 if key1 in ['anya','anyatara','itara',
     'ekatama','katara','katama','yatara','yatama','tatara','tatama']:
  decl = Decline_pron_1(gender,key1,key2)
 elif key1 in ['sarva','viSva',
   'sama', 
   'sima','uBa','uBaya',
   # the 'sarva' group
   # itara --  Kale has it here and in the 'anya' group
   'ekatara',
   'tva', # Kale section 149
   ]:
  decl = Decline_pron_2(gender,key1,key2)
 else:
  return
 if not decl.status:
  return
 chktable = decl.table
 # check agreement 
 ok = True
 for i in range(0,len(table)):
  if chktable[i] != table[i]:
   print('check_pron difference',gender,key1,i,chktable[i] , table[i])
   ok = False
 if ok:
  print('check_pron agreement:',gender,key1)

def init_card_data(filein):
 import os 
 dir_path = os.path.dirname(os.path.realpath(__file__))
 pathin = '%s/%s' % (dir_path,filein)
 with codecs.open(pathin,"r","utf-8") as f:
  recs = [PcoData(x) for x in f if not x.startswith(';')]
 d = {}
 for rec in recs:
  d[rec.key] = rec
 return d 

class Decline_m_card(object):
 """ declension table for cardinal numbers in masculine gender
 """
 # class variable
 d = init_card_data('decline_card_data.txt')
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  datakey = '%s,%s' %(self.key2,'m_card')
  d = Decline_m_card.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections # list form
   return
  # Word not directtly in the data file.
  # compute it as a compound
  head,base = self.splitkey2()
  datakey = '%s,%s' %(base,'m_card')
  if datakey in d:
   rec = d[datakey]
   table = rec.inflections # list form of base
   # concatenate head with table entries
   table1 = []
   for x in table:
    if x == '':
     item = ''
    elif isinstance(x,str):
     item = head + x
    else: # alternates, in list
     item = [(head+y) for y in x]
    table1.append(item)
   self.table = table1
   self.status = True
   return
  if self.key2 == 'saptAzwan':
   # same as previous, but take into account sandhi
   head = 'saptA'
   base = 'azwan'
   datakey = '%s,%s' %(base,'m_card')
   rec = d[datakey]
   table = rec.inflections # list form of base
   # concatenate head with table entries
   table1 = []
   for x in table:
    if x == '':
     item = ''
    elif isinstance(x,str):
     item = head + x[1:]  # saptA + zwa, for example
    else: # alternates, in list
     item = [(head+y[1:]) for y in x]
    #print('chk: x=',x,'item=',item)
    table1.append(item)
   self.table = table1
   self.status = True
   return
  # no luck   
  self.status = False
  self.table = None
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_f_card(object):
 """ declension table for cardinal numbers in feminine gender
 """
 # class variable
 d = init_card_data('decline_card_data.txt')
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  datakey = '%s,%s' %(self.key2,'f_card')
  d = Decline_f_card.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections
   return
  # Word not directtly in the data file.
  # compute it as a compound
  head,base = self.splitkey2()
  datakey = '%s,%s' %(base,'f_card')
  if datakey in d:
   rec = d[datakey]
   table = rec.inflections # list form of base
   # concatenate head with table entries
   table1 = []
   for x in table:
    if x == '':
     item = ''
    elif isinstance(x,str):
     item = head + x
    else: # alternates, in list
     item = [(head+y) for y in x]
    table1.append(item)
   self.table = table1
   self.status = True
   return
  # no luck
  self.status = False
  self.table = None
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_n_card(object):
 """ declension table for cardinal numbers in neuter gender
 """
 # class variable
 d = init_card_data('decline_card_data.txt')
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  datakey = '%s,%s' %(self.key2,'n_card')
  d = Decline_n_card.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections
  else:
   self.status = False
   self.table = None

