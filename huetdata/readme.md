## huetdata

This directory contains documents closely derived from the published 
inflection data provided by [Gerard Huet](https://sanskrit.inria.fr/DATA/XML/).


The file `huet_conj_tables_aor.txt` is copied from
https://github.com/funderburkjim/elispsanskrit/blob/master/huetcompare/verbs-tp-aor/huet_conj_tables_aor.txt.
This is a previous version. For the latest version, see below


This csl-inflect repository integrates Huet's aorist forms, thereby greatly
extending the number of such aorist forms previously gleaned from 
Professor Deshpande's book.

## redo.sh
* retrieve huet_conj_tables_aor.txt from a temporary local location
  * current location ../temp_20200427_huetverbs-tp-aor/
* map a few Huet root spellings to MW
python huet_mw_map.py huet_conj_tables_aor.txt

The result is now used in ../verbs/pysanskritv2/manual/aor
