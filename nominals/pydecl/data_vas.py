""" data_vas.py
 12-05-2018
 data used in stem_model.py to identify reduplicated perfect participles
 Contains three fields:
 - the citation form (of last pada of key2) 
 - the associated feminine stem
 - the root (excluding prefixes)
"""
import re
data_vas_lines="""
vidvas viduzI vid
cakfvas cakruzI kf
papivas papuzI pA
prozivas prozuzI vas
biBIvas biByuzI BI
rarivas raruzI rA
saScivas saScuzI sac
Iyivas IyuzI i
udeyivas udeyuzI i
upeyivas upeyuzI i
pareyivas pareyuzI i
Kidvas KiduzI Kid
cikitvas cikituzI cit
jakzivas jakzuzI Gas
jaganvas jagmuzI gam
jagmivas jagmuzI gam
jaGanvas jaGnuzI han
jaGnivas jaGnuzI han
jajYivas jajYuzI jan
jUjuvas jUjuvuzI jU
SuSruvas SuSruvuzI Sru
tasTivas tasTuzI sTA
pIpivas pipyuzI pyE
SiSrivas SiSryuzI Sri
vavftvas vavftuzI vft
sAsahvas sAsahuzI sah
suzupvas suzupuzI svap
ninIvas ninyuzI nI
mIQvas mIQuzI mih
darSivas darSuzI dfS
"""
# darSuzI by analogy with jakzuzI and a few others above. No references found.
def data_vas_init():
 """ return dictionary. 
  Key is first field. 
  value is tuple (<fstem>,<root>)
 """
 lines = data_vas_lines.splitlines()
 d = {}
 for line in lines:
  line = line.rstrip('\r\n')
  parts = re.split(r' +',line)
  if len(parts) == 3:
   key,fstem,root = parts
   d[key] = (fstem,root)
 return d
