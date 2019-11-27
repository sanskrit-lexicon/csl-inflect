""" conjugate.py
"""
from conjugate_bases import Conjbase
from conjugate_bases import all_tenses,special_tenses,general_tenses
from conjugation_join_simple import conjugation_join_simple

class Conjugate(object):
 def __init__(self,root,theclass,amp_voice,tense,dbg=False,upasargas=[]):
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
  # tables is list of conjugations, one per base
  # Usually, there is only one base, so tables has length 1
  #  Each table is a list of strings; 
  self.tables = []
  baseobj = Conjbase(root,theclass,amp_voice,tense,dbg=dbg,upasargas=upasargas)
  if not baseobj.status:
   self.status = False
   self.error = baseobj.error
   return
  self.bases = baseobj.bases
  if self.tense in special_tenses:
   self.inflect_special_tense()

 def inflect_special_tense(self):
  """ tense pre, ipf, ipv, opt
  """
  supdict = { 
   # a = active voice = parasmaipada
   # m = middle voice = atmanepada
   #'pre-a':'ti:taH:anti:si:TaH:Ta:mi:vaH:maH', 
   'pre-a': 'ati:ataH:anti:asi:aTaH:aTa:Ami:AvaH:AmaH',
   #'pre-m':'te:Ite:ante:se:ITe:Dve:e:vahe:mahe',
   'pre-m':'ate:ete:ante:ase:eTe:aDve:e:Avahe:Amahe',
   'ipf-a':'t:tAm:an:s:tam:ta:am:va:ma',
   'ipf-m':'ta:ItAm:anta:TAH:ITAm:Dvam:i:vahi:mahi',
   'ipv-a':'tu:tAm:antu::tam:ta:Ani:Ava:Ama',
   'ipv-m':'tAm:ItAm:antAm:sva:ITAm:Dvam:E:AvahE:AmahE',
   'opt-a':'It:ItAm:IyuH:IH:Itam:Ita:Iyam:Iva:Ima',
   'opt-m':'Ita:IyAtAm:Iran:ITAH:IyATAm:IDvam:Iya:Ivahi:Imahi'
  }
  if self.amp_voice == 'p': # passive
   # use endings of class 4, m (middle) voice
   self.sup = supdict[self.tense + '-' + 'a']
  else:
   self.sup = supdict[self.tense + '-' + self.amp_voice]
  sups = self.getsups()
  # we use self.tables, since there MAY (rarely) be more than one base
  self.tables = []
  for b in self.bases:
   tab = [conjugation_join_simple(b,sup) for sup in sups]
   self.tables.append(tab)

 def getsups(self):
  return self.sup.split(':') 
