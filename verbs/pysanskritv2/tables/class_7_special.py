"""class_7_special.py
  read tables_1_7.txt and parse.
  This is a close variant of class_2_special.py:  simply changed '_2' to '_7'.
"""
import sys,re,codecs

class Table(object):
 def __init__(self,model,root,table):
  self.model = model
  self.root = root
  self.table = table
    
def init_table():
 from os.path import dirname, abspath
 import os
 curdir = dirname(abspath(__file__))
 filein = os.path.join(curdir,'tables_1_7.txt')
 with codecs.open(filein,"r","utf-8") as f:
  lines = [line.rstrip() for line in f if not line.startswith(';')]
  #recs = [Table(line) for line in f if not line.startswith(';')]
 recs = []
 #for iline,line in enumerate(lines):
 nlines = len(lines)
 for iline in range(0,nlines,4):
  # 1st line of form 'Conjugation of <model> <root>'
  m = re.search(r'^Conjugation of (.*?) (.*?)$',lines[iline + 0])
  model = m.group(1)
  root = m.group(2)
  # initialize conjugation table
  tab = []
  # 2nd line of form '3p x y z'
  m = re.search(r'^3p (.*?) (.*?) (.*?)$',lines[iline + 1])
  tab.append(m.group(1))
  tab.append(m.group(2))
  tab.append(m.group(3))
  # 3rd line of form '2p x y z'
  m = re.search(r'^2p (.*?) (.*?) (.*?)$',lines[iline + 2])
  tab.append(m.group(1))
  tab.append(m.group(2))
  tab.append(m.group(3))
  # 4th line of form '1p x y z'
  m = re.search(r'^1p (.*?) (.*?) (.*?)$',lines[iline + 3])
  tab.append(m.group(1))
  tab.append(m.group(2))
  tab.append(m.group(3))
  # replace missing values ('_') with empty string
  tab = [x.replace('_','') for x in tab]
  # generate a Table record
  rec = Table(model,root,tab)
  recs.append(rec)
 return recs

recs = init_table()
d = {}
for rec in recs:
 key = (rec.model,rec.root)
 if key not in d:
  d[key] = []
 d[key].append(rec.table)

