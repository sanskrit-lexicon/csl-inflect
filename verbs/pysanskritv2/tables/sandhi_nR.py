"""sandhi_nR.py
  Sandhi rule for for changing 'n' to 'R'.
  Separated out from sandhi.py for pedagogical 
"""
#import init
## only the constants vowel_set, guttural_set, and labial_set are used from 
## init.py
def sandhi_nR(xin,nR_parm=None):
 """ 
  xin is a Sanskrit word spelled with slp1 transliteration
  Antoine 17
  When, in the same word, 'n' is preceded by 'f', 'F', 'r', or 'z' and
  followed by a vowel or by 'n', 'm', 'y', or 'v', then it is changed to
  'R' even when there are letters between the preceding 'f' (etc) and 'n'
  provided these intervening letters be vowel, gutturals, labials, 
  'y', 'v', h', or 'M' (anusvAra).
  Returns None if no change
  If the rule applies and there is a change in spelling, the changed
  spelling is returned.
 """
 vowel_set = 'aiufxAIUFXeEoO'
 #guttural_set = 'kKgGNhH'
 #labial_set = 'pPbBmvH'
 guttural_set = 'kKgGN'
 labial_set = 'pPbBm'
 ifirst = nR_parm
 if not ifirst:
  ifirst = 0
 changed = False
 tokar = xin
 n = len(tokar)
 i = 0
 while ( i < n):
  x1 = tokar[i]
  i = i+1
  if x1 in 'fFrz':
   i1 = i
   i2 = None
   ok = False
   while (i < n):
    x2 = tokar[i]
    i = i+1
    if  (x2 == 'n') and (i < n):
     x3 = tokar[i]
     if (x3 in vowel_set) or (x3 in 'nmyv'):
      i = i - 1
      i2 = i
      i = n # break inner while loop
   i = i1
   if i2:
    # found a subsequent "n". Now check intervening letters
    ok = True
    while ok and (i < i2):
     y = tokar[i]
     #if (y in vowel_set) or (y in guttural_set) or (y in labial_set) or (y in 'yvhM'):
     # current version
     # See https://github.com/sanskrit-lexicon/MWinflect/issues/5#issuecomment-431489929
     if (y in vowel_set) or (y in guttural_set) or (y in labial_set) or (y in 'yvhM'):  
     # test version - remove MH
     #if (y in vowel_set) or (y in guttural_set) or (y in labial_set) or (y in 'yvh'): 
      i = i + 1
     else:
      ok = False # breaks while loop
    if ok:
     if (ifirst <= i2):
      # make the change
      changed = True
      # recall tokar is a string so next does not work in Python
      #tokar[i2] = 'R'
      # rather:
      tokar = tokar[:i2]+'R'+tokar[i2+1:]
      i = i2 + 1
 if changed:
  return tokar
 else:
  return None
