# stems for nominals

calc_stems.txt is the main input to the nominal inflections (in ../tables)
The notes below describes how calc_stems.txt is derived from  inputs/lexnorm-all2.txt
These `redo.sh` script carries out these steps.

## format of calc_stems.txt
csv file with 3 tab-delimited fields:
* model  A model name recognized by the declension algorithms in ../../pydecl/decline.py.  All the model names appear, for reference, in file calc_models.txt.
* stem  The stem to be used for declension.  The 'padas' are separated by '-' character. Examples:
  ```
  f_aYc_I	an-UcI	8730,anvaYc
  m_a	rAma	177264,rAma:177267,rAma
  f_A	rAmA	177264,rAma:177277,rAmA:177649,rAmA
  f_1_c	vAc	189809,vAc
  ```
* Lrefs The MW references, presented as pairs L,key1; Multiple references are
  separated by ':' character. 

## stems.py
```
python3 stems.py ../inputs/lexnorm-all2.txt calc_stems_0.txt calc_lexnorm_models.txt calc_models.txt calc_stems_todo.txt

```
stems.py also writes two 'log' files:
* calc_lexnorm_models.txt  provides some information relating the
  models as appearing in lexnorm-all2, and the functions of stems.py that
  end up handling them.  Hard to interpret!
* calc_models.txt  lists models, with counts, appearing in calc_stems_0.txt. currently 132 instances.
* calc_stems_todo.txt Lists cases where no model currently assigned (1062)


## remove duplicates
Two types of duplicates are removed.
* those where the model and (un-hyphenated) stems are the same:
  ```
  python3 remove_dups.py calc_stems_0.txt calc_stems_1.txt  calc_stems_dup.txt >  calc_stems_dup_log.txt
  ```
* feminines where the (un-hyphenated) stems are the same
  ```
  python3 remove_gdups.py calc_stems_1.txt calc_stems_2.txt  calc_stems_gdup.txt > calc_stems_gdup_log.txt
  ```

## stems_problems.txt
A comparison was made between the earlier elispsanskrit declension computations and the current rewrite of computations.
Differences were found in 2000+ cases.
These are in the stems_problem.txt file.

## calc_stems.txt

From calc_stems_2, we remove the cases from file stems_problem.txt 
```
python3 stem_model_diff.py calc_stems_2.txt stems_problem.txt calc_stems.txt
```

## nominals currently without declension models
These are in these files
* calc_stems_todo.txt : mentioned above 
* several cases mentioned in `inputs/readme.md`

## notes directory
This contains miscellaneous notes prepared to aid in the stem-model
classification.

