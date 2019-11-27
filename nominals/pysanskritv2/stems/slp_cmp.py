# -*- coding: utf-8 -*-
"""slp_cmp
   comparison function for sorting Sanskrit words coded as slp into
   Sanskrit alphabetical order.
   12-11-2018.  Requires Python3 for 'str' module. 
   Python2 uses 'string' instead
"""


# import str
# Note 'L' and '|' and 'Z' and 'V' are not present
# Not sure where they go 
tranfrom="aAiIuUfFxXeEoOMHkKgGNcCjJYwWqLQ|RtTdDnpPbBmyrlvSzsh"
tranto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy"
import sys
info = sys.version_info
if sys.version_info[0] == 2:
 import string
 trantable = string.maketrans(tranfrom,tranto)
else:
 trantable = str.maketrans(tranfrom,tranto)

def slp_cmp(a,b):
 a = str(a)  # required since a,b are unicode, not acceptable to translate
 b = str(b)
 try:
  a1 = str.translate(a,trantable)
  b1 = str.translate(b,trantable)
 except Exception as e:
  print("slp_cmp error: a='%s',b='%s'" %(a,b))
  print("Error=",e)
  exit(1)
 return cmp(a1,b1)

def slp_cmp_key(a):
 try:
  return str.translate(str(a),trantable)
 except Exception as e:
  print('slp_cmp_key ERROR',e)
  print('a=',a)
  exit(1)

