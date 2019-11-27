""" conjugation_join_simple.py
 Uses a minimum amount of sandhi
"""
from sandhi_nR import sandhi_nR

def conjugation_join_simple(base,sup,dbg=False):
 """ get an inflected form by joining a base and an ending (sup)
   base and sup are strings.
   Often this is string concatenation, but sometimes sandhi rules apply
   and the result is not concatenation.
   This has most, but not all, of the functionality of conjugation_join in 
    elispsanskrit/pysanskritv1/conjugation_general_1cons.py
 """
 # concatenate base and sup
 ans = base+sup
 if dbg:
    print("conjugation_join_simple uses concatenation: (%s +%s => %s)" %(base,sup,ans))
 # nR sandhi
 nR_parm = len(base) - 1  
 ans1 = sandhi_nR(ans,nR_parm)
 if ans1 != None:
  ans = ans1
 return ans

if __name__ == "__main__":
 import sys
 base = sys.argv[1]
 sup = sys.argv[2]
 ans = conjugation_join_simple(base,sup,dbg=True)
