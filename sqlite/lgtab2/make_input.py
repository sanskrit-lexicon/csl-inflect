# -*- coding: utf-8 -*-
"""make_input.py  for lgtab2
"""
import sys,re,codecs
 
class Rec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  self.model,self.stem,self.refstr,self.infldata_str = line.split('\t')
  refs = self.refstr.split(':')
  self.match = False
  self.equal1 = False
  self.Lnums = []
  self.keys = []
  for refstr in refs:
   L,key1 = refstr.split(',')
   self.Lnums.append(L)
   self.keys.append(key1)
  self.Lnum0 = min([float(L) for L in self.Lnums])
  stem1 = self.stem.replace('-','')
  model = self.model
  self.key =  model + '+' + stem1
  if model == 'ind':
   gender = 'ind'
  elif model.startswith(('m_','f_','n_')):
   gender = model[0]
  else:  # never happens
   gender = None
   print('unexpected model:',model)
  self.gender = gender
  self.keyg = gender + '+' + stem1
  self.infltab = parse_infldata(self.infldata_str)
  if len(self.infltab) not in [1, 24]:
   print('Rec error: ',line)

def parse_infldata(s):
 parts = s.split(':')
 ans = []
 for part in parts:
  ans1 = sorted(part.split('/'))
  ans.append(ans1)
 return ans

if __name__ == "__main__":
 filein = sys.argv[1] 
 fileout = sys.argv[2]
 fout = codecs.open(fileout,"w","utf-8") 
 nout = 0
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   rec = Rec(line)
   # get distinct inflection table entries, excluding empty strings
   d = {}
   for infltabitems in rec.infltab:
    # infltabitems is a list!
    for infl in infltabitems:
     if infl != '':
      d[infl]=True
   inflitems = d.keys()
   for inflitem in inflitems:
    out = "%s\t%s\t%s" %(inflitem,rec.model,rec.stem)
    fout.write(out + '\n')
    nout = nout + 1
 fout.close()
 print(nout,"records written to",fileout)

