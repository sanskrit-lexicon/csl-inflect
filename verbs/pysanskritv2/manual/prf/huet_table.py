""" huet_table.py
    For perfect tense
"""
import sys,re,codecs

class Huettab(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  head,self.tabstr = line.split(':')
  self.head = head
  self.root,self.tp,self.parm = head.split(' ')
  # tabstr is a list in string form, separated by spaces
  #  [a b c]
  self.tab = self.tabstr[1:-1].split(' ')
  if self.tp == 'aor':
   self.kind,self.pada = list(self.parm)
  elif self.tp in ['prf']:
   self.kind = None
   self.pada = self.parm
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
   if rec.pada in option:
    rec.visarga_adjust()
    recs.append(rec)
 print("init_huettabs:",n,"tables read from",filein)
 print("init_huettabs:",len(recs),"tables kept")
 return recs

def write(fileout,hrecs):

 pada2voice = {
  'P':'a',  # Parasmaipada == active voice
  'A':'m',  # Atmanepada == middle voice
  'Q':'p'   # passive voice
 }
 persons = ['3p','2p','1p']
 nskip = 0
 with codecs.open(fileout,"w","utf-8") as f:
  n = 0
  for hrec in hrecs:  # a Huettab object
   tense = hrec.tp
   #assert hrec.tp == tense
   #kind,pada = list(hrec.parm)   # e.g. 5A, 1P, 4Q
   pada = hrec.pada
   #if pada not in option:  #['A','P']:
   # nskip = nskip + 1
   # continue
   # convert to middle voice or active voice
   voice = pada2voice[pada]
   root = hrec.root
   outarr = []
   outarr.append("Conjugation of _,%s,%s %s" %(voice,tense,root))
   tab = hrec.tab
   for i in [0,1,2]:
    a = [persons[i]] + tab[3*i:3*i+3]
    outarr.append(' '.join(a))
   for out in outarr:
    f.write(out+'\n')
   n = n + 1
 print(n,"tables written to",fileout)
 #print(nskip,"tables skipped since not ",option)

def merge_dups(hrecs):
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

def write_duplog(f,ndup,dups,rec):
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

def merge(hrecs,filelog):
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
 option = sys.argv[1]
 # Q is for passive.  Not used for perfect
 known_options = ['AP','Q'] 
 if not option in known_options:
  print('option error: expect one of',known_options)
  exit(1)
 filein = sys.argv[2]  # huet conjugation table
 fileout = sys.argv[3]
 filelog = sys.argv[4]

 hrecs = init_huettabs(filein,option)
 hrecs1 = merge(hrecs,filelog)
 
 write(fileout,hrecs1)
