""" verb_cp_manual.py
"""
import sys,re,codecs
#from clean import init_roots
class Verbcp(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.root,self.L,formstr) = line.split(':')
  self.cps = formstr.split(',')
  self.huet = None

 def classes(self):
  return set(c for c,v in self.cps)

def init_roots(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for iline,line in enumerate(f):
   if line.startswith(';'):
    continue
   try:
    recs.append(Verbcp(line))
   except:
    print('init_roots ERROR at line %s of %s'%(iline+1,filein))
    print(line)
 print('init_roots: %s records read from %s'%(len(recs),filein))
 return recs

persons = ['3p','2p','1p']

class ConjTable(object):
 def __init__(self,lines):
  self.lines = lines
  lineparts = [line.split(' ') for line in lines]
  tablines = []
  tab = []
  for iparts,parts in enumerate(lineparts):
   assert len(parts) == 4
   if iparts == 0:
    assert parts[0] == 'Conjugation'
    assert parts[1] == 'of'
    self.model = parts[2]
    self.root = parts[3]
   else:
    assert parts[0] == persons[iparts-1]
    tablines = tablines + parts[1:]
    forms = parts[1:]
    tab = tab + forms
  self.tab = tab
  self.tabstr = ' '.join(tablines)
  self.key = self.root + ' ' + self.model

def init_conjtab(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f if not x.startswith(';')]
  nlines = len(lines)
  if not (nlines % 4) == 0:
   print('init_conjtab ERROR: wrong number of non-comment lines in',linein)
   exit(1)

  recs = []
  nrecs = int(nlines / 4)
  for irec in range(0,nrecs):
   reclines = lines[4*irec: 4*(irec+1)]
   recs.append(ConjTable(reclines))
 print('init_conjtab:',len(recs),"tables read from",filein)
 return recs

def recs_dict(recs):
 d = {}
 for rec in recs:
  root = rec.root
  if root in d:
   print('recs_dict duplicate root',rec.line)
  d[root] = rec
 return d

def match(hrecroots,recs):
 dr = recs_dict(recs)
 hrec_mwd = []
 no = 0
 prob = []
 for root in hrecroots:
  if root in dr:
   mwrec = dr[root]
   hrec_mwd.append(mwrec)
  else:
   print('root not found',root)
   #hrec_mwd[root] = None
   no = no + 1
 print(no,"roots not matched")
 print(len(hrecroots)-no,"roots DO match")
 return hrec_mwd

def groups(tabrecs):
 d = {}
 keys = []
 for tabrec in tabrecs:
  k = tabrec.root
  if k not in d:
   d[k] = []
   keys.append(k) 
  d[k].append(tabrec)
 print('groups:',len(keys),"distinct roots in tabrecs")
 return d,keys

def write(fileout,tabrec_mwd):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in tabrec_mwd:  # a Verbcp object
   outarr = []
   outarr.append(rec.line)
   for out in outarr:
    f.write(out + '\n')
 print("write %s records to %s"%(len(tabrec_mwd),fileout))

if __name__ == "__main__":
 filein = sys.argv[1]  # verb_cp.txt
 filein1 = sys.argv[2] # verb_cp_extra.txt
 filein2 = sys.argv[3] # conjugation tables file from ../manual
 fileout = sys.argv[4]
 
 recs = init_roots(filein) + init_roots(filein1)
 tabrecs = init_conjtab(filein2)
 tabrecsd,tabrecroots = groups(tabrecs)
 tabrec_mwd = match(tabrecroots,recs)
 write(fileout,tabrec_mwd)
