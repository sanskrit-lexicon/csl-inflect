"""pysanskritv2/bases/bases_test2.py
"""
import sys
import sandhi1 
""" this complication is unneeded for direct use of bases_test2
    but is needed when used in conj_compare_file in above directory
sys.path.append('../../pysanskritv1') # doesn't work in above context
"""
from os.path import dirname, abspath
import os
curdir = dirname(abspath(__file__))
parent = dirname(curdir)
parentparent = dirname(parent)
pysanskritv1 = os.path.join(parentparent,'pysanskritv1')
sys.path.append(pysanskritv1)
try:
 import test2
 import sandhi
except:
 print('bases_test2. cannot import test2')
 print(sys.path)
 exit(1)

import codecs,re
import benedictive
import perfect
import ppfactn

class RootModel(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  try:
   (self.model,self.root,self.Lrefs) = line.split('\t')
   (self.theclass,self.voice,self.tense) = self.model.split(',')
  except:
   print('bases_test2 RootModel parse ERROR:',line)
   exit(1)

def init_rootmodel(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [RootModel(line) for line in f if not line.startswith(';')]
 return recs

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
class BaseObj(object):
 def __init__(self,rec,dbg=False):
  # rec is a rootmodel instance
  self.rootmodel = rec
  self.dbg = dbg
  self.bases = []
  self.status = True
  # opt == pot (optative = potential)
  special_tenses = ['pre','ipf','ipv','opt']   
  general_tenses = ['ppf','prf','fut','con','pft','ben']
  active_voices = ['a','m']
  a_classes = ['1','4','6','10']
  b_classes = ['2','3','5','7','8','9']
  if (rec.voice == 'p') and (rec.tense in special_tenses):
   self.bases = self.any_passive_special()
   self.status = (self.bases != [])
  elif (rec.voice in active_voices) and (rec.tense in special_tenses) and\
   (rec.theclass in a_classes):
   self.bases = self.a_active_special()
   self.status = (self.bases != [])
  elif (rec.voice in active_voices) and (rec.tense in special_tenses) and\
   (rec.theclass == '2'):
   self.bases = self.active_special_2()
   self.status = (self.bases != [])
  elif (rec.voice in active_voices) and (rec.tense in special_tenses) and\
   (rec.theclass == '3'):
   self.bases = self.active_special_3()
   self.status = (self.bases != [])
  elif (rec.voice in active_voices) and (rec.tense in special_tenses) and\
   (rec.theclass == '5'):
   self.bases = self.active_special_5()
   self.status = (self.bases != [])
  elif (rec.voice in active_voices) and (rec.tense in special_tenses) and\
   (rec.theclass == '7'):
   self.bases = self.active_special_7()
   self.status = (self.bases != [])
  elif (rec.voice in active_voices) and (rec.tense in special_tenses) and\
   (rec.theclass == '8'):
   self.bases = self.active_special_8()
   self.status = (self.bases != [])
  elif (rec.voice in active_voices) and (rec.tense in special_tenses) and\
   (rec.theclass == '9'):
   self.bases = self.active_special_9()
   self.status = (self.bases != [])
  elif  (rec.tense == 'aor') :
   self.bases = self.active_special_aor()
   self.status = (self.bases != [])
  elif (rec.tense == 'ppf'):
   self.bases = self.active_ppf()
  elif (rec.tense == 'prf'):
   self.bases = self.active_prf()
  elif (rec.voice in active_voices) and (rec.tense in general_tenses):
   if rec.tense == 'fut':
    self.bases = self.active_future()
   elif rec.tense == 'pft':
    self.bases = self.active_pft()
   elif rec.tense == 'con':
    self.bases = self.active_con()
   elif rec.tense == 'ben':
    self.bases = self.active_ben()
  else:
   print('BaseObj: unknown inputs:', self.rootmodel.line)
  #return 

 def any_passive_special(self):
  """ passive for tense pre, ipf, ipv, pot """
  rec = self.rootmodel
  c = rec.theclass 
  v = rec.voice
  root = rec.root
  # class and voice probably not needed. But they are part of the
  # calling sequence. The 'pada' argument is probably 'P' or 'A'
  voice_pada = {'p':'passive'}
  pada = voice_pada[v]
  upasargas=[]
  bases = test2.construct_conjpassbase1a(root,c,pada,upasargas,dbg=self.dbg)
  if rec.tense == 'ipf':
   bases = self.ipf_adjust(bases)
  return bases

 def ipf_adjust(self,bases):
  bs = bases
  bases = []
  for b in bs:
   b0 = b[0]
   #if b0 in sandhi1.simplevowel_set:
   if b0 in sandhi1.vfdDi:  # seems to vary from test2. Example 'iK'
    bnew = sandhi1.vfdDi[b0] + b[1:]
   elif b0 == 'C':
    # a + C -> acC.  Example Cad
    bnew = 'a' + 'c' + b
   else:
    bnew = 'a' + b
   bases.append(bnew)
  return bases

 def active_future(self):
  rec = self.rootmodel
  c = rec.theclass 
  v = rec.voice
  root = rec.root
  tense = rec.tense
  tense2 = tenses_sl_test2[tense]
  # class and voice probably not needed. But they are part of the
  # calling sequence. The 'pada' argument is probably 'P' or 'A'
  voice_pada = {'a':'P','m':'A'}
  pada = voice_pada[v]
  upasargas = []
  base = test2.future_base(root,c,pada,upasargas,tense2)
  #print('base=',base)
  if isinstance(base,str):
   bases = [base]
  elif isinstance(base,list):
   bases = base
  else:
   bases = []
  # get sew code  (in vew, aniw, sew)
  #ForC = test2.ForC 
  #ForC.ForC_sym = tense2
  sew_code = test2.ForC_sewCode(root,c,pada,upasargas,tense2)
  #print('sew_code=',sew_code)
  if sew_code == 'vew':
   sew_codes = ['aniw','sew']
  else:
   sew_codes = [sew_code]
  bases1 = []
  for b in bases:
   for c in sew_codes:
    if c == 'sew':
     b = self.add_i(b)
    bases1.append(b)
  bases2 = [self.future_join_sy(b) for b in bases1]
  exceptions = {
   'aYj': ['aNkzy','aYjizy'], # Whitney
   'arT': ['arTayizy'], # Apte, Deshpande
   'UrRu': ['UrRuvizy'], # MW,  also 'UrRavizy'? 
   'f' : ['arizy'], # ref mw
   'kf': ['karizy'], # ref mw
   'Gf': ['Garizy'], # ref whitney roots
   'jf': ['jarizy'], # test2.py
   'Df': ['Darizy'], # ref mw, whitney
   'Dvf':['Dvarizy'], # ref mw
   'kfz':['karkzy','krakzy'],
   'kF':['karizy','karIzy'], # whitney
   'gam':['gamizy'], # whitney, mw
   'gAh':['GAkzy','gAhizy'], # Deshpande
   'guh':['gUhizy','Gokzy'], # Whitney
   'gF': ['garizy','garIzy'], # Whitney
   'grah':['grahIzy'], # MW. Whitney has additional forms
   'Gas': ['Gatsy'], # Whitney
   'Cfd': ['Cartsy','Cardizy'], # MW
   'jF': ['jarizy','jarIzy'], # Whitney
   'tfp': ['tarpsy','tarpizy','trapsy'], # MW
   'tF': ['tarizy','tarIzy'], # MW
   'dah': ['Dakzy'], # MW  also 'dahizy' MW, whitney
   'dih': ['Dekzy'], # MW
   'duh': ['Dokzy'], # MW
   'dF' : ['darizy','darIzy'], # Whitney
   'druh': ['Drokzy','drohizy'], # MW
   'naS': ['naSizy','naNkzy'], # MW  test2 has naMzky for naNkzy
   'nah': ['natsy'], # MW
   'nu': ['navizy','nuvizy'], # MW, Whitney
   'pF': ['parizy','parIzy'], # Whitney
   'banD': ['Bantsy','banDizy'], # MW, Whitney
   'buD': ['Botsy'], #Whitney
   'BaYj': ['BaNkzy'], # MW
   'Bf': ['Barizy'], # MW, Whitney
   'man': ['maMsy','manizy'], # MW, Whitney
   'mf': ['marizy'], # MW
   'raYj': ['raNkzy'], # MW
   'vf': ['varizy','varIzy'], # MW, Whitney
   'vft': ['vartsy','vartizy'], # MW,
   'vfD': ['vartsy','varDizy'], # MW,
   'vraSc': ['vrakzy','vraScizy'], # MW
   'SfD':['Sartsy','SarDizy'], # MW
   'SF': ['Sarizy','SarIzy'], # MW
   'saYj': ['saNkzy'], # MW
   'sf': ['sarizy'], # MW
   'sfj': ['srakzy'], # MW
   'stf': ['starizy'], # MW
   'spf': ['sparizy'], # MW
   'spfS':['sparkzy','sprakzy'], # MW
   'smf': ['smarizy'], # MW
   'syand': ['syantsy','syandizy'], # MW
   'svf': ['svarizy'], # MW
   'han': ['haMsy','hanizy'], # MW
   'hf': ['harizy'], # MW
   'hvf': ['hvarizy'], # MW
  }
  # differences between test2 and this code confirmed by MW or Whitney
  diff_confirmed = {
   'aj': ['ajizy'], # MW
   'kam':['kamizy'], # Whitney
   'kruD':['krotsy'], # MW
   'gam':['gamizy'], #MW, Whitney
  }
  if root in exceptions:
   bases2 = exceptions[root]
  return bases2
  
 def add_i(self,b): # static
  if b.endswith(('u','U')):
   return b[0:-1]+'av'+'i'
  if b.endswith('o'):  # BU, as
   return b[0:-1]+'av'+'i'
  if b.endswith('e'):  # qI
   return b[0:-1]+'ay'+'i'
  # default
  return b+'i'

 def future_join_sy(self,b):
  """ static method """
  e = 'sy'
  if b.endswith('i'):
   # e starts with 's', which becomes 'z' after 'i'
   return b + 'z' + e[1:]
  if b.endswith(('e','o')):
   # e starts with 's', which becomes 'z' after 'e', 'o'
   return b + 'z' + e[1:]  
  if b.endswith(('d','D')):
   # switch to hard consonant before initial 's' of 'e'
   return b[0:-1]+'t'+e
  if b.endswith('kz'):
   # root=takz 
   return b+e[1:]
  if b.endswith(('S','z','h','k')):
   # change final sibilant to 'k' and replace initial 's' with z'
   return b[0:-1]+'kz'+e[1:]
  if b.endswith(('s')):
   # change final sibilant to 't' 
   return b[0:-1]+'t'+e
  if b.endswith(('j','c')):
   # change final 'j' or 'c' to 'k' and replace initial 's' with z'
   return b[0:-1]+'kz'+e[1:]
  if b.endswith('m'):
   # replace 'm' with 'M' before 'sy'
   return b[0:-1] + 'M' + e
  if b.endswith('B'):
   # replace 'B' with 'p' before 'sy'
   return b[0:-1] + 'p' + e
  # default
  return b+e

 def active_pft(self):
  rec = self.rootmodel
  c = rec.theclass 
  v = rec.voice
  root = rec.root
  tense = rec.tense
  tense2 = tenses_sl_test2[tense]
  # class and voice probably not needed. But they are part of the
  # calling sequence. The 'pada' argument is probably 'P' or 'A'
  voice_pada = {'a':'P','m':'A'}
  pada = voice_pada[v]
  upasargas = []
  #base = test2.future_base(root,c,pada,upasargas,tense2)
  # Deshpande 295.  Base for periphrastic future is 'same' as infinituve
  #   without the 'tum'
  dtype=None
  inf = test2.sl_inf(root,c,v,dtype)
  #print('base=',base)
  if isinstance(inf,str):
   infs = [inf]
  elif isinstance(inf,list):
   infs = inf
  else:
   infs = []
  # remove just the ending 'um' of the infitive(s)
  bases = [re.sub('um$','',inf) for inf in infs]
  return bases

 def active_con(self):
  """ Deshpande p. 327.  Get future base(s), then add 'a' augment, as
      with imperfect tense.
  """
  bases = self.active_future()
  bases = self.ipf_adjust(bases)
  return bases

 def active_ben(self):
  """ Use only the cases from benedictive_3s.txt
  """
  d = benedictive.d
  key = (self.rootmodel.root,self.rootmodel.voice)
  if key not in d:
   # We don't know anything of this
   return []
  rec = d[key]
  return rec.bases

 def unused_active_ben(self):
  """ Use test2.benedictive_base function.
   MW and Whitney have only a few examples.
   Be sure exceptions agree with Deshpande table on page 330ff.
  """
  rec = self.rootmodel
  c = rec.theclass 
  v = rec.voice
  root = rec.root
  tense = rec.tense
  tense2 = tenses_sl_test2[tense]
  # class and voice probably not needed. But they are part of the
  # calling sequence. The 'pada' argument is probably 'P' or 'A'
  voice_pada = {'a':'P','m':'A'}
  pada = voice_pada[v]
  upasargas = []
  base = test2.benedictive_base(root,c,pada,upasargas)
  if isinstance(base,str):
   bases = [base]
  elif isinstance(base,list):
   bases = base
  else:
   bases = []
  if v == 'm':
   # get sew code  (in vew, aniw, sew)
   sew_code = test2.ForC_sewCode(root,c,pada,upasargas,tense2)
   if sew_code == 'vew':
    sew_codes = ['aniw','sew']
   else:
    sew_codes = [sew_code]
   bases1 = []
   for b in bases:
    for c in sew_codes:
     if c == 'sew':
      b = self.add_i(b)
     bases1.append(b)
   #bases2 = [self.future_join_sy(b) for b in bases1]
   bases2 = bases1
  else: 
   # v == a
   bases2 = bases
  return bases2

 def active_ppf(self):
  """ Use only the cases from ppfactn.txt
  """
  d = ppfactn.d
  key = (self.rootmodel.root,self.rootmodel.model)
  if key not in d:
   # We don't know anything of this
   return []
  rec = d[key]
  return rec.bases


 def active_prf(self):
  """ Use only the cases from perfect_bases.txt
    see perfect_bases.py for the logic which uses test2 to get bases
   Refer Kale p. 306,7. 
   There are 4 pieces of information in a 'base':
   - the reduplicated base to be used before strong endings
      namely, the singular parasmaipada (active voice) endings
   - the reduplicated base to be used before weak endings 
      namely, all the other endings
   - The 'sew_code' relevant for all endings EXCEPT the ending 'Ta' of
     the 2nd person singular active voice ending
   - The 'sew_code' relevant for the ending 'Ta'

  """
  d = perfect.d
  rec = self.rootmodel
  key = (rec.model,rec.root)
  if key not in d:
   # We don't know anything of this
   return []
  baserecs = d[key]  # there may be more than one
  bases = [baserec.base for baserec in baserecs]
  return bases

 def unused_active_prf(self):
  """ 
   Use functions from pysanskritv1
   In this case the 'bases' returned contains information needed to
   derive the conjugations, but the information is complex.
   Refer Kale p. 306,7. 
   There are 4 pieces of information:
   - the reduplicated base to be used before strong endings
      namely, the singular parasmaipada (active voice) endings
   - the reduplicated base to be used before weak endings 
      namely, all the other endings
   - The 'sew_code' relevant for all endings EXCEPT the ending 'Ta' of
     the 2nd person singular active voice ending
   - The 'sew_code' relevant for the ending 'Ta'
  """
  rec = self.rootmodel
  c = rec.theclass 
  v = rec.voice
  root = rec.root
  voice_pada = {'a':'P','m':'A'}
  pada = voice_pada[v]
  upasargas = []
  #bitab = test2.liw_main_get_bitab(upasargas,c,pada,root)
  #print(root,c,v,bitab)
  sew_codes = test2.construct_sewPERF_code1a(root,c,pada,upasargas)
  # sew_codes has 2 elements, which are sew,vew, or aniw
  if (len(sew_codes) != 2) or\
      (not set(sew_codes).issubset(set(['sew','vew','aniw']))):
   print("bases_test2 - active_prf error 1:",sew_codes)
   print(rec.line)
   exit(1)
  wparts = sandhi.word_parts(root)
  redups = test2.reduplicate_perfect(root,wparts)
  # The redups list has either 1 or 2 elements, which are strings 
  if (len(redups) not in [1,2]):
   print("bases_test2 - active_prf error 2:",redups)
   print(rec.line)
   exit(1)
  # When redups has length 1, then the value of both reduplicates is the same
  if len(redups) == 1:
   redups = [redups[0],redups[0]]
  # Allow for alternate redupes
  redups1 = [redups]
  redups1_exceptions = {
   'ji':[['jigi','jigy']],
   'ci':[['ciki','ciky'],['cici','cicy']],
   'tF':[['tatF','ter']]
  }
  if root in redups1_exceptions:
   redups1 = redups1_exceptions[root]
  bases = []
  for redups in redups1:
   # convert the 4 values into 1 string, which we call the base
   base = ','.join(redups+sew_codes)
   bases.append(base)
  #bases = [base]
  return bases

 def a_active_special(self):
  rec = self.rootmodel
  c = rec.theclass 
  v = rec.voice
  root = rec.root
  voice_pada = {'a':'P','m':'A'}
  pada = voice_pada[v]
  upasargas=[]
  bases = test2.class_a_base(root,c,pada,self.dbg)
  if rec.tense == 'ipf':
   bases = self.ipf_adjust(bases)
  return bases

 def active_special_2(self):
  """ Class 2 base is almost useless, there being so many special cases.
     Formally, we set the base to be the root.
  """
  rec = self.rootmodel
  bases = [rec.root]
  return bases

 def active_special_3(self):
  """ Class 3 base returns a pair: root,redup
      where redup is from a pysanskritv1 function
      This is where test2.conjugation_tab_3 starts (the function used
        in test2 for conjugation of class 3 verbs)
  """
  rec = self.rootmodel
  root = rec.root
  redup = sandhi.reduplicative_pfx(root)
  base = '%s,%s' %(root,redup)
  bases = [base]
  return bases

 def active_special_5(self):
  """ Class 5 base.  Use test2.construct_conjbase1a.
   The result is not very interesting -- just the root, except for Sru, damB
  """
  bases = self.active_special_other()
  return bases

 def active_special_7(self):
  """ Class 7 base.  Use test2.construct_conjbase1a.
   The result is not very interesting -- just the root
  """
  bases = self.active_special_other()
  return bases

 def active_special_8(self):
  """ Class 8 base.  Use test2.construct_conjbase1a.
   The result is not very interesting -- just the root
  """
  bases = self.active_special_other()
  return bases

 def active_special_9(self):
  """ Class 9 base.  Use test2.construct_conjbase1a.
   The result is not very interesting -- just the root
  """
  bases = self.active_special_other()
  return bases

 def active_special_aor(self):
  """ 'base' for aorist (tense == 'aor'). Just the root.
      Not useful
  """
  rec = self.rootmodel
  bases = [rec.root]
  return bases

 def active_special_other(self):
  # same as a_active_special
  rec = self.rootmodel
  c = rec.theclass 
  v = rec.voice
  root = rec.root
  voice_pada = {'a':'P','m':'A'}
  pada = voice_pada[v]
  upasargas=[]
  tense2 = tenses_sl_test2[rec.tense]
  voice2 = 'active'
  #self.dbg=True
  #print('CALLING(%s,%s,%s,%s,%s)' % (root,c,pada,upasargas,voice2))
  bases = test2.construct_conjbase1a(root,c,pada,upasargas,voice2,self.dbg)
  if False:
   print('CHECK active_special_other',rec.line,'bases=',bases)
   print(root,c,pada,upasargas,voice2)
  if not isinstance(bases,list):
   print('active_special_2 error:',rec.line)
  elif rec.tense == 'ipf':
   bases = self.ipf_adjust(bases)
  return bases

def test_p3sa(rec,option = 'p3s',dbg=False):
 """ present passive base.  Use conj
 """
 c,voice = rec.cvs[0] 
 dtype = None
 # class and voice probably not needed. But they are part of the
 # calling sequence. The 'pada' argument is probably 'P' or 'A'
 voice_pada = {'a':'P','m':'A'}
 pada = voice_pada[voice]
 upasargas=[]
 t3sarr = test2.construct_conjpassbase1a(rec.root,c,pada,upasargas,dbg=dbg)
 t3s = '/'.join(t3sarr)
 rec.outa = '%s %s' %(rec.root,t3s) 
 return
 
if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 recs = init_rootmodel(filein)
 f = codecs.open(fileout,"w","utf-8")
 for irec,rec in enumerate(recs):
  try:
   baseobj = BaseObj(rec)
   if baseobj.status and (baseobj.bases != []):
    for base in baseobj.bases:
     out = baseobj.rootmodel.line + '\t' + base
     f.write(out + '\n')
   else:
    print('ERROR computing bases for %s '% rec.line)
  except:
   print('Program bug computing bases for %s '% rec.line)
   print('-------------------------------------------------')
   baseobj = BaseObj(rec,dbg=True)
 f.close()

