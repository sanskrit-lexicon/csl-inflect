""" decline_file.py
"""
import sys,re,codecs

class Rec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  try:
   (self.model,self.key2,self.refs) = line.split('\t')
  except:
   print('Rec. Error parsing line\n',line)
   exit(1)

if __name__ == "__main__":
 filein1 = sys.argv[1]
 filein2 = sys.argv[2]
 fileout = sys.argv[3]
 with codecs.open(filein2,"r","utf-8") as f:
  nrec2 = 0
  d = {}
  for line in f:
   if line.startswith(';'):
    continue # skip comment
   rec = Rec(line)
   d[rec.line]=False
   nrec2 = nrec2 + 1
 with codecs.open(filein1,"r","utf-8") as f:
  recouts = []
  nrec1 = 0
  for line in f:
   if line.startswith(';'):
    continue # skip comment
   rec = Rec(line)
   nrec1 = nrec1 + 1
   if (rec.line not in d):
    recouts.append(rec.line)
   else:
    d[rec.line] = True
 with codecs.open(fileout,"w","utf-8") as f:
  for line in recouts:
   f.write(line + '\n')
 #
 print(nrec1,"lines from",filein1)
 print(nrec2,"lines from",filein2)
 print(len(recouts),"lines written",fileout)
 lines2a = [line for line in d.keys() if d[line]==False]
 print(len(lines2a),"records not accounted for from",filein2)

 
    
