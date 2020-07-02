# -*- coding: utf-8 -*-
""" conjugate_one.py, based on test2 code  11-21-2019
"""
import sys,re,codecs
class ConjRec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.model,self.root,self.Lrefs,self.base,self.tab) = line.split('\t')
  self.key = (self.model,self.root)

def init_conjtables(filein):
 with codecs.open(filein,"r","utf-8") as f:
  d = {}
  for line in f:
   if not line.startswith(';'):
    rec = ConjRec(line)
    k = rec.key
    if k not in d:  # there can be duplicates
     d[k] = []
    d[k].append(rec)
 return d

def stringify_tab(model,verb,recs):
 outarr = []
 tables = [rec.tab for rec in recs]
 for itable,table in enumerate(tables):
  table = table.split(':')
  out = "Conjugation of %s %s " %(model,verb)
  #if len(tables) != 1:
  # out = '%s (version %s of %s)' %(out,itable+1,len(tables))
  outarr.append(out)
  casenames = ['3p','2p','1p'] # persons
  for icell in range(0,9,3):
   a = []
   case = (icell // 3) + 1
   a.append(casenames[case-1])
   #a.append('Case %d: ' % case)
   for i in range(0,3):
    x = table[icell+i]
    a.append(x)
   out = ' '.join(a)
   outarr.append(out)
  #if len(tables)!= 1:
  # outarr.append('')
 return outarr

def test(model,verb,recs):
 outarr = stringify_tab(model,verb,recs)
 for out in outarr:
  print(out)

def test_md(model,verb,recs):
 # generate a markdown table
 #key1 = verb.replace('-','')
 #line = '%s\t%s\t%s' %(model,verb,'')
 #conj = ConjRec(line)
 #inflectionTable = conj.inflection  # string format
 #print inflectionTable
 #if inflectionTable == None:
 # print("Problem with conjugation of",model,verb)
 # exit(1)
 #tables = inflectionTable.split('&') # multiple bases allowed
 
 tables = [rec.tab for rec in recs]
 outarr = []
 for itable,table in enumerate(tables):
  table = table.split(':')
  out = "Conjugation of %s %s " %(model,verb)
  if len(tables) != 1:
   out = '%s (version %s of %s)' %(out,itable+1,len(tables))
  outarr.append(out)
  outarr.append('')

  outarr.append('|Case|S|D|P|')
  outarr.append('|-|-|-|-|')
  #casenames = ['3rd Person','2nd Person','1st Person'] # persons
  casenames = ['3p','2p','1p'] # persons

  for icell in range(0,9,3):
   a = []
   case = (icell // 3) + 1
   a.append(casenames[case-1])
   for i in range(0,3):
    x = table[icell+i]
    a.append(x)
   out = '|'.join(a)
   out = '|' + out + '|'
   outarr.append(out)
  if len(tables)!= 1:
   outarr.append('')
 for out in outarr:
  print(out)

if __name__ == "__main__":
 dtab = init_conjtables('tables1_prs_huet.txt')
 model = sys.argv[1]
 verb = sys.argv[2]
 try:
  format = sys.argv[3]
 except:
  format = None
 if (model,verb) not in dtab:
  print('conjugation table unknown for %s %s'%(model,verb))
  exit(0)
 drecs = dtab[(model,verb)]
 if format == None:
  test(model,verb,drecs)
 elif format == 'md':
  test_md(model,verb,drecs)
 #elif format == 'md1':
 # test_md1(model,verb)
 else:
  print('Unknown format option',format)
  print('The format options are: md, md1')


