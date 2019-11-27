"""decline.py
"""
from declension_join_simple import declension_join_simple
from decline_pco import Decline_m_card,Decline_f_card,Decline_n_card
from decline_pco import Decline_m_pron,Decline_f_pron,Decline_n_pron
from decline_1cons import Decline_1
import sys
class Decline_ind(object):
 """ Makes a 1-table entry for indeclineables.
     Of course indeclineables are not declined,
     so this is just for making the indeclineables formally similar
     to declineables.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = ''
  self.status = True
  self.table = [self.key1]
  sups = self.getsups()
 def getsups(self):
  return self.sup.split(':') 

class Decline_m_a(object):
 """ declension table for masculine nouns ending in 'a'
 sup-m-a=as:O:As:am:O:An:ena:AByAm:Es:Aya:AByAm:eByas:At:AByAm:eByas:asya:ayos:AnAm:e:ayos:ezu:a:O:As
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'aH:O:AH:am:O:An:ena:AByAm:EH:Aya:AByAm:eByaH:At:AByAm:eByaH:asya:ayoH:AnAm:e:ayoH:ezu:a:O:AH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  #print('Decline_m_a. init.',key1,key2)
  # for m_a, our sups assume final 'a' is removed from the base
  base1 = base[0:-1]
  #print('  head,base,base1 =',head,base,base1)
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_n_a(object):
 """ declension table for neuter nouns ending in 'a'
sup-n-a=am:e:Ani:am:e:Ani:ena:AByAm:Es:Aya:AByAm:eByas:At:AByAm:eByas:asya:ayos:AnAm:e:ayos:ezu:a:e:Ani
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2

  self.sup = 'am:e:Ani:am:e:Ani:ena:AByAm:EH:Aya:AByAm:eByaH:At:AByAm:eByaH:asya:ayoH:AnAm:e:ayoH:ezu:a:e:Ani' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # for n_a, our sups assume final 'a' is removed from the base
  base1 = base[0:-1]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_f_A(object):
 """ declension table for feminine nouns ending in 'A'
sup-f-A=A:e:AH:Am:e:AH:ayA:AByAm:ABiH:AyE:AByAm:AByaH:AyAH:AByAm:AByaH:AyAH:ayoH:AnAm:AyAm:ayoH:Asu:e:e:AH

 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'A:e:AH:Am:e:AH:ayA:AByAm:ABiH:AyE:AByAm:AByaH:AyAH:AByAm:AByaH:AyAH:ayoH:AnAm:AyAm:ayoH:Asu:e:e:AH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  #print('  head,base,base1 =',head,base,base1)
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_f_I(object):
 """ declension table for feminine nouns ending in 'I'
sup-f-I=I:yO:yaH:Im:yO:IH:yA:IByAm:IBiH:yE:IByAm:IByaH:yAH:IByAm:IByaH:yAH:yoH:InAm:yAm:yoH:Izu:i:yO:yaH

 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'I:yO:yaH:Im:yO:IH:yA:IByAm:IBiH:yE:IByAm:IByaH:yAH:IByAm:IByaH:yAH:yoH:InAm:yAm:yoH:Izu:i:yO:yaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  #print('  head,base,base1 =',head,base,base1)
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_f_U(object):
 """ declension table for feminine nouns ending in 'U'
sup-f-U=UH:vO:vaH:Um:vO:UH:vA:UByAm:UBiH:vE:UByAm:UByaH:vAH:UByAm:UByaH:vAH:voH:UnAm:vAm:voH:Uzu:u:vO:vaH
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'UH:vO:vaH:Um:vO:UH:vA:UByAm:UBiH:vE:UByAm:UByaH:vAH:UByAm:UByaH:vAH:voH:UnAm:vAm:voH:Uzu:u:vO:vaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  #print('  head,base,base1 =',head,base,base1)
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_m_i(object):
 """ declension table for masculine nouns ending in 'i'
sup-m-i=iH:I:ayaH:im:I:In:inA:iByAm:iBiH:aye:iByAm:iByaH:eH:iByAm:iByaH:eH:yoH:InAm:O:yoH:izu:e:I:ayaH
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'iH:I:ayaH:im:I:In:inA:iByAm:iBiH:aye:iByAm:iByaH:eH:iByAm:iByaH:eH:yoH:InAm:O:yoH:izu:e:I:ayaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  #print('  head,base,base1 =',head,base,base1)
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_f_i(object):
 """ declension table for feminine nouns ending in 'i'
sup-f-i=iH:I:ayaH:im:I:IH:yA:iByAm:iBiH:yE,aye:iByAm:iByaH:yAH,eH:iByAm:iByaH:yAH,eH:yoH:InAm:yAm,O:yoH:izu:e:I:ayaH
 This declension has alternative endings.
 It forms the table from the base inflections by prepend_head method,
    which generalizes string concatenation used in previous algorithms.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'iH:I:ayaH:im:I:IH:yA:iByAm:iBiH:yE/aye:iByAm:iByaH:yAH/eH:iByAm:iByaH:yAH/eH:yoH:InAm:yAm/O:yoH:izu:e:I:ayaH' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_n_i(object):
 """ declension table for neuter nouns ending in 'i'
sup-n-i=i:inI:Ini:i:inI:Ini:inA:iByAm:iBiH:ine:iByAm:iByaH:inaH:iByAm:iByaH:inaH:inoH:InAm:ini:inoH:izu:i,e:inI:Ini
 This declension has alternative endings.
 It forms the table from the base inflections as in Decline_f_i
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'i:inI:Ini:i:inI:Ini:inA:iByAm:iBiH:ine:iByAm:iByaH:inaH:iByAm:iByaH:inaH:inoH:InAm:ini:inoH:izu:i/e:inI:Ini'  
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_m_u(object):
 """ declension table for masculine nouns ending in 'u'
sup-m-u=uH:U:avaH:um:U:Un:unA:uByAm:uBiH:ave:uByAm:uByaH:oH:uByAm:uByaH:oH:voH:UnAm:O:voH:uzu:o:U:avaH
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'uH:U:avaH:um:U:Un:unA:uByAm:uBiH:ave:uByAm:uByaH:oH:uByAm:uByaH:oH:voH:UnAm:O:voH:uzu:o:U:avaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  #print('Decline_m_a. init.',key1,key2)
  # for m_a, our sups assume final 'a' is removed from the base
  base1 = base[0:-1]
  #print('  head,base,base1 =',head,base,base1)
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_f_u(object):
 """ declension table for feminine nouns ending in 'u'
sup-f-u=uH:U:avaH:um:U:UH:vA:uByAm:uBiH:vE,ave:uByAm:uByaH:vAH,oH:uByAm:uByaH:vAH,oH:voH:UnAm:vAm,O:voH:uzu:o:U:avaH
 This declension has alternative endings.
 It forms the table from the base inflections by prepend_head method.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'uH:U:avaH:um:U:UH:vA:uByAm:uBiH:vE/ave:uByAm:uByaH:vAH/oH:uByAm:uByaH:vAH/oH:voH:UnAm:vAm/O:voH:uzu:o:U:avaH' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_n_u(object):
 """ declension table for neuter nouns ending in 'u'
sup-n-u=u:unI:Uni:u:unI:Uni:unA:uByAm:uBiH:une:uByAm:uByaH:unaH:uByAm:uByaH:unaH:unoH:UnAm:uni:unoH:uzu:u,o:unI:Uni
 This declension has alternative endings.
 It forms the table from the base inflections as in Decline_f_i
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'u:unI:Uni:u:unI:Uni:unA:uByAm:uBiH:une:uByAm:uByaH:unaH:uByAm:uByaH:unaH:unoH:UnAm:uni:unoH:uzu:u/o:unI:Uni' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_f_o(object):
 """ declension table for feminine nouns ending in 'o'
 declension for masculine nouns ending in 'o' is same.
 The code allows for alternate endings, though currently none are found
 It forms the table from the base inflections by prepend_head method.
Os:AvO:Avas:Am:AvO:As:avA:oByAm:oBis:ave:oByAm:oByas:os:oByAm:oByas:os:avos:avAm:avi:avos:ozu:Os:AvO:Avas 
"""
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'OH:AvO:AvaH:Am:AvO:AH:avA:oByAm:oBiH:ave:oByAm:oByaH:oH:oByAm:oByaH:oH:avoH:avAm:avi:avoH:ozu:OH:AvO:AvaH'  
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  # although known examples need to nR sandhi, we use it (via 
  # declension_join_simple).
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_f_O(object):
 """ declension table for feminine nouns ending in 'O'
 declension for masculine nouns ending in 'O' is same.
 The code allows for alternate endings, though currently none are found;
 It forms the table from the base inflections by prepend_head method.
Os:AvO:Avas:Avam:AvO:Avas:AvA:OByAm:OBis:Ave:OByAm:OByas:Avas:OByAm:OByas:Avas:Avos:AvAm:Avi:Avos:Ozu:Os:AvO:Avas 
"""
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'OH:AvO:AvaH:Avam:AvO:AvaH:AvA:OByAm:OBiH:Ave:OByAm:OByaH:AvaH:OByAm:OByaH:AvaH:AvoH:AvAm:Avi:AvoH:Ozu:OH:AvO:AvaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  # although known examples need to nR sandhi, we use it (via 
  # declension_join_simple).
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_m_e(object):
 """ declension table for masculine or feminine nouns ending in 'e'
 The code allows for alternate endings, though currently none are found;
 It forms the table from the base inflections by prepend_head method.
"""
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'eH:ayO:ayaH:ayam:ayO:ayaH:ayA:eByAm:eBiH:aye:eByAm:eByaH:eH:eByAm:eByaH:eH:ayoH:ayAm:ayi:ayoH:ezu:e:ayO:ayaH'  
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  # although known examples need to nR sandhi, we use it (via 
  # declension_join_simple).
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_m_E(object):
 """ declension table for masculine or feminine nouns ending in 'E'
 The code allows for alternate endings, though currently none are found;
 It forms the table from the base inflections by prepend_head method.
"""
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'AH:AyO:AyaH:Ayam:AyO:AyaH:AyA:AByAm:ABiH:Aye:AByAm:AByaH:AyaH:AByAm:AByaH:AyaH:AyoH:AyAm:Ayi:AyoH:Asu:AH:AyO:AyaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  # although known examples need to nR sandhi, we use it (via 
  # declension_join_simple).
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_n_E(object):
 """ declension table for neuter of nominals in 'E'
 The code allows for alternate endings
 It forms the table from the base inflections by prepend_head method.
 Refer Kale, p. 53
 The neuter pra-rE is changed to prari and should be declined like
  vAri except before the consonantal terminations, when it should
  be declined like rE m.f.
  nom. acc.  prari, prariRI, prarIRi
  instr.     prariRA, prarAByam, prarABiH, etc.
"""
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  # from decline_n_i
  sup_i = 'i:inI:Ini:i:inI:Ini:inA:iByAm:iBiH:ine:iByAm:iByaH:inaH:iByAm:iByaH:inaH:inoH:InAm:ini:inoH:izu:i/e:inI:Ini' 
  # from decline_m_E
  sup_E = 'AH:AyO:AyaH:Ayam:AyO:AyaH:AyA:AByAm:ABiH:Aye:AByAm:AByaH:AyaH:AByAm:AByaH:AyaH:AyoH:AyAm:Ayi:AyoH:Asu:AH:AyO:AyaH' 
  # The consonantal terminations are from the 'normal-case-terminations' on
  # p. 34:
  # 3d, 3p, 4d, 4p, 5d,5p, 7p.
  # Note: 1s shows in p. 34 table as 's' (a consonant), but excluded
  #  for the purpose of this declension, acc. to example 'prari' above.
  # turn into arrays
  sups_i = sup_i.split(':')
  sups_E = sup_E.split(':')
  # the array indices corresponding to consonantal endings are:
  cons_indices = [7,8, 10,11, 13,14, 20]
  sups = []
  for i,sup0 in enumerate(sups_i):
   if i in cons_indices:
    sup = sups_E[i]
   else:
    sup = sups_i[i]
   sups.append(sup)
  self.sup = ':'.join(sups)
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  # although known examples need to nR sandhi, we use it (via 
  # declension_join_simple).
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_m_F(object):
 """ declension table for masculine or feminine nouns ending in 'F' (long
 vocalic 'r')
 The code allows for alternate endings.
 It forms the table from the base inflections by prepend_head method.
 See Kale, p. 51 Example kF
"""
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = ':'.join([
   'IH/FH','irO/rO','iraH/raH',
   'iram/Fm','irO/rO','iraH/Fn',
   'irA/rA','IrByAm/FByAm','IrBiH/FBiH',
   'ire/re','IrByAm/FByAm','IrByaH/FByaH',
   'iraH/ruH','IrByAm/FByAm','IrByaH/FByaH',
   'iraH/ruH','iroH/roH','irAm/rAm',
   'iri/ri','iroH/roH','Irzu/Fzu',
   'IH/FH','irO/rO','iraH/raH'
  ])
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  # although known examples need to nR sandhi, we use it (via 
  # declension_join_simple).
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_m_x(object):
 """ declension table for masculine or feminine nouns ending in 'x' (short
 vocalic 'l')
 The code allows for alternate endings, though there are none
 It forms the table from the base inflections by prepend_head method.
 See Kale, p. 52 Example gamx
"""
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = ':'.join([
   'A','alO','alaH',
   'alam','alO','Fn',
   'lA','xByAm','xBiH',
   'le','xByAm','xByaH',
   'ul','xByAm','xByaH',
   'ul','loH','FRAm',
   'ali','loH','xzu',
   'al','alO','alaH',
  ])
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  base1 = base[0:-1]
  # join key2base and all the endings
  # allow variants for each sup
  # although known examples need to nR sandhi, we use it (via 
  # declension_join_simple).
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_m_in(object):
 """ declension table for masculine nouns ending in 'in'
  These are classified as nouns with two stems, but we can treat them
  has nouns with one stems, by using appropriate (non-standard) sups,
  and for the [single] base dropping the 'in'.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'I:inO:inaH:inam:inO:inaH:inA:iByAm:iBiH:ine:iByAm:iByaH:inaH:iByAm:iByaH:inaH:inoH:inAm:ini:inoH:izu:in:inO:inaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'in' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_n_in(object):
 """ declension table for neuter nouns ending in 'in'
  These are classified as nouns with two stems, but we can treat them
  has nouns with one stems, by using appropriate (non-standard) sups,
  and for the [single] base dropping the 'in'.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  # note alternate in 8s.  3-7 same as for m_in
  self.sup = 'i:inI:Ini:i:inI:Ini:inA:iByAm:iBiH:ine:iByAm:iByaH:inaH:iByAm:iByaH:inaH:inoH:inAm:ini:inoH:izu:i/in:inI:Ini'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'in' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  # allow variants for each sup
  base_infls = []
  for sup in sups:
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(base1,sup))
   else:
    # join each alternate sup to base1
    infls = [declension_join_simple(base1,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]  # drop the final 'in'
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_m_vat(object):
 """ declension table for masculine nouns ending in 
    possessive suffixes 'vat','mat'
    or adjectives of quantity ending in 'yat' or 'vat'

  These are classified as nouns with two stems, but we can treat them
  has nouns with one stems, by using appropriate (non-standard) sups,
  and for the [single] base dropping the 'at'.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'An:antO:antaH:antam:antO:ataH:atA:adByAm:adBiH:ate:adByAm:adByaH:ataH:adByAm:adByaH:ataH:atoH:atAm:ati:atoH:atsu:an:antO:antaH'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'at' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_n_vat(object):
 """ declension table for neuter nouns ending in 
  possessive suffixes 'vat','mat'
  or adjectives of quantity ending in 'yat' or 'vat'
  These are classified as nouns with two stems, but we can treat them
  has nouns with one stems, by using appropriate (non-standard) sups,
  and for the [single] base dropping the 'at'.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  # cases 3-7 same as for m_vat. cases 2 and 8 same as case 1
  self.sup = 'at:atI:anti:at:atI:anti:atA:adByAm:adBiH:ate:adByAm:adByaH:ataH:adByAm:adByaH:ataH:atoH:atAm:ati:atoH:atsu:at:atI:anti'
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'at' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_m_Iyas(object):
 """ declension table for masculine nominals ending in 'Iyas' or 'eyas'
    comparative adjectives

  These are classified as nouns with two stems, but we can treat them
  has nouns with one stems, by using appropriate (non-standard) sups,
  and for the [single] base dropping the 'as'.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'An:AMsO:AMsaH:AMsam:AMsO:asaH:asA:oByAm:oBiH:ase:oByAm:oByaH:asaH:oByAm:oByaH:asaH:asoH:asAm:asi:asoH:aHsu:an:AMsO:AMsaH' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'as' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_n_Iyas(object):
 """ declension table for neuter nouns ending in 'Iyas' or 'eyas'
  comparative adjectives
  These are classified as nouns with two stems, but we can treat them
  has nouns with one stems, by using appropriate (non-standard) sups,
  and for the [single] base dropping the 'as'.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  # cases 3-7 same as for m_Iyas. cases 2 and 8 same as case 1
  self.sup = 'aH:asI:AMsi:aH:asI:AMsi:asA:oByAm:oBiH:ase:oByAm:oByaH:asaH:oByAm:oByaH:asaH:asoH:asAm:asi:asoH:aHsu:aH:asI:AMsi' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'as' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

sys.path.append('../inputs/nominals')
from data_vas import data_vas_init
dict_vas = data_vas_init()

class Decline_m_vas(object):
 """ declension table for masculine nouns ending in vas, which are
  reduplicated perfect participles.
  These are classified as nouns with three stems, but we can treat them
  has nouns with two stems, by using appropriate (non-standard) sups.
  This logic requires computation of two stems (which we call strong
  and weak).  The strong stem just drops the 'vas' from the citation form.
  The weak form comes from pre-computed data, which is in file 
  inputs/nominals/data_vas.py
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  
  self.sup = 'vAn:vAMsO:vAMsaH:vAMsam:vAMsO:uzaH:uzA:vadByAm:vadBiH:uze:vadByAm:vadByaH:uzaH:vadByAm:vadByaH:uzaH:uzoH:uzAm:uzi:uzoH:vatsu:van:vAMsO:vAMsaH' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'vas' is removed from the base
  base1 = base[0:-3] # strong
  # weak base is derived from feminine
  base2 = self.weakbase(base)
  # for decline_one logic in inflect
  self.base1 = head + base1
  self.base2 = head + base2
  # join base and all the endings
  base_infls = []
  for sup in sups:
   if sup.startswith('v'):
    b = base1
   elif sup.startswith('u'):
    b = base2
   else:
    print('Decline_m_vas error: sup=%s'%sup)
    b = base1
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(b,sup))
   else:
    # join each alternate sup to b
    infls = [declension_join_simple(b,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def weakbase(self,base):
  if base in dict_vas:
   (fstem,root) = dict_vas[base]
   assert fstem.endswith('uzI'),"Decline_m_vas. weakbase error 1: %s %s %s" %(base,fstem,root)
   return fstem[0:-3]   # drop the uzI
  else:
   # just drop the 'vas' at end of base, i.e., weak and strong bases the same
   assert base.endswith('vas'),"Decline_m_vas. weakbase error 2: %s %s %s" %(base,fstem,root)
   return base[0:-3]
   
 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_n_vas(object):
 """ declension table for neuter nouns ending in vas, which are
  reduplicated perfect participles.
  These are classified as nouns with three stems, but we can treat them
  has nouns with two stems, by using appropriate (non-standard) sups.
  This logic requires computation of two stems (which we call strong
  and weak).  The strong stem just drops the 'vas' from the citation form.
  The weak form comes from pre-computed data, which is in file 
  inputs/nominals/data_vas.py
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  
  self.sup = 'vat:uzI:vAMsi:vat:uzI:vAMsi:uzA:vadByAm:vadBiH:uze:vadByAm:vadByaH:uzaH:vadByAm:vadByaH:uzaH:uzoH:uzAm:uzi:uzoH:vatsu:vat:uzI:vAMsi' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'vas' is removed from the base
  base1 = base[0:-3] # strong
  # weak base is derived from feminine
  base2 = self.weakbase(base)
  # for decline_one logic in inflect
  self.base1 = head + base1
  self.base2 = head + base2
  # join base and all the endings
  base_infls = []
  for sup in sups:
   if sup.startswith('v'):
    b = base1
   elif sup.startswith('u'):
    b = base2
   else:
    print('Decline_m_vas error: sup=%s'%sup)
    b = base1
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(b,sup))
   else:
    # join each alternate sup to b
    infls = [declension_join_simple(b,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def weakbase(self,base):
  if base in dict_vas:
   (fstem,root) = dict_vas[base]
   assert fstem.endswith('uzI'),"Decline_m_vas. weakbase error 1: %s %s %s" %(base,fstem,root)
   return fstem[0:-3]   # drop the uzI
  else:
   # just drop the 'vas' at end of base, i.e., weak and strong bases the same
   assert base.endswith('vas'),"Decline_m_vas. weakbase error 2: %s %s %s" %(base,fstem,root)
   return base[0:-3]
   
 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_m_as(object):
 """ declension table for masculine (or feminine) nouns ending in 'as'.
  These are classified as nouns with one stem.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'AH:asO:asaH:asam:asO:asaH:asA:oByAm:oBiH:ase:oByAm:oByaH:asaH:oByAm:oByaH:asaH:asoH:asAm:asi:asoH:aHsu:aH:asO:asaH' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'as' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

Decline_f_as = Decline_m_as  # f_as same algorithm as m_as

class Decline_n_as(object):
 """ declension table for neuter nouns ending in 'as'.
  These are classified as nouns with one stem.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'aH:asI:AMsi:aH:asI:AMsi:asA:oByAm:oBiH:ase:oByAm:oByaH:asaH:oByAm:oByaH:asaH:asoH:asAm:asi:asoH:aHsu:aH:asI:AMsi' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'as' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_m_is(object):
 """ declension table for masculine (or feminine) nouns ending in 'is'.
  These are classified as nouns with one stem.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'iH:izO:izaH:izam:izO:izaH:izA:irByAm:irBiH:ize:irByAm:irByaH:izaH:irByAm:irByaH:izaH:izoH:izAm:izi:izoH:iHzu:iH:izO:izaH' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'is' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

Decline_f_is = Decline_m_is  # f_is same algorithm as m_is

class Decline_n_is(object):
 """ declension table for neuter nouns ending in 'is'.
  These are classified as nouns with one stem.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'iH:izI:IMzi:iH:izI:IMzi:izA:irByAm:irBiH:ize:irByAm:irByaH:izaH:irByAm:irByaH:izaH:izoH:izAm:izi:izoH:iHzu:iH:izI:IMzi' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'is' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

class Decline_m_us(object):
 """ declension table for masculine (or feminine) nouns ending in 'us'.
  These are classified as nouns with one stem.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'uH:uzO:uzaH:uzam:uzO:uzaH:uzA:urByAm:urBiH:uze:urByAm:urByaH:uzaH:urByAm:urByaH:uzaH:uzoH:uzAm:uzi:uzoH:uHzu:uH:uzO:uzaH' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'is' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

Decline_f_us = Decline_m_us  # f_us same algorithm as m_us

class Decline_n_us(object):
 """ declension table for neuter nouns ending in 'is'.
  These are classified as nouns with one stem.
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  self.sup = 'uH:uzI:UMzi:uH:uzI:UMzi:uzA:urByAm:urBiH:uze:urByAm:urByaH:uzaH:urByAm:urByaH:uzaH:uzoH:uzAm:uzi:uzoH:uHzu:uH:uzI:UMzi' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final 'is' is removed from the base
  base1 = base[0:-2]
  # join key2base and all the endings
  base_infls = [declension_join_simple(base1,sup) for sup in sups]
  self.table = [head+infl for infl in base_infls]
  self.status = True

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base

consonant_set = 'kKgGNcCjJYwWqQRtTdDnpPbBmyrlvhzSsHM'

def stems_an(key2):
 b0 = key2.replace('-','')
 b = b0[0:-2]  # remove final 'an'
 #s = b + 'A' # strong
 s = b
 m = b + 'a' # middle
 w = b       # weak
 manvanflag = False
 if b.endswith('h'): 
  # -han
  #w = b[0:-1]+'G'
  pass ## do this in declension_join_an
 elif b0.endswith('mUrDan'):
  # Deshpande, Huet. Appears to be exception to next rule.
  pass
 #elif (len(b) > 2) and (b[-2] in consonant_set):
 elif (len(b) > 2) and (b[-2] in consonant_set) and b.endswith(('m','v')):
  # example vartman, Atman, varman
  w = m  
  manvanflag=True
 return (s,m,w,manvanflag)

def declension_join_an(b,sup0):
 """ b and sup0 are strings
   If sup0 contains '/', it is parsed as a list, 
     and a list of strings is returned.
   If sup0 is a string, a string is returned.
   This has special sandhi logic :only used for declensions ending in 'an'.
    1. b endswith 'j': (j+n -> j+Y) (rAjan) 
    2. han (a killer) and its compounds.  Recognized here by b == 'h'
       There are many other irregularities among 'an' nominals (ref. Kale).
       When we deal with these other irregularities, perhaps move the
       'han' compounds to be with that code.
 """
 sups = sup0.split('/')
 infls = []
 for sup in sups:
  b0 = b
  if b0.endswith(('j','J','c','C')):
   if sup.startswith('n'):
    sup = 'Y' + sup[1:]  # replace initial 'n' with 'Y'
  if b0 == 'h': 
   # han and its compounds
   if sup.startswith('n'):
    # h changes to G
    b0 = 'G'
   elif sup != 'an':
    sup = sup.replace('n','R')
   # only Nom. Sing. sup is long A
   if sup.startswith('A'):
    if sup != 'A':
     # Ax -> ax
     sup = 'a'+sup[1:]
  infls.append(declension_join_simple(b0,sup))
 if len(sups) == 1:
  # case 1 sup (no alternates)
  ans = infls[0] # return a string
 else:
  ans = infls  # return a list
 return ans

class Decline_an(object):
 """ declension logic for masculine and neuter of nominals ending in 'an'
 """
 def __init__(self,sup,gender,key1,key2=None):
  self.sup = sup
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  sups = self.getsups()
  head,lastpada = self.splitkey2()
  s,m,w,manvanflag = stems_an(lastpada)
  accpl = w  # introduced 11-15-2019 to correct errors.
  if manvanflag:
   # 'ni' not part of locative singular
   sups[18] = 'ani'
   if gender == 'n':
    # 'nI' is not part of 1d,2d and 8d.  Note: I am uncertain of this
    for i in [1,4,22]:
     sups[i] = 'anI'
    accpl = s
  bases = [s,s,s, 
           s,s,accpl,
           w,m,m,
           w,m,m,
           w,m,m,
           w,w,w,
           s,w,m,   # singular w->s
           s,s,s]   # singular w->s
  
  self.status = True
  self.table = []
  # join base and all the endings
  base_infls = []
  for isup,sup in enumerate(sups):
   b = bases[isup]
   base_infls.append(declension_join_an(b,sup))
  self.table = self.prepend_head(head,base_infls)
  self.status = True
  # for decline_one in inflect directory
  self.bases = bases
  self.head = head

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_m_an(Decline_an):
 """ declension table for masculine nouns ending in an
  These are classified as nouns with three stems.
  This algorithm does just that
 """
 def __init__(self,key1,key2=None):
  sup = 'A:AnO:AnaH:'+\
             'Anam:AnO:naH:'+\
             'nA:ByAm:BiH:'+\
             'ne:ByAm:ByaH:'+\
             'naH:ByAm:ByaH:'+\
             'naH:noH:nAm:'+\
             'ni/ani:noH:su:'+\
             'an:AnO:AnaH'
  super().__init__(sup,'m',key1,key2=key2)  # python 3 syntax

Decline_f_an = Decline_m_an

class Decline_n_an(Decline_an):
 """ declension table for neuter nouns ending in an
  Same as masculine m_an, except the sups for nom., acc., and voc. cases
 """
 def __init__(self,key1,key2=None):
  sup = 'a:nI/anI:Ani:'+\
             'a:nI/anI:Ani:'+\
             'nA:ByAm:BiH:'+\
             'ne:ByAm:ByaH:'+\
             'naH:ByAm:ByaH:'+\
             'naH:noH:nAm:'+\
             'ni/ani:noH:su:'+\
             'a/an:nI/anI:Ani'
  super().__init__(sup,'n',key1,key2=key2)  # python 3 syntax


stems_han = stems_an  

def declension_join_han(b,sup0):
 """ b and sup0 are strings
   If sup0 contains '/', it is parsed as a list, 
     and a list of strings is returned.
   If sup0 is a string, a string is returned.
   This has special sandhi logic for 'han' ('killer) and its compounds
    Recognized here by b ends with 'h'
 """
 sups = sup0.split('/')
 infls = []
 for sup in sups:
  b0 = b
  # han and its compounds
  if sup.startswith('n'):
   # h changes to G
   # the '*' blocks nR sandhi, if any, for G+n'
   b0 = b[0:-1] + 'G*'  
  if sup.startswith('A'):
   # only Nom. Sing. sup is long A
   suptemp=sup
   if sup != 'A':
    # Ax -> ax
    sup = 'a'+sup[1:]
  temp = declension_join_simple(b0,sup)
  if sup.startswith('n'):
   # remove block of nR sandhi, if present
   temp=temp.replace('*','')
  infls.append(temp)
 if len(sups) == 1:
  # case 1 sup (no alternates)
  ans = infls[0] # return a string
 else:
  ans = infls  # return a list
 return ans

class Decline_han(object):
 """ declension logic for masculine and neuter of nominals ending in 'an'
 """
 def __init__(self,sup,gender,key1,key2=None):
  self.sup = sup
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  sups = self.getsups()
  head,lastpada = self.splitkey2()
  s,m,w,manvanflag = stems_han(lastpada)
  if manvanflag:
   # 'ni' not part of locative singular
   sups[18] = 'ani'
   if gender == 'n':
    # 'nI' is not part of 1d,2d and 8d.  Note: I am uncertain of this
    for i in [1,4,22]:
     sups[i] = 'anI'
  bases = [s,s,s, 
           s,s,w,
           w,m,m,
           w,m,m,
           w,m,m,
           w,w,w,
           s,w,m,   # singular w->s
           s,s,s]   # singular w->s
  
  self.status = True
  self.table = []
  # join base and all the endings
  base_infls = []
  for isup,sup in enumerate(sups):
   b = bases[isup]
   base_infls.append(declension_join_han(b,sup))
  self.table = self.prepend_head(head,base_infls)
  self.status = True
  # for decline_one in inflect directory
  self.bases = bases
  self.head = head

 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  # for compounds ending in 'han', restate last pada to include
  # prior pada, if any
  parts = self.key2.split('-')
  # base is last TWO part
  # head is joining of all prior parts. 
  if len(parts) == 1:
   head = ''
   base = parts[0]
  else:
   base = ''.join(parts[-2:])
   head = ''.join(parts[0:-2])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

class Decline_m_han(Decline_han):
 """ declension table for masculine nouns ending in an
  These are classified as nouns with three stems.
  This algorithm does just that
 """
 def __init__(self,key1,key2=None):
  sup = 'A:AnO:AnaH:'+\
             'Anam:AnO:naH:'+\
             'nA:ByAm:BiH:'+\
             'ne:ByAm:ByaH:'+\
             'naH:ByAm:ByaH:'+\
             'naH:noH:nAm:'+\
             'ni/ani:noH:su:'+\
             'an:AnO:AnaH'
  super().__init__(sup,'m',key1,key2=key2)  # python 3 syntax

Decline_f_han = Decline_m_han

class Decline_n_han(Decline_han):
 """ declension table for neuter nouns ending in an
  Same as masculine m_han, except the sups for nom., acc., and voc. cases
 """
 def __init__(self,key1,key2=None):
  sup = 'a:nI/anI:Ani:'+\
             'a:nI/anI:Ani:'+\
             'nA:ByAm:BiH:'+\
             'ne:ByAm:ByaH:'+\
             'naH:ByAm:ByaH:'+\
             'naH:noH:nAm:'+\
             'ni/ani:noH:su:'+\
             'a/an:nI/anI:Ani'
  super().__init__(sup,'n',key1,key2=key2)  # python 3 syntax


from data_aYc import data_aYc_init
dict_aYc = data_aYc_init()

class Decline_m_aYc(object):
 """ declension table for masculine nouns ending in aYc or AYc or ac, which are
  directional words 
  These are classified as nouns with three stems, but we can treat them
  has nouns with two stems, by using appropriate (non-standard) sups.
  This logic requires computation of two stems (which we call strong
  and weak).  
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  
  self.sup = 'N:YcO:YcaH:Ycam:YcO:caH:cA:gByAm:gBiH:ce:gByAm:gByaH:caH:gByAm:gByaH:caH:coH:cAm:ci:coH:kzu:N:YcO:YcaH' 
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final Yc or Yc or ac removed
  if base.endswith('ac'):
   # assume alternate citation spelling with 'real' spelling ending in aYc
   base = base[0:-1] + 'Yc'  # replace final 'c' with 'Yc'
  assert base.endswith(('aYc','AYc')),"decline.Decline_aYc. Error in base:%s"%self.keys
  base1 = base[0:-2] # strong. remove final 'Yc'
  # weak base is derived from feminine
  base2 = self.weakbase(base)
  # for decline_one logic in inflect
  self.base1 = head + base1
  self.base2 = head + base2
  # join base and all the endings
  base_infls = []
  for isup,sup in enumerate(sups):
   if isup in [5,6,9,12,15,16,17,18,19]:
    b = base2
   else:
    b = base1
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(b,sup))
   else:
    # join each alternate sup to b
    infls = [declension_join_simple(b,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def weakbase(self,base):
  if base in dict_aYc:
   fstem,  = dict_aYc[base]
   assert fstem.endswith(('cI',)),"Decline_m_aYc. weakbase error 1: %s %s" % (base,fstem)
   return fstem[0:-2]   # drop the cI
  else:
   print("decline.decline_aYc.weakbase error:",base)
   exit(1)
   # just drop the 'vas' at end of base, i.e., weak and strong bases the same
   #assert base.endswith('vas'),"Decline_m_aYc. weakbase error 2: %s %s %s" %(base,fstem,root)
   #return base[0:-3]
   
 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b

#from data_aYc import data_aYc_init
#dict_aYc = data_aYc_init()

class Decline_n_aYc(object):
 """ declension table for masculine nouns ending in aYc or AYc or ac, which are
  directional words 
  These are classified as nouns with three stems, but we can treat them
  has nouns with two stems, by using appropriate (non-standard) sups.
  This logic requires computation of two stems (which we call strong
  and weak).  
 """
 def __init__(self,key1,key2=None):
  self.key1 = key1
  if key2 == None:
   self.key2 = key1
  else:
   self.key2 = key2
  
  self.sup = 'k:cI:Yci:k:cI:Yci:cA:gByAm:gBiH:ce:gByAm:gByaH:caH:gByAm:gByaH:caH:coH:cAm:ci:coH:kzu:k:cI:Yci'  
  self.status = True
  self.table = []
  sups = self.getsups()
  head,base = self.splitkey2()
  # our sups assume final Yc or Yc or ac removed
  if base.endswith('ac'):
   # assume alternate citation spelling with 'real' spelling ending in aYc
   base = base[0:-1] + 'Yc'  # replace final 'c' with 'Yc'
  assert base.endswith(('aYc','AYc')),"decline.Decline_aYc. Error in base:%s"%self.keys
  #if base.endswith(('aYc','AYc')):
  base1 = base[0:-2] # strong. remove final 'Yc'
  # weak base is derived from feminine
  base2 = self.weakbase(base)
  # for decline_one logic in inflect
  self.base1 = head + base1
  self.base2 = head + base2
  # join base and all the endings
  base_infls = []
  for isup,sup in enumerate(sups):
   if isup in [1,4,6,9,12,15,16,17,18,19,22]:
    b = base2
   else:
    b = base1
   if '/' not in sup:
    # no variants for this sup
    base_infls.append(declension_join_simple(b,sup))
   else:
    # join each alternate sup to b
    infls = [declension_join_simple(b,sup1) for sup1 in sup.split('/')]
    base_infls.append(infls)
  self.table = self.prepend_head(head,base_infls)
  self.status = True

 def weakbase(self,base):
  if base in dict_aYc:
   fstem,  = dict_aYc[base]
   assert fstem.endswith(('cI',)),"Decline_m_aYc. weakbase error 1: %s %s" % (base,fstem)
   return fstem[0:-2]   # drop the cI
  else:
   print("decline.decline_aYc.weakbase error:",base)
   exit(1)
   # just drop the 'vas' at end of base, i.e., weak and strong bases the same
   #assert base.endswith('vas'),"Decline_m_aYc. weakbase error 2: %s %s %s" %(base,fstem,root)
   #return base[0:-3]
   
 def getsups(self):
  return self.sup.split(':') 
 def splitkey2(self):
  parts = self.key2.split('-')
  # base is last part
  # head is joining of all prior parts.  If no '-', head is empty string
  base = parts[-1]
  head = ''.join(parts[0:-1])
  return head,base
 # static method
 def prepend_head(self,head,infls):
  b = []
  for x in infls:
   if isinstance(x,list):
    y = [head + i for i in x]
   else: # assume string
    y = head + x
   b.append(y)
  return b



# --------------------------------------
def test_m_a(key1,key2):
 decl = Decline_m_a(key1,key2)
 if not decl.status :
  print("Problem with declension of",key1,key2)
  exit(1)
 print("Decline_m_a(%s,%s) ->\n%s" %(key1,key2,decl.table))

if __name__ == "__main__":
 import sys
 key1 = sys.argv[1]
 if len(sys.argv) > 2:
  key2 = sys.argv[2]
 else:
  key2 = None
 test_m_a(key1,key2)

  
