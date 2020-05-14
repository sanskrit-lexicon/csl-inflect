manual/aor

* tables_aorist_deshpande.txt
  Digitized from Deshpande text 

* tables_aorist_huet.txt
python huet_table.py AP ../../../../huetdata/huet_conj_tables_aor.txt tables_aorist_huet.txt huet_table_aorist_log.txt

Construct in same format as tables_aorist_deshpande.txt.

Example:
Input:
akz aor 5A:[Akzizwa AkzizAtAm Akzizata AkzizWAH AkzizATAm AkziDvam Akzizi Akzizvahi Akzizmahi]
Output: 'aor 5A' -> '_,m,aor
Conjugation of _,m,aor akz
3p Akzizwa AkzizAtAm Akzizata
2p AkzizWAH AkzizATAm AkziDvam
1p Akzizi Akzizvahi Akzizmahi

NOTE 1:
Only for 'A' (middle voice) and 'P' (active voice).
(program excludes passive voice aorist forms)
NOTE 2:
Change 'ur' ending of 3rd person plural to 'uH'
NOTE 3:
combine multiple aorist forms for a given root into 1 table
NOTE 4:  mapping verb spellings to MW form
4 Huet spelling DyA -> MW spelling DyE
2 Huet spelling praS -> MW spelling praC
2 Huet spelling mUrC -> MW spelling murC
2 Huet spelling mlecC -> MW spelling mleC
2 Huet spelling vyA -> MW spelling vye
4 Huet spelling SA -> MW spelling Si
2 Huet spelling SU -> MW spelling Svi
2 Huet spelling sA -> MW spelling so
2 Huet spelling hU -> MW spelling hve

* ../tables_aorist.txt
output files are:
 ../tables_aorist.txt   (used elsewhere, such as inputs/redo.sh)
 merge_tables_aorist_log.txt  For analysis of differences
input files are:
 tables_aorist_huet.txt
 tables_aorist_deshpande.txt

python merge_tables.py ../tables_aorist.txt merge_tables_aorist_log.txt  tables_aorist_huet.txt tables_aorist_deshpande.txt

combine one or more tables.
Take into account duplication.
merge_tables_log.txt shows the merged tables, and identifies the
  differences in tables.

* tables_aorist_passive_deshpande.txt
  Digitized from Deshpande text 

* tables_aorist_passive_huet.txt

python huet_table.py Q ../../../../huetdata/huet_conj_tables_aor.txt tables_aorist_passive_huet.txt huet_table_aorist_passive_log.txt

* ../tables_aorist_passive.txt
python merge_tables.py ../tables_aorist_passive.txt merge_tables_aorist_passive_log.txt  tables_aorist_passive_huet.txt tables_aorist_passive_deshpande.txt



* note on merge_tables_aorist_log.txt (using 04-27-2020 data)
The file has 398 cases. 
Each case a merged conjugation table for a key (root  and aorist voice).
The cases are in Sanskrit alphabetical order.
The Sanskrit words are in SLP1 transcoding.

The file is designed to be useful for examination with Emacs, selecting
certain subsets with the 'occur' regexp filtering function.

166  'huet Single case'  (no Deshpande forms)
128  'deshpande Single case'  (no Huet forms)
104  'Double case' (forms present from both Huet and Deshpande).
  Each double case is characterized as
82  '(trivial difference' -- 
  for each person-number:
   each form of Deshpande is AMONG the forms of Huet; or vice-versa
22 '(non-trivial difference'
  for some person-number, the Huet and Deshpande forms differ.

* note on merge_tables_aorist_log.txt (using 05-09-2020 data)
The file has 401 cases. 
Each case a merged conjugation table for a key (root  and aorist voice).
The cases are in Sanskrit alphabetical order.
The Sanskrit words are in SLP1 transcoding.

The file is designed to be useful for examination with Emacs, selecting
certain subsets with the 'occur' regexp filtering function.

169  'huet Single case'  (no Deshpande forms)
125  'deshpande Single case'  (no Huet forms)
107  'Double case' (forms present from both Huet and Deshpande).
  Each double case is characterized as
107  '(trivial difference' -- 
  for each person-number:
   each form of Deshpande is AMONG the forms of Huet; or vice-versa
15 '(non-trivial difference'
  for some person-number, the Huet and Deshpande forms differ.

  
* comparison between 04-27-2020 data and 05-09-2020 data
based on merge_tables_aorist_log.txt
filter                 04-27     05-09
------------------     -----     -----
# of cases             398       401   case = root + aorist voice (a/m)
huet Single case       166       169   no Deshpande forms
deshpande Single case  128       125   no Huet forms
Double case            104       107   both Huet and Deshpande forms
  trivial difference    82        92   
  non-trivial diff.     22        15

based on merge_tables_aorist_passive_log.txt
Note: for some reason, the 04-27 file is not comparable.  
So these just show the current 05-09 counts for aorist passive
filter                 04-27     05-09
------------------     -----     -----
# of cases                       201   case = root + aorist voice (a/m)
huet Single case                   8   no Deshpande forms
deshpande Single case            164   no Huet forms
Double case                       29   both Huet and Deshpande forms
  trivial difference              28   
  non-trivial diff.               01   gam
