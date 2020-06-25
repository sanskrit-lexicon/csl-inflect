# tables

## conjugate_from_bases
python3 conjugate_from_bases.py ../bases/calc_bases.txt calc_tables.txt

## conjugate_one
This program allows one to retrieve conjugation tables from calc_tables.txt
and to print these tables in an easily readable form.

`python conjugate_one.py 1,a,pre  BU`

Conjugation of 1,a,pre BU
3p Bavati BavataH Bavanti
2p Bavasi BavaTaH BavaTa
1p BavAmi BavAvaH BavAmaH

## markdown table output
`python conjugate_one.py 1,a,pre  BU md`
Generates a markdown table

Conjugation of _,a,aor BU

|Case|S|D|P|
|-|-|-|-|
|3p|aBUt|aBUtAm|aBUvan|
|2p|aBUH|aBUtam|aBUta|
|1p|aBUvam|aBUva|aBUma|

It is necessary to know the model for a given root.
e.g., '1,a,pre' means class 1, active voice (parasmaipada), present tense.
The root spellings use SLP1 transliteration, and generally agree with the
spellings of MW (Monier-Williams) dictionary.

### Unknown models
`python conjugate_one.py 1,a,present  BU`
yields `conjugation table unknown for 1,a,present BU` .

### classes
1 through 10.  The given class must be known for the root.  This is applicable
for the conjugational tenses.

Use '_' for non-conjugational tenses (e.g. perfect).

### voices
|abbreviation|voice|*pada*|
|----|----|----|
|a|active voice|parasmaipada|
|m|middle voice|atmanepada|
|p|passive voice|---|

### conjugational tenses
|abbreviation|tense|Sanskrit tense (SLP1)|
|----|----|---|
|pre|present|law|
|ipf|imperfect|laN|
|ipv|imperative|low|
|opt|optative|viDiliN|

### non-conjugational tenses
|abbreviation|tense|Sanskrit tense (SLP1)|
|----|----|---|
|ppf|periphrastic perfect|liw-p|
|prf|reduplicative perfect|liw-r|
|fut|simple future|lfw|
|con|conditional|lfN|
|pft|periphrastic future|luw|
|ben|benedictive|ASIrliN|
|aor|aorist|luN|
