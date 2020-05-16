""" huet_mw_map.py
"""
import sys,re,codecs
from huet_mw_map_data import huet_mw_map

class Huettab(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  head,self.tabstr = line.split(':')
  self.root,self.tp,self.parm = head.split(' ')
  # tabstr is a list in string form, separated by spaces
  #  [a b c]
  self.tab = self.tabstr[1:-1].split(' ')
  if self.root in huet_mw_map:
   self.mw = huet_mw_map[self.root]
  else:
   self.mw = self.root
 def mwline(self):
  mwhead = ' '.join([self.mw,self.tp,self.parm])
  newline = ':'.join([mwhead,self.tabstr])
  return newline

def init_huettabs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for line in f:
   if line.startswith(';'):
    continue
   recs.append(Huettab(line))
   #try:
   # recs.append(Huettab(line))
   #except:
   # print('problem line:',line)
 return recs

def write(fileout,hrecs):
 changes = {}

 with codecs.open(fileout,"w","utf-8") as f:
  for hrec in hrecs:  # a Huettab object
   f.write(hrec.mwline() + '\n')
   if hrec.root != hrec.mw:
    change = (hrec.root,hrec.mw)
    if change not in changes:
     changes[change] = 0
    changes[change] = changes[change] + 1

 for c in changes:
  old,new = c
  print('%d Huet spelling %s -> MW spelling %s'%(changes[c],old,new))

if __name__ == "__main__":
 filein = sys.argv[1]  # huet conjugation table
 fileout = sys.argv[2]
 #filelog = sys.argv[3]
 hrecs = init_huettabs(filein)
 write(fileout,hrecs)
