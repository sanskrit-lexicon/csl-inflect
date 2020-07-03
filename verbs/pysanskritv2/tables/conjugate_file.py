""" conjugate_file.py
"""
import sys,re,codecs
import conjugate_one

class ModelVerb(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  parts = line.split()  # split on white space(tabs or space)
  self.model = parts[0]
  self.verb = parts[1]

def init_modelverbs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [ModelVerb(x) for x in f if not x.startswith(';')]
 return recs

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 modelverbs = init_modelverbs(filein)
 dtab = conjugate_one.init_conjtables('tempprev_calc_tables.txt')
 outall = []
 n = 0
 for modelverb  in modelverbs:
  model = modelverb.model
  verb = modelverb.verb
  if (model,verb) not in dtab:
   print('Conjugation not found: %s %s'%(model,verb))
   continue
  n = n + 1
  conjrecs = dtab[(model,verb)]
  if len(conjrecs) > 1:
   print(len(conjrecs),"conjugations for",model,verb)
  outarr = conjugate_one.stringify_tab(model,verb,conjrecs)
  outall = outall + outarr
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outall:
   f.write(out+'\n')
 print(n,"conjugations written to",fileout)
   
 exit(1)
 try:
  option = sys.argv[3]
  # when option is 1, also write the refs to output
 except:
  option = None
 with codecs.open(filein,"r","utf-8") as f:
  nrec = 0
  with codecs.open(fileout,"w","utf-8") as fout:
   for line in f:
    if line.startswith(';'):
     continue # skip comment
    rec = ConjRec(line)
    if option == '1':
     out = '%s\t%s\t%s\t%s' %(rec.model,rec.verb,rec.refs,rec.inflection)
    else:
     out = '%s\t%s\t%s' %(rec.model,rec.verb,rec.inflection)
    fout.write(out+'\n')
    nrec = nrec + 1
    if nrec == 1000000:
     print('debug quit after',nrec,'cases')
     break
 print(nrec,"records from",filein,"processed and written to",fileout)


