""" perfect_join.py
 a function to handle all the complications of joining base to sup for
 tense = prf
"""
import re

shortsimplevowel_set = 'aiufx'
longsimplevowel_set = 'AIUFX'
simplevowel_set = 'aiufxAIUFX'
diphthong_set = 'eEoO'
vowel_set = 'aiufxAIUFXeEoO'
K_set = 'kKgGN'
CH_set = 'cCjJY'
TT_set = 'wWqQR'
T_set = 'tTdDn'
P_set = 'pPbBm'
semivowel_set = 'yrlvh'
sibilant_set = 'zSsH'
consonant_set = 'kKgGNcCjJYwWqQRtTdDnpPbBmyrlvhzSsHM'
guttural_set = 'kKgGNhH'
palatal_set = 'cCjJYyS'
cerebral_set = 'wWqQRrz'
dental_set = 'tTdDnls'
labial_set = 'pPbBmvH'
hardnonaspirate_set = 'kcwtp'
hardaspirate_set = 'KCWTP'
softnonaspirate_set = 'gjqdb'
softaspirate_set = 'GJQDB'
nasal_set = 'NYRnm'
hard_set = 'kcwtpKCWTPzSsH'
soft_set = 'gjqdbGJQDBNYRnmyrlvh'
mute_set = 'kcwtpKCWTPgjqdbGJQDBNYRnm'
#------------------------------------------------------------------------
# guRa and vfdDi
# represent these as python dictionaries
# based on Antoine
guRa = {'a':'a', 'A':'a', 
        'i':'e', 'I':'e',
        'u':'o', 'U':'o',
        'f':'ar', 'F':'ar',
        'x':'al', 'X':'al'}
vfdDi = {'a':'A', 'A':'A', 
        'i':'E', 'I':'E',
        'u':'O', 'U':'O',
        'f':'Ar', 'F':'Ar',
        'x':'Al', 'X':'Al'}
#  this varies from antoine, but seems necessary in implementing
#  algorithm for imperfect tense, namely verbs like 'uz' (of Conj 1)
vfdDi['o'] = 'O'
vfdDi['e'] = 'E'
vfdDi['O'] = 'O'
vfdDi['E'] = 'E'
guRa['E'] = 'E'
guRa['e'] = 'E'
guRa['o'] = 'O'
guRa['O'] = 'O'
#------------------------------------------------------------------------
# semivowels associated to vowel (samprasarana)
semivowel_of_vowel = {'i':'y', 'I':'y',
                      'u':'v', 'U':'v',
                      'f':'r', 'F':'r',
                      'x':'l', 'X':'l'}
def word_parts(citation):
 """ from gram2.el
   return a pair (x,y) where
   x is a list of strings, each of which is either all vowels or all 
    consonants, and whose concatenation is citation and
   y is a string of 'v' and 'c' corresponding.
   Examples: rAma -> [['r','A','m','a'],'cvcv']
   akza -> [['a','kz','a'],'vcv']
   strI -> [['str','I'],'cv']
 """
 parts=[]
 types=[]
 def typeof(x):
  if x in consonant_set:
   return "c"
  else:
   return "v"
 prevtype=None
 prevpart=''
 for x in citation:
  t = typeof(x)
  if not prevtype:
   prevpart=x
   prevtype=t
  elif prevtype == t:
   prevpart = prevpart+x
  else:
   parts.append(prevpart)
   types.append(prevtype)
   prevpart=x
   prevtype=t
 # last one
 parts.append(prevpart)
 types.append(prevtype)
 return [parts,''.join(types)]


def perfect_join(root,isup,b,sc,sup,strong):
 """ return a list of strings
 """
 dbg = False

 b1 = monosyllabic_a_base(root,isup,b,sup,strong,sc)
 if sc == 'aniw':
  ans = perfect_join_aniw(root,isup,b,sup,strong)
 elif sc == 'sew':
  if sup[0] in consonant_set:
   if strong and (isup == 3):  
    # use alternate base before 'Ta' 
    ans = perfect_join_sew(root,isup,b1,sup,strong)
   else:
    ans = perfect_join_sew(root,isup,b,sup,strong)
  else:
   # use
   ans = perfect_join_aniw(root,isup,b1,sup,strong)
 else : # sc == vew
  ans1 = perfect_join_aniw(root,isup,b,sup,strong)
  if sup[0] in consonant_set:
   if strong and (isup == 3):  
    # use alternate base before 'Ta' 
    ans2 = perfect_join_sew(root,isup,b1,sup,strong)
   else:
    ans2 = perfect_join_sew(root,isup,b,sup,strong)
  else:
   ans2 = []
  ans = ans1 + ans2
 return ans

def perfect_join_aniw(root,isup,b,sup,strong):
 if strong and (isup == 1) and (b[-1] in consonant_set):
  print('perfect_join_aniw anomaly:',b,sup)
  exit(1)
 p,t = word_parts(b)
 b1s = [b]

 dbg = False
 if strong and (isup == 0):
  # 3s in parasmaipada.
  if t.endswith('vc') and (len(p[-1]) == 1):
   # b has penultimate vowel.  
   # Note this requires that the ending consonant be simple (= non-conjunct)
   # So, for instance with krand, the last 'a' in cakrand is NOT considered
   # penultimate
   pv = p[-2] 
   if pv in shortsimplevowel_set:
    if pv != 'a':
     # Before strong ending, penultimate short vowel takes its guRa substitute,
     b1 = ''.join(p[0:-2]) +  guRa[pv] + p[-1]
     b1s = [b1]
    else:
     # The penultimate 'a' takes vriddhi necessarily in 3s
     b1 = ''.join(p[0:-2]) +  'A' + p[-1]
     b1s = [b1]
  elif t.endswith('v'): 
   # final vowel takes vrddhi necessarily in 3s
   fv = p[-1]
   b1 = ''.join(p[0:-1]) + vfdDi[fv]
   b1s = [b1]
 elif strong and (isup == 6):
  # 1s in parasmaipada.
  if t.endswith('vc') and (len(p[-1]) == 1):
   # b has penultimate vowel.  
   # Note this requires that the ending consonant be simple (= non-conjunct)
   # So, for instance with krand, the last 'a' in cakrand is NOT considered
   # penultimate
   pv = p[-2] 
   if pv in shortsimplevowel_set:
    if pv != 'a':
     # Before strong ending, penultimate short vowel takes its guRa substitute,
     b1 = ''.join(p[0:-2]) +  guRa[pv] + p[-1]
     if dbg:
      print('aniw CHECK 1:',root,isup,b,sup,strong,'b1=',b1)
     b1s = [b1]
    else:
     # The penultimate 'a' takes vriddhi optionally in 1s
     b1 = ''.join(p[0:-2]) +  'A' + p[-1]
     b1s = [b,b1]
  elif t.endswith('v'):
   # final vowel optionally takes vfdDi
   fv = p[-1]
   b1 = ''.join(p[0:-1]) + vfdDi[fv]
   b1s = [b,b1]
  if dbg:
   print('aniw CHECK 2:',root,isup,b,sup,strong,'b1s=',b1s)
 elif strong and (isup == 3):
  # 2s in parasmaipada.
  if t.endswith('vc') and (len(p[-1]) == 1):
   # b has penultimate vowel.  
   # Note this requires that the ending consonant be simple (= non-conjunct)
   # So, for instance with krand, the last 'a' in cakrand is NOT considered
   # penultimate
   pv = p[-2] 
   if pv in shortsimplevowel_set:
    if pv != 'a':
     # Before strong ending, penultimate short vowel takes its guRa substitute,
     b1 = ''.join(p[0:-2]) +  guRa[pv] + p[-1]
     b1s = [b1]
  elif t.endswith('v'): 
   # final vowel takes guRa 
   fv = p[-1]
   b1 = ''.join(p[0:-1]) + guRa[fv]
   b1s = [b1]
  if dbg:
   print('aniw CHECK 3:',root,isup,b,sup,strong,'b1s=',b1s)
 # ----------------------------------------------------
 # done with alterations of base.  Now join with sup
 # ----------------------------------------------------
 infls = []
 for b1 in b1s:
  if b1.endswith('A') or (b1.endswith('E') and (not root.endswith(('i','I')))):
   if (sup == 'a') and strong:
    # xA + a -> xO  . (active voice 1s or 1p)
    infl = b1[0:-1]+'O'
   elif sup[0] in vowel_set:
    # xA + vy -> xvy
    infl = b1[0:-1] + sup
   elif b1.endswith('E') and (sup == 'Ta'):
    # replace E with A
    infl = b1[0:-1] + 'A' + sup
   else:
    infl = b1+sup
  elif b1.endswith('E'):
   # also, root ends with i or I
   if (sup == 'a') and strong:
    infl = b1[0:-1]+'Aya'
   elif sup[0] in vowel_set:
    # xE + y -> xiy
    infl = b1[0:-1] + 'iy' + sup
   elif b1.endswith('E') and (sup == 'Ta'):
    if root == 'i':
     infl = 'iye' + sup
    else:
     # replace E with A
     infl = b1[0:-1] + 'A' + sup
   else:
    infl = b1+sup
  elif b1.endswith('e'):
   # also, root ends with i or I
   if (sup == 'a') and strong:
    infl = b1[0:-1]+'aya'
   elif sup[0] in vowel_set:
    # xe + y -> xay
    infl = b1[0:-1] + 'ay' + sup
   #elif (sup == 'Ta'):
   # infl = 'iye' + sup
   else:
    infl = b1+sup
  elif b1.endswith('O'):
   # vfdDi of 'u'
   if (sup == 'a') and strong:
    infl = b[0:-1] + 'Av' + sup
   else:
    infl = b1 + sup
  elif b1.endswith(('u','U')):
   if (sup[0] in vowel_set) and (not strong):
    infl = b1[0:-1] + 'uv' + sup
   elif (sup[0] in vowel_set) and (strong):
    infl = b1[0:-1] + 'av' + sup
   else:
    infl = b1 + sup
  elif b1.endswith(('i','I')):
   if (sup[0] in vowel_set) and (not strong):
    infl = b1[0:-1] + 'i' + 'y' + sup
   elif (sup[0] in vowel_set) and (strong):
    infl = b1[0:-1] + 'ay' + sup
   else:
    infl = b1 + sup
  elif b1.endswith(('f','F')):
   if (sup[0] in vowel_set) and (not strong):
    infl = b1[0:-1] + 'r' + sup
   elif (sup[0] in vowel_set) and (strong):
    infl = b1[0:-1] + 'ar' + sup
   else:
    infl = b1 + sup
  elif b1.endswith(('j','c')) and sup == 'Ta':
   infl = b1[0:-1] + 'k' + sup
  else:
   # default
   infl = b1+sup
  if dbg: 
   print('aniw:',root,isup,b,sup,strong,'b1=',b1,'infl=',infl)
  infls.append(infl)
 return infls

def perfect_join_sew(root,isup,b,sup,strong):
 # assume sup[0] is consonant
 dbg = False
 if (root == 'Sri') and (isup == 0) and dbg:
  print('perfect_join_sew CHECK:',root,isup,b,sup,strong)
 b1 = b
 if (isup,strong) == (3,True):
  # Ta
  if root == 'Baj':
   b1 = 'Bej'

 b1s = [b1]
 infls = []
 for b1 in b1s:
  if b1.endswith(('A','E')):
   # drop final A/E of base
   infl = b1[0:-1] + 'i' + sup
  elif b1.endswith('e'):
   infl = b1[0:-1] + 'ay' + 'i' + sup
  elif b1.endswith(('u','U')):
   # since sew ending in u, model is ru (Kale p.310)
   if (sup[0] in vowel_set) and (not strong):
    infl = b1[0:-1] + 'v' + 'i' + sup
   elif (sup[0] in vowel_set) and (strong):
    print('perfect_join_sew anomaly 1:',root,isup,b,sup,strong)
    exit(1)
   # now we know sup[0] is a consonant
   elif strong:
    # since strong, and sup[0] is consonant, sup = Ta
    infl = b1[0:-1] + 'av' + 'i' + sup
   else:
    # sup[0] is a consonant AND is a weak ending
    # Also, we are sew.  So u + i -> uvi 
    # Also assume U + i -> uvi
    if sup.startswith('s'):
     sup1 = 'i' + 'z' + sup[1:]
    else:
     sup1 = 'i' + sup
    infl = b1[0:-1] + 'uv' + sup1
  elif b1.endswith(('i','I')):
   # since sew ending in i, model is Sri (Kale p.311)
   if (sup[0] in vowel_set) and (not strong):
    infl = b1[0:-1] + 'y' + 'i' + sup
   elif (sup[0] in vowel_set) and (strong):
    print('perfect_join_sew anomaly 2:',root,isup,b,sup,strong)
    exit(1)
   # now we know sup[0] is a consonant
   elif strong:
    # since strong, and sup[0] is consonant, sup = Ta
    infl = b1[0:-1] + 'ay' + 'i' + sup
   else:
    # sup[0] is a consonant AND is a weak ending
    # Also, we are sew.  So i + i -> iyi 
    # Also assume I + i -> iyi
    if sup.startswith('s'):
     sup1 = 'i' + 'z' + sup[1:]
    else:
     sup1 = 'i' + sup
    infl = b1[0:-1] + 'iy' + sup1
  elif b1.endswith(('f','F')):
   if sup.startswith('s'):
    sup1 = 'i' + 'z' + sup[1:]
   else:
    sup1 = 'i' + sup
   infl = b1[0:-1] + 'ar' + sup1
  else:
   # b1 doesn't end with a vowel
   if sup.startswith('s'):
    infl = b1 + 'i' + 'z' + sup[1:]
   else:
    infl = b1 + 'i' + sup
  if dbg:
   print('sew: ',root,isup,b,sup,strong,b1,infl)
  infls.append(infl)
 return infls

def monosyllabic_a_base(root,isup,b,sup,strong,sc):
 """ Kale 500
 """
 if root == 'jan':
  # the rest of the logic would apply to the strong base 'jajan' of 'jan',
  # but 
  return b
 p,t = word_parts(root)
 if t != 'cvc': 
  return b
 # root is monosyllabic beginning with consonant
 if p[1] != 'a': 
  return b
 # middle vowel is 'a'
 if len(p[2]) != 1:  
  return b
 # root ends with a single consonant
 if len(p[0]) != 1:
  return b
 # root begins with a single consonant.  Note Kale 500 does NOT mention this.
 if b[0] != root[0]:
  return b
 # Now, root is of form xay, where x and y are simple consonants.
 # Check that 'b' is of form xaxay
 #  Note this rules out jan with the weak base jajY
 if ''.join([p[0],p[1],p[0],p[1],p[2]]) != b:
  return b
 # Replace the reduplicated base with xey  (replace penultimate 'a' with 'e')
 b1 = root[0] + 'e' + root[2]
 if not strong:
  return b1  #  use b1 before weak endings
 # strong ending. i.e., active voice, singular
 if isup != 3:
  return b
 # We know strong, active voice, 2nd person singular
 if sc == 'aniw':
  return b
 # We will use this provided this 'Ta' sup takes 'i' (i.e. sc = sew, vew)
 # This final test will be done by the perfect_join caller of this function
 return b1 
