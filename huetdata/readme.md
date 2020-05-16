## huetdata

This directory contains documents closely derived from the published 
inflection data provided by [Gerard Huet](https://sanskrit.inria.fr/DATA/XML/).


This csl-inflect repository integrates Huet's aorist forms, thereby greatly
extending the number of such aorist forms previously gleaned from 
Professor Deshpande's book.

## sh redo.sh aor
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

    