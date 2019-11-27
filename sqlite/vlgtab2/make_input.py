# -*- coding: utf-8 -*-
"""make_input.py  for vlgtab2
"""
import sys,re,codecs
 
class Rec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
#  self.model,self.stem,self.refstr,self.infldata_str = line.split('\t')
  self.model1,self.root,self.refstr,self.base,self.infldata_str = line.split('\t')
  self.match = False
  self.equal1 = False
  self.Lnums = self.refstr.split(',')
  self.keys = [self.root for L in self.Lnums]
  self.Lnum0 = min([float(L) for L in self.Lnums])
  self.theclass,self.voice,self.tense = self.model1.split(',')
  if (self.theclass == '_') and (self.voice == 'p'):
   self.model = '%s-%s' % (self.tense,self.voice)
  else:
   self.model = '%s-%s%s' %(self.tense,self.theclass,self.voice)
  self.key =  self.model1 + '+' + self.base
  self.infltab = parse_infldata(self.infldata_str)
  if len(self.infltab) not in [9]:
   print('vlgtab1 make_input.py: Rec error: ',line)
   exit(1)

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
    out = "%s\t%s\t%s" %(inflitem,rec.model,rec.base)
    fout.write(out + '\n')
    nout = nout + 1
 fout.close()
 print(nout,"records written to",fileout)

