# -*- coding: utf-8 -*-
""" root_model.py
"""
import sys,re,codecs
## next used for perfect  (init_rootmodel_4)
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
 print('models/root_model.py ERROR: cannot import test2')
 print(sys.path)
 exit(1)
inputdir = os.path.join(parent,'inputs')
sys.path.append(inputdir)
import verb_cp_manual

class Root(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  try:
   parts = line.split(':')
   (self.root,self.Lrefstr,self.cvstr) = parts[0:3]
  except:
   print('root_model - Root ERROR. Cannot parse',line)
   exit(1)
  if ',' in self.cvstr :
   parts = self.cvstr.split(',')
  else:
   # allow no cv string.
   parts = []
  cvs = []
  for part in parts:
   m = re.search(r'^([0-9]+)([ma])$',part)
   if m == None:
    print('Root ERROR 2. bad cvpart',part)
    print('line = ',line)
    exit(1)
   c = m.group(1)
   voice = m.group(2)
   cv = (c,voice)
   cvs.append(cv)
  self.cvs = cvs

 def classes(self):
  return set(c for c,v in self.cvs)

def init_roots(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for line in f:
   if line.startswith(';'):
    continue
   recs.append(Root(line))
 return recs

class RootModel(object):
 def __init__(self,root,Lrefstr,theclass,voice,tense):
  self.root = root
  self.Lrefstr = Lrefstr
  if theclass == None:
   theclass = '_'
  if voice == None:
   voice = '_'
  a = [theclass,voice,tense]
  self.model = ','.join(a)
 def toString(self):
  a = [self.model,self.root,self.Lrefstr]
  return '\t'.join(a)

def init_rootmodel_1(recs,classes):
 ans = []
 tenses = ['pre','ipf','ipv','opt']
 #classes = ['1','4','6','10']
 for rec in recs:
  for c,v in rec.cvs:
   if c in classes:
    for tense in tenses:
     rootmodel = RootModel(rec.root,rec.Lrefstr,c,v,tense)
     ans.append(rootmodel)
 return ans

def init_rootmodel_2(recs):
 # passive
 ans = []
 tenses = ['pre','ipf','ipv','opt']
 #classes = ['1','4','6','10']
 for rec in recs:
  #c,v = rec.cvs[0]
  for tense in tenses:
   v = 'p'   
   c = None
   rootmodel = RootModel(rec.root,rec.Lrefstr,c,v,tense)
   ans.append(rootmodel)
 return ans

def init_rootmodel_3(recs,tense):
 ans = []
 tenses = [tense]
 for rec in recs:
  # get all voices ('a','m') that occur. Ignore the classes
  voices = list(set(v for c,v in rec.cvs))
  for v in voices:
   c = None
   for tense in tenses:
    rootmodel = RootModel(rec.root,rec.Lrefstr,c,v,tense)
    ans.append(rootmodel)
 return ans

def init_rootmodel_4(recs,tense):
 """ prf (reduplicative perfect) and 
     ppf (periphrastic perfect)
     Use code from pysanskritv1 to determine
 """
 assert tense in ['prf','ppf'],"root_model error. init_rootmodel_4. Wrong tense" % tense
 ans = []
 dups = {}
 for rec in recs:
  root = rec.root
  for c,v in rec.cvs:
   if ( (tense == 'prf') and test2.reduplicative_liw_P(root,c)):
    key = (root,v,tense)
    c0 = None
   elif ( (tense == 'ppf') and test2.periphrastic_liw_P(root,c)):
    # exclude several cases where Deshpande shows no periphrastic perfect
    # Make this consistent with bases/ppfactn.txt
    if (root in ['Bf','hf']) or\
       ((root == 'vid') and (v == 'm')):
     print('root_model. Skipping',c,v,tense,root)
     continue
    # Construct the root-model
    if c == '10':
     c0 = c # None # c
     key = (root,v,tense,c)
    else:
     c0 = None
     key = (root,v,tense)
   else:
    continue
   # found another case for root model
   if key in dups:
    print('skip root_model_duplicate:',key,c)
   else:
    rootmodel = RootModel(root,rec.Lrefstr,c0,v,tense)
    ans.append(rootmodel)
    dups[key]=True
 return ans

def init_rootmodel_5(recs,tense,conjtabs):
 """  for manual.
  Build models with conjtabs, and use recs to get L
  Make note of root duplicates
  Make note of unused roots
 """
 # get dictionary into recs with key = root
 d = {}
 dups = {}  # duplicate RootModel
 for rec in recs:
  k = rec.root
  if k in d:
   print('init_rootmodel_5 WARNING: duplicate root',k)
  d[k] = rec
  rec.used = True  # True if this root appears in conjtab
 ans = []
 for conjtab in conjtabs:
  # gather parameters for RootModel
  root = conjtab.root
  if root in d:
   rec = d[root]
   Lrefstr = rec.Lrefstr
  else:
   print('init_rootmodel_5 ERROR: skip unknown root',root)
   for line in conjtab.lines:
    print(line)
   continue
  model = conjtab.model
  theclass,voice,tense = model.split(',')
  key = (root,voice,tense,theclass)
  if key in dups:
   print('init_rootmodel_5 WARNING: skip root_model_duplicate',key)
   for line in conjtab.lines:
    print(line)
  else:
   rootmodel = RootModel(root,Lrefstr,theclass,voice,tense)
   ans.append(rootmodel)
   dups[key]=True
 return ans

if __name__ == "__main__":
 # filein is like tempverb/pysanskritv2/inputs/verb_cp.txt
 option = sys.argv[1]
 filein = sys.argv[2]  
 optionparts = option.split(',')
 if optionparts[0] == '5':
  filetables = sys.argv[3] 
  fileout = sys.argv[4]
  #exit(1)
 else:
  fileout = sys.argv[3]

 #filelog = sys.argv[4]
 recs = init_roots(filein)
 if optionparts[0] == '1':
  if len(optionparts) == 1:
   classes = ['1','4','6','10']
  else:
   classes = optionparts[1:]
  rootmodels = init_rootmodel_1(recs,classes)
 elif option == '2': # passive
  rootmodels = init_rootmodel_2(recs)
 elif optionparts[0]== '3':
  tense = optionparts[1]  # option == 3,fut, etc.
  rootmodels = init_rootmodel_3(recs,tense)
 elif optionparts[0]== '4':
  tense = optionparts[1]  # option == 4,prf or 4,ppf
  rootmodels = init_rootmodel_4(recs,tense)
 elif optionparts[0] == '5':
  #print('root_model_error: option 5 not implemented')
  tense = optionparts[1]  # used?
  conjtabs = verb_cp_manual.init_conjtab(filetables)
  print(len(conjtabs),"conjugation tables read from",filetables)
  rootmodels = init_rootmodel_5(recs,tense,conjtabs)
 else:
  print('root_model.py. Unknown option',option)
 with codecs.open(fileout,"w","utf-8") as f:
  for rootmodel in rootmodels:
   out = rootmodel.toString()
   f.write(out + '\n')
  print(len(rootmodels),"models written to",fileout)
