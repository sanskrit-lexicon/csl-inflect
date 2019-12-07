"""bases/perfect.py
  parse data from bases/perfect_bases.txt
"""
import sys,re,codecs

class Perfect(object):
 def __init__(self,line):
  line = line.rstrip()
  try:
   (self.model,self.root,self.base) = re.split('\t',line)
  except:
   print('bases/perfect.py: ERROR 0:',line)
   exit(1)
    
def init_perfect():
 from os.path import dirname, abspath
 import os
 curdir = dirname(abspath(__file__))
 filein = os.path.join(curdir,'perfect_bases.txt')
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Perfect(line) for line in f if not line.startswith(';')]
 return recs

recs = init_perfect()
d = {}
for rec in recs:
 key = (rec.model,rec.root)
 if key not in d:
  d[key] = []
 d[key].append(rec)

