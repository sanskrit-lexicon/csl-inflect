
verb_cp_orig.txt  from Github repository
   MWvlex/step1/verb_cp.txt
   sample:
   ac:1767:1P,1A

There are 2150 lines in verb_cp_orig.txt

Manual revisions to verb_cp_orig.txt
- aS  
 old : ;aS:19412:0A,0P,0A,0A,0A
       ;aS:19416:0
 new : aS:19412:5A
       aS:19416:9P
- am 
 old : am:13748:0A
 new : am:13748:1P
- Urj
 old : Urj:38037:0P,0A
 new : Urj:38037:10P,10A
- luRW
 old : luRW:182935:0
 new : luRW:182935:1P
- vIq
 old : vIq:203469:0P,0A
 new : vIq:203469:10P,10A   mw has causal only
- Cand
 old : NOT PRESENT
 new : Cand:75687:1A

verb_cp_orig_clean.txt
 Change from pada to voice
 remove duplicates
 comment out 0's    259 lines commented out with #zero 
 merge duplicates   156 lines commented out with #dup
python clean.py verb_cp_orig.txt verb_cp_orig_clean.txt
There are also 2150 lines in verb_cp_orig_clean.txt.
After removing the commented out lines, there are 1735 lines remaining.

================================================================
mw_genuine_roots.txt
ref: https://github.com/sanskrit-lexicon/MWS/blob/master/mw_genuine_roots.txt
There are 748 non-comment lines in mw_genuine_roots.txt.
Note that some roots appear twice, such as 'hf', 'hA'.

Changed one L-number, for  a root in the supplement.
old 324500  uB              1
new 37051.1  uB              1
Added one item: 55571 kxp	
================================================================
python3 genuine_filter.py verb_cp_orig_clean.txt mw_genuine_roots.txt verb_cp_orig_1_clean.txt

verb_cp_orig_1_clean.txt has 1735 lines, but 1052 of the lines are
commented out as 'not-genuine'.
This leaves 684 'genuine' roots.  This should be compared to the 748
roots of mw_genuine_roots.  The reason for the smaller number (684) is
due to the presence of duplicate root spellings in mw_genuine_roots,
while duplicate spellings have been merged in verb_cp_orig_1_clean.txt.

================================================================
verb_cp.txt
For compatibility with previous code,  we rename :
mv verb_cp_orig_1_clean.txt verb_cp.txt
Note that redo.sh script is a slight variant:
python3 genuine_filter.py verb_cp_orig_clean.txt mw_genuine_roots.txt verb_cp.txt

================================================================
verb_cp_extra.txt
This contains some non-genuine roots (i.e. lines commented out in verb_cp.txt)
for which we want to have some inflections.
This file is developed 'manually'.

================================================================
verb_cp_aorist.txt
inputs for manual aorist forms
python3 verb_cp_manual.py verb_cp.txt verb_cp_extra.txt ../manual/tables_aorist.txt verb_cp_aorist.txt
================================================================
verb_cp_aorist_passive.txt
inputs for manual aorist (passive voice)
python3 verb_cp_manual.py verb_cp.txt verb_cp_extra.txt ../manual/tables_aorist_passive.txt verb_cp_aorist_passive.txt

================================================================
verb_cp_prf.txt
inputs for manual perfect tense
python3 verb_cp_manual.py verb_cp.txt verb_cp_extra.txt ../manual/tables_prf.txt verb_cp_prf.txt
================================================================
verb_cp_deshpande_330.txt
This has 191 roots from the table in Deshpande, p. 330-335 of future,
 conditional, and benedictive.
The benedictive conjugations are restricted to this list (see models/redo.sh).

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


================================================================
