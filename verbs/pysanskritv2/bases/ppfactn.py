"""bases/ppfactn.py
  parse data from bases/ppfactn.txt
"""
import sys,re,codecs

class Ppfactn(object):
 def __init__(self,line):
  line = line.rstrip()
  try:
   (self.model,self.root,self.Lrefs,self.ppfactn) = re.split(r' +',line)
  except:
   print('bases/ppfactn.py: ERROR 0:',line)
   exit(1)
  self.bases = self.ppfactn.split('/')  # no multiple instances currently
    
def init_ppfactn():
 from os.path import dirname, abspath
 import os
 curdir = dirname(abspath(__file__))
 filein = os.path.join(curdir,'ppfactn.txt')
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Ppfactn(line) for line in f if not line.startswith(';')]
 return recs

recs = init_ppfactn()
d = {}
for rec in recs:
 key = (rec.root,rec.model)
 if key in d:
  print('bases/ppfactn.py. Warning Duplicate key:',key)
 d[key] = rec

