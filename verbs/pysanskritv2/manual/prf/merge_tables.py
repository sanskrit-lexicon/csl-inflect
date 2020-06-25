""" merge_tables.py
"""
import sys,re,codecs

persons = ['3p','2p','1p']

class Tab(object):
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

def init_tab(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f if not x.startswith(';')]
  nlines = len(lines)
  if not (nlines % 4) == 0:
   print('init_tab ERROR: wrong number of non-comment lines in',linein)
   exit(1)

  recs = []
  nrecs = int(nlines / 4)
  for irec in range(0,nrecs):
   reclines = lines[4*irec: 4*(irec+1)]
   recs.append(Tab(reclines))
 print(len(recs),"tables read from",filein)
 return filein,recs

def write(fileout,mergerecs):

 with codecs.open(fileout,"w","utf-8") as f:
  n = 0
  for mergerec in mergerecs:  # a Huettab object
   
   root = mergerec.root
   model = mergerec.model
   outarr = []
   #outarr.append("Conjugation of _,%s,%s %s" %(voice,tense,root))
   outarr.append("Conjugation of %s %s" %(model,root))
   #tab = hrec.tab
   tab = mergerec.mergetab
   for i in [0,1,2]:
    a = [persons[i]] + tab[3*i:3*i+3]
    outarr.append(' '.join(a))
   for out in outarr:
    f.write(out+'\n')
   n = n + 1
 print(n,"tables written to",fileout)

def jointabval(old,next):
 oldparts = old.split('/')
 nextparts = next.split('/')
 for nextpart in nextparts:
  if nextpart in oldparts:
   pass
  elif nextpart == '?':
   pass  # missing value
  else:
   oldparts.append(nextpart)
 newparts = [x for x in oldparts if x != '?']
 if newparts == []:
  new = '?'
 else:
  new = '/'.join(newparts)
 return new
  
def jointabs(tabs):
 # start with a copy of the first table
 newtab = []
 for form in tabs[0].tab:
  newtab.append(form)
 # merge or extend newtab based on the additional tabs
 changeflag = False
 for nexttabobj in tabs[1:]:
  nexttab = nexttabobj.tab
  for i,oldtabval in enumerate(newtab):
   nexttabval = nexttab[i]
   oldtabval = newtab[i]
   newtabval = jointabval(oldtabval,nexttabval)
   if newtab[i] != newtabval:
    newtab[i] = newtabval
    changeflag = True
 # 
 sigdiff = []
 for i,newform in enumerate(newtab):
  oldforms = [t.tab[i] for t in tabs]
  sigdiff.append(significant_difference(newform,oldforms))
 return newtab,changeflag,sigdiff

def significant_difference(newform,oldforms):
 def formset(form):
  return set([x for x in form.split('/') if x != '?'])
 newset = formset(newform)
 oldsets = [formset(oldform) for oldform in oldforms]
 n = len(oldsets)
 for i1 in range(0,n):
  oldset1 = oldsets[i1]
  for i2 in range(i1+1,n):
   oldset2 = oldsets[i2]
   if oldset1.issubset(oldset2) or oldset2.issubset(oldset1):
    pass
   else:
    # significant difference found
    return True
 # no significant differences found
 return False

def significant_difference_v1(newform,oldforms):
 # unused
 def formset(form):
  return set([x for x in form.split('/') if x != '?'])
 newset = formset(newform)
 
 for oldform in oldforms:
  oldset = formset(oldform)
  if len(oldset) == 0:
   # don't worry about missing values
   continue
  if not newset.issubset(oldset):
   # some value of new forms is not in this particular oldform.
   # count this situation as a significant difference
   return True
 # no significant differences found
 return False
 
class Mergerec(object):
 def __init__(self,key,filetabarr):
  self.key = key
  #   self.key = self.root + ' ' + self.model
  self.root,self.model = key.split(' ')
  #self.filetabarr = filetabarr
  self.fileins = [x[0] for x in filetabarr]
  self.tabs = [x[1] for x in filetabarr]
  self.ntabs = len(filetabarr)
  self.mergetab = None
  self.sigdiff = None
  self.status = None
  self.sameflag = False

 def jointab(self):
  newtab,changeflag,sigdiff = jointabs(self.tabs)
  self.mergetab = newtab
  self.sigdiff = sigdiff
  #tables = [t.tab for t in self.tabs]
  #self.sameflag = newtab in tables
  self.sameflag = True not in sigdiff
  #if self.key in ['kfz _,a,aor']: print('jointab chk:',self.key,self.sigdiff,'sameflag=',self.sameflag)
  self.status = changeflag

def merge(tabarrays):
 d = {}
 keys = []
 for itabarray,tabarray in enumerate(tabarrays):
  filein,tabrecs = tabarray
  for tab in tabrecs:
   key = tab.key
   if key not in d:
    d[key] = []
    keys.append(key)
   d[key].append((filein,tab))
 mergerecs = [Mergerec(key,d[key]) for key in keys]
 for mergerec in mergerecs:
  mergerec.jointab()
 return mergerecs

def get_short_filenames(names):
 a = []
 for name in names:
  m = re.search(r'_([^_]*?)[.]txt$',name)
  if m:
   a.append(m.group(1))
  else:
   a.append(name)
 return a

person_codes = ['3s','3d','3p','2s','2d','2p','1s','1d','1p']

def dup_output(case,mergerec):
 outarr = []
 key = mergerec.key
 ndiff = 0
 duplist = mergerec.tabs
 if mergerec.sameflag:
  diff = ''
  ndiff = 0
 else:
  diff = ' (Difference)'
  ndiff = 1
 #outarr.append('; Dup case: %03d for key=%s, #dups=%s%s'%(
 #    case,key,len(duplist),diff))
 outarr.append('; Double case: %03d for key=%s'%(
     case,key))
 #a = mergerec.fileins + ['MERGED']
 shortnames = get_short_filenames(mergerec.fileins)
 #a = ' + '.join(mergerec.fileins)
 a = ' + '.join(shortnames)
 a = '%s -> %s' %(a,'MERGED')
 outarr.append(a)
 tablen = len(mergerec.mergetab)
 realdiff = False
 for i in range(tablen):
  #a = [t.tab[i] for t in mergerec.tabs] + [mergerec.mergetab[i]]
  a = [t.tab[i] for t in mergerec.tabs]
  b = ' + '.join(a)
  if mergerec.sigdiff[i]:
   d = " **realdiff"
   realdiff = True
  else:
   d = ""
  c = '%s %s -> %s%s' %(person_codes[i],b,mergerec.mergetab[i],d)
  outarr.append(c)
 outarr.append(';------------------------------------------------------')
 if realdiff and (ndiff == 1):
  outarr[0] = outarr[0] + ' (non-trivial difference)'
 elif realdiff and (ndiff == 0):
  outarr[0] = outarr[0] + ' (unexpected realdiff)'
 elif (not realdiff) and (ndiff == 0):
  outarr[0] = outarr[0] + ' (trivial difference)'
 else:
  outarr[0] = outarr[0] + ' (unexpected difference)'
 return outarr,ndiff

def single_output(case,mergerec):
 outarr = []
 key = mergerec.key
 shortnames = get_short_filenames(mergerec.fileins)
 name = ' + '.join(shortnames)
 outarr.append('; %s Single case : %03d for key=%s'%(
     name,case,key))
 a = '%s only'%name
 outarr.append(a)
 tablen = len(mergerec.mergetab)
 for i in range(tablen):
  #a = [t.tab[i] for t in mergerec.tabs] + [mergerec.mergetab[i]]
  a = [t.tab[i] for t in mergerec.tabs]
  b = ' + '.join(a)
  c = '%s %s ' %(person_codes[i],b)
  #c = '%s %s -> %s%s' %(person_codes[i],b,mergerec.mergetab[i],d)
  outarr.append(c)
 outarr.append(';------------------------------------------------------')
 return outarr

slp_from = "aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh"
slp_to =   "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw"
slp_from_to = str.maketrans(slp_from,slp_to)

def write_log(fileout,mergerecs):
 dups = [r for r in mergerecs if r.ntabs > 1]
 print('merge:',len(dups),'duplicate keys found')
 outarr = []
 nrealdiff = 0
 keys = [mergerec.key for mergerec in mergerecs]
 keys = sorted(keys,key = lambda x: x.translate(slp_from_to))
 idup = 0
 #for ikey,mergerec in enumerate(mergerecs):
 for ikey,key in enumerate(keys):
  mergerec = mergerecs[ikey]
  case = ikey+1
  if mergerec.ntabs == 1:
   outa = single_output(case,mergerec)
  else:
   idup = idup + 1
   outa,nrdiff = dup_output(case,mergerec)
   nrealdiff = nrealdiff + nrdiff
  outarr = outarr + outa
 print(nrealdiff,"Real differences in tables")
 with codecs.open(filelog,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print('adjustments written to',filelog)

if __name__ == "__main__":
 fileout = sys.argv[1]
 filelog = sys.argv[2]
 filesin = sys.argv[3:]  # one or more input files

 tabarrays = [init_tab(filein) for filein in filesin]
 mergerecs = merge(tabarrays)
 write_log(filelog,mergerecs)

 #exit(1)
 write(fileout,mergerecs)
