# -*- coding: utf-8 -*-
""" 
    
"""
import sys,re,codecs
logdir='compare_logs'

class Rec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  self.model,self.stem,self.refstr = line.split('\t')
  self.dup = False
  refs = self.refstr.split(':')
  self.Lnums=[]
  self.keys=[]
  for refstr in refs:
   L,key1 = refstr.split(',')
   self.Lnums.append(L)
   self.keys.append(key1)
  self.Lnum0 = min([float(L) for L in self.Lnums])
 def appendrefs(self,rec):
  n = 0 # number of new L's
  for i,L in enumerate(rec.Lnums):
   key = rec.keys[i]
   if L not in self.Lnums:
    self.Lnums.append(L)
    self.keys.append(key)
    n = n + 1
  return n
 def new_refstr(self):
  refs = []
  for i,L in enumerate(self.Lnums):
   key = self.keys[i]
   ref = '%s,%s' %(L,key)
   refs.append(ref)
  refstr = ':'.join(refs)
  return refstr

def init_recs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Rec(x) for x in f]
 return recs


def do_dups(recs1,fout,fdup):
 ndup = 0
 nout = 0
 e = {}
 recdup = []
 recout = []
 for irec1,rec1 in enumerate(recs1):
  stem1 = rec1.stem.replace('-','')
  model = rec1.model
  key =  model + '+' + stem1
  iline = irec1 + 1
  linestr='%06d' % iline
  if (key in e) :
   # rec1 is a duplicate
   ndup = ndup + 1
   rec0 = e[key]
   rec1.dup = True
   # update rec0.Lnums and rec0
   nf = rec0.appendrefs(rec1)
   if nf == 0:  
    # unexpected
    print('Odd duplicate:')
    print(' old=',rec0.line)
    print(' new=',rec.line)
   recdup.append(rec1)
   print('Duplicate %03d'%ndup)
   print(rec0.line)
   print(rec1.line)
   print()
  else:
   # non-duplicate
   nout = nout + 1
   recout.append(rec1)
   e[key]= rec1 
 print(ndup,"Duplicates found")
 print(nout,"non-duplicates")
 #recout1 = sorted(recout,key = lambda rec: rec.Lnum0)
 recout1 = recout
 for rec1 in recout1:
  refstr1 = rec1.new_refstr()
  line = '\t'.join([rec1.model,rec1.stem,refstr1])
  fout.write(line + '\n')
 #recdup1 = sorted(recdup,key = lambda rec: rec.Lnum0)
 recdup1 = recdup
 for rec1 in recdup1:
  fdup.write(rec1.line + '\n')

if __name__ == "__main__":
 filein = sys.argv[1] # 
 fileout = sys.argv[2] # non-dups
 filedup = sys.argv[3]
 recs = init_recs(filein)
 fout = codecs.open(fileout,"w","utf-8")
 fdup = codecs.open(filedup,"w","utf-8")
 do_dups(recs,fout,fdup)
 fout.close()
 fdup.close()
