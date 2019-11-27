# -*- coding: utf-8 -*-
""" analyze_f.py
   Write analysis of lexnorm-all2 records that end with 'f' (vocalic 'r'
   python analyze_f.py <regex> <filein> <fileout> <tranout>
"""
import sys,re,codecs
from slp_cmp import slp_cmp
sys.path.append('../../transcode')   # MWinflect
import transcoder
transcoder.transcoder_set_dir('../../transcode/transcode');

class Lexnorm(object):
 """
  The format of a line of lexnorm.txt is now 4 tab-delimited fields:
  lnum, key1, key2, lexinfo
  And, the lexinfo field has form of 1 or more colon-delimited fields, each
  of which has one of two forms:
  gender OR  gender#ending
 """
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.L,self.key1,self.key2,self.lexnorm) = line.split('\t')
  self.keep = False
  
 def toString(self):
  s = '\t'.join([self.L,self.key1,self.key2,self.lexnorm])
  return s

def init_lexnorm(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Lexnorm(x) for x in f]
 print(len(recs),"read from",filein)
 return recs

def pada_parts(rec):
 key = rec.key2
 parts = key.split('-')
 if len(parts) == 1:
  a = ''
  b = parts[0]
 else:
  b = parts[-1]
  a = ''.join(parts[0:-1])
 return (a,b)
def pada_cmp(rec1,rec2):
 """ rec is a Lexnorm object
  
 """
 (a1,b1) = pada_parts(rec1)
 (a2,b2) = pada_parts(rec2)
 if b1 == b2:
  return slp_cmp(a1,a2)
 else:
  return slp_cmp(b1,b2)

def setpadas(recs):
 """ add pada1 and pada2 attributes """
 for rec in recs:
  rec.pada1,rec.pada2 = pada_parts(rec)

def pada2_dict(recs):
 d = {}
 for rec in recs1:
  pada2 = rec.pada2
  if pada2 not in d:
   d[pada2]=[]
  d[pada2].append(rec)
 return d

def agent_relation(pada2):
 relations = [
  ##  masculine
  # Deshpande
  'pitf','BrAtf','jAmAtf',
  'nf', # 6p: nfRAm/nFRAm
  # Kale additionally
  'devf', # husband's brother
  'SaMstf', # one who praises
  'savyezWf', # a charioteer   Kale spells as ..wf; 
             # AP has both, and also savyezWAtf, savyezWa
  ## feminine
  # Deshpande
  'mAtf','duhitf','nanAndf',
  # Kale
  'nanandf',
  'yAtf',  # a husband's brother's wife
  ]
 agent_relations = [
  ### relation nouns that are declined like agent nouns
  ## masculine
  'naptf','Bartf',
  ## feminine
  'svasf', # 2p = svasFH
 ]

 if pada2 in relations:
  return 'R'
 elif pada2 in agent_relations:
  return 'RA'
 else:
  return 'A'

def set_rel_agent(recs):
 for rec in recs:
  rec.type = agent_relation(rec.pada2)

def remove_duplicate_pada1(recs):
 ans = []
 prev = None
 for rec in recs:
  if rec.pada1 != prev:
   ans.append(rec)
  prev = rec.pada1
 return ans

def write_d(d,f,rel_agent_type,tranout='slp1'):
 outarr = []
 outarr.append('; ----------------------------------')
 if rel_agent_type == 'R':
  outarr.append('; Decline as relation')
 elif rel_agent_type == 'RA':
  outarr.append('; Relation nouns declined as agent')
 else:
  outarr.append('; Decline as agent')
 outarr.append('; ----------------------------------')
 allkeys = d.keys()
 keys = [pada2 for pada2 in allkeys if agent_relation(pada2) == rel_agent_type]
 keys = sorted(keys,cmp=slp_cmp)

 def dcmp(rec1,rec2):
  return slp_cmp(rec1.pada1,rec2.pada1)

 for ikey,key in enumerate(keys):
  drecs = d[key]
  drecs1 = sorted(drecs,cmp=dcmp)
  drecs1 = remove_duplicate_pada1(drecs1)
  outarr1 = [x.pada1+'-' for x in drecs1[1:]]
  out1 = ' '.join(outarr1)
  out = '%03d\t%s\t%02d\t%s' %(ikey+1,key,len(drecs1),out1)
  outarr.append(out)
 print(len(keys),"of type",rel_agent_type)
 
 for out in outarr:
  out1 = transcode(out,tranout=tranout)
  f.write(out1+'\n')
  
def transcode(x,tranout='slp1'):
 """ transcode from slp1 to tranout, unless line starts with ';'
 """
 if x.startswith(';'):
  return x
 else:
  return transcoder.transcoder_processString(x,'slp1',tranout)

if __name__ == "__main__":
 tranout = sys.argv[1]
 filein = sys.argv[2] # lexnorm-all2
 fileout = sys.argv[3]

 regex = 'f$'
 recs = init_lexnorm(filein)
 recs1 = [r for r in recs if re.search(regex,r.key2)]
 setpadas(recs1) # add pada1,pada2 attributes
 set_rel_agent(recs1)
 # construct dictionary from recs1 with pada2 as key
 d = pada2_dict(recs1)
 print len(d.keys())
 with codecs.open(fileout,"w","utf-8") as f:
  write_d(d,f,'R',tranout)  # declined as relation
  write_d(d,f,'RA',tranout)  # relation nouns declined as agent
  write_d(d,f,'A',tranout)  # declined as agent
