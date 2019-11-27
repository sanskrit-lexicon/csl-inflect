
# pysanskritv2/analysis

Various utilities and analyses of the conjugations computed by pysanskritv2.

## conjugate_file_v2.py
python3 conjugate_file_v2.py INPUT OUTPUT
This uses the sl_conjtab function within test2.py to compute conjugations.
The INPUT file contains lines with 2 or 3 tab-delimited fields:
* model  class,voice,tense
* root
* refs   a reference string; optional. 

The output shows the model, root, and conjugation as a colon-delimited string. For example:
```
1,a,pre BU      Bavati:BavataH:Bavanti:Bavasi:BavaTaH:BavaTa:BavAmi:BavAvaH:BavAmaH
```

## conjugate_one_v2.py
This is a command-line program based on conjugate_file_v2.py;  the conjugation table
is printed in readable form.  For example:
```
python3 conjugate_one_v2.py 1,a,pre BU
# output is:
Conjugation of 1,a,pre BU
3p Bavati BavataH Bavanti
2p Bavasi BavaTaH BavaTa
1p BavAmi BavAvaH BavAmaH

```

The output can also be shown as a table in Github markdown:
```
python3 conjugate_one_v2.py 1,a,pre BU md
# output is
Conjugation of 1,a,pre BU

|Case|S|D|P|
|-|-|-|-|
|3p|Bavati|BavataH|Bavanti|
|2p|Bavasi|BavaTaH|BavaTa|
|1p|BavAmi|BavAvaH|BavAmaH|
```
The output is rendered as:

Conjugation of 1,a,pre BU

|Case|S|D|P|
|-|-|-|-|
|3p|Bavati|BavataH|Bavanti|
|2p|Bavasi|BavaTaH|BavaTa|
|1p|BavAmi|BavAvaH|BavAmaH|

## conj_compare_file.py
This program compares the pysanskritv1 and pysanskritv2 conjugations for
a file of root-models.


```
python3 conj_compare_file.py INPUT OUTPUT
```
The input file must contains on each line a model and root.
An example input file might be:
```
1,a,pre BU
1,m,pre laB
1,a,pre gam
```
This would generate the output file:
```
v1 == v2 for 1,a,pre BU	Bavati:BavataH:Bavanti:Bavasi:BavaTaH:BavaTa:BavAmi:BavAvaH:BavAmaH
v1 == v2 for 1,m,pre laB	laBate:laBete:laBante:laBase:laBeTe:laBaDve:laBe:laBAvahe:laBAmahe
v1 == v2 for 1,a,pre gam	gacCati:gacCataH:gacCanti:gacCasi:gacCaTaH:gacCaTa:gacCAmi:gacCAvaH:gacCAmaH&gamati:gamataH:gamanti:gamasi:gamaTaH:gamaTa:gamAmi:gamAvaH:gamAmaH
```

By using ../models/calc_models.txt as input, we get a test for all current
models.
```
python3 conj_compare_file.py ../models/calc_models.txt temp.txt
```
The program also reports that there are 60 differences out of 7336 examples.
The differences are in the output file temp.txt. The first difference is:
```
v1 != v2 for 1,a,ipf	iK	28635
v1: eKat:eKatAm:eKan:eKaH:eKatam:eKata:eKam:eKAva:eKAma
v2: EKat:EKatAm:EKan:EKaH:EKatam:EKata:EKam:EKAva:EKAma
```
In this case, the v2 version looks right for the imperfect.  
