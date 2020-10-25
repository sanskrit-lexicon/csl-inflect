""" compare_cologne_huet_file.py
 Read a file with cologne-model and key,
 For each, compute declension table according to Cologne and Huet.
 Report results to output file
"""
import sys,re,codecs
import decline_one_huet as HUET
import decline_one as COLOGNE

class Stem(object):
 def __init__(self,key,gender):
  self.key = key
  self.gender = gender
  self.outarr = []   # result of comparing Cologne and Huet declensions
  if key[-1] in 'j':
   self.model = '%s_1_%s' %(self.gender,key[-1])  # m_1_j, for example
  else:
   print('STEM ERROR. Cannot get model for',key,gender)
   exit(1)

def init_stems(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for line in f:
   line = line.rstrip('\r\n')
   if line.startswith(';'):
    continue # skip comment
   m = re.search(r'^(.*?):(.*)$',line)
   if m == None:
    continue
   key = m.group(1)
   genders = m.group(2).split(',')
   for g in genders:
    if g in ['m','f','n']:
     recs.append(Stem(key,g))
 return recs

def ndiff_cologne_huet(clines,hlines):
 if len(clines)!=len(hlines):
  return -1,0
 ndiff = 0
 diffs = []
 # iline == 0 is 'Declension of model key
 # iline == 1 to 8 is case
 for iline,hline in enumerate(hlines):
  if iline == 0:
   continue
  cline = clines[iline]
  if cline != hline:
   diffs.append(iline)
 ndiff = len(diffs)
 return ndiff,diffs

def test_outarr(model,key):
 hlines = HUET.test_helper(model,key)
 clines = COLOGNE.test_helper(model,key)
 outarr = []
 ndiff,diffcases = ndiff_cologne_huet(clines,hlines)
 if ndiff == 0:
  outarr.append('SAME %s' %hlines[0])
  return outarr
 if hlines[0] != clines[0]:
  outarr.append('ERROR: different declensions')
  outarr.append('C=%s'%clines[0])
  outarr.append('H=%s'%hlines[0])
  return outarr
 # there is some difference in the conjugations

 for iline,hline in enumerate(hlines):
  if iline == 0:
   diffcases_as_str = ['%s' % c for c in diffcases]
   diffstr = ','.join(diffcases_as_str)
   outarr.append('%s cases Different %s' % (diffstr,clines[0]))
   continue
  cline = clines[iline]
  if hline == cline:
   status = 'SAME'
   outarr.append( '%s %s' %(status,cline))
  else:
   status = 'DIFF'
   outarr.append('C=%s'%cline)
   outarr.append('H=%s'%hline)
 return outarr

def testprint(model,key):
 outarr = test_outarr(model,key)
 for out in outarr:
  print(out)

def write(recs,fileout):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   for out in rec.outarr:
    f.write(out+'\n')

def test_fixed():
 testprint('m_a','rAma')
 testprint('f_1_j','sfj')
 testprint('m_1_j','rAj')

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 recs = init_stems(filein)
 print(len(recs))
 # compute outarr attribute for each rec
 for rec in recs:
  rec.outarr = test_outarr(rec.model,rec.key)
 write(recs,fileout)
