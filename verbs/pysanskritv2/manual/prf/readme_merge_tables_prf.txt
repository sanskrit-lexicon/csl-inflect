These are notes on the comparison between Huet and Deshpande regarding
reduplicative perfect tense.

* root spelling changes
The Huet results have been subjected to some verb spelling changes, for
the purpose of matching, as in this Python dictionary (SLP1 transliteration).
Note especially klIba, dIv, dev.

huet_mw_map = {
 'in':'inv', #
 'Irz':'Irzy', #
 'utkaRW':'utkaRWa', #
 'und':'ud', #  MW/Huet ud or und
 'umB':'uB', #
 'uruz':'uruzya', #
 'knU':'knUY', # MW or knu
 'klIba':'klIb', #  Huet has both verb and noun forms in one entry!
 'kzI':'kzi', #
 'trA':'trE', #
 'dIv':'div', #
 'dfh':'dfMh', # 
 'dev':'div', # HU dIv = div,92229, dev = div,92228
 'DyA':'DyE', 
 'palAy':'pal', # 
 'puzp':'puzpya', #
 'pUla':'pUl', #
 'pyA':'pyE', #
 'praS':'praC', 
 'Bfjj':'Brajj', #
 'mUrC':'murC', 
 'mlA':'mlE', #
 'mlecC':'mleC', 
 'vyA':'vye', 
 'SA':'Si', 
 'SU':'Svi', 
 'SyA':'SyE', #
 'sA':'so', 
 'sIv':'siv',
 'styA':'styE', #
 'sPA':'sPAy', # 
 'hU':'hve',
}


* note on merge_tables_prf_log.txt (using 05-09-2020 huet data)
The file has 810 cases. 
Each case a merged conjugation table for a key (root and perfect voice).
The cases are in Sanskrit alphabetical order.
The Sanskrit words are in SLP1 transcoding.

The file is designed to be useful for examination with Emacs, selecting
certain subsets with the 'occur' regexp filtering function.

613  'huet Single case'  (no Deshpande forms)
 13  'deshpande Single case'  (no Huet forms)
184  'Double case' (forms present from both Huet and Deshpande).
  Each double case is characterized as
178 '(trivial difference' -- 
  for each person-number:
   each form of Deshpande is AMONG the forms of Huet; or vice-versa
 6 '(non-trivial difference'
  for some person-number, the Huet and Deshpande forms differ.

krI middle voice : cikrye (huet) v. cikriye (deshpande), etc.  
   There is evidence from other sources for cikriye
krI active voice: no direct evidence for Deshpande's cikriyatUh, cikriyuH, 
but likely by analogy with middle voice.

KAd active.  3p caKAduH (huet) + caKaduH (Deshpande).  
  No direct evidence
  I checked that Deshpande text shows short 'a' '..aduH' .  This looks
  suspicious, for example comparing 'rAj' where Deshpande 
  has rarAjatuH and rarAjuH.

jAgf active. 3s the same, but 
  3d jajAgratuH (H.) vs.  jajAgaratuH (D.), and similar for 3p.
  No direct evidence.

tF active.  3s the same. but
  3d tataratuH (H) vs. teratuH (D.) and similar for 3p.
  evidence in VCP, MW for teratuH. 

vas active. 3s the same, but
  3d UsatuH (H.) vs.  UzatuH (D.)
  Possible evidence for UsatuH in VCP (print quality is poor in VCP), 
  Evidence for UzuH in Whitney roots and Burnouf.

div active  3s the same. but
  3d didevatuH (H.) vs. didivatuH (D.) and
  3p didevuH (H.) vs. didivuH (D.)

 Note: H. has 2 verbs which he spells 'dIv' and 'dev'
 These are BOTH matched to MW verb 'div'.
 Deshpande has 'div' as the 4p (play) root, which would correspond to HU. 'dIv'

HU: #HU=√ दीव् dīv_1 v. [4] pr. (dīvyati) pr. r. (dīvyate) pft. (dideva) pp. (dyūta) jouer, s'amuser ; se moquer de <acc.> | parier, jouer pour le gain, mettre en jeu <g. dat. i.> | briller, resplendir | être joyeux ; être ivre — ca. (devayati) faire resplendir.
#HU=√ देव् dev v. [1] pr. (devati) ca. (devayati) pp. (dyūna) pf. (pari) [inusité sans pf.].

#MW={@div@},92228:1. cl. 1. P. {@-devati@} cl. 10. P. {@-devayati@}, to cause to lament, to pain, vex; to ask, beg; to go; Ā. {@°te@}, to suffer pain,
#MW={@div@},92229:2. cl. 4. {@dI/vyati@}, {@°te@}, ; (perf. {@dide/va@}, ; fut. {@devizyati@}; cond. {@adevizyat@}, ; aor. {@adevIt@}, ; inf. {@devitum@}, ; ind.p. {@devitvA@}, ; {@-dIvya@}, ) to cast, throw, esp. dice i.e. play, gamble ({@akzEs@}, ; {@akzAn@}, ), with (instr. ), for (instr., ; acc. ; dat. ; gen. [{@Satasya@}] ); to lay a wager, bet with ({@sArDam@}), upon (dat.), ; to play, sport, joke, trifle with (acc. ); to have free scope, spread, increase ( {@varDati@}); to shine, be bright [Zd. dīv; (?) Lit. {@dyvas@}] ; to praise, rejoice, be drunk or mad; to sleep; to wish for; to go, : Caus. {@devayati@}, to cause to play (Sch.) or to sport, : Desid. {@didevizati@} and {@dudyUzati@}, ; : Caus. of Desid. {@dudyUzayati@}, to incite to play, : Intens. {@dedivIti@}, {@dedyeti@}, {@dedeti@} ,
#MW={@dev@},95516:See √ 1. 2. {@div@}.

