""" decline_1cons.py
  This is sufficiently complicated to be separated out
"""
from declension_join_simple import declension_join_simple
import re
class Decline_1_helper(object):
 def __init__(self,supin,ending,base,key1):
  """ supin is a string
     calculate newsup (also a string), based on ending and base;
      sometimes key1 is also needed.
  """
  sups = supin.split(':') 
  self.ending = ending
  self.base = base
  self.key1 = key1
  newsups = []
  for sup in sups:
   if sup.startswith(('O','a','A','e','o','i','I')): # sup starts with vowel
    if self.key1.endswith('os'):
     # dos. Kale p. 69
     newsup = 'z' + sup
    else:
     newsup = self.ending + sup 
   elif sup.startswith('B'):
    newsup = self.B(sup)
   elif sup == 'su':
    newsup = self.su(sup)  # 7p only
   elif sup == '':
    newsup = self.empty()  
   elif sup == '*i' : 
    # neuter: 1p (and 2p and 8p)
    newsup = self.neuter1p(sup)
   else:
    print('decline.Decline_1_helper ERROR 1',sup,ending,base,key1)
    exit(1)
   if newsup == None:
    print('decline.Decline_1_helper ERROR 2',sup,ending,base,key1)
    #exit(1)
    continue
   newsups.append(newsup)
  self.newsup = ':'.join(newsups)

 def B(self,sup):
  # base this on the 'empty' ending
  end1 = self.empty()
  end2dict = { 't':'d', 'k':'g', 'w':'q', 'R':'R', 'p':'b','n':'n','N':'N',
               'k/w':'k/w'}
  if end1 in end2dict:
   if end1 == 'k/w':
    return '%s%s/%s%s' %('g',sup,'q',sup)
   else:
    end2 = end2dict[end1]
    return end2 + sup
  elif self.ending in ['r','l','v']:
   return self.ending + sup
  elif self.ending in ['s']:
   if self.key1.endswith('os'):
    # dos Kale p. 69
    return 'r' + sup
   else: 
    # Kale: BAs, hiMs
    return sup
  else:
   return None

 def su(self,sup):
  # base this on the 'empty' ending
  # expect sup == 'su'
  end1 = self.empty()
  end2dict = { 't':'t', 'k':'k', 'w':'w', 'R':'R', 'p':'p','n':'n','N':'N',
               'k/w':'k/w'}
  if end1 in end2dict:
   end2 = end2dict[end1]
   if end2 == 'k':
    sup = 'zu'
    return end2+sup
   elif end2 == 'k/w':
    return 'kzu/wsu'
   else:
    return end2 + sup
  elif self.ending in ['r','l']:
   return self.ending + 'zu'  # Kale p. 58 for 'l'
  elif self.ending in ['s']:
   if self.key1.endswith('os'):
    # dos Kale, p. 69, who has alternates 'dozzu','doHzu'
    return 'zzu'
   else:
    return 's' + 'su' # Per Kale p. 68, BAs 7p = BAssu
  else:
   return None
  

 # class variable used to get 'empty' endings
 nominativeSingularEndings = {
  'rAj':'w',  # Deshpande p.157, samrAj m. Kale sam-rAj
  'BrAj':'w', # BrAj, deva-BrAj (MW) ; vi-BrAj (Kale)
  'vrAj':'w', # pari-vrAj (MW,Kale)
  'drAj':'w', # MW DrAj is only example, but nom. singular not given.
  'devej':'w', # MW, Kale
  #'viSvasfj':'w', # Kale p. 58. MW 'sfk'
  'parimfj':'w', # Kale
  'Darmamfj':'k', # MW, PW
  'yAj':'w', # MW
  'rej':'w', # MW
  'saraG':'w', # MW 
  'kruYc':'N', # Huet
  'KaYj':'n',  # MW, PWG, PW. Huet has 'N'
  'Bfjj':'w',  # Kale
  'vfSc':'w',  # Kale su-vfSc
  'diS':'k',   # Deshpande
  'dfS':'k',   # MW, Kale p. 58
  'spfS':'k',  # MW
  'Dfz':'k',   # MW. for da-Dfz. Assume for other compounds
 }

 def empty(self):
  """ nominative singular only for masculine, feminine gender
      nominative, accusative or vocative singular for neuter gender
     According to Kale, when ending is in one of the vargas (k,c,w,t,p),
     Then there are two optional endings, namely either of the non-aspirate
     forms of the varga  (e.g., k or g for the k-varga).
     Bucknell does not support this optional form version.
     Sometimes it is rather arbitrary which is used.
  """
  # next two handle some irregularities
  # first, key1 may be special - e.g. viSvasfj -> 'w' (Kale) but 
  # 'sfj' -> 'k' (MW, and assumed so for all other compounds of 'sfj')
  if self.key1 in Decline_1_helper.nominativeSingularEndings:
   return Decline_1_helper.nominativeSingularEndings[self.key1]
  if self.base in Decline_1_helper.nominativeSingularEndings:
   return Decline_1_helper.nominativeSingularEndings[self.base]
  elif self.ending in ['t','T','d','D']:
   return 't' 
  elif self.ending in ['k','K','g','G']:
   return 'k'  # from 'k' + 'su' (sup is assumed to be 'su')
  elif self.ending in ['c','C','j','J']:
   return 'k' 
  elif self.ending in ['w','W','q','Q']:
   return 'w' 
  elif self.ending == 'R':
   return 'R' 
  elif self.ending in ['p','P','b','B']:
   return 'p' 
  elif self.ending == 'm':
   return 'n' 
  elif self.ending in ['l','v']:
   return self.ending
  elif self.ending in ['r']:
   return 'H'
  elif self.ending in ['S']:
   return 'w'
  elif self.ending in ['z']:
   if self.base.endswith('kz'):
    return 'k'  # i.e., drop the 'z'
   else:
    return 'w'
  elif self.ending in ['s']:
   if self.base.endswith(('As','os')):
    return 'H' # 1s,8s, and n2s
   elif self.base.endswith('Ms'):  
    # hiMs. Confer Kale p. 68 su-hiMs and jiGAMs (not MW)
    return 'n'
   else:  # no examples currently
    return None
  elif self.ending in ['h']:
   if self.base in ['muh','snih','snuh','druh']:
    # Kale p.59; MW
    return 'k/w'
   elif self.base in ['duh','dah','spfh']:
    # Kale p. 59, MW 
    # spfh: ni-spfh (MW)
    return 'k'
   elif self.base in ['nah']:
    # upAnah (MW) nat.  Also Deshpande p. 385
    return 't'
   elif self.key1 in ['Aruh','gartAruh']:
    # MW
    return 'k'
   elif self.key1 in ['svAruh']:
    # MW 
    # Assume other '-ruh'  are default 'w'
    return 't'
   else:
    return 'w' # Default, acc. to Kale p. 58 (comment under rAw)
  else:
   return None

 def neuter1p(self,sup0):
  """Kale Section 91(c)
   'n' is prefixed to the 'i' of N. & Acc. plural in the case of 
   neuter nouns ending in a consonant except a nasal or 
   a semi-vowel; but not in the case of a noun derived from the
   frequentative base.
   'sup0' enters as the synthetic '*i'
  """
  sup = self.ending + 'i'
  # insert nasal appropriate for the ending
  if self.ending in ['t','T','d','D']:
   return 'n' +  sup
  elif self.ending in ['k','K','g','G']:
   return 'N' + sup
  elif self.ending in ['c','C','j','J']:
   if self.base.endswith(('Yc','Yj','Sc')):
    # kruYc
    return sup
   else:
    return 'Y' + sup
  elif self.ending in ['w','W','q','Q']:
   return 'R' + sup
  elif self.ending == 'R':
   return sup
  elif self.ending in ['p','P','b','B']:
   return 'm' + sup
  elif self.ending == 'm':
   return sup
  elif self.ending in ['l','r']:
   return sup
  elif self.ending in ['S']:
   return 'Y' + sup
  elif self.ending in ['z']:
   if self.base.endswith('kz'):
    return 'Nk' + sup
   else:
    return 'N' + sup
  elif self.ending in ['s']:
   if self.key1.endswith('os'):
    # dos. Kale p. 67
    return 'M' + 'zi'
   elif self.key1.endswith('As'):
    # BAs , etc. No example in Kale
    return 'n' + sup
   else:
    return sup
  elif self.ending in ['h']:
    return 'M' + 'hi'
  else:
   return None

class Decline_irregular(object):
 key1set = set(['div','puMs','vah','anaquh'])
 def __init__(self,model,key1,key2,base):
  self.status=False
  self.table = None
  if base not in Decline_irregular.key1set:
   return
  m = re.search(r'^([mfn])_(.*)$',model)
  if not m:
   return
  gender = m.group(1)
  submodel = m.group(2)
  if base == 'div':
   self.decl_div(gender,submodel)
  elif base == 'puMs':
   self.decl_puMs(gender,submodel)
  elif base == 'vah':
   self.decl_vah(gender,submodel)
  elif base == 'anaquh':
   self.decl_anaquh(gender,submodel)

 def decl_div(self,gender,submodel):
  # MW headword 'div'
  # Declension from Huet, with additions from MW
  d={}
  d['m'] = ['dyOH/dyuH','dyAvO/divO','dyAvaH/divaH',  #dyuH MW
            'dyAm/divam','dyAvO/divO','divaH',
            'divA/dIvA','','dyuBiH',  #dIvA MW
            'dyave/dive','','dyuByaH',
            'dyoH/divaH','','dyuByaH',
            'dyoH/divaH','','divAM',
            'dyavi/divi','','dyuzu',
            'dyOH','','divaH'
           ]
  d['f'] = d['m']
  # no idea for neuter
  if gender in ['m','f']:
   self.table = d[gender]
   self.status = True

 def decl_puMs(self,gender,submodel):
  # MW headword 'puMs' (and its compounds)
  # Declension from Huet, with additions from MW
  d={}
  d['m'] = ['pumAn','pumAMso','pumAMsaH',
            'pumAMsam','pumAMsO','puMsaH',
            'puMsA','pumByAm','pumBiH',
            'puMse','pumByAm','pumByaH',
            'puMsaH','pumByAm','pumByaH',
            'puMsaH','puMsoH','puMsAm',
            'puMsi','puMsoH','puMsu',
            'puman','pumAMso','pumAMsaH'
           ]
  d['f'] = d['m']
  
  # no idea for neuter
  if gender in ['m','f']:
   self.table = d[gender]
   self.status = True
  elif gender == 'n':
   table = d['m']
   # change cases 1,2,8
   row = ['pum','puMsI','pumAMsi']
   table[0:3] = row
   table[3:6] = row
   table[21:24] = row
   self.table = table
   self.status = True

 def decl_vah(self,gender,submodel):
  # MW headword 'vah' (and its compounds)
  # Declension from Kale, p. 61 (viSva-vah)
  # Huet gives 'ohA' for 3s for vah, which looks right.
  # Further sandhi changes take place in compounds of vah.
  # These are currently handled elsewhere
  d={}
  d['m'] = ['vAw','vAhO','vAhaH',
            'vAham','vAhO','ohaH',
            'ohA','vAqByAm','vAqBiH',
            'ohe','vAqByAm','vAqByaH',
            'ohaH','vAqByAm','vAqByaH',
            'ohaH','ohoH','ohAm',
            'ohi','ohoH','vAwsu',
            'vAw','vAhO','vAhaH',   # Huet has 'van' for 7s
           ]
  d['f'] = d['m']
  
  # no idea for neuter
  if gender in ['m','f']:
   self.table = d[gender]
   self.status = True
  elif gender == 'n':
   table = d['m']
   # change cases 1,2,8
   row = ['vAw','vAhI','vAMhi',]
   table[0:3] = row
   table[3:6] = row
   table[21:24] = row
   self.table = table
   self.status = True
 def decl_vah_join(self,head):
  if head == '':
   return self.table ## nothing to join.
  # There is further sandhi when joining 'head' to the declension of 'vah'
  ans = []
  e = head[-1] # details depend on last letter of the prefix
  for x in self.table:
   # compute the join head+x, call it y
   if not x.startswith('o'):
    y = head + x
   elif e == 'a':
    # viSva-vah, etc  
    # viSva + ohA -> viSvOhA
    y = head[0:-1] + 'O' + x[1:]
   elif e == 'A':
    # dakziRA-vah
    y = head[0:-1] + 'O' + x[1:]
   elif e == 'U':
    # BU-vah Per Kale 
    y = head + x[1:]  # remove 'o' from vah declensino
   elif e == 'u':
    # Use corresponding semi-vowel before 'o'  (deduced from Huet)
    y = head[0:-1]+'v' + x
   elif e == 'i':
    # Use corresponding semi-vowel before 'o'  (deduced from Huet)
    y = head[0:-1]+'y' + x
   elif e == 'f':
    # Use corresponding semi-vowel before 'o'  (deduced from Huet)
    # no MW examples
    y = head[0:-1]+'r' + x
   elif e == 'o':
    # sroto-vah  
    # sroto + ohA -> srot + a + u + ohA
    #   -> srot + a + vohA -> srotavohA
    y = head[0:-1]+'av' + x
   elif e == 'e':
    # no examples. Do by analogy to e==o
    y = head[0:-1] + 'ay' + x
   else:
    # only known case: havir-vah
    y = head + x
   ans.append(y)
  return ans

 def decl_anaquh(self,gender,submodel):
  # MW headword 'anaquh' (and its compounds)
  # Declension from Kale, p. 61 and Deshpande p.384
  d={}
  d['m'] = ['anaqvAn','anaqvAhO','anaqvAhaH',
            'anaqvAham','anaqvAhO','anaquhaH',
            'anaquhA','anaqudByAm','anaqudBiH',
            'anaquhe','anaqudByAm','anaqudByaH',
            'anaquhaH','anaqudByAm','anaqudByaH',
            'anaquhaH','anaquhoH','anaquhAm',
            'anaquhi','anaquhoH','anaqutsu',
            'anaqvan','anaqvAhO','anaqvAhaH'
           ]
  d['f'] = d['m']
  
  if gender in ['m','f']:
   self.table = d[gender]
   self.status = True
  elif gender == 'n':  
   # Kale p. 61
   table = d['m']
   # change cases 1,2,8
   row = ['anaqut','anaquhI','anaqvAMhi']
   table[0:3] = row
   table[3:6] = row
   table[21:24] = row
   self.table = table
   self.status = True

class Decline_1(object):
 """ Declension of the '1-stem' consonant-ending nominals 
 """
 def __init__(self,model,key1,key2=None):
  m = re.search(r'^([mfn])_1_(.)$',model)
  gender = m.group(1)
  ending = m.group(2)
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  head,base = self.splitkey2()
  if gender in ['m','f']:
   # masculine, feminine declined the same
   sup0 = ':O:aH:am:O:aH:A:ByAm:BiH:e:ByAm:ByaH:aH:ByAm:ByaH:aH:oH:Am:i:oH:su::O:aH'
  else:
   # gender == 'n', supposedly
   # same as m, f except for cases 1,2,8. where endings are ':I:anti'
   # But the plural is unique, in that the ending has form
   #  <nasal> + <ending> + i, assuming 
   #       <ending> is not a nasal or semi-vowel or a noun
   #       derived from the frequentative base.
   #  and <ending> + i, otherwise
   sup0 = ':I:*i::I:*i:A:ByAm:BiH:e:ByAm:ByaH:aH:ByAm:ByaH:aH:oH:Am:i:oH:su::I:*i'
  # derive actual sups from general sup ('sup' variable) and ending
  obj = Decline_1_helper(sup0,ending,base,self.key1)

  self.sup = obj.newsup # a string
  sups = self.getsups()
  # We've made variations in the sups.
  # What we combine with the sups is just the base without its final letter.
  base1 = base[0:-1]
  # join base and all the endings
  base_infls = []
  for isup,sup in enumerate(sups):
   b = base1
   if base in ['buD','baD','bAD']:
    # special case of compounds of 'buD' (Whitney Section 391b)
    # Following Huet, I apply also to baD and bAD
    if sup.startswith(('t','dB')):
     b = 'B' + b[1:] # replace initial 'b' with 'B'
   elif base in ['duh','druh','dah','dih','dfh']:
    if ((isup in [0,7,8,10,11,13,14,20,21]) or
        ((gender == 'n') and (isup in [3]))):
      b = 'D' + b[1:]
   elif base in ['guh','gfh']:
    if ((isup in [0,7,8,10,11,13,14,20,21]) or
        ((gender == 'n') and (isup in [3]))):
      b = 'G' + b[1:]
   elif base in ['kruYc','Bfjj','KaYj','vfSc']:
    # to agree with Huet
    if isup in [0,7,8,10,11,13,14,20,21]:
     b = base1[0:-1]  # remove ending 'Y'
    elif (gender == 'n') and (isup in [3]):
     b = base1[0:-1]  # remove ending 'Y'
   elif self.key1 == 'yuj':
    # to agree with Kale, p. 59
    if gender in ['m','f']:
     if isup in [0,21]:
      sup = 'N'
     elif isup in [1,2,3,4,22,23]:
      b = base1 + 'Y'
    elif gender == 'n': 
     # this is speculative. No printed examples
     if isup in [0,3,21]:
      sup = 'N'
     #elif isup in [1,2,3,4,22,23]:
     # b = base1 + 'Y'
   elif (ending in ['r']):
    if isup in [0,7,8,10,11,13,14,20,21]:
     lengthen = True
    elif (isup == 3) and (gender == 'n'):
     lengthen = True
    else:
     lengthen = False
    if lengthen:
     if base1.endswith(('a','i','u')):
      # lengthen vowel in 1s, 8s, 7p.and before 'B' endings (Deshpande p. 158)
      # and if neuter, also in 2s
      d = {'a':'A','i':'I','u':'U'}
      b = base1[0:-1] + d[base1[-1]]
   elif self.key1 == 'avayaj':
    # Kale Section 102:
    # The current forms are avayak, avayajO,... avayagBiH,.. avayakzu
    # and base1 = 'ya'
    # first, change ya to yA in base
    b = base1[0:-1] + 'A'
    if (isup in [0,21]) or ((gender == 'n') and (isup == 3)):
     sup = 'H'
    elif sup.startswith('g'): # the 'B' endings, 3p, etc.
     # yagBiH -> yoBiH, etc.
     b = base1[0:-1]
     sup = 'o' + sup[1:]
    elif sup == 'kzu':
     # yakzu -> yassu
     b = base1[0:-1]
     sup = 'ssu'
   elif base.endswith(('kz','Ms')):
    # Example vivizk, Kale p. 58. for several cases, drop the 'k'
    # Examples su-hiMs, jiGAMs Kale p. 68
    if isup in [0,7,8,10,11,13,14,20,21]:
     lengthen = True
    elif (isup == 3) and (gender == 'n'):
     lengthen = True
    else:
     lengthen = False
    if lengthen:
     b = base1[0:-1]
    if base.endswith('kz') and (gender == 'n') and (isup in [2,5,23]):
     # drop the 'k' ending base1
     b = base1[0:-1]
   # end of adjustments to base
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(b,sup))
   else:
    # join each alternate sup to b
    infls = [declension_join_simple(b,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)

  # look for irregular declension of base
  # if it exists, prefer the irregular forms of the base.
  irreg = Decline_irregular(model,key1,key2,base)
  if irreg.status:
   base_infls = irreg.table
   if base == 'vah':
    self.table = irreg.decl_vah_join(head)
   else:
    self.table = self.prepend_head(head,base_infls)
  else:
   self.table = self.prepend_head(head,base_infls)
   if self.key1 == 'viSvarAj':
    # Kale Section 99:  before 'rAw' (or 'rAw', viSva becomes viSvA,
    self.table = [re.sub(r'viSvarA([wq])',r'viSvArA\1',x) for x in self.table]
  self.status = True

 def getsups(self):
  sup = self.sup
  return sup.split(':') 
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
