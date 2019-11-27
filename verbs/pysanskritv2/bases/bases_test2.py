"""pysanskritv2/mining/mine_test2.py
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
except:
 print('bases_test2. cannot import test2')
 print(sys.path)
 exit(1)

import codecs,re

class RootModel(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.model,self.root,self.Lrefs) = line.split('\t')
  (self.theclass,self.voice,self.tense) = self.model.split(',')

def init_rootmodel(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [RootModel(line) for line in f if not line.startswith(';')]
 return recs

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
  bases = self.ipf_adjust(bases)
  return bases

 def ipf_adjust(self,bases):
  if self.rootmodel.tense == 'ipf':
   bs = bases
   bases = []
   for b in bs:
    b0 = b[0]
    #if b0 in sandhi1.simplevowel_set:
    if b0 in sandhi1.vfdDi:  # seems to vary from test2. Example 'iK'
     bnew = sandhi1.vfdDi[b0] + b[1:]
    else:
     bnew = 'a' + b
    bases.append(bnew)
  return bases

 def a_active_special(self):
  rec = self.rootmodel
  c = rec.theclass 
  v = rec.voice
  root = rec.root
  # class and voice probably not needed. But they are part of the
  # calling sequence. The 'pada' argument is probably 'P' or 'A'
  voice_pada = {'a':'P','m':'A'}
  pada = voice_pada[v]
  bases = test2.class_a_base(root,c,pada,self.dbg)
  bases = self.ipf_adjust(bases)
  return bases

 def unused_passive_pre(self,rec,option = 'p3s',dbg=False):
  """ present passive base.
  """
  c,voice = rec.cvs[0] 
  dtype = None
  tab = test2.sl_conjtab(rec.root,c,'p',[],'pre',dtype,dbg=dbg)
  #tab = test2.v_file_init_alt1_pre_helper(rec.root,c,'p','pre',None)
  #print(len(tab))
  #print(tab)
  if len(tab) == 9:
   tabs = [tab]
  else:
   tabs = tab
  t3sarr = []
  for t in tabs:
   x = t[0]  # 3rd singular of present passive
   assert x.endswith('ate'),'Does not end in ate: ' + rec.line
   x = re.sub(r'ate$','',x)
   t3sarr.append(x)
  t3s = '/'.join(t3sarr)
  rec.out = '%s %s' %(rec.root,t3s) 

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

