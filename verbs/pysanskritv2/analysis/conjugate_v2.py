""" conjugate.py.  Based on bases
"""
import sys
sys.path.append('../bases')
from bases_test2 import RootModel, BaseObj
sys.path.append('../tables')
from conjugate_from_bases import BaseRec, ConjTable

class Conjugate(object):
 def __init__(self,root,theclass,amp_voice,tense,upasargas=[],dbg=False):
  """  root : string, MW spelling
       theclass: string, '1' to '10'
       amp_voice: string 
          'a' : active voice (Parasmaipada)
          'm' : middle voice (Atmanepada)
          'p' : passive voice
       tense: string - one of the keys of all_tenses
       upasargas:  a list of upasargas (e.g. ['pra','vi']).
                   There are a few situations (e.g. in passive) where
                   the base varies if there are upasargas present.
                   This situation needs to be further explored (11-20-2019)
  """
  self.root = root
  self.theclass = theclass
  self.amp_voice = amp_voice
  self.tense = tense
  self.dbg = dbg
  self.status = True
  # interface to bases_test2
  self.init_rootmodel()
  self.init_bases()
  # interface to conjugate_from_bases
  self.conjtablerecs = []  # list of Conjtable objects
  for b in self.bases:
   self.init_baserec(b)
   rec = self.baserec
   self.conjtablerecs.append(
    ConjTable(rec.root,rec.theclass,rec.voice,rec.tense,rec.base))
  self.tables = [conj.table for conj in self.conjtablerecs]
  #self.inflections = [':'.join(tab) for tab in self.conjtablerecs]
  #self.inflection = '&'.join(self.inflections)

 def init_rootmodel(self):
  Lrefs = ''
  line = '%s,%s,%s\t%s\t%s' %(self.theclass,self.amp_voice,self.tense,
         self.root,Lrefs)
  self.rootmodel = RootModel(line)

 def init_baserec(self,b):
  line = '%s\t%s' % (self.rootmodel.line,b)
  self.baserec = BaseRec(line)

 def init_bases(self):
  self.baseobj = BaseObj(self.rootmodel)
  self.bases = self.baseobj.bases
