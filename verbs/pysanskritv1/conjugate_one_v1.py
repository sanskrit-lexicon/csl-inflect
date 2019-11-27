# -*- coding: utf-8 -*-
""" conjugate_one_v1.py, based on test2 code  11-21-2019
"""
import sys,re,codecs
#import test2
from conjugate_file_v1 import ConjRec
def test(model,verb):
 line = '%s\t%s\t%s' %(model,verb,'')
 conj = ConjRec(line)
 inflectionTable = conj.inflection  # string format
 #print(inflectionTable)
 if inflectionTable == None:
  print("Problem with conjugation of",model,verb)
  exit(1)
 tables = inflectionTable.split('&') # multiple bases allowed
 outarr = []
 for itable,table in enumerate(tables):
  table = table.split(':')
  out = "Conjugation of %s %s " %(model,verb)
  if len(tables) != 1:
   out = '%s (version %s of %s)' %(out,itable+1,len(tables))
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
  if len(tables)!= 1:
   outarr.append('')
 for out in outarr:
  print(out)

def test_md(model,verb):
 # generate a markdown table
 key1 = verb.replace('-','')
 line = '%s\t%s\t%s' %(model,verb,'')
 conj = ConjRec(line)
 inflectionTable = conj.inflection  # string format
 #print inflectionTable
 if inflectionTable == None:
  print("Problem with conjugation of",model,verb)
  exit(1)
 tables = inflectionTable.split('&') # multiple bases allowed
 
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
 model = sys.argv[1]
 verb = sys.argv[2]
 try:
  format = sys.argv[3]
 except:
  format = None
 if format == None:
  test(model,verb)
 elif format == 'md':
  test_md(model,verb)
 #elif format == 'md1':
 # test_md1(model,verb)
 else:
  print('Unknown format option',format)
  print('The format options are: md, md1')


