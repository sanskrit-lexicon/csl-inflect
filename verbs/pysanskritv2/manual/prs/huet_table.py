""" huet_table.py
    For present tenses
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
  # relplace 'nil' with '?'
  for i,t in enumerate(self.tab):
   if t == 'nil':
    self.tab[i] = '?'
  if self.tp == 'aor':
   self.kind,self.pada = list(self.parm)
   self.theclass = '_'
  elif self.tp in ['prf']:
   self.kind = None
   self.pada = self.parm
   self.theclass = '_'
  elif self.tp in ['im','ip','op','pr']:
   #self.tense = huet_tense_map[self.tp]
   self.pada = self.parm[-1]  # P,A,Q  (Q = passive)
   self.theclass = self.parm[0:-1]
  else:
   print('Huettab ERROR: cannot interpret parm:',self.parm)
   print(self.line)
   exit(1)
  self.key = (self.root,self.tp,self.pada)

 def visarga_adjust(self):
  for i,form in enumerate(self.tab):
   new = re.sub(r'r$','H',form)
   new = re.sub(r'r/','H/',new)
   if new != form:
    #print('Visarga change (%s):  %s -> %s'%(self.head,form,new))
    self.tab[i] = new

excluded_roots = {
  'utkaRWa':0,
   'uruzya':0,
   'puzpya':0,
   'lelA':0,
   'hhuj':0}
def root_filter(root,option=None):
 if (option == 'Q') and root.endswith('a'): #denominative skip for now
  return False
 if (option == 'Q'): 
  if root in ['udaSru','tiras','mAlA','mudrA','meDA','rAjan','laG']:
   return False
 if root not in excluded_roots:
  return True
 if excluded_roots[root] == 0:
  excluded_roots[root] = excluded_roots[root] + 1
  print('root_filter: root excluded',root)
 return False

def agrees_with_option(rec,option):
 if rec.tp in ['aor','prf']:
  return rec.pada in option   # e.g., rec.pada == 'A', option == 'AP'
 if rec.tp in ['im','ip','op','pr']:
  if (option == 'AP') and (rec.theclass in ['1','2','3','4','5','6','7','8','9','10'])and (rec.pada in option):
   return True
  elif (option == 'AP11') and (rec.theclass == '11') and (rec.pada in option):
   return True
  elif (option == 'Q') and (rec.pada == 'Q'):
   return True
  else:
   return False
 return False

def init_huettabs(filein,option):
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
 }

pada2voice = {
  'P':'a',  # Parasmaipada == active voice
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
 #print(nskip,"tables skipped since not ",option)

def unused_merge_dups(hrecs):
 """
   r.key is same for all r in hrecs.
   construct tabstr, then new Huettab object
 """
 # copy of first table
 tab = []
 for t in hrecs[0].tab:
  tab.append(t)
 for r in hrecs[1:]:
  t = r.tab  
  for i,tabi in enumerate(tab):
   ti = t[i]
   # handle missing value in one of the two
   if tabi == '?':
    newt = ti
   elif ti == '?':
    newt = tabi
   else:
    # assume the two values are different. 
    # could make a check here, instead
    newt = '%s/%s' %(tabi,ti)
   # replace tab[i]
   tab[i] = newt
 # now, construct line needed by Huettab constructor
 tabspace = ' '.join(tab)
 tabstr = '[' + tabspace + ']'
 # Since we don't use 'rec.kind', for head just use head of first dup
 head = hrecs[0].head
 line = '%s:%s'%(head,tabstr)
 rec = Huettab(line)
 return rec

def unused_write_duplog(f,ndup,dups,rec):
 outarr = []
 outarr.append('; Case %03d, head=%s, number of dups = %s' %(
      ndup,rec.key,len(dups)))
 tablen = len(rec.tab)
 for i in range(tablen):
  a = 'indx %02d'%i
  barr = [d.tab[i] for d in dups]
  b = ' + '.join(barr)
  c = rec.tab[i]
  out = '%s: %s = %s'%(a,b,c)
  outarr.append(out)
 outarr.append('')
 for out in outarr:
  f.write(out+'\n')

def unused_merge(hrecs,filelog):
 """ combine into one table, multiple tables with same 'key'
 """
 keys = []
 d = {}
 f = codecs.open(filelog,"w","utf-8") 
 for hrec in hrecs:
  key = hrec.key
  if key not in d:
   d[key] = []
   keys.append(key)
  d[key].append(hrec)
 recs = []
 ndup = 0
 print(len(keys),'keys found')
 for key in keys:
  dups = d[key]
  if len(dups) == 1:
   rec = dups[0]
  else:
   rec = merge_dups(dups)
   ndup = ndup + 1
   if True:
    write_duplog(f,ndup,dups,rec)
  recs.append(rec)
 f.close()
 print(ndup,"cases written to",filelog)
 return recs
if __name__ == "__main__":
 # 0 = one-line conjugation
 # 1 = multi-line conjugation
 printopt = sys.argv[1]  
 assert printopt in ['0','1']
 option = sys.argv[2]
 # Q is for passive.  Not used for perfect
 known_options = ['AP','AP11','Q'] 
 if not option in known_options:
  print('option error: expect one of',known_options)
  exit(1)
 filein = sys.argv[3]  # huet conjugation table
 fileout = sys.argv[4]
 #filecp = sys.argv[5]  

 hrecs = init_huettabs(filein,option)
 #hrecs1 = merge(hrecs,filelog)
 
 #write(fileout,hrecs1)
 if printopt == '0':
  write(fileout,hrecs)
 elif printopt == '1':
  write1(fileout,hrecs)
 else:
  print('Unknown print option',printopt)
 #write_cps(filecp,hrecs)
