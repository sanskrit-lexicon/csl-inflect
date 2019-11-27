""" data_aYc.py
 12-18-2018
 data used in stem_model.py to identify adjectives of direction
 Contains fields:
 - the citation form (of last pada of key2 - as in lexnorm-all2
 - the associated feminine stem
 
"""
import re
data_aYc_lines="""
yaYc IcI
vaYc UcI
tiryaYc tiraScI
daYc dIcI
AYc AcI
gavAYc gocI
prAYc prAcI
uruvyaYc urUcI
"""
def data_aYc_init():
 """ return dictionary. 
  Key is first field. 
  value is tuple (<fstem>,)
 """
 lines = data_aYc_lines.splitlines()
 d = {}
 for line in lines:
  line = line.rstrip('\r\n')
  parts = re.split(r' +',line)
  if len(parts) == 2:
   key,fstem = parts
   d[key] = (fstem,)
 return d
