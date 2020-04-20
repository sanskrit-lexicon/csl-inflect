""" verb_cp_huet_aor.py
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
  for line in f:
   if line.startswith(';'):
    continue
   try:
    recs.append(Verbcp(line))
   except:
    print('problem line:',line)
 # some extra roots of MW, that are not in verb_cp
 added_verb_cp = """
am:13748:
KyA:62110:2a,2m
gup:65898,65890,65959:4a,4m,6a,6m
cur:74646:10a,10m,1a,1m
cezw:74971:1a,1m
jalp:78292:1m
tvar:89087:1a,1m
tviz:89141:1a,1m
das:91129:1a,1m,4m
dfS:95263:
vaD:185579:
spaS:256550:
""".splitlines()
 for line in added_verb_cp:
  if line != '':
   recs.append(Verbcp(line))
 return recs

huet_mw_map = {
 'DyA':'DyE', 
 'praS':'praC', 
 'mUrC':'murC', 
 'mlecC':'mleC', 
 'vyA':'vye', 
 'SA':'Si', 
 'SU':'Svi', 
 'sA':'so', 
 'hU':'hve'
}
class Huettab(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  head,tabstr = line.split(':')
  self.root,self.tp,self.parm = head.split(' ')
  # tabstr is a list in string form, separated by spaces
  #  [a b c]
  tab = tabstr[1:-1].split(' ')
  # missing values are 'nil', replace with '?'
  self.tab = []
  for t in tab:
   if t == 'nil':
    self.tab.append('?')
   else:
    self.tab.append('t')
  if self.root in huet_mw_map:
   self.mw = huet_mw_map[self.root]
  else:
   self.mw = self.root

def init_huettabs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for line in f:
   if line.startswith(';'):
    continue
   try:
    recs.append(Huettab(line))
   except:
    print('problem line:',line)
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
 for mwroot,huetroot in hrecroots:
  if mwroot in dr:
   mwrec = dr[mwroot]
   mwrec.huet = huetroot
   hrec_mwd.append(mwrec)
  else:
   print('root not found',root)
   #hrec_mwd[root] = None
   no = no + 1
 print(no,"roots from Huet not matched")
 print(len(hrecroots)-no,"roots from Huet DO match")
 return hrec_mwd

def groups(hrecs):
 d = {}
 keys = []
 for hrec in hrecs:
  k = hrec.mw
  if k not in d:
   d[k] = []
   keys.append([k,hrec.root]) 
  d[k].append(hrec)
 print(len(keys),"distinct roots in hrecs")
 return d,keys

def write(fileout,hrec_mwd):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in hrec_mwd:  # a Verbcp object
   outarr = []
   if rec.huet != rec.root:
    out = '; Huet spelling %s -> MW spelling %s'%(rec.huet,rec.root)
    print(out)
    outarr.append(out)
   outarr.append(rec.line)
   for out in outarr:
    f.write(out + '\n')

if __name__ == "__main__":
 filein = sys.argv[1]  # verb_cp.txt
 filein1 = sys.argv[2] # huet_conj_tables_aor.txt
 fileout = sys.argv[3]
 #filelog = sys.argv[3]
 recs = init_roots(filein)
 hrecs = init_huettabs(filein1)
 hrecsd,hrecroots = groups(hrecs)
 print(len(hrecroots),"distinct huet roots")
 hrec_mwd = match(hrecroots,recs)
 write(fileout,hrec_mwd)
