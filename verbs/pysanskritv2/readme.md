
# pysanskritv2

This contains the current algorithms for generating conjugations.
The present computational framework considers a conjugation table
to be derived from a combination of a *base* form with a table of endings.

The generation is viewed as consisting of 4 steps, occurring in
subdirectories *inputs, models, bases, tables*.


## inputs: the roots
The roots based on MW are  in file `inputs/verb_cp.txt`.
This file is constructed by the script `inputs/redo.sh`.
Details of the construction are described in `inputs/readme.txt`.
Records of verb_cp.txt contain 3 colon-delimited fields:
* root
* Lrefs  Cologne ids for the root in MW-1899 dictionary
* class-voice list:   a comma-delimited list 

For example:
```
Buj:151217,151348:6a,6m,7a,7m
BU:151456:1a,1m
```

## models
The models, in file `models/calc_models.txt`,  are computed from
`inputs/verb_cp.txt` by script `models/redo.sh`. Some description is
in `models/readme.org`.  Essentially, the `calc_models.txt` file contains
a line for each combination of `root  + class,voice + tense`.  
* The tense is (currently) restricted to one of the four *special tenses* 
  (present, imperfect, imperative, optative). 
  * The other 6 conjugations and some aorist forms will be added later.
* the class,voice is either 
  * a class,voice appearing in `verb_cp.txt` for the root
  * _,p  for passive voice  (here class is irrelevant)

For example, Here are the `calc_models.txt` lines derived from the `BU:151456:1a,1m` 
entry in `verb_cp.txt`:
```
 1,a,pre	BU	151456
 1,a,ipf	BU	151456
 1,a,ipv	BU	151456
 1,a,opt	BU	151456
 1,m,pre	BU	151456
 1,m,ipf	BU	151456
 1,m,ipv	BU	151456
 1,m,opt	BU	151456
 _,p,pre	BU	151456
 _,p,ipf	BU	151456
 _,p,ipv	BU	151456
 _,p,opt	BU	151456

```

## bases
The conjugational bases are in file `bases/calc_bases.txt`, computed by script
`bases/redo.sh` from `calc_models.txt`.
Each model+root is considered to generate a base form (or occasionally
alternate base forms, or strong-weak base forms) 


## tables 
`tables/calc_tables.txt` contains conjugation tables generated
from `bases/calc_bases.txt`.  The `tables/redo.sh` script does the 
computation.
In general terms, the model specifies 
* the table of endings, and
* the method of  combination of the base with the endings

The result is the table of conjugational forms.


  