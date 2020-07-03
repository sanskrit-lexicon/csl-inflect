import sys,re,codecs
import conjugate_one_base

class Rec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  line = line.strip()
  self.line = line
  try:
   (self.cv,self.root,self.pre3s) = re.split(r' +',line)
  except:
   print('ERROR on input:',line)
   exit(1)
  self.c,self.v = self.cv.split(',')

def read(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Rec(line) for line in f if not line.startswith(';')]
 return recs

def write(fileout,recs):
 tenses = ['pre','ipf','ipv','opt']
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   if not rec.pre3s.endswith(('ati','ate')):
    print('error ',rec.line)
    exit(1)
   base = rec.pre3s[0:-3]  # remove ati/ate
   for tense in tenses:
    model = '%s,%s,%s' %(rec.c,rec.v,tense)
    outarr = conjugate_one_base.compute_outarr(model,rec.root,base)
    for out in outarr:
     f.write(out+'\n')
 print(len(recs),'present tenses written to',fileout)

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 recs = read(filein)
 write(fileout,recs)
