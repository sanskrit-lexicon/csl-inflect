manual/prf


NOTE : The perfect forms merge two sources:
  tables_prf_deshpande.txt
    - Deshpande text, Chapter 37, digitized by Funderburk
  tables_prf_huet.txt
    - Extracted from Gerard Huet's inflection data,
      See below

NOTE: Manually rerun the redo.sh script when either of the two sources is
 modified.  The top-level csl-inflect/redo.sh script then needs to be
 rerun to install the changes.

* tables_prf_deshpande.txt
  Digitized from Deshpande text 

* tables_prf_huet.txt
python huet_table.py AP ../../../../huetdata/mapextract/huet_conj_tables_prf.txt tables_prf_huet.txt huet_table_prf_log.txt

Construct in same format as tables_prf_deshpande.txt.

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

