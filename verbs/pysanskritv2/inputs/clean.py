""" clean.py
  Remove duplicates, etc. as described in readme.txt
"""
import sys,re,codecs
class Root(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.root,self.L,self.formstr) = line.split(':')
  parts = self.formstr.split(',')
  cps = []
  for part in parts:
   m = re.search(r'^([0-9]+)([AP]?)$',part)
   c = m.group(1)
   ap = m.group(2)
   d = {'A':['m'],'P':['a'],'':['a','m']}
   voices = d[ap]
   for voice in voices:
    cp = (c,voice)
    cps.append(cp)
  self.cps = cps
  cps1 = remove_dup_cp2(self.cps)
  cps1 = [c + v for c,v in cps1]
  try:
   self.cps_str = ','.join(cps1)
  except:
   print('Root error 2\n',line,'\n',cps1)
   exit(1)

 def classes(self):
  return set(c for c,v in self.cps)

def init_roots(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for line in f:
   if line.startswith(';'):
    continue
   recs.append(Root(line))
 return recs


def dup_roots(recs):
 d = {}
 for rec in recs:
  rec.duproot = False
  rec.newL = rec.L
  root = rec.root
  if '0' in rec.classes():
   # don't consider them. EXample 'ah'
   continue
  if root not in d:
   d[root] = []
  d[root].append(rec)

 for root in d:
  drecs = d[root]
  if len(drecs) == 1:
   continue
  rec0 = drecs[0]
  Larr = [rec0.L]
  cparr = rec0.newcps
  for rec in drecs[1:]:
   rec.duproot = True
   if rec.L in Larr:
    print('unexpected duplicate L:',rec.line)
   else:
    Larr.append(rec.L)
    cparr = cparr + rec.newcps
  rec0.newL = ','.join(Larr)
  rec0.newcps = remove_dup_cp2(cparr)

def remove_dup_cp2(cps):
 cps_set = set(cps)  # this removes duplicates
 vord = {'a':'0','m':'1'}
 newcps = sorted(list(cps_set),key = lambda (c,v): ('%02d'%int(c)) + vord[v])
 return newcps

def remove_dup_cp(recs):
 for rec in recs:
  rec.newcps = remove_dup_cp2(rec.cps)

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 #filelog = sys.argv[3]
 recs = init_roots(filein)
 remove_dup_cp(recs)
 dup_roots(recs)
 #flog = codecs.open(filelog,"w","utf-8")
 f = codecs.open(fileout,"w","utf-8")
 for rec in recs:
  if '0' in rec.classes():
   out = '; ' + (':'.join([rec.root,rec.L,rec.cps_str]))+ '  #zero'
  elif rec.duproot:
   out = '; ' + (':'.join([rec.root,rec.L,rec.cps_str])) + '  #dup#'
  else:
   newforms = ['%s%s' %(c,p) for c,p in rec.newcps]
   newformstr = ','.join(newforms)
   outarr = [rec.root,rec.newL,newformstr]
   out = ':'.join(outarr)
  f.write(out+'\n')
 f.close()
