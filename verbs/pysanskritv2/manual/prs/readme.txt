manual/prs

Source data from huet for present and passive tenses is
../../../../huetdata/mapextract/huet_conj_tables_prs.txt.

This is remapped to the current form.
There are also comparisons made to computations from pysanskritv2 code,
and for present tenses, some of these are additional to Huet's.
Currently, for passive tenses, only the results of Huet are used.

The end results are twofold:
1. file with names of form present_tabs_*.txt  are
concatenated and copied to ../tables_present.txt
2. tables_passive_huet.txt, which is copied to ../tables_present.txt
These two files are used for the final tables/calc_tables.txt.

notes_present_tabs.txt discusses differences between huet tables 
and the pysanskritv2 tables.

Now we present some notes on how the present_tabs_*.txt files and
the tables_passive_huet.txt file are created.

* tables_prs_huet.txt

# options:
  AP = present tenses, Atmanepada or Parasmaipada, classes 1 through 10
  AP11 = same, but class 11
  Q   = present tenses, Passive voice  (class is always '_')
python huet_table.py 0 AP ../../../../huetdata/mapextract/huet_conj_tables_prs.txt tables_prs_huet.txt 
python huet_table.py 1 AP ../../../../huetdata/mapextract/huet_conj_tables_prs.txt tables1_prs_huet.txt 
  The tables1 file is used by conjugate_one.py and conjugate_file.py,
  which are simply utilities for extracting the conjugations on demand.


The program changes the 'voice' parameter as follows:
  P -> a  (parasmaipada -> active voice)
  A -> m  (atmanepada -> middle voice)
  Q -> p  (pas -> passive voice)


* conjugate_one.py
  python conjugate_one.py 1,a,pre BU
Outputs conjugation table, if available, from tables1_prs_huet.txt

==================================================================
class pada comparisons.
python makecv.py  tables1_prs_huet.txt huet_prs_cv.txt

python compare_cv.py H,huet_prs_cv.txt G,../../inputs/verb_cp.txt compare_cv.txt

See 'old_compare' directory for some preliminary steps of comparing
present tense conjugations from Huet and previous csl-inflect.


-----------------------------------------------------------------
We are going to treat ALL the conjugations as manual.
We will use pysanskritv2 only as a check.  Perhaps it will be further
developed later.

Thus, the use of the 'stem' notion will be sidestepped for now.

-----------------------------------------------------------------
We will consider the conjugations in several categories, depending on
the source of the conjugation.
 notes_present.txt  has notes corresponding to comparisons between Huet and
  Algorithm/Deshpande

1. The many present tense (pre, ipf, ipv, opt) models which:
 -  are present in both Huet and the current system
 -  have conjugations which agree between Huet and the current system

 present_models_1.txt is this file. 2736 model-verb-tense combinations
Generate manual conjugation tables using Huet data for these
python conjugate_file.py present_models_1.txt present_tabs_1.txt
2733 conjugations
2. present tense conjugations (for classes 2,3,5,7,8,9) that are present
   only in Huet
  present_models_2.txt
python conjugate_file.py present_models_2.txt present_tabs_2.txt

3. present tense conjugations (for any class 1-10) that are present in 
both Algorithm (class 1,4,6,10) or Deshpande (2,3,5,7,8,9) but that differ
in some way.
 present_models_3.txt
 present_tabs_3.txt has the adjusted conjugations for present_models_3.txt.


4. present tense conjugations with class-voice unique to Huet.
python make_compare_tabs.py 1,H compare_cv.txt temp.sh
sh temp.sh > present_tabs_4.txt
580 tables.

5. present tense conjugations for roots with
  - some Huet present tense conjugations
  - root is Genuine in MW
  - some class-voice instances unique to MW
  - class is 1,4,6,10
python make_compare_tabs.py 2,G compare_cv.txt present_models_5.txt
cd ../../tables/
python conjugate_file.py ../manual/temp_huet_prs/present_models_5.txt ../manual/temp_huet_prs/present_tabs_5.txt
cd ../manual/temp_huet_prs/

For these, we want to use the conjugation tables currently in tables directory,
 which takes into account both pysanskritv2 algorithm (for classes 1,4,6,10)
 and Deshpande tables (for classes 2,3,5,7,8,9).
 There will be some missing.

Surprisingly, there are 44 models in present_models_5.txt 
for which present-tense conjugations have not been previously computed.
The file present_prebase_5a.txt was constructed for these cases, by
consultation with MW and MW72 dictionaries. 
Each line is of form:
 c,v root pre3s
Example:
1,a pruz prozati

From such lines, conjugate_file_base.py generates 
conjugation tables (for pre, ipf, ipv, and opt tenses).
It uses the tables/conjugate_from_bases.py program.
cd ../../tables
python conjugate_file_base.py ../manual/temp_huet_prs/present_prebase_5a.txt ../manual/temp_huet_prs/present_tabs_5a.txt

Note: conjugations from '1,a mlE mlAti' cannot be handled!

6,a,pre fc  fcati
1,m,pre kal kalate
10,a,pre kup kopayati
10,m,pre kF kArayate
1,m,pre kvaT kvaTate
10,a,pre kzap kzapayati
1,a,pre kzE kzAyati
10,m,pre gF gArayate
1,m,pre cal calate
1,m,pre cumb cumbate
10,a,pre cumb cumbayati  exemplar in MW72
; 10,m,pre cumb middle voice not mentioned in MW.
1,m,pre jap japate
1,m,pre jIv jIvate
1,a,pre tan tanati
; 1,m,pre tan  1,m not mentioned in MW
10,a,pre tan tAnayati
; 10,m,pre tan  10,m not mentioned in MW
4,m,pre tam tAmyate
1,m,pre tarj tarjate
1,a,pre tij tejati
;4,m,pre tfz  4,a not 4,m
10,a,pre tras trAsayati 
10,a,pre div devayati
10,m,pre div devayate
1,a,pre duh dohati
6,a,pre dfp dfpati dfmpati 
1,a,pre drA drAyati
1,m,pre drA drAyate
1,m,pre nu navate
1,a,pre pad padati 
4,m,pre pI pIyate
6,m,pre pf priyate 
10,a,pre praT prATayati parTayati
1,a,pre pruz prozati (mw72)
;10,a,pre bfh cl. 10 exemplar not found
10,a,pre BaYj BaYjayati
1,a,pre mid medati
1,a,pre miz mezati
1,a,pre mI mayati 
10,a,pre mI mAyayati
1,m,pre muc mocate
10,a,pre mud modayati
1,a,pre mlE mlAyati mlAti
10,a,pre raR raRayati
4,a,pre vas  vasyati
1,a,pre viS  veSati
1,a,pre Siz  Sezati
4,m,pre SI   SIyate
1,a,pre Sliz Slezati
4,a,pre sah sahyati
1,m,pre su  savate

Conjugations for these are computed from bases, using the
conjugate_one_base.py program.  This is done via script present_tabs_5a.sh:
sh present_tabs_5a.sh > present_tabs_5a.txt

There are also some cases where there are TWO conjugations found.
These are edited in present_tabs_5.txt (manually)
2 conjugations for 10,a,pre Cad  OK Cadayati/CAdayati
2 conjugations for 10,m,pre Cad  OK Cadayati/CAdayati
2 conjugations for 4,m,pre tras  Remove trasate, etc (class 1 forms)
2 conjugations for 10,a,pre paw  OK pawayati/pAwayati
2 conjugations for 10,m,pre paw  OK pawayate/pAwayate
2 conjugations for 10,a,pre puw  OK puwayati/powayati
2 conjugations for 10,a,pre vas  OK vasayati/vAsayati
2 conjugations for 1,m,pre sf    Remove DAvati forms

================================================================
copy all the present_tabs_*.txt to manual
cat present_tabs_*.txt > ../tables_present.txt

================================================================
passive voice
python huet_table.py 0 Q ../../../../huetdata/mapextract/huet_conj_tables_prs.txt tables_passive_huet.txt 
cp tables_passive_huet.txt  ../tables_passive.txt

------- rest is old comment

Example:
Input:
akz prf P:[Anakza Anakzatur Anakzur AnakziTa AnakzaTur Anakza Anakza Anakziva Anakzima]

Output:
Conjugation of _,a,prf akz
3p Anakza AnakzatuH AnakzuH
2p AnakziTa AnakzaTuH Anakza
1p Anakza Anakziva Anakzima


NOTE 1:
Only for 'A' (middle voice) and 'P' (active voice).
(For reduplicative perfect, passive voice is same as middle voice)
NOTE 2:
Change 'ur' ending of 3rd person plural to 'uH'
NOTE 3:  mapping verb spellings to MW form
  These counts are taken from csl-inflect/huetdata 
  sh redo.sh prf
1 Huet spelling DyA -> MW spelling DyE
2 Huet spelling praS -> MW spelling praC
1 Huet spelling mUrC -> MW spelling murC
1 Huet spelling mlecC -> MW spelling mleC
2 Huet spelling vyA -> MW spelling vye
2 Huet spelling SA -> MW spelling Si
1 Huet spelling SU -> MW spelling Svi
1 Huet spelling sA -> MW spelling so
1 Huet spelling sIv -> MW spelling siv
2 Huet spelling hU -> MW spelling hve

* ../tables_prf.txt
python merge_tables.py ../tables_prf.txt merge_tables_prf_log.txt  tables_prf_huet.txt tables_prf_deshpande.txt
output files are:
 ../tables_prf.txt   (used elsewhere, such as inputs/redo.sh)
 merge_tables_prf_log.txt  For analysis of differences
input files are:
 tables_prf_huet.txt
 tables_prf_deshpande.txt


combine one or more tables.
Take into account duplication.
merge_tables_prf_log.txt shows the merged tables, and identifies the
  differences in tables.


* see readme_merge_tables.txt

