"""aorist.py
  Read tables_aorist.txt and tables_aorist_passive.txt
  and parse.
"""
import sys,re,codecs

class Table(object):
 def __init__(self,model,root,table):
  self.model = model
  self.root = root
  self.table = table
    
def init_table(filein0):
 from os.path import dirname, abspath
 import os
 curdir = dirname(abspath(__file__))
 filein = os.path.join(curdir,filein0)
 with codecs.open(filein,"r","utf-8") as f:
  lines = [line.rstrip() for line in f if not line.startswith(';')]
  #recs = [Table(line) for line in f if not line.startswith(';')]
 recs = []
 #for iline,line in enumerate(lines):
 nlines = len(lines)
 for iline in range(0,nlines,4):
  # 1st line of form 'Conjugation of <model> <root>'
  m = re.search(r'^Conjugation of (.*?) (.*?)$',lines[iline + 0])
  if not m:
   print('class_9_special.py Input ERROR @ line:',lines[iline + 0])
   exit(1)
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

def unused_reformat_table():
 from os.path import dirname, abspath
 import os
 curdir = dirname(abspath(__file__))
 filein = os.path.join(curdir,'tempsave_aorist_tables.txt')

 with codecs.open(filein,"r","utf-8") as f:
  lines = [line.rstrip() for line in f]
 fileout = os.path.join(curdir,'aorist_tables.txt')
 print('writing',fileout)
 outpassive = []
 passive_keys = {}
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   if not line.startswith('_'):
    f.write(line + '\n')
    continue
   try:
    model,root,thirds,passive3 = line.split(':')
    c,v,tense = model.split(',')
   except:
    print('Format ERROR:',line)
    exit(1)
   outarr = []
   outarr.append('Conjugation of %s %s' %(model,root))
   outarr.append('3p %s' %thirds)
   outarr.append('2p ? ? ?')
   outarr.append('1p ? ? ?')
   for out in outarr:
    f.write(out + '\n')
   # prepare passive - unless it has already been done
   modelp = '%s,p,%s' %(c,tense)
   key = (modelp,root)
   if key in passive_keys:
    continue
   passive_keys[key] = True
   outpassive.append('Conjugation of %s %s' %(modelp,root))
   outpassive.append('3p %s ? ?' % passive3)
   outpassive.append('2p ? ? ?')
   outpassive.append('1p ? ? ?')
 fileout = os.path.join(curdir,'aorist_passive.txt')
 print('writing',fileout)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outpassive:
   f.write(out+'\n')
#reformat_table()

recs1 = init_table('tables_aorist.txt')
recs2 = init_table('tables_aorist_passive.txt')
recs = recs1 + recs2
d = {}
for rec in recs:
 key = (rec.model,rec.root)
 if key not in d:
  d[key] = []
 d[key].append(rec.table)

