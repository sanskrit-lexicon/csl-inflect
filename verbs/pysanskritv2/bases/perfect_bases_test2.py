"""pysanskritv2/bases/perfect_bases_test2.py
 This is used to compute perfect bases using the logic
 of test2. bases_test2.py itself uses a file 'perfect_bases.txt' for
 the bases.
 Usage: takes an input file such as models/calc_models.txt,  but expects
  only perfect tense (prf). So a line of the input file has 
  2 or more  tab-delimited fields, the first two being used:
  fields: like model<tab>root
_,a,prf	ad
_,m,prf	ad
The output  adds a 'base' field like:
_,a,prf	ad	Ad,Ad,sew,sew
_,m,prf	ad	Ad,Ad,sew,sew
See active_prf method for a description of the 4 comma-delimited fields of
the base field
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

class RootModel(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  parts  = line.split('\t')
  self.model = parts[0]
  self.root = parts[1]
  self.Lrefs = 'None'
  (self.theclass,self.voice,self.tense) = self.model.split(',')

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
  if (rec.tense == 'prf'):
   self.bases = self.active_prf()
  else:
   print('perfect_bases_test2: BaseObj: unknown inputs:', self.rootmodel.line)

 def active_prf(self):
  """ Use functions from pysanskritv1
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
     rec = baseobj.rootmodel
     out = '%s\t%s\t%s' %(rec.model,rec.root,base)
     #out = baseobj.rootmodel.line + '\t' + base
     f.write(out + '\n')
   else:
    print('ERROR computing bases for %s '% rec.line)
  except:
   print('Program bug computing bases for %s '% rec.line)
   print('-------------------------------------------------')
   baseobj = BaseObj(rec,dbg=True)
 f.close()

