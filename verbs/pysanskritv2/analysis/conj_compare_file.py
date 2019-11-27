# -*- coding: utf-8 -*-
""" conj_compare.py
  compare pysanskritv1 and pysanskritv2 
"""
import sys,codecs,re
import conjugate_file_v2 as v2
sys.path.append('../../pysanskritv1/')
import conjugate_file_v1 as v1

def compare(line):
 v2_conj = v2.ConjRec(line)
 v1_conj = v1.ConjRec(line)
 outarr = []
 status = v1_conj.inflection == v2_conj.inflection
 if status:
  outarr.append('v1 == v2 for %s\t%s' %(line,v1_conj.inflection))
 else:
  outarr.append('v1 != v2 for %s' % line)
  outarr.append('v1: %s' % v1_conj.inflection)
  outarr.append('v2: %s' % v2_conj.inflection)
 return status,outarr

if __name__ == "__main__":
 filein = sys.argv[1] 
 fileout = sys.argv[2]
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f if not x.startswith(';')]
 nprob = 0
 f = codecs.open(fileout,"w","utf-8")
 for line in lines:
  (status,outarr) = compare(line)
  if not status:
   nprob = nprob + 1
  for out in outarr:
   f.write(out + '\n')
 f.close()
 print(nprob,'differences out of',len(lines),'examples')


 
