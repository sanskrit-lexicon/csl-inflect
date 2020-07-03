manual/fut

Source data from huet for several tenses are from
 directory ../../../../huetdata/mapextract/
future     huet_conj_tables_fut.txt
benedictive huet_conj_tables_ben.txt
conditional huet_conj_tables_cnd.txt
periphrastic_future huet_conj_tables_pef.txt  (pef -> pft)
injunctive  huet_conj_tables_inj.txt  NOT DONE yet.

Currently,  only the results of Huet are used.
Later, we may include forms from Deshpande and or from local algorithms.

These files are converted to the 'manual' form, and then copied to the
parent directory for further use.


python huet_table.py 0 fut_exclude.txt ../../../../huetdata/mapextract/huet_conj_tables_fut.txt tables_fut_huet.txt 

cp tables_fut_huet.txt  ../tables_fut.txt

fut_exclude.txt contains roots which we exclude.
Currently, these are roots whose spelling ends in 'a' (denominative roots ?),
of which there are about 150; and another 50 or so (which are other denominative
roots).


