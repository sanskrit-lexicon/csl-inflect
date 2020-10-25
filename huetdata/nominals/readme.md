# huetdata/nominals

This is similar to the 'extract' directory, which is geared to verbs.
Here, we want to extract declension information from Huet's data,
and reformat the data.

We make use of similar code from the [elispsanskrit](https://github.com/funderburkjim/elispsanskrit/) repository, in the *huetcompare* folder.

```
python nouns.py ../download/SL_morph.xml huet_noun_stems_genders.txt huet_noun_tables.txt > nouns_log.txt
```
