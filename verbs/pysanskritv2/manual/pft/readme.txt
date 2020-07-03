manual/pft

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

periphrastic future is 'pef' in Huet, 'pft' in Scharf.
python huet_table.py 0 pft_exclude.txt ../../../../huetdata/mapextract/huet_conj_tables_pef.txt tables_pft_huet.txt 

For some reason, the 'pada' in our extraction from Huet looks like '_P' for 
 periphrastic future.  We change this to 'a' (active voice)
cp tables_pft_huet.txt  ../tables_pft.txt

fut_exclude.txt contains roots which we exclude.
Currently, these are roots whose spelling ends in 'a' (denominative roots ?),
of which there are about 150; and another 50 or so (which are other denominative
roots).


