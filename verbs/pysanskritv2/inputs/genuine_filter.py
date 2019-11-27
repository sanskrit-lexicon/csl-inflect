""" genuine_filter.py
 Separate verb_cp - type file into genuine and non-genuine
"""
import sys,re,codecs
class Root(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.root,self.L,self.formstr) = line.split(':')
 
def init_roots(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for line in f:
   if line.startswith(';'):
    continue
   recs.append(Root(line))
 return recs

class Genuine(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.L,self.root,self.hom,dummy) = line.split('\t')
  self.used = False

def init_genuine(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for line in f:
   if line.startswith(';'):
    continue
   recs.append(Genuine(line))
 return recs

def mark_genuine(recs,grecs):
 # get dictionary of grecs, based on L
 g = {}
 for grec in grecs:
  # check for duplicate L
  L = grec.L
  if L in g:
   print('grec unexpected duplicate L',grec.line)
   exit(1)
  g[L] = grec

 for rec in recs:
  if rec.L in g:
   rec.genuine = True
   grec = g[rec.L]
   grec.used = True  # so we can note genuine roots not in recs
   # check root spelling in rec and grec
   if grec.root != rec.root:
    print('Difference in root spelling')
    print('  rec: ',rec.line)
    print(' grec: ',grec.line)
  else:
   rec.genuine = False

if __name__ == "__main__":
 filein = sys.argv[1]
 filegen = sys.argv[2]  # mw_genuine 
 fileout = sys.argv[3]  
 recs = init_roots(filein)
 grecs = init_genuine(filegen)
 mark_genuine(recs,grecs)
#flog = codecs.open(filelog,"w","utf-8")
 
 f = codecs.open(fileout,"w","utf-8")
 for rec in recs:
  if rec.genuine:
   out = rec.line
  else: # comment out this rec
   out = ';not-genuine ' + rec.line
  f.write(out+'\n')
 f.close()
 ## note unused genuine recs, if any
 unused = [grec for grec in grecs if not grec.used]
 if len(unused) == 0:
  print('All genuine records used')
 else:
  print('These genuine records not used:')
  for grec in unused:
   print(grec.line)
