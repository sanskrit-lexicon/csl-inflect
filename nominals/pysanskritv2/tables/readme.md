# declension tables

Scripts and programs to generate inflection tables and check the results.

## decline_file program
```
python decline_file.py  INPUT OUTPUT
```

### input file format
The input file has three tab-delimited fields:
1) <model>   the model name1
2) key2  the word to inflect, with '-' to delimit padas
3) refs MW source records, specified as a colon-delimited sequence of 'L,key1' pairs

### output file format
The output file has four tab-delimited fields:
1) <model>  copied from input file
2) key2     copied from input file
3) refs     copied from input file
4) inflect  inflection table
   * For nominals, the inflection table format in the output file is
     a csv string with ':' delimiter, with 24 fields. These 28 fields are
     in the order of declension cases 1s,1d,1p,...8s,8d,8p  (8 = vocative).
    * Each of the 24 fields allows the possibility of multiple values, separated
      by '/' character.
  * For indeclineables,  the inflection table format has 1 value, the stem (without '-')

## calc_tables.txt
The table of all declensions is also computed by decline_file.py with input
../stems/calc_stems.txt
```
python3 decline_file.py ../stems/calc_stems.txt calc_tables.txt
```
This is what the `redo.sh` script does.

## decline_one.py
This is a command-line program based on decline_file.py;  the declension table
is printed in readable form.  For example:
```
python3 decline_one.py m_a rAma
# output is:
Declension of m_a rAma
Case 1:  rAmaH rAmO rAmAH
Case 2:  rAmam rAmO rAmAn
Case 3:  rAmeRa rAmAByAm rAmEH
Case 4:  rAmAya rAmAByAm rAmeByaH
Case 5:  rAmAt rAmAByAm rAmeByaH
Case 6:  rAmasya rAmayoH rAmARAm
Case 7:  rAme rAmayoH rAmezu
Case 8:  rAma rAmO rAmAH
```

The output can also be shown as a table in Github markdown:
```
python3 decline_one.py m_a rAma md
# output is
Declension of m_a rAma

|Case|S|D|P|
|-|-|-|-|
|Nominative|rAmaH|rAmO|rAmAH|
|Accusative|rAmam|rAmO|rAmAn|
|Instrumental|rAmeRa|rAmAByAm|rAmEH|
|Dative|rAmAya|rAmAByAm|rAmeByaH|
|Ablative|rAmAt|rAmAByAm|rAmeByaH|
|Genitive|rAmasya|rAmayoH|rAmARAm|
|Locative|rAme|rAmayoH|rAmezu|
|Vocative|rAma|rAmO|rAmAH|

```
The output is rendered as:

Declension of m_a rAma

|Case|S|D|P|
|-|-|-|-|
|Nominative|rAmaH|rAmO|rAmAH|
|Accusative|rAmam|rAmO|rAmAn|
|Instrumental|rAmeRa|rAmAByAm|rAmEH|
|Dative|rAmAya|rAmAByAm|rAmeByaH|
|Ablative|rAmAt|rAmAByAm|rAmeByaH|
|Genitive|rAmasya|rAmayoH|rAmARAm|
|Locative|rAme|rAmayoH|rAmezu|
|Vocative|rAma|rAmO|rAmAH|


## decline_checks.txt
This contain inflections (using decline_one.py) that have been checked
and agree with various published declensions.

