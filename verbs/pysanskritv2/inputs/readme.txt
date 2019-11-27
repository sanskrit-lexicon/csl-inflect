
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
