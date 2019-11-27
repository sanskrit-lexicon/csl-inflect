
# verbs
The script 'redo.sh' does all the computations necessary to rebuild
the conjugation tables. The result is in file
`pysanskritv2/tables/calc_tables.txt`.

## pysanskritv2
pysanskritv2 is the current version of conjugation algorithms.
  It directly 'mines' parts of the pysanskritv1/test2.py code to
  get 'bases' for conjugation algorithms, and then uses simplified
  algorithms to construct conjugation tables by combining bases with endings.
  see pysanskritv2/readme  

## pysanskritv1
pysanskritv1 is derived from https://github.com/funderburkjim/elispsanskrit.
  It contains just enough so that the 'test2.py' program works.
  This 'test2.py' program does conjugations, but is very complicated.
  It is used by programs in pysanskritv2.

## pysanskrit_work
pysanskrit_work is intended for a  rewrite of conjugation algorithms of 
  pysanskritv1/test2.py.
  IT IS INCOMPLETE and is not currently used elsewhere.
  Perhaps it may be continued at some future time.

