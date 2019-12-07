"""perfect_3p.py
  Read perfect_3p.txt, parse into a dictionary.
"""
import codecs
from os.path import dirname, abspath
import os

def init_perfect_3p():
 curdir = dirname(abspath(__file__))
 filein = 'perfect_3p.txt'
 filepath = os.path.join(curdir,filein)
 d = {}
 with codecs.open(filepath,"r","utf-8") as f:
  for line in f:
   line = line.rstrip()
   if line.startswith(';'):
    continue
   parts = line.split(' ')
   if len(parts) == 5:
    key = '%s %s' %(parts[0],parts[1])
    value = '%s %s %s' %(parts[2],parts[3],parts[4])
    # allow alternates
    if key not in d:
     d[key] = []
    d[key].append(value)
 return d

perfect_3p_dict = init_perfect_3p()
