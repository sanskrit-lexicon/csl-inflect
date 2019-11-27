# -*- coding: utf-8 -*-
""" conjugate_bases.py
   11-19-2019 adapted from modules of pysanskrit1/test2.py
  Need to review usage of sanskritverb_flag.
  Passive:   The bases for the passive voice are derived in test2.py.
          But the reasoning is extremely complex.  In this code,
          I am going to restrict to examples given in Deshpande
"""
import init
sanskritverb_flag=True
from sandhi import word_parts, sandhi_internal_diphthong_a, guna
from sandhi import vfdDi, sandhi_internal_diphthong_A
import conjugate_bases_passive_pre
# ----------------------------------------------------------------
# utility functions, used by Conjbase class
# ----------------------------------------------------------------

def dhAtu_parts(root):
 """  
 """
 x = word_parts(root)
 (parts,types)=x
 if 3 < len(parts):
  # 03-19-02 dealing with [s a M m A n] where
  # parts = [[s] [a] [M m] [A] [n]]
  # types = "cvcvc"
  # we want to return ([s a M m] [aa] [n] "cvc")
  # so want p1 = [[s a M m] [aa] [n]] t1 = "cvc"
  t1 = types[-3:]
  w = parts[-2:]
  u = parts[0:-2]
  u1 = u
  v = ''.join(u)  # string
  v1 = [v]
  p1 = v1 + w # concatenate string lists
 elif 3 == len(parts):
  p1 = parts
  t1 = types
 elif 2 == len(parts):
  t1 = types
  if types == 'cv':
   # this is tricky edge case.  
   # parts is a list of 2 strings, a constant and a vowel  (['B' 'U'])
   # We return a list of 3 strings, 
   # the last being the empty string (['B' 'U' ''])
   p1 = parts + ['']
  else: # types='vc'
   p1 = [''] + parts
 elif 1 == len(parts): 
  # must be a 1-vowel root, like 'f', 'i'
  t1 = types
  if types == 'v':
   p1 = ['']+parts+['']
  else:
   # types == 'c', should not happen
   p1 = parts + [''] + ['']
 # return a list of strings, by appending t1 to p1
 return p1 + [t1]

def kale_394(c1,v,c2,thetype,dbg=False):
 """
   ;  returns a possibly modified vowel
   ;   the following rule is due to Kale (sec. 394) and applies
   ;  to roots of conjugations 1,4,6,10. It applies when guna
   ;  (or vrddhi) has not applied
   ;  assume already tested that v = [RI] (long)
  ; Note: the condition Kale phrases as 
  ;   'a labial or ##va## precedes'
  ; is interpreted by the predicate labial-P, since I 
  ; include ##va## among the labials
 """
 if thetype == 'cvc':
  if c1 in init.labial_set: # python version of labial-P 
   return 'Ur'
  else:
   return 'Ir'
 elif thetype == 'cv':
  if c1 in init.labial_set:
   return 'ur'
  else:
   return 'ir'
 elif thetype == 'vc':
  return 'Ir'
 elif thetype == 'v':
  return 'ir'
 else:
  # this condition should never be reached
  raise NameError("kale_394(%s,%s,%s,%s) ERROR bad type=%s" %(c1,v,c2,thetype,thetype))

def kale_395(c1,v,c2,thetype,dbg=False):
 """
 ; returns a possibly modified vowel
   ;   the following rule is due to Kale (sec. 395) and applies
   ;  to roots of conjugations 1,4,6,10. It applies when guna
   ;  (or vrddhi) has not applied
   ;  assume already tested that 
   ;   a. v = [v0] and v0 is i u R^i or L^i
; we first check that c2
;  a. begins with either "r" or "v", and
;  b. is a compound consonant
 """
 if len(c2) == 0:
  # when c2 is not present, v is unchanged
  return v
 # in subsequent cases, c2 is not the empty string
 if not c2.startswith(('r','v')):
  # when c2 does not start with "r" or "v", v is unchanged
  return v
 # in subsequent cases, c2 begins with 'r' or 'v'
 if 1 < len(c2):
  # when c2 is a compound consonant, v is lengthened
  return lengthen_vowel(v)
 # otherwise, v unchanged
 return v

# ----------------------------------------------------------------
# constants used by Conjbase
# ----------------------------------------------------------------
all_tenses = {
  "pre":"law",
  "ipf":"laN",
  "ipv":"low",
  "opt":"viDiliN",
  "ppf":"liw-p",
  "prf":"liw-r",
  "fut":"lfw",
  "con":"lfN",
  "pft":"luw",
  "ben":"ASIrliN",
  "aor1":"luN1",
  "aor2":"luN2",
  "aor3":"luN3",
  "aor4":"luN4",
  "aor5":"luN5",
  "aor6":"luN6",
  "aor7":"luN7"
 }
special_tenses = ['pre','ipf','ipv','opt']
general_tenses = ['ppf','prf','fut','con','pft','ben']
aorist_tenses = ['aor1','aor2','aor3','aor4','aor5','aor6']

# ----------------------------------------------------------------
# Conjbase class
# ----------------------------------------------------------------

class Conjbase(object):
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
  self.bases = [] # a list of strings that will be computed
  # check inputs for known values
  if amp_voice not in ['a','m','p']:
   self.status = False
   self.error = 'Conjbase. voice error'
   return
  if theclass not in ['1','2','3','4','5','6','7','8','9','10']:
   self.status = False
   self.error = 'Conjbase. class error'
   return
  if tense not in all_tenses.keys():
   self.status = False
   self.error = 'Conjbase. tense error'
   return
  # compute bases
  if tense in special_tenses:
   # construct_conjbase1a from test2.py
   if self.amp_voice == 'p':
    self.special_tense_passive()
   elif self.theclass in ['1','4','6','10']:
    if self.theclass == '1':
     self.special_tense_a_1()
    elif self.theclass == '4':
     self.special_tense_a_4()
    elif self.theclass == '6':
     self.special_tense_a_6()
    else:
     self.special_tense_a_10()
   elif self.theclass == '2':
    self.bases = [[]] ## odd!
   else:
    self.special_tense_non_a()

  elif tense in general_tenses:
   self.general_tense()
  else:
   self.aorist_tense()

 def special_tense_passive(self):
  """
  # construct_conjpassbase1a
  # tense in pre, ipf, ipv, opt
  # amp_voice = p
  # theclass is unconstrained
   the logic of construct_conjpassbase1a is so convoluted (in test2.py)
   that it was decided not to include it here.
   Rather, a list of 3rd-singular-present passive bases was computed
   using test2.py. 
   Comparisons of the results were made to those of Deshpande, Kale and others
  """
  dbg = True
  root = self.root
  #theclass = self.theclass
  #upasargas = self.upasargas  
  #voice = self.amp_voice
  if root in conjugate_bases_passive_pre.bases:
   self.bases = conjugate_bases_passive_pre.bases[root]
   if (self.bases == []):
    print('special_tense_passive: root=',root,'found but has empty bases')
  elif dbg:
   print('special_tense_passive: root=',root,'not found')
   #self.bases = b.split('/')  # splitting done in bases_passive_pre.py
  # otherwise self.bases = []

 def special_tense_a_1(self):
  # class_a_base_1
  # tense in pre, ipf, ipv, opt
  # assume active or middle voice
  # theclass is 1
  irreg_bases_1={
 # "ag":["aNg"],  Don't know where 'aNg' comes from
 "f":["fcC"],
 "ft":["ftIy"],
 "kam":["kAmay"],
 "kasj":["kajj"],
 "kit":["cikits"],
 "kfp":["kalp"], # per Sanskrit Verb, Madhaviya .
 # roots kram, tras, Bram, BrAS, BlAS and laz.  (and klam)
 # These are class 1 roots (only) in Dhatupathas, but there is a
 # Panini sutra (3.1.70)
 # which says that these roots take 'Sap'/'Syan' suffix (1st and 4th class) optionally by 
 # वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः॥ ३।१।७०.
 # for consistency in comparing to SanskritVerb, I'm giving these roots
 # the (optional) class 4 stems here in this list of class 1 stems.
 # This is admittedly goofy.
 "kram":["krAm","krAmy"],
 "klam":["klAm","klAmy"],
 "Bram":["Bram","BrAmy"], # this also appears for a class 4 Dhatupatha Bram
 "BrAS":["BrAS","BrASy"],
 "BlAS":["BlAS","BlASy"],
 "laz":["laz","lazy"],
 "klam":["klAm"],
 # ; gam can have a normal base, as well as 'gacC' Acc. to MW
 # Dhaval views the 'gam' base as an error in MW.
 "gam":["gacC","gam"],#"gam":["gacC","gam"], 
 
 #"gup,1,p=gopAy"],
 #"gup,1,a=jugups"],
 "guh":["gUh"],
 "GrA":["jiGr"],
 #"cam":["cAm"],  # it is 'cam' acc. to KaleDK
 "jaB":["jamB"],
#; ; 01-09-05. 'titikSh' is desiderative form.
#; ;     ((equal dhAtu 'tij) (setq ans 'titikSh)) ; 1 A tej
 "daMS":["daS"],
 "dA":["yacC"],
 "dfS":["paSy"],
 "DUp":["DUpAy"],
 "DmA":["Dam"],
 "paR":["paRAy"],
 "pA":["pib"],
 "muc":["muYc"],
 "murC":["mUrC"], # Kale has ["mUrcC"], mUrC agrees with SanskritVerb/MW
 "mfj":["mArj"],
 "mnA":["man"],
 "yam":["yacC"],
 "raYj":["raj"],
 "lasj":["lajj"],
 "Sad":["SIy"],
 "zWiv":["zWIv"],
 "zwyE":["styAy"], # SanskritVerb
 "sad":["sId"],
 "saYj":["saj"],
 "sasj":["sajj"],
 "sf":["sar","DAv"],
 "sTA":["tizW"],
 "svaYj":["svaj"],
 "lAYC":["lAYC"], # otherwise, the other logic changes to lAYcC
 "vAYC":["vAYC"], # otherwise, the other logic changes to vAYcC
 "hurC":["hUrC"], # otherwise, logic changes to hUrcC.
                  # Kale DK has hurcC as root, hUrcCati
                  # Madhaviya has hUrCati, MW has hUrCati
  }
  root = self.root
  # check for irregularities first
  if root in irreg_bases_1:
   self.bases = irreg_bases_1[root]
   return
  if root == 'gup':
   #if pada == 'p':
   if self.amp_voice == 'a':
    self.bases = ["gopAy"]
   else:
    self.bases = ["jugups"]
    return
  # otherwise...
  x = dhAtu_parts(root)
  (c1,v,c2,thetype) = x
  if thetype in ['cv','v']:
   # 1.  A final vowel takes guna
   v = guna(v)
  elif (v in 'iufx') and (1<len(c2)):
   # 2. penultimate i,u,f,x  may be modified 
   #    preceding a compound consonant beginning with r or v
   v = kale_395(c1,v,c2,thetype)
  elif (len(c2) == 1) and (v in init.shortsimplevowel_set):
   # 3. A short medial vowel takes guna
   #  a medial vowel is a vowel which stands between consonants
   #  Note: Kale refers to 'the penultimate' short vowel - i.e.,
   #  a vowel followed by a consonant, but not necessarily also
   #  preceded by a consonant - i.e. type = "VC".  The 
   #  following uses the Kale interpretation
   #  a short medial vowel is a medial vowel provided
   #    1) it is a short simple vowel
   #    2) the final consonant (c2) is not compound.
   # Note that when the length of c2 is non-zero, then the
   # type is either cvc or vc (it cannot be cv or v)
   v = guna(v)
  elif v == 'F':
   # 4. Vowel (long) 'F' is modified :
   #  For conjugation 1 verbs, this could not happen in types cv or v,
   #  as guna is already applied by case 1. However, it could happen
   #  with types cvc or vc as 'F' is not short
   v = kale_394(c1,v,c2,thetype)
  # in get_conj_elt_1, the next letter will be "a" or "A"
  # when the original root ends in a vowel whose
  # guna is "e" or "o", this may require a sandhi change
  # to v
  if thetype in ["cv","v"]:
   v = sandhi_internal_diphthong_a(v)
   ans0 = c1 + v
  else:
   ans0 = c1 + v + c2
  # Sep 21, 2016. Adjustments to agree with Kale
  if root.endswith('C'):
   #print "check root",root
   # Kale spells these with 'cC'. And the base should end in 'cC'
   # example roots: uC, fC, murC, mleC, laC, hrIC, 
   #  (not in Kale, MW confirms) yuC
   ans0 = ans0[0:-1]+'cC'
   # further exceptions
   if root == 'uC':
    #  uC does not gunate (i.e., it is not ocCati)
    ans0 = 'u' + ans0[1:]
   elif root == 'yuC':
    # u does not gunate
    ans0 = 'yucC'
   elif root == 'murC': 
    # Note this case is handled by class_a_base_irreg. 
    # So, this logic branch is never reached.
    pass
  #if (root == 'gA') and (pada == 'a'):
  # print "CHK:",root,pada,ans0
  self.bases = [ans0]
 

 def special_tense_a_4(self):
  # class_a_base_4
  # tense in pre, ipf, ipv, opt
  # assume active or middle voice
  # theclass is 4
  irreg_bases_4={
 "klam":["klAmy"],
 "kzam":["kzAmy"],
 "jan":["jAy"],
 "tam":["tAmy"],
 # See comment under 'kram' in irreg_bases_1 for
 # tras, Bram
 "tras":["tras","trasy"],
 "Bram":["Bram","BrAmy"], # this also appears for a class 1 Dhatupatha Bram
 "dam":["dAmy"],
 "do":["dy"], # ??
 "Co":["Cy"],
 "BraMS":["BraSy"],
 "mad":["mAdy"],
 "mid":["medy"],
 "raYj":["rajy"],
 "vyaD":["viDy"],
 "Sam":["SAmy"],
 "So":["Sy"],
 "Sram":["SrAmy"],
 "so":["sy"],
  }
  root = self.root
  if root in irreg_bases_4:
   self.bases = irreg_bases_4[root]
   return
  # following Antoine I.16 and Kale 389
  # 'y' is added to root
  root1 = root + "y"
  x =  dhAtu_parts(root1)
  c1 = x[0]
  v =  x[1]
  c2 = x[2]
  thetype = x[3]
  if (v in 'iufx') and (1 < len(c2)):
   # penultimate i u f x may be modified 
   # preceding a compound consonant beginning with "r" or "v"
   v = kale_395(c1,v,c2,thetype)
  elif (v == 'F'):
   # Vowel F may be modified
   v = kale_394(c1,v,c2,thetype)
  ans = c1 + v + c2
  # subsequent logic requires that a list be returned, not a string
  self.bases = [ans] 

 def special_tense_a_6(self):
  # class_a_base_6
  # tense in pre, ipf, ipv, opt
  # assume active or middle voice
  # theclass is 6
  irreg_bases_6={
  "iz":["icC"],
  # "fmP":["fmP","fP"] acc. to Kale DK
  "kft":["kfnt"],
  "Kid":["Kind"],
  "gF":["gir","gil"],
  #This verb doesn't take the nasal. Nasal is limited to मुच्लृ मुञ्चति। लुप्लृ लुम्पति। विद्लृ विन्दति। लिपि लिम्पति। सिच् सिञ्चति। कृती कृन्तति। खिद खिन्दति। पिश पिंशति। and तृम्फति। दृम्फति। गुम्फति। उम्भति। शुम्भति।. This verb gives only cftatai. See http://sanskritdocuments.org/learning_tools/sarvanisutrani/7.1.59.htm
  # This list (mostly, at least) agrees with the special cases shown in 
  # Kale section 398.  Since cft is missing from Kale's list, we would infer
  # that the present is formed without an inserted nasal.
  # HOWEVER, this conflicts with the Kale Dhatukosha, which shows 'cfntati' as
  # the present tense exemplar.
  #"cft":["cfnt"],
  #"DU":["Du"],
  "piS":["piMS"],
  "praC":["pfcC"],
  "Brasj":["Bfjj"],
  "masj":["majj"],
  "muc":["muYc"],
  "lip":["limp"],
  "lup":["lump"],
  "viC":["vicCAy"], # acc. to Kale DK (root spelled as vicC)
  "vyac":["vic"],
  "vraSc":["vfSc"],
  "sad":["sId"],
  "sasj":["sajj"],
  "sic":["siYc"],
  "vid":["vind"],
  #"sU":["su"], # remove 10-5-2016 for agreement with Kale DK
  "tfMh":["tfh"], # per SanskritVerb and Madhaviya.
  }
 
  """ ; following Antoine I.23, Kale 390
      ; 05-13-04: brU has base bru (Whitney) when in class 6.
  """
  root = self.root
  if root in irreg_bases_6:
   self.bases =  irreg_bases_6[root]
   return
  root1 = root
  x =  dhAtu_parts(root1)
  c1 = x[0]
  v =  x[1]
  c2 = x[2]
  thetype = x[3]
  if (v in 'iufx') and (1 < len(c2)):
   # 1. penultimate i u f x may be modified 
   #    preceding a compound consonant beginning with "r" or "v"
   v = kale_395(c1,v,c2,thetype)
  elif len(c2)==0:
   # 2. final vowel may be changed
   # Kale 390
   v0 = v
   if v0 in 'iI':
    v = v + 'y'
   #elif root=='brU':
   # v = 'uv'
   elif v0 in 'uU':
    #v = v + 'v'
    v = 'uv'
   elif v0 == 'f':
    v = 'riy'
   elif v0 == 'F':
    v = 'ir'
  ans = c1 + v + c2
  # Sep 21, 2016. Adjustments to agree with Kale
  if root.endswith('C'):
   # Kale spells these with 'cC'. And the base should end in 'cC'
   # example roots: miC,
   ans = ans[0:-1]+'cC'
  elif root == 'kU':
   ans = 'kuv'
  elif root == 'lasj':
   ans = 'lajj'
  elif root == 'sU':
   ans = 'suv'
  elif root == 'Brajj':
   ans = 'Bfjj'
  elif root == 'Sad':
   ans = 'SIy'
  elif root == 'dfmp':
   ans = 'dfp'
  # subsequent logic requires that return value be a list
  self.bases = [ans]

 def special_tense_a_10(self):
  # class10_base, class_a_base_10
  # tense in pre, ipf, ipv, opt
  # assume active or middle voice
  # theclass is 10
  irreg_bases_10={
   # "According to Kale DhAtukosha, these class 10 verbs have
   # "two forms. Sometimes, the given forms are associated with
   # "different meanings (e.g. 'vas') and sometimes not (e.g. 'aMs')
   "aMS":["aMSApay","aMSay"],
   "aMs":["aMsay","aMsApay"],
   "kal":["kalay","kAlay"],  # kalay gatO saMKyAne ca; kAlay kzepe
   #"kfp":["kfpay","kfpAy"], # NOT IN KALE DK
   #"kuR":["kuRay","koRay"], # NOT IN KALE DK
   #"gad":["gaday","gAday"], # NOT IN KALE DK. Shows in Kale section 400 as gaday
   "DU":["DUnay","DAvay"], # KALE only DUnay. MW DUnay, DAvay (causal)
   "dal":["dAlay","dalay"], # KALE DK only dAlay. MW dAlay, dalay (causal)
   "paw":["paway","pAway"], # granTe (to clothe, envelop); BAzAyAM vewaRe ca (to speak, to cover)
   #"paR":["paRAy","pARay"], # NOT IN KALE DK
   #"pan":["panAy","pAnay"], # NOT IN KALE DK AS CLASS 10
   "pan":["panAy"],  # under class 1A. to praise; panate, panAyati 
   "puw":["puway","poway"], # saMsarge to bind together; BAzAyAM dIptO ch to speak, to shine, to reduce to powder
   "prI":["prIRay","prAyay"],# KALE DL" tarpaRe to please;  also 1U prayati-te
                             # MW causal  prIRay, prApay, prAyay
   "laj":["lajay","lAjay"], # prakASane to appear; apavAraRe to conceal
   "vas":["vasay","vAsay"], # nivAse to dwell; snehacCedApaharaRezu to love, to cur, to take away
   "SaW":["SaWay","SAWay"], # samyagavaBAzaRe to speak well or ill, to deceive;
                            # asaMskAragatyoH to leave unfinished, to go  AND
                            # 10A, SlAGAyAM to flatter
   #"daB":["damBay"], # NOT IN KALE DK 
   #--------------------------------------------
   # These cases are from Kale section 399, which gives
   # optional forms according to SAkawAyana and others
   # These optionalal second forms are also acc. to SAnskritVerb
   "lajj":["lajjay","lajjApay"],
   "gaR":["gaRay","gaRApay"],
   #---------------------------------------------
   # from Kale DK
   "jYA":["jYApay"],
   #---------------------------------------------
   "piC":["picCay"],  # not in Kale DK. picCayati in MW, sanskritverb.
   "viC":["vicCay"],  # in Kale DK as vicC. vicCayati in MW, Kale DK, sanskritverb.
   "mraC":["mracCay"], # Not in Kale DK, nor MW. Change to form of sanskritverb
   "mleC":["mlecCay"], # Kale spells root mlecC
   "vyay":["vyayay","vyAyay"], # KALE DK has only vyayay form. MW has also vyAyay
   "SvaW":["SvaWay","SvAWay"], # KALE DK has both forms, as separate roots.
   "smi":["smAyay","smApay"],  # KALE DK forms in causal. smApay only for Atmanepada
   "Cad":["Caday","CAday"], # Kale DK has only CAdayati. MW has both, sanverb both
   "ci":["cayay","capay","cAyay"], # Kale DK first two. 
                     #MW ALSO shows cAyay, cApay.
                     # ignoring cApay for consistency with SanskritVerb
   #"kfp":["karpay","kfpay"], # Not sure why 2nd form. Not in Kale DK
   }
  if not sanskritverb_flag:
   tempd = {
    # These cases are from Kale section 399, which gives
    # optional forms according to SAkawAyana and others
    # These are not acc. to SanskritVerb.
    "arT":["arTay","arTApay"],
    "vaRw":["vaRway","vaRwApay"]
   } 
   # Ref for this way to merge dictionaries:
   # http://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression
   irreg_bases_10 = dict(irreg_bases_10,**tempd)
  #-------------------------------
  root = self.root
  """ = dhAtu-a~Nga-10 of Elisp.
   following Antoine I.32, Kale 391 p. 243
   tokar is assumed to be an array of alphabetical tokens
   the function returns a token array
   Kale's description of the 10th class member roots (p. 243, footnote)
    This class contains a few primitive verbs, almost all the roots
    belong to it being derivative; besides, all Causals and some Nominal
    verbs may be regarded as belong to this class.
   Kale's description of base formation:
    Roots of the 10th or 'churAdi' class add 'aya' before the personal
    terminations. Before 'aya',
     - the penultimate short vowel (except 'a') takes the guna substitute
     - the final vowel and the penultimate 'a', not prosodially long, take
       the vriddhi substitute
    Note: By Kale 11 (p. 14), a short vowel is prosodially long when
     followed by a conjunct consonant.
  """
  root = self.root
  if root in irreg_bases_10:
   return irreg_bases_10[root]
  root1 = root
  x =  dhAtu_parts(root1)
  c1 = x[0]
  v =  x[1]
  c2 = x[2]
  thetype = x[3]
  #print "dhAtu_parts=",x
  if thetype in ["cv","v"]:
   # 1. A final vowel takes vrddhi and may be subject to sandhi
   #    change before the affixation of "ay"
   v = vfdDi(v)
   v = sandhi_internal_diphthong_A(v)  # E -> Ay
  elif (len(c2) == 1) and (v == 'a'):
   # short 'a' not prosodially long
   # 2. A penultimate 'a' takes vrddhi
   # Note: Kale also has additional requirement 'not prosodially long'.
   # Later Note: (Kale 14 p. 11). Short vowels when followed by a
   # conjunct consonant are said to be 'prosodially long' ; e.g. the
   # 'a' in 'daRq'
   v = vfdDi(v)
  elif (v in 'iufx') and (1 < len(c2)):
   # 3a. penultimate i u R^i L^i may be modified 
   #   preceding a compound consonant beginning with "r" or "v"
   v = kale_395(c1,v,c2,thetype)
  elif (len(c2)==1) and (v in init.shortsimplevowel_set):
   # 4. penultimate short vowel (other than A) takes guna
   #  a short medial vowel is a medial vowel provided
   #    1) it is a short simple vowel
   #    2) the final consonant (c2) is not compound.
   # Note that when the length of c2 is non-zero, then the
   # type is either CVC or VC (it cannot be CV or V)
   v = guna(v)
  elif v == 'F':
   # 4. Vowel (long) F is modified (when it does not take guna or vrddhi)
   v = kale_394(c1,v,c2,thetype)
  # 'ay' is added to the adjusted word
  # This adjusted for example sAmaya.  
  # It could be that (a) sAmaya is not a real class 10 root or
  # (b) the analysis of this function is faulty.
  #  Currently, c1 = 'sAma', v='y', and c2='a' for this word.
  #print "chk: c1,v,c2=%s,%s,%s" %(c1,v,c2)
  ans = c1 + v + c2 + 'ay'
  """
  if preserve_elisp_errors and (c2 == 'a'):
   if root == 'sAmaya':
    ans = 'sAmayAy' #'sAmayAy'
   else:
    ans = c1 + v + 'Ay'
  """
  # usage requires that a list of strings 
  self.bases = [ans]

 def special_tense_non_a(self):
  # assume active or middle voice
  # tense in pre, ipf, ipv, opt
  # assume active or middle voice
  # theclass is NOT 1,4,6 or 10 and not 2
  pass

 def general_tense(self):
  pass
 def aorist_tense(self):
  pass

def test1():
 import sys
 root = sys.argv[1]
 c = sys.argv[2]  # class
 v = sys.argv[3]  # a,m,or p
 tense = sys.argv[4]
 b = Conjbase(root,c,v,tense)
 print("status=",b.status)
 print('bases=',b.bases)
 
def test2():
 import sys,codecs,re
 filein = sys.argv[1]  # like conjugation_test.txt
 fileout = sys.argv[2]
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 for line in lines:
  m = re.search(r'^([^,]*),([^,]*),([^,]*),([^,=]*)=',line)
  if not m:
   continue
  (root,c,v,tense) = (m.group(1),m.group(2),m.group(3),m.group(4))
  b = Conjbase(root,c,v,tense)
  if b.status:
   stat = 'ok'
  else:
   stat = 'nok'
  basestr = 'bases=' + ('%s' %b.bases)
  rec = (root,c,v,tense,stat,basestr)
  recs.append(rec)
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   out = ', '.join(rec)
   f.write(out+'\n')

if __name__ == "__main__":
 #test1()
 test2()
