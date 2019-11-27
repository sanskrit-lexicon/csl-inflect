# csl-inflect/sqlite

Scripts to construct various sqlite database files related to inflections.

redo.sh script recreates all the sqlite files.
The resulting sqlite files are in subdirectory 'db'.
The construction inputs for each sqlite file are in separate subdirectories.
Briefly, the sqlite files are:
* lgmodel.sqlite - links from the model codes to Kale Higher Sanskrit Grammar
  * model  the model code
  * descr  description of model
  * ref    reference to page in Kale, in form 'Kale N'
* lgtab1.sqlite - nominals/pysanskritv2/tables/calc_tables.txt
  Declension tables.
  NOTE: We (probably) assume that model-stem duplicates are removed.
  * model 
  * stem
  * refs  - MW sources
  * data  - inflection table (1 item for model='ind', 24 items for other models)
* lgtab2.sqlite 
  * key -- a declined form (one of the 24); or an indeclineable form
           i.e. one of the items appearing in the 'data' portion of lgtab1.
  * model  same as in lgtab1
  * stem   same as in lgtab1
* vlgtab1.sqlite - verbs/pysanskritv2/tables/calc_tables.txt
  Conjugation tables
  NOTE: We (probably) assume that model-stem duplicates are removed.
  * model 
  * stem
  * refs  - MW sources
  * data  - inflection table (9 items)
* vlgtab2.sqlite 
  * key -- a conjugated form (one of the 9); 
           i.e. one of the items appearing in the 'data' portion of vlgtab1.
  * model  same as in vlgtab1
  * stem   same as in vlgtab1
