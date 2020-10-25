""" decline_one_huet.py
    Program dones one declension, printing declension table.
    Declension is from huetdata/nominals/huet_noun_tables.txt
"""
#from decline_file import DeclRec
import sys,re,codecs

class DeclRec(object):
 def __init__(self,model,key):
  gender = model[0]
  dkey = '%s-%s'%(key,gender)
  if dkey not in HuetDecl.d:
   self.inflection  = None
  else:
   huetrec = HuetDecl.d[dkey]
   self.inflection = huetrec.tablestr

def test_helper(model,key2):
 key1 = key2.replace('-','')
 #line = '%s\t%s\t%s' %(model,key2,'')
 #decl = DeclRec(line)
 decl = DeclRec(model,key1)
 inflectionTable = decl.inflection  # string format
 outarr = []
 if inflectionTable == None:
  #print("Problem with declension of",model,key2)
  #exit(1)
  outarr.append("Problem with declension of %s %s" %(model,key2))
  return outarr
 table = inflectionTable.split(':')
 #print("Declension of %s %s " %(model,key2))
 outarr.append("Declension of %s %s " %(model,key2))
 for icell in range(0,24,3):
  a = []
  case = (icell // 3) + 1
  a.append('Case %d: ' % case)
  for i in range(0,3):
   x = table[icell+i]
   a.append(x)
  out = ' '.join(a)
  outarr.append(out)
 return outarr

def test(model,key2):
 outarr = test_helper(model,key2)
 for out in outarr:
  print(out)
 
def test_md(model,key2):
 # generate a markdown table
 key1 = key2.replace('-','')
 line = '%s\t%s\t%s' %(model,key2,'')
 decl = DeclRec(line)
 inflectionTable = decl.inflection  # string format
 #print inflectionTable
 if inflectionTable == None:
  print("Problem with declension of",model,key2)
  exit(1)
 table = inflectionTable.split(':')
 print("Declension of %s %s " %(model,key2))
 outarr = []
 outarr.append('')
 outarr.append('|Case|S|D|P|')
 outarr.append('|-|-|-|-|')
 casenames = ['Nominative','Accusative','Instrumental',
  'Dative','Ablative','Genitive','Locative','Vocative']
 for icell in range(0,24,3):
  a = []
  case = (icell // 3) + 1
  #a.append('Case %d: ' % case)
  a.append(casenames[case-1])
  for i in range(0,3):
   x = table[icell+i]
   #if isinstance(x,list):
   # y = '/'.join(x)
   #else:
   # y = x
   #a.append(y)
   a.append(x)
  out = '|'.join(a)
  out = '|' + out + '|'
  outarr.append(out)
 for out in outarr:
  print(out)

class HuetDecl(object):
 d = {}
 def __init__(self,line):
  line = line.rstrip('\r\n')
  m = re.search(r'^([^ ]+) (.):(.*)$',line)
  if m == None:
   print('decline_one_huet. HuetDecl problem with line\n',line)
   exit(1)
  self.key = m.group(1)
  self.gender = m.group(2)
  self.tablestr = m.group(3)
  self.table = self.tablestr.split(':')
  dkey = '%s-%s' %(self.key,self.gender)
  HuetDecl.d[dkey] = self

def init_huet_declension(filename):
 recs = []
 with codecs.open(filename,"r","utf-8") as f:
  for x in f:
   if not x.startswith(';'):
    rec = HuetDecl(x)
    recs.append(rec)
 return recs
huet_noun_filename = '../../../huetdata/nominals/huet_noun_tables.txt'
huetrecs = init_huet_declension(huet_noun_filename)

if __name__ == "__main__":
 #print(len(huetrecs))
 
 model = sys.argv[1]
 key2 = sys.argv[2]
 try:
  format = sys.argv[3]
 except:
  format = None
 if format == None:
  test(model,key2)
 elif format == 'md':
  test_md(model,key2)
 #elif format == 'md1':
 # test_md1(model,key2)
 else:
  print('Unknown format option',format)
  print('The format options are: md')


