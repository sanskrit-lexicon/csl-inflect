""" sandhi.py
"""
#------------------------------------------------------------------------
# sets are represented as strings of Sanskrit letters in SLP1 transliteration
# set names use '_' in place of the '-' of the Elisp variable names
# 
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
#------------------------------------------------------------------------
# semivowels associated to vowel
semivowel_of_vowel = {'i':'y', 'I':'y',
                      'u':'v', 'U':'v',
                      'f':'r', 'F':'r',
                      'x':'l', 'X':'l'}
