"""pysanskritv2/bases/ppf_bases_test2.py
 This is used to compute periphrastic perfect bases  using the logic
 of test2;  this is used for a one-time initialization of ppfactn.txt.

 Usage: takes an input file such as models/calc_models_ppf.txt.
 python3 ppf_bases_test2.py ../models/calc_models_ppf.txt temp_ppfactn.txt

 So a line of the input file has 
  3 tab-delimited fields (model, root, Lrefs). For example
_,m,ppf	Ikz	29695
_,a,ppf	gaR	62523

The output  adds a 'base' field, containing the periphrastic perfect
action noun (ppfactn)
_,m,ppf Ikz 29695 IkzAm
_,a,ppf gaR 62523 gaRayAm

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
  self.Lrefs = parts[2]
  (self.theclass,self.voice,self.tense) = self.model.split(',')

def init_rootmodel(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [RootModel(line) for line in f if not line.startswith(';')]
 # restrict to cases where self.tense is ppf
 recs = [r for r in recs if r.tense == 'ppf']
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
  if (rec.tense == 'ppf'):
   self.bases = self.active_ppf()
  else:
   print('ppf_bases_test2: BaseObj: unknown inputs:', self.rootmodel.line)

 def active_ppf(self):
  """ Use test2 function to get periphrastic perfect action noun
  """
  rec = self.rootmodel
  c = rec.theclass 
  if rec.voice == '_':
   rec.voice = 'a'
  v = rec.voice
  root = rec.root
  voice_pada = {'a':'P','m':'A'}
  pada = voice_pada[v]
  bases = test2.periphrastic_base(root,c,pada)
  # Add 'Am' , that usually gives the periphrastic action noun
  bases1 = [b + 'Am' for b in bases]
  exceptions = {
   # root : bases
   'daRqaya':['daRqayAm'],
   'Cad': ['CAdayAm'],  # test2 also has 'CadayAm'
   'BI' : ['biBayAm'],  # test2 biBe + Am = biBayAm
  }
  if root in exceptions:
   bases1 = exceptions[root]
  # change the model, to ind_ppfactn
  #model = 'ind_ppfactn'
  #rec.line = '\t'.join([model,root,rec.Lrefs])
  return bases1


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
     # for constructing the base, we need to know if the class = 10.
     # however, we do not need further information about class.
     # So, we change class to '_'
     c = '_'
     model = ','.join([c,rec.voice,rec.tense])
     #out = '%s\t%s\t%s\t%s' %(model,rec.root,rec.Lrefs,base)
     out = '%s %s %s %s' %(model,rec.root,rec.Lrefs,base)
     f.write(out + '\n')
   else:
    print('ERROR computing bases for %s '% rec.line)
  except:
   print('Program bug computing bases for %s '% rec.line)
   print('-------------------------------------------------')
   baseobj = BaseObj(rec,dbg=True)
 f.close()

