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

class Root(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  try:
   (self.root,self.Lrefstr,self.cvstr) = line.split(':')
  except:
   print('root_model - Root ERROR. Cannot parse',line)
   exit(1)
  parts = self.cvstr.split(',')
  cvs = []
  for part in parts:
   m = re.search(r'^([0-9]+)([ma])$',part)
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
     c0 = None # c
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

if __name__ == "__main__":
 # filein is like tempverb/pysanskritv2/inputs/verb_cp.txt
 option = sys.argv[1]
 filein = sys.argv[2]  
 fileout = sys.argv[3]
 #filelog = sys.argv[4]
 recs = init_roots(filein)
 optionparts = option.split(',')
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
 else:
  print('root_model.py. Unknown option',option)
 with codecs.open(fileout,"w","utf-8") as f:
  for rootmodel in rootmodels:
   out = rootmodel.toString()
   f.write(out + '\n')
