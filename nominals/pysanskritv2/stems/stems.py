# -*- coding: utf-8 -*-
""" stem_model.py 
    extract various inflection model information for substantives
    from lexnorm-all2.txt.
    python3
"""
import sys,re,codecs
from slp_cmp import slp_cmp_key
sys.path.append('../../pydecl')
from sandhi_nR import sandhi_nR
import decline # for f_an_I. See model_an

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
  self.parsed = False
  self.models = []

 def toString(self):
  s = '\t'.join([self.L,self.key1,self.key2,self.lexnorm])
  return s

class Model(object):
 d = {}
 def __init__(self,lexrec,modelname,stem,extra=None):
  self.lexrec = lexrec
  self.name = modelname
  self.stem = stem
  self.extra = extra
  key = self.name
  if key not in Model.d:
   Model.d[key] = []
  Model.d[key].append(self)

 def toString(self):
  if self.extra != None:
   s = '\t'.join([self.L,self.model,self.stem,self.extra])
  else:
   s = '\t'.join([self.L,self.model,self.stem])
  return s

def init_lexnorm(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Lexnorm(x) for x in f if not x.startswith(';')]
 print(len(recs),"read from",filein)
 return recs

def log_models(modelname,lexnormd,f):
 keys = sorted(lexnormd.keys())
 for key in keys:
  out = '%05d %s %s' %(lexnormd[key],key,modelname)
  f.write(out +'\n')

def model_ind(recs,fmodels):
 d = {}
 for rec in recs:
  if rec.lexnorm != 'ind':
   continue
  rec.parsed = True
  model = 'ind'
  stem = rec.key2
  rec.models.append(Model(rec,model,stem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_ind',d,fmodels)

def model_m_a(recs,fmodels):
 endchar = 'a'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m']
  lexparts = rec.lexnorm.split(':')
  if not lexparts == knownparts:
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'm_a'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_m_a',d,fmodels)

def model_n_a(recs,fmodels):
 endchar = 'a'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['n']
  lexparts = rec.lexnorm.split(':')
  if not lexparts == knownparts:
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'n_a'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_n_a',d,fmodels)

def model_f_A(recs,fmodels):
 endchar = 'A'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f','f#A']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_A'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_A',d,fmodels)

def model_f_I(recs,fmodels):
 endchar = 'I'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f','f#I']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_I'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_I',d,fmodels)

def model_f_U(recs,fmodels):
 endchar = 'U'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f','f#U']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_U'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_U',d,fmodels)

def model_m_i(recs,fmodels):
 endchar = 'i'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'm_i'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_m_i',d,fmodels)

def model_f_i(recs,fmodels):
 endchar = 'i'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_i'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_i',d,fmodels)

def model_n_i(recs,fmodels):
 endchar = 'i'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['n']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'n_i'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_n_i',d,fmodels)

def model_m_u(recs,fmodels):
 endchar = 'u'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'm_u'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_m_u',d,fmodels)

def model_f_u(recs,fmodels):
 endchar = 'u'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_u'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_u',d,fmodels)

def model_n_u(recs,fmodels):
 endchar = 'u'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['n']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'n_u'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_n_u',d,fmodels)

def model_m_f(recs,fmodels):
 endchar = 'f'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'm_f'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_m_f',d,fmodels)

def model_f_f(recs,fmodels):
 endchar = 'f'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_f'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_f',d,fmodels)

def model_n_f(recs,fmodels):
 endchar = 'f'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['n']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'n_f'
   rec.models.append(Model(rec,model,mstem))
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_n_f',d,fmodels)

def model_mfn_a(recs,fmodels):
 endchar = 'a'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_a, n_a
   elif part in ['f']:
    mstem = stem[0:-1] + 'A'  # deva -> devA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   else:
    print('mfn_a Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_a',d,fmodels)

def model_mfn_i(recs,fmodels):
 endchar = 'i'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_i, n_i, f_i
   else:
    print('mfn_i Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_i',d,fmodels)

def model_mfn_u(recs,fmodels):
 endchar = 'u'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_u, n_u, f_u
   else:
    print('mfn_u Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_u',d,fmodels)

def model_mfn_f(recs,fmodels):
 endchar = 'f'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_f, n_f, f_f
   else:
    print('mfn_u Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_f',d,fmodels)

def model_mfn_a1(recs,fmodels):
 endchar = 'a'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
 
  knownlexnorms = [ 'f#A', 'm:f#I', 'm:f#A:f#I:n', 'f#A:n', 'm:f#ikA:n', 
                'm:f#A', 'm:f#I:n', 'm:f#A:n']
  if not rec.lexnorm in knownlexnorms:
   continue
  """
  knownparts = []
  for lexnorm in knownlexnorms:
   lexparts = rec.lexnorm.split(':')
   for lexpart in lexparts:
    if lexpart not in knownparts:
     knownparts.append(lexpart)
  """
  lexparts = rec.lexnorm.split(':')
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_a, n_a
   elif part == 'f#A':
    mstem = stem[0:-1] + 'A'  # deva -> devA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   elif part == 'f#I':
    mstem = stem[0:-1] + 'I'  # deva -> devI
    mpart = 'f'
    model = '%s_%s' %(mpart,'I')
   elif part == 'f#ikA':
    newend = part[2:] # 'ikA'
    if not stem.endswith(('aka','ika')):
     mstem = stem[0:-1] + newend  #  replace final a with ikA
     print("model mfn_a1: unusual stem:",stem,part,mstem)
    else:
     mstem = stem[0:-3] + newend  #  replace final aka/ika with akA or ikA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   else:
    print('mfn_a1 Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_a1',d,fmodels)

def model_mfn_a2(recs,fmodels):
 endchar = 'a'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  
  """
  knownlexnorms = [ 'f#A', 'm:f#I', 'm:f#A:f#I:n', 'f#A:n', 'm:f#ikA:n', 
                'm:f#A', 'm:f#I:n', 'm:f#A:n']
  if not rec.lexnorm in knownlexnorms:
   continue
  """
  """
  knownparts = []
  for lexnorm in knownlexnorms:
   lexparts = rec.lexnorm.split(':')
   for lexpart in lexparts:
    if lexpart not in knownparts:
     knownparts.append(lexpart)
  """
  knownparts = ['m','f','n','f#A','f#I','f#ikA','f#akA']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  lexparts = rec.lexnorm.split(':')
  # also require that either 'm' or 'n' be one of the lexparts
  if (not 'm' in lexparts) and (not 'n' in lexparts):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_a, n_a
   elif part == 'f':
    mstem = stem[0:-1] + 'A'  # deva -> devA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   elif part == 'f#A':
    mstem = stem[0:-1] + 'A'  # deva -> devA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   elif part == 'f#I':
    mstem = stem[0:-1] + 'I'  # deva -> devI
    mpart = 'f'
    model = '%s_%s' %(mpart,'I')
   elif part in ['f#ikA','f#akA']:
    newend = part[2:] # ikA or akA
    if not stem.endswith(('aka','ika')):
     mstem = stem[0:-1] + newend  #  replace final a with ikA or akA
     print("model mfn_a2: unusual stem:",stem,part,mstem)
    else:
     mstem = stem[0:-3] + newend  #  replace final aka/ika with akA or ikA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   else:
    print('mfn_a2 Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_a2',d,fmodels)

def model_mfn_a3(recs,fmodels,fileout=None):
 """ This also writes records to a temporary file for further examination"""
 if fileout == None:
  fout = None
 else: 
  fout = codecs.open(fileout,"w","utf-8")
 nout = 0
 endchar = 'a'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  
  knownparts = ['f','f#A','f#I','f#ikA','f#akA']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  lexparts = rec.lexnorm.split(':')
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:  # not needed, but does no harm
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_a, n_a
   elif part == 'f':
    mstem = stem[0:-1] + 'A'  # deva -> devA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   elif part == 'f#A':
    mstem = stem[0:-1] + 'A'  # deva -> devA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   elif part == 'f#I':
    mstem = stem[0:-1] + 'I'  # deva -> devI
    mpart = 'f'
    model = '%s_%s' %(mpart,'I')
   elif part in ['f#ikA','f#akA']:
    newend = part[2:] # ikA or akA
    if not stem.endswith(('aka','ika')):
     mstem = stem[0:-1] + newend  #  replace final a with ikA or akA
     print("model mfn_a3: unusual stem:",stem,part,mstem)
    else:
     mstem = stem[0:-3] + newend  #  replace final aka/ika with akA or ikA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   else:
    print('mfn_a3 Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
   if not (part in ['m','n']):
    # write record to temp file for feminine stem
    out = rec.toString() + '\t' + mstem
    out = "%s\t%s\t%s" %(rec.toString(),part,mstem)
    if fout != None:
     fout.write(out + '\n')
    nout = nout + 1
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_a3',d,fmodels)
 if fout != None:
  fout.close()
  print(nout,"lexnorm records written to",fileout)

def model_mfn_a4(recs,fmodels,fileout=None):
 """ This also writes records to a temporary file for further examination"""
 if fileout == None:
  fout = None
 else:
  fout = codecs.open(fileout,"w","utf-8")
 nout = 0
 endchar = 'a'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n','f#A','f#I','f#akA','f#ikA',
                'f#enI','f#apI','f#apyA', 'f#sI',
                'f#iknI','f#ArI','f#AvI','f#enikA','f#vI',
                'f#padI','f#i','f#u','f#IkA', 'f#tyA','f#yanI',
                'f#iRI','f#inI','f#inikA','f#arI','f#rI',
                'f#sOrI','f#U', 'f#stI',
                'ind#am','ind']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  lexparts = rec.lexnorm.split(':')
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:  # not needed, but does no harm
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_a, n_a
   elif part in ['f','f#A']:
    mstem = stem[0:-1] + 'A'  # deva -> devA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   elif part == 'f#I':
    mstem = stem[0:-1] + 'I'  # deva -> devI
    mpart = 'f'
    model = '%s_%s' %(mpart,'I')
   elif part in ['f#ikA','f#akA']:
    newend = part[2:] # ikA or akA
    if not stem.endswith(('aka','ika')):
     mstem = stem[0:-1] + newend  #  replace final a with ikA or akA
     print("model mfn_a4: unusual stem:",stem,part,mstem)
    else:
     mstem = stem[0:-3] + newend  #  replace final aka/ika with akA or ikA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   elif part in ['f#enI']:
    ending = part[2:]
    assert stem.endswith('eta')
    mstem = stem[0:-3] + ending
    model = 'f_I'
   elif part in ['f#apI','f#apyA']:
    ending = part[2:]
    assert stem.endswith('apya')
    mstem = ending
    model = 'f_%s' %ending[-1]
   elif part in ['f#sI']:
    ending = part[2:]
    assert stem == 'apasya'
    mstem = stem[0:-3] + ending
    model = 'f_I'
   elif part in ['f#iknI']:
    ending = part[2:]
    assert stem in ['asita','palita']
    mstem = stem[0:-3] + ending # replace 'ita' with 'iknI'
    model = 'f_I'
   elif part in ['f#ArI']:
    ending = part[2:]
    assert stem == 'Arya'
    mstem = ending
    model = 'f_I'
   elif part in ['f#AvI']:
    ending = part[2:]
    assert stem == 'Avya'
    mstem = ending
    model = 'f_I'
   elif part in ['f#enikA']:
    ending = part[2:]
    assert stem == 'etaka'
    mstem = ending
    model = 'f_A'
   elif part in ['f#vI']:
    ending = part[2:]
    assert stem == 'Ekalavya'
    mstem = stem[0:-3] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#padI']:
    ending = part[2:]
    assert stem in ['kumBa-pAda','dru-pAda']
    mstem = stem[0:-4] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#i']:
    ending = part[2:]
    mstem = stem[0:-1] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#u']:
    ending = part[2:]
    mstem = stem[0:-1] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#U']:
    assert stem == 'svana'
    ending = part[2:]
    mstem = stem[0:-1] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#IkA']:
    assert stem == 'KuqqAka'
    ending = part[2:]
    mstem = stem[0:-3] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#tyA']:
    assert stem in ['cEkayata','bElvayata']
    ending = part[2:]
    mstem = stem[0:-2] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#yanI']:
    assert stem in ['brADnAyanya']
    ending = part[2:]
    mstem = stem[0:-5] + ending # replace yanya with yanI
    model = 'f_%s' % ending[-1]
   elif part in ['f#iRI']:
    assert stem in ['Barita','rohita','Sukla-harita','harita']
    ending = part[2:]
    mstem = stem[0:-3] + ending # replace ita with iRI
    model = 'f_%s' % ending[-1]
   elif part in ['f#inI']:
    # what about compounds ending with lohita ?
    assert stem in ['lohita']
    ending = part[2:]
    mstem = stem[0:-3] + ending # replace ita with inI
    model = 'f_%s' % ending[-1]
   elif part in ['f#inikA']:
    # what about compounds ending with lohita ?
    assert stem in ['lohitaka']
    ending = part[2:]
    mstem = stem[0:-5] + ending # replace itaka with inikA
    model = 'f_%s' % ending[-1]
   elif part in ['f#arI']:
    assert stem in ['vi-BAva']
    ending = part[2:]
    mstem = stem[0:-1] + ending # replace final 'a' with arI
    model = 'f_%s' % ending[-1]
   elif part in ['f#rI']:
    assert stem in ['vEdUrya']
    ending = part[2:]
    mstem = stem[0:-3] + ending # replace final 'rya' with rI
    model = 'f_%s' % ending[-1]
   elif part in ['f#sOrI']:
    assert stem in ['sOrya']
    ending = part[2:]
    mstem = ending 
    model = 'f_%s' % ending[-1]
   elif part in ['f#stI']:
    assert stem in ['Agastya']
    ending = part[2:]
    mstem = stem[0:-4] + ending # replace final 'stya' with stI
    model = 'f_%s' % ending[-1]
   elif part in ['ind#am']:
    assert stem in ['nada','muKa','sAkzika']
    ending = part[4:]  # am
    mstem = stem[0:-1] + ending # replace final 'a' with 'am'
    model = 'ind'
   elif part in ['ind']:
    if stem not in ['ka','tIra','tUla','paSca']:
     print('mfn_a  unexpected "ind"',stem)
    mstem = stem
    model = 'ind'
   else:
    print('mfn_a4 Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
   if not (part in ['m','n']):
    # write record to temp file for feminine stem
    out = rec.toString() + '\t' + mstem
    out = "%s\t%s\t%s" %(rec.toString(),part,mstem)
    if fout != None:
     fout.write(out + '\n')
   nout = nout + 1

  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_a4',d,fmodels)
 if fout != None:
  fout.close()
  print(nout,"lexnorm records written to",fileout)

def model_mfn_i1(recs,fmodels,fileout=None):
 """ This also writes records to a temporary file for further examination"""
 if fileout == None:
  fout = None
 else:
  fout = codecs.open(fileout,"w","utf-8")
 nout = 0
 endchar = 'i'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n','f#I',
                'f#i', # redundant. Could replace with 'f'
                'f#is','f#tnI','f#yA','f#A','f#ikA','ind','f#tinI']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   print('model_mfn_i1: unexpected lexnorm:',rec.toString())
   continue
  lexparts = rec.lexnorm.split(':')
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)  
   elif part in ['f#I']:
    ending = part[2:]
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'I'
    model = 'f_%s' %ending
   elif part in ['f#i']:
    ending = part[2:]
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'i'  (same as 'f')
    model = 'f_%s' %ending
   elif part in ['f#is']:
    ending = part[2:]
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'is'
    model = 'f_%s' %ending
   elif part in ['f#A']:
    ending = part[2:]
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'A'
    model = 'f_%s' %ending
   elif part in ['f#ikA']:
    ending = part[2:]
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'ikA'
    model = 'f_%s' %ending[-1]
   elif part in ['f#tnI']:
    ending = part[2:]
    assert stem.endswith('pati')
    mstem = stem[0:-2] + ending  # replace ending 'ti' with 'tnI'
    model = 'f_%s' %ending[-1]
   elif part in ['f#tinI']:
    ending = part[2:]
    assert stem == 'prati-prati'
    mstem = stem[0:-2] + ending  # replace ending 'ti' with 'tinI'
    model = 'f_%s' %ending[-1]
   elif part in ['ind']:
    assert stem in ['vazaw-kfti']
    mstem = stem
    model = 'ind'
   elif part in ['f#yA']:
    ending = part[2:]
    # question this in dEva-yajYi. WOuld give dEva-yajYyA Right? Yes acc. to pwg
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'yA'
    model = 'f_%s' %ending[-1]
   else:
    print('mfn_i1 internal ERROR',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
   if not (part in ['m','n']):
    # write record to temp file for feminine stem
    out = rec.toString() + '\t' + mstem
    out = "%s\t%s\t%s\t%s" %(rec.toString(),part,model,mstem)
    if fout != None:
     fout.write(out + '\n')
    nout = nout + 1

  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_i1',d,fmodels)
 if fout != None:
  fout.close()
  print(nout,"lexnorm records written to",fileout)

def model_mfn_u1(recs,fmodels,fileout=None):
 """ This also writes records to a temporary file for further examination"""
 if fileout == None:
  fout = None
 else:
  fout = codecs.open(fileout,"w","utf-8")
 nout = 0
 endchar = 'u'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n','f#U','f#u','f#vI',
                'f#pUrvI','f#I','f#us','f#Us','ind']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   print('model_mfn_u1: unexpected lexnorm:',rec.toString())
   continue
  lexparts = rec.lexnorm.split(':')
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)  
   elif part in ['f#U']:
    mstem = stem[0:-1] + 'U'  # replace ending 'u' with 'U'
    mpart = 'f'
    model = '%s_%s' %(mpart,'U')
   elif part in ['f#u']:
    mstem = stem
    mpart = 'f'
    model = '%s_%s' %(mpart,'u')
   elif part in ['f#vI']:
    mstem = stem[0:-1] + 'vI'  # replace final 'u' with 'vI'
    model = 'f_I'
   elif part in ['f#pUrvI']:
    assert stem == 'puru'
    ending = part[2:]
    mstem = ending
    model = 'f_%s' %ending[-1]
   elif part in ['f#I']:
    assert stem == 'SASabindu'
    ending = part[2:]
    mstem = stem[0:-1]+ending  # replace final 'u' with 'I'
    model = 'f_%s' %ending[-1]
   elif part in ['f#us']:
    # treat MW's 'us' as same as 'u' (Denu_. Refer his grammar, p. 88, where
    # he writes 'Denus' for nom. singular.
    assert stem in ['an-uru','kawu','cAru','tanu']
    mstem = stem
    model = 'f_u' 
   elif part in ['f#Us']:
    ## interpret this as f_U  (like vaDU). See MW grammar as above, p. 91.
    assert stem in ['asita-jYu','kamaRqalu','kaSeru','guggulu','guNgu',
                   'jatu','tanu']
    mstem = stem[0:-1] + 'U'
    model = 'f_U'  # 
   elif part in ['ind']:
    assert stem in ['yuvAku']
    mstem = stem
    model = 'ind'
   else:
    print('mfn_u1 internal ERROR',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
   if not (part in ['m','n']):
    # write record to temp file for feminine stem
    out = rec.toString() + '\t' + mstem
    out = "%s\t%s\t%s\t%s" %(rec.toString(),part,model,mstem)
    if fout != None:
     fout.write(out + '\n')
    nout = nout + 1

  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_u1',d,fmodels)
 if fout != None:
  fout.close()
  print(nout,"lexnorm records written to",fileout)

def model_mfn_f1(recs,fmodels,fileout=None):
 """ This also writes records to a temporary file for further examination"""
 if fileout == None:
  fout = None
 else:
  fout = codecs.open(fileout,"w","utf-8")
 nout = 0
 endchar = 'f'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n','f#trI','f#attrI','f#zwrI','f#rI','f#wrI',
            'f#yantrI','f#sanutrI','f#A','f#metA','f#I','f#f']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   print('model_mfn_f1: unexpected lexnorm:',rec.toString())
   continue
  lexparts = rec.lexnorm.split(':')
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)  
   elif part in ['f#trI','f#attrI','f#zwrI','f#rI','f#wrI','f#yantrI','f#sanutrI','f#I']:
    # remove final 'f' and replace with 'rI'
    mstem = stem[0:-1] + 'rI'
    model = 'f_I'
   elif part == 'f#I':
    assert stem in ['varDayitf']
    # Not sure. Assume replace final 'f' with 'rI'
    mstem = stem[0:-1] + 'rI'
    model = 'f_I'
   elif part == 'f#A':
    assert stem in ['manotf','su-ketf']
    # replace final 'f' with 'A'
    mstem = stem[0:-1] + 'A'
    model = 'f_A'
   elif part == 'f#metA':
    assert stem in ['metf']
    # replace final 'f' with 'A'
    mstem = stem[0:-1] + 'A'
    model = 'f_A'
   elif part == 'f#f':
    if stem not in ['sapta-svasf']:
     print('model_mfn_f ERROR "f#f"',stem,rec.lexnorm)
    mstem = stem
    model = 'f_f'
   else:
    print('mfn_f1 internal ERROR',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
   if not (part in ['m','n']):
    # write record to temp file for feminine stem
    out = rec.toString() + '\t' + mstem
    out = "%s\t%s\t%s\t%s" %(rec.toString(),part,model,mstem)
    if fout != None:
     fout.write(out + '\n')
    nout = nout + 1

  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_f1',d,fmodels)
 if fout != None:
  fout.close()
  print(nout,"lexnorm records written to",fileout)

def model_mfn_o(recs,fmodels):
 endchar = 'o'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_o, f_u
   elif part == 'n':
    # change final 'o' to 'u' and decline like maDu. Ref Kale, p.53
    mstem = stem[0:-1]+'u'
    model = 'n_u'
   else:
    print('mfn_o Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_o',d,fmodels)

def model_mfn_O(recs,fmodels):
 endchar = 'O'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_O, f_O
   elif part == 'n':
    # change final 'O' to 'u' and decline like maDu. Ref Kale, p.53
    mstem = stem[0:-1]+'u'
    model = 'n_u'
   else:
    print('mfn_O Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_O',d,fmodels)

def model_mfn_e(recs,fmodels):
 endchar = 'e'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f#si','n']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_e
   elif part == 'f#si':
    # change final 'e' to 'i' and decline like mati
    # speculative. Inferred MW's f#si
    # only case se
    mstem = stem[0:-1]+'i'
    model = 'f_i'
   elif part == 'n':
    # change final 'e' to 'i' and decline like vAri. 
    # speculative. Inferred from Kale p. 52,53
    # only case se
    mstem = stem[0:-1]+'i'
    model = 'n_i'
   else:
    print('mfn_e Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_e',d,fmodels)

def model_mfn_E(recs,fmodels):
 endchar = 'E'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','f','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_E, f_E, n_E
   else:
    print('mfn_E Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_E',d,fmodels)

def model_mfn_Fx(recs,fmodels):
 endchars = ('F','x')
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchars):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  endchar = stem[-1]
  knownparts = ['m','f']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   
   else:
    print('mfn_Fx Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_mfn_Fx',d,fmodels)


def model_f_AIU(recs,fmodels):
 endchars = ['A','I','U']
 for rec in recs:
  stem = rec.key2
  endchar = stem[-1]
  if not endchar in endchars:
   continue
  lexparts = rec.lexnorm.split(':')
  if lexparts != ['f']:
   continue
  rec.parsed = True
  mstem = stem
  mpart = 'f'
  model = '%s_%s' %(mpart,endchar)  
  rec.models.append(Model(rec,model,mstem))

def model_mfn_in(recs,fmodels):
 ending = 'in'
 knownparts = set(['m','f','n','f#inI','f#iRI',
      'f#TI','f#I','f#nI',])
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(ending):
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)  
   elif part == 'f':
    # must decide stem using sandhi
    stemparts = stem.split('-')
    lastpart = stemparts[-1]
    firstparts = stemparts[0:-1]  # empty list if no '-' in stem
    firstpart = '-'.join(firstparts)
    lastpart1 = lastpart + 'I'
    lastpart2a = sandhi_nR(lastpart1)
    # lastpart2 is empty if no change
    if lastpart2a == None:
     lastpart2 = lastpart1
    else:
     lastpart2 = lastpart2a
    # lastpart2 used in new stem
    if firstpart == '':
     mstem = lastpart2
    else:
     mstem = firstpart + '-' + lastpart2
    if True and (lastpart2a == None):
     # write cases where ignoring pada-structure gives a different answer
     mstem1 = ''.join(stemparts) + 'I'
     mstem2 = sandhi_nR(mstem1)
     #if (mstem2 != None) and mstem2.endswith('RI'):
     # print('stem %s+I , without pada -> %s' %(stem,mstem2))
    #if lastpart2a != None:  # debugging
    # print('chk:',stem,"->",mstem)
    # model is f_in_I  (which is same as f_I)
    model = 'f_in_I'
    #rec.models.append(Model(rec,model,mstem))
   elif part in ['f#inI','f#iRI']:
    ending1 = part[2:] # inI or iRI
    mstem = stem[0:-2] + ending1  # replace ending 'in' 
    mpart = 'f'
    model = 'f_in_I' # '%s_%s' %(mpart,'I')
   elif part in ['f#TI']:
    assert rec.key1 == 'supaTin'
    mstem = stem[0:-2] + 'I'  # replace ending 'in'
    model = 'f_in_I'
   elif part in ['f#I','f#nI']:
    assert rec.key1 in ['kulapAMsin','munipizwakin','prativeSavAsin',
           'prativeSin']
    mstem = stem + 'I'  # pAMsinI.  Probably what is meant
    model = 'f_in_I'
   else:
    print('model_in Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))

endings_Iyas = ('Iyas', 'jyAyas','Sreyas','preyas','BUyas')

def model_Iyas(recs,fmodels):
 """ comparative adjectives in Iyas """

 ending = 'Iyas'
 for rec in recs:
  stem = rec.key2
  found = False
  if not stem.endswith(endings_Iyas):
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(['m','f','n'])):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)  
   elif part == 'f':
    # feminine stem add 'I' to weak stem.
    # the weak stem is just stem
    mstem = stem + 'I'
    model = 'f_Iyas_I'
   rec.models.append(Model(rec,model,mstem))

def model_mfn_as(recs,fmodels):
 """ nouns with 1 stem ending in 'as' """

 ending = 'as'
 for rec in recs:
  stem = rec.key2
  found = False
  if not stem.endswith(ending):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(['m','f','n','ind'])):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)  
   elif part in ['ind']:
    mstem = stem
    model = 'ind'
   else:
    print('mfn_as Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))

def model_mfn_is(recs,fmodels):
 """ nouns with 1 stem ending in 'is' """

 ending = 'is'
 for rec in recs:
  stem = rec.key2
  found = False
  if not stem.endswith(ending):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(['m','f','n','ind'])):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)  
   elif part in ['ind']:
    mstem = stem
    model = 'ind'
   else:
    print('mfn_is Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))

def model_mfn_us(recs,fmodels):
 """ nouns with 1 stem ending in 'us' """

 ending = 'us'
 for rec in recs:
  stem = rec.key2
  found = False
  if not stem.endswith(ending):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(['m','f','n','ind','f#uzI'])):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)  
   elif part in ['ind']:
    mstem = stem
    model = 'ind'
   elif part in ['f#uzI']:
    mstem = stem[0:-2] + 'uzI'  # vapus -> vapuzI
    model = 'f_us_I'
   else:
    print('mfn_is Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))

def model_vat(recs,fmodels):
 # key2 ends with '-vat', '-mat', or
 # 'yat' and is one of kiyat, iyat 
 #ending = 'vat'
 #ending1 = '-' + ending
 knownparts = ['m','f','n','f#atI','ind',
               'f#atnI'  # antarvat
               ]
 for rec in recs:
  stem = rec.key2
  if (not stem.endswith(('-mat','-vat')) and (stem not in ['iyat','kiyat'])):
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  if lexparts == ['ind']:
   # these are handled in model_ind
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,'vat')    # use m_vat even for -mat or iyat, kiyat
   elif part == 'f':
    # add 'I' to stem
    mstem = stem + 'I'
    model = 'f_vat_I'  # normal feminine ending in 'I'. Use _vat for knowledge
    rec.models.append(Model(rec,model,mstem))
   elif part == 'f#atI':
    mstem = stem + 'I'
    model = 'f_vat_I'  # normal feminine ending in 'I'
    rec.models.append(Model(rec,model,mstem))
   elif part == 'f#atnI':
    assert stem in ['antar-vat']
    mstem = stem[0:-2]+'atnI'  # replace ending 'at' with 'atnI'
    model = 'f_vat_I'  # normal feminine ending in 'I'
    rec.models.append(Model(rec,model,mstem))
   elif part in ['ind']:
    if stem not in ['harza-vat']:
     print('model_vat:  unexpected "ind"',stem)
    mstem = stem
    model = 'ind'
   else:
    print('mfn_vat Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))

import data_vas
dvas = data_vas.data_vas_init()
def model_vas(recs,fmodels):
 """ This is quite different from previous functions.

 """
 knownparts = ['m','f','n','f#','m#'
               ]
 for rec in recs:
  stem = rec.key2
  stempadas = stem.split('-')
  lastpada = stempadas[-1]
  firstpadas = stempadas[0:-1]  # all but last of stempadas. May be empty
  if lastpada not in dvas:
   continue
  (fstem,root) = dvas[lastpada]
  lexparts = rec.lexnorm.split(':')
  rec.parsed = True
  for part in lexparts:
   if part.startswith('m#'):
    part = 'm'  # darSivas
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,'vas') 
   elif part.startswith(('f','f#')):
    newstempadas = firstpadas + [fstem]
    mstem = '-'.join(newstempadas)
    assert mstem.endswith('I')
    model = 'f_vas_I'  # normal feminine ending in 'I'. 
    rec.models.append(Model(rec,model,mstem))
   else:
    print('mfn_vas Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))


def model_Iyas(recs,fmodels):
 # key2 ends with 'Iyas' or 'eyas': comparative adjective
 ending = 'Iyas'
 ending1 = '-' + ending
 knownparts = ['m','f','n']
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(('Iyas','eyas')) :
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,'Iyas')    
   elif part == 'f':
    # add 'I' to stem
    mstem = stem + 'I'
    model = 'f_Iyas_I'  # normal feminine ending in 'I'. Use _vat for knowledge
    rec.models.append(Model(rec,model,mstem))
   else:
    print('mfn_Iyas Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))

def model_an(recs,fmodels):
 # key2 ends with 'an'
 ending = 'an'
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(ending):
   continue
  if rec.parsed:
   continue  # already handled. Could be for indeclineables
  # For adjectives ending in 'an', the feminine stem is formed by adding
  # 'I' to the weak stem. (This is rule in Antoine I).
  # However, from Kale (p. 190, section 326) and Whitney (section 435),
  # for nominals ending in 'van', the feminine changes the final 'an' to 'arI'.
  # Specifically, we compute the declension of the word as a masculine,
  # then take the 3s (instrumental singular), which ends in 'A', and 
  # change that 'A' to 'I' to form the feminine.
  # Otherwise, the feminine is declined like a masculine ending in 'an'.
  # In fact, the only example of this feminine is sIman (Deshpande, Kale)
  # and we restrict to the (5) words of MW ending in sIman
  lexparts = rec.lexnorm.split(':')
  knownparts =['m','f','n','f#GnI','f#mnI','f#jYI','f#arI','f#varI',
               'f#rzRI','f#SIrzRI','f#zRI', 'f#DnI', 'f#jA', 'f#haRI',
               'f#hnI','f#mRI','ind','f#yUnI','f#yuvatI','f#yuvati']
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)    
   elif part == 'f':
    if stem.endswith('van'):
     mstem = stem[0:-1]+'rI'
    else:
     # Decline the last pada
     padas = rec.key2.split('-')
     firstpadas = padas[0:-1]
     lastpada = padas[-1]
     decl = decline.Decline_m_an(lastpada,lastpada)
     inflection = decl.table  #  a list
     instr = inflection[6]  # for m_an, we know instr is a string
     assert isinstance(instr,str) and instr.endswith('A'),"%s %s" %(rec.key2,instr)
     lastpada_f = instr[0:-1] + 'I'
     firstpadas.append(lastpada_f)
     mstem = '-'.join(firstpadas)
    model = 'f_an_I'  
   elif part == 'f#GnI':
    assert stem.endswith('han')
    mstem = stem[0:-3] + 'GnI'
    model = 'f_an_I'
   elif part == 'f#haRI':
    assert stem.endswith('han')
    mstem = stem[0:-1] + 'RI' # replace final 'n' with 'RI'
    model = 'f_an_I'
   elif part == 'f#hnI':
    assert stem.endswith('han')
    mstem = stem[0:-3] + 'hnI'
    model = 'f_an_I'
   elif part == 'f#mnI':
    assert stem.endswith('man')
    mstem = stem[0:-3] + 'mnI'
    model = 'f_an_I'
   elif part == 'f#jYI':
    assert stem.endswith('rAjan')
    mstem = stem[0:-3] + 'jYI'
    model = 'f_an_I'
   elif part == 'f#jA':
    assert stem.endswith('rAjan')
    mstem = stem[0:-2] + 'A'  # replace final 'an' with 'A'
    model = 'f_A'  # count as normal f_A model
   elif part in ['f#arI','f#varI']:
    assert stem.endswith('van')
    mstem = stem[0:-2] + 'arI' # replace final 'an' with 'arI'
    model = 'f_an_I'
   elif part in ['f#rzRI','f#SIrzRI','f#zRI']:
    assert stem.endswith('SIrzan')
    mstem = stem[0:-2] + 'RI'  # replace final 'an' with 'RI'
   elif part == 'f#DnI':
    assert stem.endswith('Dan')
    mstem = stem[0:-2] + 'nI' # replace final 'an' with 'nI'
    model = 'f_an_I'
   elif part == 'f#mRI':
    assert stem.endswith('zAman')
    mstem = stem[0:-3] + 'mRI'
    model = 'f_an_I'
   elif part == 'ind':
    if stem not in ('pari-jman','tman'):
     print('skipping',rec.key1,rec.lexnorm)
     continue
    mstem = stem
    model = 'ind'
   elif part in ['f#yUnI','f#yuvatI','f#yuvati']:
    assert stem == 'yuvan'
    mstem = part
    model = 'f_an_I'  
   else:
    print('model_an internal ERROR',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))

import data_aYc
daYc = data_aYc.data_aYc_init()

def model_aYc(recs,fmodels):
 """ This is quite different from previous functions, except for model_vas

 """
 knownparts = ['m','f','n',
               ]
 for rec in recs:
  stem = rec.key2
  stempadas = stem.split('-')
  lastpada = stempadas[-1]
  firstpadas = stempadas[0:-1]  # all but last of stempadas. May be empty
  """
   1/2/2019.  key2 of lexnorm-all2 for these cases (such as udac) 
   have been changed, to end in 'Yc'. Thus, this logic not needed.
  if lastpada.endswith('ac'):
   lastpada = lastpada[0:-1]+'Yc'  # change spelling
   stem = stem[0:-1] + 'Yc'
  """
  if lastpada not in daYc:
   continue
  if not rec.key1.endswith('Yc'):
   print('model_aYc: not end in "Yc":',rec.key1)
  (fstem,) = daYc[lastpada]
  lexparts = rec.lexnorm.split(':')
  if rec.parsed:
   continue # such as for indeclineable akuDryaYc
  rec.parsed = True
  for part in lexparts:
   if part.startswith(('m','f','n')):
    part = part[0] # we don't use MW feminine hints
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,'aYc') 
   elif part == 'f':
    newstempadas = firstpadas + [fstem]
    mstem = '-'.join(newstempadas)
    assert mstem.endswith('I')
    model = 'f_aYc_I'  # normal feminine ending in 'I'. 
    rec.models.append(Model(rec,model,mstem))
   else:
    print('model_aYc Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))

def model_pron(recs,fmodels):
 stems = {} # prepare to list the distinct pronominal stems
 for rec in recs:
  m = re.search(r'^(.*)LEXID=pron,STEM=(.*)$',rec.lexnorm)
  if not m:
   continue
  genders = m.group(1)
  stem = m.group(2)
   # for L=40112, hw = 'ena', stem is given as 'idam,etad' in lexnorma-all2.txt
  # we change this to 'idam'
  if stem == 'idam,etad':
   stem = 'idam'
   print('change pronoun stem from "idam,etad" to "idam"')
  if genders != '':
   assert rec.key2.endswith('-Bavat'),"model_pron ERROR 1: %s"%rec
   genders = re.sub(',$','',genders)
   lexparts = genders.split(':')
   stem = rec.key2
  elif stem in ['asmad','yuzmad']:
   # These have no gender.  Assume gender = 'm' for convenience
   lexparts = ['m']  
  else:
   lexparts = ['m','n','f']
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,'pron')  
   else:
    print('model_pron internal ERROR')
    exit(1)
   rec.models.append(Model(rec,model,mstem))
   if mstem not in stems:
    stems[mstem] = []
   if part not in stems[mstem]:
    stems[mstem].append(part)
 filetemp = "temp_pron_stems.txt"
 with codecs.open(filetemp,"w","utf-8") as f:
  keys = sorted(stems.keys(),key=slp_cmp_key)
  for key in keys:
   f.write('%s %s\n' %(key,','.join(stems[key])))
  print(len(keys),"pron stems written to",filetemp)

def model_card(recs,fmodels):
 for rec in recs:
  m = re.search(r'^LEXID=card,STEM=(.*)$',rec.lexnorm)
  if not m:
   continue
  stem = m.group(1)
  if stem in ['eka','dvi','tri','catur']:
   lexparts = ['m','n','f']
  elif stem.endswith('i'):
   lexparts = ['f']
  elif stem.endswith('t'):
   lexparts = ['f']
  elif stem in ['Sata','sahasra']:
   lexparts = ['m','n']  # Deshpande only neuter
  else:
   # These have no gender.  Assume gender = 'm' for convenience
   lexparts = ['m']  
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,'card')  
   else:
    print('model_card internal ERROR')
    exit(1)
   rec.models.append(Model(rec,model,mstem))

def model_mfn_1cons(recs,fmodels,ending):
 """ nouns with 1 stem ending in various consonants
   Note ending comes in as parameter; thus this routine
   generates files for various consonsants.
 """

 for rec in recs:
  stem = rec.key2
  found = False
  if not stem.endswith(ending):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(['m','f','n','ind'])):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_1_%s' %(part,ending)  
   elif part in ['ind']:
    mstem = stem
    model = 'ind'
   else:
    print('mfn_1cons Internal error',part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))

def prevmodel_mfn_f1(recs,fmodels):
 endchar = 'f'
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  knownparts = ['m','f','n','f#trI','f#attrI','f#zwrI','f#rI','f#wrI',
            'f#yantrI','f#sanutrI','f#A','f#metA','f#I','f#f']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar) 
   elif part in ['f#trI','f#attrI','f#zwrI','f#rI','f#wrI','f#yantrI','f#sanutrI','f#I']:
    # remove final 'f' and replace with 'rI'
    mstem = stem[0:-1] + 'rI'
    model = 'f_I'
   elif part == 'f#I':
    assert stem in ['varDayitf']
    # Not sure. Assume replace final 'f' with 'rI'
    mstem = stem[0:-1] + 'rI'
    model = 'f_I'
   elif part == 'f#A':
    assert stem in ['manotf','su-ketf']
    # replace final 'f' with 'A'
    mstem = stem[0:-1] + 'A'
    model = 'f_A'
   elif part == 'f#metA':
    assert stem in ['metf']
    # replace final 'f' with 'A'
    mstem = stem[0:-1] + 'A'
    model = 'f_A'
   elif part == 'f#f':
    if stem not in ['saptasvasf']:
     print('model_mfn_f ERROR "f#f"',stem,rec.lexnorm)
    assert stem in ['sapta-svasf']
    # Not sure. assume no change
    mstem = stem
    model = 'f_f'
   else:
    print('model_mfn_f internal ERROR',stem,part)
    exit(1)
   rec.models.append(Model(rec,model,mstem))

known_1stems_list = [
 # palatal final from Deshpande
 'vAc','samrAj','viS','fc','tvac','Suc''vaRij','BiSaj','ftvij',
   'parivrAj','diS',
 # cerebral from Kale
 'gaR', # su-gaR from Kale.
 
 'parAR','prAR', # mw.txt
 # dental final from Deshpande
 'marut','sarit','jagat', 'BUBft', 'vidyut',
 'suhfd','Apad','sampad','parizad','viyat','kzuD',
 # dental final from Antoine
 'udBid','samiD',
 # ending in 'D' from mw headwords
 'agniD','agnID','kruD','ruD','vfD','buD','yuD','sriD','baD','bAD',
 'vIruD','iziD','ziD','spfD','pfkzuD','viD','mfD','sAD','guD','SuruD',
 'fD','spfD','srid','zamiD',
 # ending in 'd' from mw headwords
 'vid','pad','sad','zad','pAd','Bid','rud','kakud','kAkud','mud','SArad','nud',
 'samad','cCid','cCad','Cad','Cid','hfd','mfd','dad',
 # labial final from Antoine
 'kakuB',
 # r final
 'gir','dvAr','pur','Dur',
 # other r final from mw.txt
 'aNgir','jur','sPur','aptur','mur','svar','stir','dir','kir','ASir',
 'CidrAntar','jUr','tUr','dur','wur','Sar','yantur',
 'vaDar','vanDur','zwir','sabar',
 # ahar (a day) -- this is irregular
 'gur','tur',
 # l final - from mw
 'anekAl','SIl','hal',
 # cerebral final from Antoine
 'vfz','dviz', # prAvfz
 # cerebral z-final from mw
 'juz','tviz','iz','ruz','ukz','pfkz','muz','miz','susUz',
 'pruz','Sriz','akz','tfz','uz','kfz','viz','puz','kavaz',
 'Dfz','takz','rakz','camriz','cikIrz','tfz','diDakz','diDikz',
 'Sliz','Suz','pipakz','pipaWiz','makz','mUz','BAz','riz','roz','rez',
 'rohiz','rOhiz','prez','pluz','vivikz',
 # S final from mw.txt
 'spfS','dfS','IS','diS','naS','niS','qAS','LAS',
 'paS','piS','prAS','arRaS','yakzeS','liS','pAS','spaS',
 'zpaS','vriS','dAS','DaneS',
 # s-final from Deshpande
 'candramas', 'veDas','payas','uras',
 'sumanas','yaSas','havis','Ayus',
 'manas','cetas','uzas','tamas','vayas','tapas','cakzus','Danus',
 'jyotis','havis',
 # s-final from Antoine
 'tejas','Siras','sadas',
 # probable s-final 1-stems affixes from mw . These end in 'vas'
  'javas','dASvas','Savas','Sravas','Cravas','yavas','avas','Ayavas',
  'fBvas','cyavas','javas','juvas','tavas',
  'duvas','Dvas','ravas','tavas','Baktivas','sravas','BUvas',
  'Sikvas','savas','prasavas','sAhvas','pIvas','vas',
  'Sevas','sravas','avas','havas','hftsvas',
 # additional s-final 1-stem affixes from mw - don't end in 'vas'
  'cCandas','Candas','apas','vAsas','srotas','anDas','okas','ojas',
  'meDas','rajas','rakzas','rahas','retas',
 # h final from Antoine
 'maDulih','upAnah','kamaduh',
 
]
known_1stems = set(known_1stems_list)

def model_1stem(recs,fmodels):
 for rec in recs:
  stem = rec.key2
  # logic to determine whether stem ends in a consonant
  # and is declined with 1 stem.
  found = False
  if stem in known_1stems:
   found = True
  elif '-' in stem:
   m = re.search(r'^.*-([^-]*)$',stem)
   if m:
    # require that stem ends with '-X' where X is a known 1-stem noun
    if m.group(1) in known_1stems:
     found = True
  if not found:
   # other tests
   if stem.endswith(('k','K','g','G')):
    found = True
   elif stem.endswith('ac'):
    if stem not in ['ud-ac','dakziRA-pratyac','deva-dryac']:
     # these three are like 'aYc' direction adjectives, not 1-stem
     found = True
   elif stem.endswith('c') and not stem.endswith('Yc'):
    # exclude direction adjectives
    found = True
   elif stem.endswith(('C','j','J')):
    found = True
   elif stem.endswith(('w','W','q','Q')):
    found = True
   elif re.search(r'[^a]t$',stem):
    # must exclude stems ending in 'at', as some are pr. active participles
    found = True  
   elif stem.endswith(('T','d','D')):
    # things like 'yuzmad' will be excluded by lexnorm test below
    found = True
   elif stem.endswith(('p','P','b','B')):
    found = True
   elif stem.endswith(('is','us')):
    found = True
   elif stem.endswith('kas'):  
    # 45. Okas, and aNkas
    found = True
   elif stem.endswith(('kas','Kas','gas','Gas')):  
    # 45. Okas, and aNkas
    # 13. gas  (various)
    # 1.  Kas (sadmamaKas)
    # 3   Gas
    found = True
   elif stem.endswith(('cas','Cas','jas','Jas')):
    # cas:  93 (varcas, vacas, vyacas, etc.)
    # jas:  66 (pAjas, 'Ojas', etc.)
    found = True
   elif stem.endswith(('was','Was','qas','Qas','Ras')):
    # qas:   1 (heqas)
    # Ras:  24 (arRas, draviRas, etc.)
    found = True
   elif stem.endswith(('tas','Tas','das','Das','nas')):
    # tas:  12 (cetas, Srotas, etc.)
    # Tas:   6 (praTas, pATas)
    # das:  33 (vedas, medas, etc.)
    # Das:  63 (rADas, UDas, etc.)
    # nas:  43  (nas (nose), enas, etc.)
    found = True
   elif stem.endswith(('pas','Pas','bas','Bas','mas')):
    # pas:  25 (vepas, varpas,Apas, etc.)
    # Pas:   5 (SePas, rePas, varPas)
    # bas:   0 
    # Bas:  42 (amBas, naBas, raBas, etc.)
    # mas:   4 (candramas, namas)
    found = True
   # yas - excluding comparatives in Iyas
   elif stem.endswith(endings_Iyas):
    found = False
   elif stem.endswith('yas'):
    #   (gAyas,vasyas, hAyas, DAyas, etc.)
    found = True
    #print('check ..yas stem1',stem)
   elif stem.endswith('ras'):
    # 101  (saras, aNgiras, haras, jaras, taras, etc.
    found = True
   elif stem.endswith('las'):
    #   3  (las, calas)
    found = True
   elif stem.endswith('zas'):
    #   67  (cakzas, vakzas, dakzas, etc.
    found = True
   elif stem.endswith('Sas'):
    #   39  (Sas, peSas, etc.)
    found = True
   elif stem.endswith('sas'):
    #   17  (apsas, daMsas
    found = True
   elif stem.endswith('has'):
    #   62  (aMhas, raMhas, barhas, etc.)
    found = True
   elif stem.endswith('h'):
    found = True
  if not found:
   # record not recognized as a 1-stem noun
   continue
  lexparts = rec.lexnorm.split(':')
  knownparts = ['m','f','n','ind',
                'f#A','f#padI','f#I','f#AcI','f#AdI','f#AtI','f#AntI',
                'ind#Sam',
                'f#ryOhI','f#BArOhI','f#viSvOhI','f#SAlyUhI']
  if not set(lexparts).issubset(set(knownparts)):
   # we don't know how to handle the extra lex information yet
   print("model_1stem skipping:",stem,rec.lexnorm)
   continue
  if lexparts == ['ind']:
   # handled in model_ind
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_1stem' %part
   elif part == 'ind':
    mstem = stem
    model = 'ind'
   elif part == 'f#A':
    assert stem in ['an-apa-sPur']
    mstem = stem + 'A'
    model = 'f_A'
   elif part == 'f#padI':
    assert stem.endswith('pad')
    mstem = stem + 'I'
    model = 'f_I'
   elif part == 'f#AdI':
    assert stem == 'Sata-pAd'
    mstem = stem + 'I'
    model = 'f_I'
   elif part == 'f#AtI':
    assert stem == 'ni-drAt'
    mstem = stem + 'I'
    model = 'f_I'
   elif part == 'f#AntI':
    assert stem == 'ni-drAt'
    mstem = 'ni-drAntI'
    model = 'f_I'
   elif part == 'f#I':
    assert stem.endswith(('pad','dfS','mah'))
    mstem = stem + 'I'
    model = 'f_I'
   elif part == 'f#AcI':
    assert stem in ['devAc','satrAc']
    mstem = stem + 'I'
    model = 'f_I'
   elif part == 'ind#Sam':
    assert stem == 'vi-pAS'
    mstem = stem + 'am'
    model = 'ind'
   elif part == 'f#ryOhI':
    assert stem == 'turya-vah'
    mstem = 'turyOhI'
    model = 'f_I'
   elif part == 'f#BArOhI':
    assert stem == 'BAra-vah'
    mstem = 'BArOhI'
    model = 'f_I'
   elif part == 'f#viSvOhI':
    assert stem == 'viSva-vah'
    mstem = 'viSvOhI'
    model = 'f_I'
   elif part == 'f#SAlyUhI':
    assert stem == 'SAli-vah'
    mstem = 'SAlyUhI'
    model = 'f_I'
   else:
    print('model_1stem internal ERROR')
    exit(1)
   rec.models.append(Model(rec,model,mstem))

def lexnorm_todo(recs,fmodels):
 """ not yet parsed """
 fileout = "temp_lexnorm_todo.txt"
 f = codecs.open(fileout,"w","utf-8")
 nout =0 
 for rec in recs:
  if rec.parsed:
   continue
  out = rec.toString()
  f.write(out + '\n')
  nout = nout + 1
 f.close()
 print(nout,fileout)

def model_stem_string(mrecs):
 """ model is list of Model instances, all of which
   have same model-name and stem
 """
 outarr = []
 mrec = mrecs[0]
 name = mrec.name  # model name
 outarr.append(name)
 outarr.append(mrec.stem)
 # get all the L-numbers
 Larr = [(mrec.lexrec.L,mrec.lexrec.key1) for mrec in mrecs]
 Larr = sorted(Larr,key = lambda x : float(x[0]))  # in L order
 Larr1 = ['%s,%s'%mrec for mrec in Larr]
 # remove duplicates, if any. 
 Larr2 = []
 prev = None
 for x in Larr1:
  if x != prev:
   Larr2.append(x)
  prev = x
 Larrstr = ':'.join(Larr2)
 outarr.append(Larrstr)
 out = '\t'.join(outarr)
 return out

def adjust_case(x):
 """ change uppercase letters X to x1  
 """
 def f(m):
  # A -> a1,  U -> u1, etc.
  u = m.group(0)
  v = u.lower()
  return v+'1'
 y = re.sub(r'[A-Z]',f,x)
 return y

def write_model_instances(modelname,instances,fout=None):
 if fout == None:
  fileout = "%s.txt" % modelname
  # change uppercase letters since windows file system is case insensitive
  fileout = adjust_case(fileout)
  f = codecs.open(fileout,"w","utf-8")
 else:
  f = fout
 # instances is array of Model records
 # group by stem
 e = {}
 for mrec in instances:
  k = mrec.stem
  if k not in e:
   e[k] = []
  e[k].append(mrec)
 stems = e.keys()  # all stems for this model
 #stems = sorted(stems, cmp=slp_cmp)  # not valid for python3
 stems = sorted(stems,key=slp_cmp_key)
 nout = 0
 ntot = 0
 for stem in stems:
  mrecs = e[stem]  
  ntot = ntot + len(mrecs)
  # each item in mrecs is a Model instance
  # All items in mrecs have same value for stem
  model_names = list(set([mrec.name for mrec in mrecs]))
  model_names = sorted(model_names)
  for model_name in model_names:
   # All items in mrecs1 have same value for stem and model-name
   mrecs1 = [mrec for mrec in mrecs if mrec.name == model_name]
   out = model_stem_string(mrecs1)
   nout = nout + 1
   f.write(out + '\n')
 if fout == None:
  f.close()
  print(nout,"written to",fileout," (%s)"%ntot)

def write_normal_models(special_models,fout=None):
 d = Model.d
 models = d.keys()
 # for 'normal' models, write model
 special_endings = tuple(['_'+x for x in special_models])
 for model in models:
  if not model.endswith(special_endings):
   write_model_instances(model,d[model],fout=fout)

def write_special_models(sfx,fout=None):
 d = Model.d
 models = d.keys()
 instances = []  # aggregate over genders
 for model in models:
  if not model.endswith(sfx):
   continue
  instances = instances + d[model]
   
 write_model_instances(sfx,instances,fout=fout)

def write_stem_models(fout):
 d = Model.d
 models = d.keys()
 # for 'normal' models, write model
 
 for model in models:
  instances = d[model]
  count = len(instances)
  out = '%05d %s' % (count,model)
  fout.write(out+'\n')

def lexnorm_todo(recs,fileout):
 f = codecs.open(fileout,"w","utf-8")
 nout = 0
 for rec in recs:
  if rec.parsed:
   continue
  # print unparsed record
  nout = nout + 1
  out = rec.toString()
  f.write(out + '\n')
 f.close()
 print(nout,"written to",fileout)

def non_special_models(recs,fmodels):
 model_ind(recs,fmodels)
 model_pron(recs,fmodels)
 model_m_a(recs,fmodels)
 model_n_a(recs,fmodels)
 model_f_A(recs,fmodels)
 model_f_I(recs,fmodels)
 model_f_U(recs,fmodels)
 model_m_i(recs,fmodels)
 model_f_i(recs,fmodels)
 model_n_i(recs,fmodels)

 model_m_u(recs,fmodels)
 model_f_u(recs,fmodels)
 model_n_u(recs,fmodels)
 model_mfn_a(recs,fmodels)
 model_mfn_i(recs,fmodels)
 model_mfn_u(recs,fmodels)

 model_m_f(recs,fmodels)
 model_f_f(recs,fmodels)
 model_n_f(recs,fmodels)
 model_mfn_f(recs,fmodels)
 model_card(recs,fmodels)
 model_mfn_a1(recs,fmodels)
 model_mfn_a2(recs,fmodels)
 model_mfn_a3(recs,fmodels) #,'model_mfn_a3.txt')  # cases written to file
 model_mfn_a4(recs,fmodels) #,'model_mfn_a4.txt')  # cases written to file
 model_mfn_i1(recs,fmodels) #,'model_mfn_i1.txt')  # cases written to file
 model_mfn_u1(recs,fmodels) #,'model_mfn_u1.txt')  # cases written to file
 model_mfn_f1(recs,fmodels) #,'model_mfn_f1.txt')  # cases written to file
 model_mfn_o(recs,fmodels)
 model_mfn_O(recs,fmodels)
 model_mfn_e(recs,fmodels)
 model_mfn_E(recs,fmodels)
 model_mfn_Fx(recs,fmodels)
 model_mfn_in(recs,fmodels)
 model_vat(recs,fmodels)  #  -vat, -mat, some -yat
 model_vas(recs,fmodels)  #  reduplicated participle ending in 'vas'
 model_Iyas(recs,fmodels)
 model_mfn_as(recs,fmodels)
 model_mfn_is(recs,fmodels)
 model_mfn_us(recs,fmodels)
 model_an(recs,fmodels)
 model_aYc(recs,fmodels)  #  reduplicated participle ending in 'aYc'


if __name__ == "__main__":
 filein = sys.argv[1] # lexnorm-all2
 fileout = sys.argv[2] # stems.txt
 filelexmodels = sys.argv[3] # lexnorm_models.txt
 filemodels = sys.argv[4] # models present in stems.txt
 filetodo = sys.argv[5]  # cases where no model or stem could be computed 
 recs = init_lexnorm(filein)
 with codecs.open(filelexmodels,"w","utf-8") as fmodels:
  non_special_models(recs,fmodels)
  special_models=['pron','card']
  flag1cons=True
  consonants = 'kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh'
  for cons in consonants:
   #  '1-stem' models.
   #  model name is of form: <gender>_1_<cons>, e.g. m_1_t
   # all genders written to file 1_<cons>, e.g. 1_t.txt
   if flag1cons:
    model_mfn_1cons(recs,fmodels,cons)  
    special_models.append('1_'+cons)

 with codecs.open(fileout,"w","utf-8") as fout:
  write_normal_models(special_models,fout=fout)
  for model in special_models:
   write_special_models(model,fout=fout)
 with codecs.open(filemodels,"w","utf-8") as f:
  write_stem_models(f)
 with codecs.open(filetodo,"w","utf-8") as f:
  lexnorm_todo(recs,filetodo)
