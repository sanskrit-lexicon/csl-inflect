# -*- coding: utf-8 -*-
""" makecv.py
"""
import sys,re,codecs
from conjugate_one import init_conjtables

def get_cvs(dtab):
 rootd = {}
 roots = []
 for model,root in dtab.keys():
  c,v,t = model.split(',') # class, voice, tense
  if root not in rootd:
   rootd[root] = []
   roots.append(root)
  cv = '%s%s' %(c,v)
  if cv not in rootd[root]:
   rootd[root].append(cv)
 recs = []
 for root in roots:
  cvs = rootd[root]
  cvstr = ','.join(cvs)
  rec = (root,cvstr)
  recs.append(rec)
 return recs

def write(fileout,recs):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   root,cvstr = rec
   out = '%s:%s' %(root,cvstr)
   f.write(out+'\n')
 print(len(recs),"records written to",fileout)
if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 dtab = init_conjtables(filein)
 recs = get_cvs(dtab)
 write(fileout,recs)
