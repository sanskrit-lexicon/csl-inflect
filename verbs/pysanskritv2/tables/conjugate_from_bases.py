""" conjugate_from_bases.py
"""
#from conjugate_bases import Conjbase
#from conjugate_bases import all_tenses,special_tenses,general_tenses
from conjugation_join_simple import conjugation_join_simple
special_tenses = ['pre','ipf','ipv','opt']   
general_tenses = ['ppf','prf','fut','con','pft','ben']
all_tenses = special_tenses + general_tenses

class ConjTable(object):
 def __init__(self,root,theclass,amp_voice,tense,base,dbg=False,upasargas=[]):
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
  self.base = base
  self.dbg = dbg
  self.status = True
  # Each table is a list of strings; 
  self.table = []
  #if self.tense in special_tenses:
  self.inflect_special_tense()

 def inflect_special_tense(self):
  """ tense pre, ipf, ipv, opt
  """
  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   #'pre-a':'ti:taH:anti:si:TaH:Ta:mi:vaH:maH', 
   #'pre-m':'te:Ite:ante:se:ITe:Dve:e:vahe:mahe',
   #'ipf-a':'t:tAm:an:s:tam:ta:am:va:ma',
   #'ipf-m':'ta:ItAm:anta:TAH:ITAm:Dvam:i:vahi:mahi',
   #'ipv-a':'tu:tAm:antu::tam:ta:Ani:Ava:Ama',
   #'ipv-m':'tAm:ItAm:antAm:sva:ITAm:Dvam:E:AvahE:AmahE',
   #'opt-a':'It:ItAm:IyuH:IH:Itam:Ita:Iyam:Iva:Ima',
   #'opt-m':'Ita:IyAtAm:Iran:ITAH:IyATAm:IDvam:Iya:Ivahi:Imahi'

   'pre-a': 'ati:ataH:anti:asi:aTaH:aTa:Ami:AvaH:AmaH',
   'pre-m':'ate:ete:ante:ase:eTe:aDve:e:Avahe:Amahe',
   'ipf-a':'at:atAm:an:aH:atam:ata:am:Ava:Ama',
   'ipf-m':'ata:etAm:anta:aTAH:eTAm:aDvam:e:Avahi:Amahi',
   'ipv-a':'atu:atAm:antu:a:atam:ata:Ani:Ava:Ama',
   'ipv-m':'atAm:etAm:antAm:asva:eTAm:aDvam:E:AvahE:AmahE',
   'opt-a':'et:etAm:eyuH:eH:etam:eta:eyam:eva:ema',
   'opt-m':'eta:eyAtAm:eran:eTAH:eyATAm:eDvam:eya:evahi:emahi'
  }
  if self.amp_voice == 'p': # passive
   # use endings of class 4, m (middle) voice
   self.sup = supdict[self.tense + '-' + 'm']
  else:
   try:
    self.sup = supdict[self.tense + '-' + self.amp_voice]
   except:
    self.sup = ''
  if self.sup != '':
   sups = self.getsups()
   self.table = [conjugation_join_simple(self.base,sup) for sup in sups]

 def getsups(self):
  return self.sup.split(':') 

import sys,re,codecs

class BaseRec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.model,self.root,self.Lrefs,self.base) = line.split('\t')
  (self.theclass,self.voice,self.tense) = self.model.split(',')

def init_baserecs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [BaseRec(line) for line in f if not line.startswith(';')]
 return recs

def conjtab(rec):
 conj = ConjTable(rec.root,rec.theclass,rec.voice,rec.tense,rec.base)
 return conj.table

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 baserecs = init_baserecs(filein)
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in baserecs:
   tab = conjtab(rec)
   tabstr = ':'.join(tab)
   out = rec.line + '\t' + tabstr
   f.write(out + '\n')
   #print rec.line
   #print tab
   #print

