# -*- coding: utf-8 -*-
""" compare_cv.py
"""
import sys,re,codecs
slp_from = "aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh"
slp_to =   "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw"
slp_from_to = str.maketrans(slp_from,slp_to)

class CV(object):
 def __init__(self,line):
  parts = line.split(':')
  if len(parts) == 2:
   self.root,self.cvstr = parts[0],parts[1]
  else: # 3 parts  middle is a list of L-numbers
   self.root,self.cvstr = parts[0],parts[2]
  self.cvs = self.cvstr.split(',')

def init_cvs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f if not x.startswith(';')]
 recs = []
 for line in lines:
  recs.append(CV(line))
 print(len(recs),'records read from',filein)
 #recs.sort(key = lambda x: x.root.translate(slp_from_to))
 return recs

def init_cvs3(filein):
 # the not-genuine roots from mw.
 pfx = ';not-genuine '
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f if  x.startswith(pfx)]
 recs = []
 for line in lines:
  line = line.replace(pfx,'')
  recs.append(CV(line))
 print('init_cvs3',len(recs),'records read from',filein)
 #recs.sort(key = lambda x: x.root.translate(slp_from_to))
 return recs

class Merger(object):
 def __init__(self,rec1,rec2,rec3):
  self.rec1 = rec1
  self.rec2 = rec2
  self.rec3 = rec3

def mergeroots(recs1,recs2,recs3):
 roots = {}
 for rec in recs1:
  root = rec.root
  roots[root] = Merger(rec,None,None)
 for rec in recs2:
  root = rec.root
  if root in roots:
   mergerec = roots[root]
   mergerec.rec2 = rec
  else:
   roots[root] = Merger(None,rec,None)
 for rec in recs3:
  root = rec.root
  if root in roots:
   mergerec = roots[root]
   mergerec.rec3 = rec
  else:
   #roots[root] = Merger(None,rec,None)
   pass

 return roots

def get_cvstr(rec):
 if rec == None:
  return 'None'
 else:
  return rec.cvstr

def write(fileout,roots,sym1,sym2,sym3):
 allroots = sorted(roots.keys(),key = lambda x: x.translate(slp_from_to))
 print(len(allroots),"merged roots")
 with codecs.open(fileout,"w","utf-8") as f:
  for root in allroots:
   mergerec = roots[root]
   rec1 = mergerec.rec1
   rec2 = mergerec.rec2
   rec3 = mergerec.rec3
   cvstr1 = get_cvstr(rec1)
   cvstr2 = get_cvstr(rec2)
   cvstr3 = get_cvstr(rec3)
   out = '%s %s=%s %s=%s %s=%s' %(root,sym1,cvstr1,sym2,cvstr2,sym3,cvstr3)
   f.write(out+'\n')
 print(len(allroots),"records written to",fileout)
if __name__ == "__main__":
 sym1,filein1 = sys.argv[1].split(',')
 sym2,filein2 = sys.argv[2].split(',')
 sym3 = 'NG'
 filein3 = filein2
 fileout = sys.argv[3]
 recs1 = init_cvs(filein1)
 recs2 = init_cvs(filein2)
 recs3 = init_cvs3(filein3)
 roots = mergeroots(recs1,recs2,recs3)
 write(fileout,roots,sym1,sym2,sym3)
 exit(1)
 dtab = init_conjtables(filein)
 recs = get_cvs(dtab)
