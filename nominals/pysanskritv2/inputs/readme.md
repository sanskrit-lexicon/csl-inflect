# inputs for nominals


## lexnorm-all2.txt

This is the main input for nominals and indeclineables.

Begin with a copy of [lexnorm-all2.txt](https://github.com/funderburkjim/MWlexnorm/blob/master/step2/lexnorm-all2.txt).

This is a csv format file (separator the tab character).
Fields:
* L = cologne record id for a record in Cologne digitization of Monier-Williams Sanskrit-English dictionary
* key1 = headword in citation form
* key2 = headword with compound-marking using '-'.
* lexnorm = inflection information in one of two forms:
  * 1: LEXID=X,STEM=Y[...]    for pronouns, cardinal numbers, etc.
  * 2: m:f#X:n   gender information, along with stem hints  


## removals from lexnorm-all2

Declensions for these records require special logic; also, the
identification of stem,models is simplified by this separation.
Thus, the two subgroups listed next are not presently in lexnorm-all2.txt.

## lexnorm-all2-part.txt
A list of headwords which should be declined as participles.
These have been removed from lexnorm-all2.txt.
This includes words already marked as LEXID=prap and LEXID=fap.
   How to generate the declensions and to identify the model?

### lexnorm-all2-inflectid.txt
   records marked with INFLECTID=...
   In these cases, the citation form in MW is a nominative dual or plural.
   How to generate the declensions and to identify the model?
   

## edit_lexnorm-all2.txt

These are the changes (shown as old/new pairs) made to the original
lexnorm-all2.txt.

## Currently unused files
These files are in the form of lexnorm-all2, but currently play no
role. 

## lexnorm-all2-pron.txt
90 records from lexnorm-all2.  There are 100 records in lexnorm-all2 with
LEXID=pron. Are the differences material?

## nominals currently without declension models
These are in these files
* stem_model_todo.txt (see ../stems): in lexnorm-all2, but stem_model.py can't handle
* lexnorm-all2-part.txt  present and other participles
* lexnorm-irregular.txt  3 cases
* lexnorm-all2-inflectid.txt 61 cases
* lexnorm-all2-pron.txt  . 90 cases. This file may be irrelevant;
   Not sure how it relates to the 100 cases of 'LEXID=pron' in lexnorm-all2.txt

note: eka appears as both a cardinal and an 'mfn' in lexnorm-all2.txt
   The lgtab1b data has both declensions.
   This needs examination.

 
## analysis directory
This contains some programs and result files for analyzing subcases.
Not of current interest.

## notes directory
This contains miscellaneous notes prepared to aid in the stem-model
classification.

## data_aYc.py and data_vas.py
These two python code files are used indirectly by stem_model.py,
namely by the imported 'decline' module.
