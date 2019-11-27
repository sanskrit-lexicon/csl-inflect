""" conjugate_file.py
"""
import sys,re,codecs
import conjugate_v2

class ConjRec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  parts = line.split()  # split on white space(tabs or space)
  if len(parts) == 3:
   (self.model,self.verb,self.refs) = parts
  elif len(parts) == 2:
   (self.model,self.verb) = parts
   self.refs = ''
  else:
   print('conjugate_file_v2: Error parsing line\n',line)
   exit(1)
  # parse verb into upasaragas and root
  parts = self.verb.split('-')
  self.root = parts[-1]  # string
  self.upasargas = parts[0:-1] # list, [] if no '-' in verb
  # parse model : class,voice,tense
  # class = 1-10, voice = a,m,p (active, middle, passive)
  # tense = pre, ipf, ipv, opt,  
  #         ppf, prf, fut, con, pft, ben
  #         aorist forms ?
  (self.theclass,self.voice,self.tense) = self.model.split(',')
  # values to be computed by inflect
  self.inflection = None
  self.sups = None
  # status of inflection computation, assumed successful
  self.status = True
  self.inflect()
 def inflect(self):
  conj = conjugate_v2.Conjugate(self.root,self.theclass,self.voice,self.tense,
                             dbg=False,upasargas=self.upasargas)
  if not conj.status:
   print('ConjRec error',self.model,self.verb)
   inflection = ['' for x in range(0,9)]
   inflections = [inflection]
  else:
   inflections = conj.tables
  #print('inflections=',inflections)
  tabs = map(lambda tab: self.list_to_string(tab),inflections)
  self.inflection = '&'.join(tabs)
  #print self.inflection
  #print(__file__)
 def list_to_string(self,a):
  b = []
  for x in a:
   if isinstance(x,list):
    y = '/'.join(x)
   else:
    y = x
   b.append(y)
  return ':'.join(b)

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
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


