# -*- coding: utf-8 -*-
""" conjugate_one_base.py
"""
import sys,re,codecs
import conjugate_from_bases
sys.path.append('../bases/')
import sandhi1 # for ipf_adjust to add prefix 'a'

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

def init_baserec(model,verb,base):
 Lrefs = 'XXX' # dummy value
 parms = [model,verb,Lrefs,base]
 line = '\t'.join(parms)
 baserec = conjugate_from_bases.BaseRec(line)
 # for ipf, add prefix 'a'
 if baserec.tense == 'ipf':
  base1 = ipf_adjust(baserec.base)
  baserec.base = base1 # over-write
 return baserec

def init_ConjRec(baserec,tab):
 tabstr = ':'.join(tab)
 parts = [baserec.model, baserec.root,baserec.Lrefs,baserec.base,tabstr]
 line = '\t'.join(parts)
 return ConjRec(line)

def ipf_adjust(b):
 """ from bases/bases_test2.py"""
 b0 = b[0]
 #if b0 in sandhi1.simplevowel_set:
 if b0 in sandhi1.vfdDi:  # seems to vary from test2. Example 'iK'
  bnew = sandhi1.vfdDi[b0] + b[1:]
 elif b0 == 'C':
  # a + C -> acC.  Example Cad
  bnew = 'a' + 'c' + b
 else:
  bnew = 'a' + b
 return bnew

def compute_outarr(model,verb,base):
 baserec = init_baserec(model,verb,base)
 tab = conjugate_from_bases.conjtab(baserec) # a ConjTable record
 conjrec = init_ConjRec(baserec,tab)
 outarr = stringify_tab(model,verb,[conjrec])
 return outarr
if __name__ == "__main__":
 model = sys.argv[1]  #class,voice,tense
 verb = sys.argv[2]
 base0 = sys.argv[3]
 base = base0
 outarr = compute_outarr(model,verb,base)
 for out in outarr:
  print(out)
 
 exit(1)
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


