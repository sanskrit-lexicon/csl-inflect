"""table.py
  Read conjugation table and construct dictionary
"""
class Table(object):
 def __init__(self,model,key2,table):
  self.model = model
  self.key2 = key2
  self.table = table
  self.nused = 0 
  #print(len(table))
  assert len(self.table) == 24  # declension table is 8*3 = 24
  self.tabstring = ':'.join(self.table)
def init_table(filein0):
 from os.path import dirname, abspath
 import os,codecs,re
 curdir = dirname(abspath(__file__))
 filein = os.path.join(curdir,filein0)
 with codecs.open(filein,"r","utf-8") as f:
  lines = [line.rstrip() for line in f if not line.startswith(';')]
  #recs = [Table(line) for line in f if not line.startswith(';')]
 recs = []
 #for iline,line in enumerate(lines):
 nlines = len(lines)
 for iline in range(0,nlines,9):
  # 1st line of form 'Conjugation of <model> <key2>'
  m = re.search(r'^Declension of (.*?) (.*?)$',lines[iline + 0])
  if not m:
   print('tableread ERROR1 @ line:',lines[iline + 0])
   exit(1)
  model = m.group(1)
  key2 = m.group(2)
  # initialize declension table
  tab = []
  for icase in [1,2,3,4,5,6,7,8]:
   # 2nd-9th line of form 'Case c:  x y z'
   m = re.search(r'^Case %s:  (.*?) (.*?) (.*?)$'%icase,lines[iline + icase])
   if not m:
    print('tableread ERROR2 @ line:',lines[iline + icase])
    exit(1)
   tab.append(m.group(1))
   tab.append(m.group(2))
   tab.append(m.group(3))
  # replace missing values ('_' or '?') with empty string
  tab = [x.replace('_','') for x in tab]
  tab = [x.replace('?','') for x in tab]
  # generate a Table record
  rec = Table(model,key2,tab)
  recs.append(rec)
 return recs
