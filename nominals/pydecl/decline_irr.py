""" decline_pco.py
  Declensions of irregular nominals
  Rather than orchestrating an algorithm joining of bases and suffixes,
  these classes read information from data files:
  decline_irr_data.txt
"""
import sys,re
import codecs

class IrrData(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  key,self.inflectionstr = line.split('\t')
  self.key = key
  m = re.search(r'^(.*?),([mfn])_(.*)$',key)
  self.headword = m.group(1)
  self.gender = m.group(2)
  self.lexid = m.group(3)
  # deserialize
  a = self.inflectionstr.split(':')
  assert len(a)==24
  b = []
  for x in a:
   y = x.split('/')
   if len(y) == 1:
    b.append(x)
   else:
    b.append(y)
  self.inflections = b

def init_irr_data(filein):
 import os 
 dir_path = os.path.dirname(os.path.realpath(__file__))
 pathin = '%s/%s' % (dir_path,filein)
 with codecs.open(pathin,"r","utf-8") as f:
  recs = [IrrData(x) for x in f if not x.startswith(';')]
 d = {}
 for rec in recs:
  d[rec.key] = rec
 return d 

class Decline_irr(object):
 """ declension table for all irregular substantives .
  All are determined by file decline_irr_data.txt
 """
 # class variable
 d = init_irr_data('decline_irr_data.txt')
 def __init__(self,gender,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  
  datakey = '%s,%s_irr' %(self.key2,gender)
  d = Decline_irr.d
  if datakey in d:
   self.status = True
   rec = d[datakey]
   self.table = rec.inflections # list form
   return
  # otherwise, fail
  else:
   self.status = False
   self.table = None
   print('decline_irr. Not found',datakey)

class Decline_m_irr(object):
 """ declension table for pronouns in masculine gender
 """
 def __init__(self,key1,key2=None):
  decl = Decline_irr('m',key1,key2)
  self.status = decl.status
  self.table = decl.table

class Decline_f_irr(object):
 """ declension table for pronouns in feminine gender
 """
 def __init__(self,key1,key2=None):
  decl = Decline_irr('f',key1,key2)
  self.status = decl.status
  self.table = decl.table

class Decline_n_irr(object):
 """ declension table for pronouns in neuter gender
 """
 def __init__(self,key1,key2=None):
  decl = Decline_irr('n',key1,key2)
  self.status = decl.status
  self.table = decl.table

