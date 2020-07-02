# -*- coding: utf-8 -*-
""" make_compare_tabs.py
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

def get_cvs(cvstr):
 items = cvstr.split(',')
 cvs = []
 for item in items:
  v = item[-1]
  c = item[0:-1]
  cvs.append((c,v))
 return cvs

def write0(fileout,recs,c0,scriptoption):
 #allroots = sorted(roots.keys(),key = lambda x: x.translate(slp_from_to))
 #print(len(allroots),"merged roots")
 recs1 = []
 for rec in recs:
  #print(rec.root,rec.Hcvstr)
  if rec.Hcvstr == 'None':
   continue
  hcvs = get_cvs(rec.Hcvstr)
  if rec.Gcvstr != 'None':
   gcvs = get_cvs(rec.Gcvstr)
  elif rec.NGcvstr != 'None':
   gcvs = get_cvs(rec.NGcvstr)
  else:
   print('write0 Error 1',rec.line)
   exit(1)
  cvs = set(hcvs).intersection(set(gcvs))
  cvs = sorted(list(cvs))
  cvs0 = [cv for cv in cvs if cv[0] == c0]
  #print(rec.root,hcvs,gcvs,cvs)
  if len(cvs0) == 0:
   continue
  rec.commoncvs = cvs0
  recs1.append(rec)

 tenses = ['pre','ipf','ipv','opt']
 if scriptoption == '0':
  script = 'compare_one_tab.sh'
 elif scriptoption == '0a':
  script = 'compare_one_tab1a.sh'
 else:
  print('write0: wrong script option=',scriptoption)
 with codecs.open(fileout,"w","utf-8") as f:
  n = 0
  for rec in recs1:
   root = rec.root
   cvs = rec.commoncvs
   for cv in cvs:
    # cv = 1a, etc.
    #v = cv[-1] # voice
    #c = cv[0:-1] # class
    (c,v) = cv
    for t in tenses:
     model = '%s,%s,%s' %(c,v,t)
     out = 'sh %s %s %s' %(script,model,root)
     f.write(out+'\n')
     n = n + 1
 print(n,"records written to",fileout)

def write1(fileout,recs,c0,scriptoption):
 # verbs with Huet conjugations AND
 #  cv unique to Huet
 #allroots = sorted(roots.keys(),key = lambda x: x.translate(slp_from_to))
 #print(len(allroots),"merged roots")
 recs1 = []
 for rec in recs:
  #print(rec.root,rec.Hcvstr)
  if rec.Hcvstr == 'None':
   continue
  hcvs = get_cvs(rec.Hcvstr)
  if rec.Gcvstr != 'None':
   gcvs = get_cvs(rec.Gcvstr)
  elif rec.NGcvstr != 'None':
   gcvs = get_cvs(rec.NGcvstr)
  else:
   print('write0 Error 1',rec.line)
   exit(1)
  #cvs = set(hcvs).intersection(set(gcvs))
  cvs = set(hcvs).difference(set(gcvs))
  cvs = sorted(list(cvs))
  cvs0 = cvs
  #cvs0 = [cv for cv in cvs if cv[0] == c0]
  #print(rec.root,hcvs,gcvs,cvs)
  if len(cvs0) == 0:
   continue
  rec.commoncvs = cvs0
  recs1.append(rec)

 tenses = ['pre','ipf','ipv','opt']
 """
 if scriptoption == '':
  script = 'compare_one_tab.sh'
 elif scriptoption == '0a':
  script = 'compare_one_tab1a.sh'
 else:
  print('write0: wrong script option=',scriptoption)
 """
 script = 'python conjugate_one.py'
 with codecs.open(fileout,"w","utf-8") as f:
  n = 0
  for rec in recs1:
   root = rec.root
   cvs = rec.commoncvs
   for cv in cvs:
    # cv = 1a, etc.
    #v = cv[-1] # voice
    #c = cv[0:-1] # class
    (c,v) = cv
    for t in tenses:
     model = '%s,%s,%s' %(c,v,t)
     out = '%s %s %s' %(script,model,root)
     f.write(out+'\n')
     n = n + 1
 print(n,"records written to",fileout)

def write2(fileout,recs,c0,scriptoption):
 # verbs which are MW genuine
 #  cv unique to MW
 
 recs1 = []
 for rec in recs:
  #print(rec.root,rec.Hcvstr)
  if rec.Hcvstr == 'None':
   continue
  hcvs = get_cvs(rec.Hcvstr)
  if rec.Gcvstr == 'None':
   continue # require an MW genuine root
  if rec.Gcvstr != 'None':
   gcvs = get_cvs(rec.Gcvstr)
  elif rec.NGcvstr != 'None':
   gcvs = get_cvs(rec.NGcvstr)
  else:
   print('write0 Error 1',rec.line)
   exit(1)
  #cvs = set(hcvs).intersection(set(gcvs))
  cvs = set(gcvs).difference(set(hcvs))
  cvs = sorted(list(cvs))
  cvs0 = [(c,v) for (c,v) in cvs if c in ['1','4','6','10']]
  if len(cvs0) == 0:
   continue
  rec.commoncvs = cvs0
  recs1.append(rec)

 tenses = ['pre','ipf','ipv','opt']

 script = 'python conjugate_one.py'
 with codecs.open(fileout,"w","utf-8") as f:
  #f.write('cd ../../tables/' + '\n')
  n = 0
  for rec in recs1:
   root = rec.root
   cvs = rec.commoncvs
   for cv in cvs:
    (c,v) = cv
    for t in tenses:
     model = '%s,%s,%s' %(c,v,t)
     #out = '%s %s %s' %(script,model,root)
     out = '%s %s' %(model,root)
     f.write(out+'\n')
     n = n + 1
 print(n,"records written to",fileout)

class Merge(object):
 def __init__(self,line):
  self.line = line
  self.root,hdata,gdata,ngdata = line.split(' ')
  sym,self.Hcvstr = hdata.split('=')
  sym,self.Gcvstr = gdata.split('=')
  sym,self.NGcvstr = ngdata.split('=')

def init_mergerecs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f if not x.startswith(';')]
 recs = []
 for line in lines:
  recs.append(Merge(line))
 print(len(recs),'records read from',filein)
 #recs.sort(key = lambda x: x.root.translate(slp_from_to))
 return recs

if __name__ == "__main__":
 option,c0 = sys.argv[1].split(',')
 filein = sys.argv[2]
 fileout = sys.argv[3]
 recs = init_mergerecs(filein)
 if option in ['0','0a']:
  write0(fileout,recs,c0,option)
 elif option in ['1']:
  write1(fileout,recs,c0,option)
 elif option in ['2']:
  write2(fileout,recs,c0,option)
 else:
  print('invalid option',option)
 exit(1)
