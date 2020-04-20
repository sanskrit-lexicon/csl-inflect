
dcpforms-MW-verb.txt   from Github repository:
   elispsanskrit/grammar/prod/inputs
   sample:
(ac 1 P <MW=ac,2319,1>)
(ac 1 A <MW=ac,2319,1>)

verb_cp_orig.txt  from Github repository
   MWvlex/step1/verb_cp.txt
   sample:
   ac:1767:1P,1A

================================================================
mw_genuine_roots.txt
ref: https://github.com/sanskrit-lexicon/MWS/blob/master/mw_genuine_roots.txt

Changed one L-number, for  a root in the supplement.
old 324500  uB              1
new 37051.1  uB              1
Added one item: 55571 kxp	
================================================================
verb_cp_orig_1.txt
python3 genuine_filter.py verb_cp_orig.txt mw_genuine_roots.txt verb_cp_orig_1.txt
The non-genuine roots are commented out  (';not-genuine ')
There are 1403 non-genuine roots, out of 2151.  Thus, there remain
748 genuine roots in verb_cp_orig_1.txt

================================================================

There are some issues:
-  some records have duplicates in the class-pada field
   e.g. iz:29439:1P,1A,4P,4P,4A
   This should be:
   iz:29439:1P,1A,4P,4A
-  Sometimes the 'class' number is '0', as in 
   iraD:29347:0A,0P or
   I:29694:0
   These should be removed from the main file (verb_cp_0.txt)
-  Sometimes two records have the same root, due to different 'L' codes.
   Not sure whether to merge these or not, but think so
   These can be merged by having L field to be allow multiple entries,
     comma separated
   Example:
     uC:30535:1P
     uC:30536:1P
   new: uC:30535,30536:1P
-  Some have just a class, with no A or P.  Assume this means A or P
   Example: uYC:30615:1,6P
     expand to uYC:30615:1P,1A,6P

python clean.py  verb_cp_orig_1.txt verb_cp.txt
  The new file has commented lines, starting with ';'
There are 748 lines in verb_cp.txt.
Of these, 65 are commented out:
 24 have no class information ('#zero')
 41 have duplicate root information, which is merged into other elements.
This leave 682 distinctly spelled roots in verb_cp.txt.

For comparison to Dhaval:  ../dhaval/roots/
================================================================
root_model 

# tense = pre, ipf, ipv, pot
# class = 1,4,6,10
# voice = a,m
python3 root_model.py 1 verb_cp.txt root_model.txt
================================================================
verb_cp_deshpande_330.txt
This has 191 roots from the table in Deshpande, p. 330-335 of future,
 conditional, and benedictive.
The benedictive conjugations are restricted to this list (see models/redo.sh).
================================================================
python verb_cp_huet_aor.py verb_cp.txt ../../../huetdata/huet_conj_tables_aor.txt verb_cp_huet_aor.txt

This shows the distinct MW roots which have aorist data from Huet's work.
The resulting list (verb_cp_huet_aor.txt) is probably not used elsewhere.
132 distinct roots are identified.

Two wrinkles:
1) for 9 roots, we believe that the Huet root spelling differs from that of MW:
; Huet spelling DyA -> MW spelling DyE
; Huet spelling praS -> MW spelling praC
; Huet spelling mUrC -> MW spelling murC
; Huet spelling mlecC -> MW spelling mleC
; Huet spelling vyA -> MW spelling vye
; Huet spelling SA -> MW spelling Si
; Huet spelling SU -> MW spelling Svi
; Huet spelling sA -> MW spelling so
; Huet spelling hU -> MW spelling hve


2) For 12 of the Huet aorist roots, the root is not in verb_cp.txt (i.e.,
   the root is not characterized as 'genuine' by MW.)  
am:13748:
KyA:62110:2a,2m
gup:65898,65890,65959:4a,4m,6a,6m
cur:74646:10a,10m,1a,1m
cezw:74971:1a,1m
jalp:78292:1m
tvar:89087:1a,1m
tviz:89141:1a,1m
das:91129:1a,1m,4m
dfS:95263:
vaD:185579:
spaS:256550:

