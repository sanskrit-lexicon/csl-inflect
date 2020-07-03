""" huet_table.py
    For future and similar tense
"""
import sys,re,codecs
def falt (m):
   x = m.group(0)
   #print('x=',x)
   x = x[1:-1]  # remove parens
   parts = x.split(' ')
   y = '/'.join(parts)
   return y

class Huettab(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  head,self.tabstr = line.split(':')
  self.head = head
  self.root,self.tp,self.parm = head.split(' ')
  # tabstr is a list in string form, separated by spaces [a b c]
  # There may also be alternatives in form (xxx yyy)
  #self.tab = self.tabstr[1:-1].split(' ')
  #print('dbg',self.tabstr)
  tab = self.tabstr[1:-1]
  tab1 = re.sub(r'\(.*?\)',falt,tab)
  if False and (tab1 != tab):
   print('Huettab check')
   print('tab = ',tab)
   print('tab1= ',tab1)
  self.tab = tab1.split(' ')
  # replace 'nil' with '?'
  for i,t in enumerate(self.tab):
   if t == 'nil':
    self.tab[i] = '?'

  if self.tp in ['cnd']:
   self.kind = None
   self.pada = self.parm
   self.theclass = '_'
  else:
   print('Huettab ERROR: cannot interpret parm:',self.parm)
   print(self.line)
   exit(1)
  self.key = (self.root,self.tp,self.pada)

 def visarga_adjust(self):
  for i,form in enumerate(self.tab):
   new = re.sub(r'r$','H',form)
   new = re.sub(r'r/','H/',new)
   new = re.sub(r's$','H',new)
   new = re.sub(r's/','H/',new)
   
   if new != form:
    #print('Visarga change (%s):  %s -> %s'%(self.head,form,new))
    self.tab[i] = new


def root_filter(root,option=None):
 if root not in excluded_roots:
  return True
 if excluded_roots[root] == 0:
  excluded_roots[root] = excluded_roots[root] + 1
  #print('root_filter: root excluded',root)
 return False

def agrees_with_option(rec,option):
 return True
 

def init_huettabs(filein,option = None):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  n = 0

  for line in f:
   if line.startswith(';'):
    continue
   try:
    rec = Huettab(line)
   except:
    print('init_huettabs parse error')
    print(line)
    exit(1)
   n = n + 1
   if not agrees_with_option(rec,option):
    continue
   if not root_filter(rec.root,option):
    continue
   # success
   rec.visarga_adjust()
   recs.append(rec)
 print("init_huettabs:",n,"tables read from",filein)
 print("init_huettabs:",len(recs),"tables kept")
 return recs

def write_cps(fileout,hrecs):
 rootd = {}
 roots = []
 for hrec in hrecs:
  tense = huet_tense_map[hrec.tp]
  pada = hrec.pada
  voice = pada2voice[pada]
  root = hrec.root
  theclass = hrec.theclass
  if root not in rootd:
   rootd[root] = []
   roots.append(root)
  cv = theclass + voice
  if cv not in rootd[root]:
   rootd[root].append(cv)
 with codecs.open(fileout,"w","utf-8") as f:
  for root in roots:
   cvs = rootd[root]
   cvstr = ','.join(cvs)
   out = '%s:%s'%(root,cvstr)
   f.write(out+'\n')
 print(len(roots),'roots written to',fileout)

def write1(fileout,hrecs):
 persons = ['3p','2p','1p']
 nskip = 0
 with codecs.open(fileout,"w","utf-8") as f:
  n = 0
  for hrec in hrecs:  # a Huettab object
   tense = huet_tense_map[hrec.tp]
   #assert hrec.tp == tense
   #kind,pada = list(hrec.parm)   # e.g. 5A, 1P, 4Q
   pada = hrec.pada
   #if pada not in option:  #['A','P']:
   # nskip = nskip + 1
   # continue
   # convert to middle voice or active voice
   voice = pada2voice[pada]
   root = hrec.root
   theclass = hrec.theclass
   outarr = []
   model = '%s,%s,%s' %(theclass,voice,tense)
   Lrefs = 'X'
   base = root
   head = '%s\t%s\t%s\t%s' %(model,root,Lrefs,base)
   tabc = ':'.join(hrec.tab)
   out = '%s\t%s' %(head,tabc)
   f.write(out+'\n')
   """
   outarr.append("Conjugation of %s,%s,%s %s" %(theclass,voice,tense,root))
   tab = hrec.tab
   for i in [0,1,2]:
    a = [persons[i]] + tab[3*i:3*i+3]
    outarr.append(' '.join(a))
   for out in outarr:
    f.write(out+'\n')
   """
   n = n + 1
 print(n,"tables written to",fileout)
 #print(nskip,"tables skipped since not ",option)

huet_tense_map = {
  'pr':'pre', # present tense
  'ip':'ipv', # imperative tense
  'im':'ipf', # imperfect tense
  'op':'opt', # optative tense
  'aor':'aor', # aorist
  'prf':'prf', # perfect tense
  'fut':'fut', # future tense
  'pef':'pft', # periphrastic future tense
  'ben':'ben', # benedictive
  'cnd':'con', # conditional
  #'inj':'inj', # injunctive (aorist without augment)
 }

pada2voice = {
  'P':'a',  # Parasmaipada == active voice
  '_P':'a', # For 'pef',  the Huet data looks this way for class-pada. Why?
  'A':'m',  # Atmanepada == middle voice
  'Q':'p'   # passive voice
 }

def write(fileout,hrecs):
 persons = ['3p','2p','1p']
 nskip = 0
 with codecs.open(fileout,"w","utf-8") as f:
  n = 0
  for hrec in hrecs:  # a Huettab object
   tense = huet_tense_map[hrec.tp]
   #assert hrec.tp == tense
   #kind,pada = list(hrec.parm)   # e.g. 5A, 1P, 4Q
   pada = hrec.pada
   #if pada not in option:  #['A','P']:
   # nskip = nskip + 1
   # continue
   # convert to middle voice or active voice
   voice = pada2voice[pada]
   root = hrec.root
   theclass = hrec.theclass
   outarr = []
   outarr.append("Conjugation of %s,%s,%s %s" %(theclass,voice,tense,root))
   tab = hrec.tab
   for i in [0,1,2]:
    a = [persons[i]] + tab[3*i:3*i+3]
    outarr.append(' '.join(a))
   for out in outarr:
    f.write(out+'\n')
   n = n + 1
 print(n,"tables written to",fileout)

def init_excluded(filein):
 with codecs.open(filein,"r","utf-8") as f:
  d = {}
  roots = []
  ndup = 0
  for x in f:
   x = x.rstrip('\r\n')
   if x not in d:
    #print(x)  # dbg
    d[x] = 0
    roots.append(x)
   else:
    # skip duplicate
    ndup = ndup + 1
 if ndup != 0:
  print(ndup,'duplicate roots found and skipped')
 return d
if __name__ == "__main__":
 # 0 = one-line conjugation
 # 1 = multi-line conjugation
 printopt = sys.argv[1]  
 assert printopt in ['0','1']
 file_exclude = sys.argv[2]
 filein = sys.argv[3]  # huet conjugation table
 fileout = sys.argv[4]
 
 excluded_roots = init_excluded(file_exclude)
 hrecs = init_huettabs(filein) #,option)
 if printopt == '0':
  write(fileout,hrecs)
 elif printopt == '1':
  write1(fileout,hrecs)
 else:
  print('Unknown print option',printopt)
 #write_cps(filecp,hrecs)
