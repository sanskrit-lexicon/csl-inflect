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

* ../tables_aorist.txt
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

