# -*- coding: utf-8 -*-
""" root_model.py
"""
import sys,re,codecs

class Root(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.root,self.Lrefstr,self.cvstr) = line.split(':')
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
   a = ['_',voice,tense]
  else:
   a = [theclass,voice,tense]
  self.model = ','.join(a)
 def toString(self):
  a = [self.model,self.root,self.Lrefstr]
  return '\t'.join(a)

def init_rootmodel_1(recs):
 ans = []
 tenses = ['pre','ipf','ipv','opt']
 classes = ['1','4','6','10']
 for rec in recs:
  for c,v in rec.cvs:
   if c in classes:
    for tense in tenses:
     rootmodel = RootModel(rec.root,rec.Lrefstr,c,v,tense)
     ans.append(rootmodel)
 return ans

def init_rootmodel_2(recs):
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
if __name__ == "__main__":
 # filein is like tempverb/pysanskritv2/inputs/verb_cp.txt
 option = sys.argv[1]
 filein = sys.argv[2]  
 fileout = sys.argv[3]
 #filelog = sys.argv[4]
 recs = init_roots(filein)
 if option == '1':
  rootmodels = init_rootmodel_1(recs)
 elif option == '2':
  rootmodels = init_rootmodel_2(recs)
 else:
  print('root_model.py. Unknown option',option)
 with codecs.open(fileout,"w","utf-8") as f:
  for rootmodel in rootmodels:
   out = rootmodel.toString()
   f.write(out + '\n')
