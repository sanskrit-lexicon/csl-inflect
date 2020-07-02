## huetdata

This directory contains documents closely derived from the published 
inflection data provided by [Gerard Huet](https://sanskrit.inria.fr/DATA/XML/).


This csl-inflect repository integrates Huet's aorist forms, thereby greatly
extending the number of such aorist forms previously gleaned from 
Professor Deshpande's book.

## sh redo_one.sh aor
This script needs to be rerun when Huet's database is recomputed,
at the end of a month.

* extract aorist tense paradigms from SL_morph.xml, and
* construct 
  * extract/huet_conj_tables_aor.txt 
  * extract/huet_stems_aor.txt  [currently not further used]
* construct mapextract/huet_conj_tables_aor.txt 
  * this changes some of Huet's root spellings to what is
    believed to be the best corresponding MW root spelling.
  * mapextract/huet_conj_tables_aor.txt is used in
    csl-inflect/verbs/pysanskritv2/manual/aor

## format of the conjugation tables for 'aor' tense paradigm

Sample line:
```
kfz aor 4P:[akArkzIt/akrAkzIt akArzwAm/akrAzwAm akArkzur/akrAkzur akArkzIH/akrAkzIH akArzwam/akrAzwam akArzwa/akrAzwa akArkzam/akrAkzam akArkzva/akrAkzva akArkzma/akrAkzma]
```

Each line has two fields, separated by a colon:
* the table identifiers:
  * root
  * tense
  * for 'aor' (aorist) tense:
    * aorist type  (digit 1 to 7)
    * pada
      * P = parasmaipada
      * A = atmanepada
      * Q = passive
* the conjugation table, in the form '[...]', where
  * there are 9 space-separated fields, representing, in order,
    3s (3rd person singular), 3d (3rd person dual), 3p (3rd person plural),
    2s (2nd person singular), 2d (2nd person dual), 2p (2nd person plural),
    1s (1st person singular), 1d (1st person dual), 1p (1st person plural)
  * for fields with multiple forms, the forms are separated by '/'

## sh redo_one.sh prf
This script extracts the perfect tense forms from Huet's corpus of forms.

## sh redo_one.sh prs
This script extracts the present tense forms from Huet's corpus of forms.
This includes present, imperfect, imperative, and optative tenses,
for any conjugation class, and for any voice (A/P/Q = passive)

## sh redo_one.sh fut
This script extracts the simple future tense forms from Huet's corpus of forms,
 for Atmanepada and Parasmaipada.

## sh redo_one.sh pef
This script extracts the periphrastic future tense forms from Huet's corpus of 
forms; only Parasmaipada are found.

## sh redo_one.sh cnd
This script extracts the conditional tense forms from Huet's corpus,
 for Atmanepada and Parasmaipada.  (only a few)

## sh redo_one.sh ben
This script extracts the benedictive tense forms from Huet's corpus,
 for Atmanepada and Parasmaipada.

## sh redo_one.sh inj
This script extracts the injunctive tense forms from Huet's corpus,
 for Atmanepada and Parasmaipada. (only a few)
'injunctive' == 'aorist without augment'

