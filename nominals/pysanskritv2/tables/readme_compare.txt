Comparing Cologne declensions and Huet declensions

## decline_one.py
 One declension using Cologne algorithms
```
python decline_one.py MODEL KEY
WHERE
 MODEL is one of the COLOGNE models; these are listed in
 ../stems/calc_models.txt
 KEY is slp1 spelling of the noun to be declined.
```
 
## decline_one_huet.py
Retrieve and display one declension table using Huet's published inflection data.

 Requires:
* download of Huet data. [reference](https://github.com/sanskrit-lexicon/csl-inflect/tree/master/huetdata/download)
* initialization of nominal extractions from downloaded Huet data.
  [reference](https://github.com/sanskrit-lexicon/csl-inflect/tree/master/huetdata/nominals).

```
python decline_one.py MODEL KEY
WHERE MODEL and KEY are as above
```

## compare_cologne_huet_file.py
python compare_cologne_huet_file.py temp_compare_huet/huet_j.txt temp_compare_huet/huet_j_comp.txt

The format of input file (in this case huet_j.txt) is
rAj:f,m,n
aDi-rAj:f,m,n
...

huet_j.txt are the headwords ending in j from Huet's declensions.


## compare_cologne_huet_one.py
This compares just one declension. Usage is
```
python compare_cologne_huet_one.py MODEL KEY
```
