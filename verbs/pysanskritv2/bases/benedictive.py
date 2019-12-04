"""bases/benedictive.py
  parse data from bases/benedictive_3s.txt
"""
import sys,re,codecs

class Benedictive(object):
 def __init__(self,line):
  line = line.rstrip()
  try:
   (self.root,self.voice,self.s3txt) = re.split(r' +',line)
  except:
   print('bases_benedictive.py: ERROR 0:',line)
   exit(1)
  self.s3arr = self.s3txt.split('/') 
  assert self.voice in ['a','m'],'bases_benedictive.py: ERROR 1: %s' %line
  self.bases = []
  self.zs = []
  for s3 in self.s3arr:
   if self.voice == 'a':
    # active voice.  3s ends in 'yAt'. remove this to get base. zs = None
    assert s3.endswith('yAt'),'bases_benedictive.py: ERROR 2: %s' %line
    self.bases.append(s3[0:-3])
    self.zs.append(None)
   else: 
    # middle voice. 3s ends with 'sIzwa' or 'zIzwa' Remove this for base.
    assert s3.endswith(('sIzwa','zIzwa')),'bases_benedictive.py: ERROR 3: %s' %line
    self.bases.append(s3[0:-5])
    self.zs.append(s3[-5:-4])  # s or z
    
def init_benedictive():
 from os.path import dirname, abspath
 import os
 curdir = dirname(abspath(__file__))
 filein = os.path.join(curdir,'benedictive_3s.txt')
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Benedictive(line) for line in f if not line.startswith(';')]
 return recs

recs = init_benedictive()
d = {}
for rec in recs:
 key = (rec.root,rec.voice)
 if key in d:
  print('bases/benedictive.py. Warning Duplicate key:',key)
 d[key] = rec

