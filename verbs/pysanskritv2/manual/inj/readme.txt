manual/ben

Source data from huet for several tenses are from
 directory ../../../../huetdata/mapextract/
future     huet_conj_tables_fut.txt
benedictive huet_conj_tables_ben.txt
conditional huet_conj_tables_cnd.txt
periphrastic_future huet_conj_tables_pef.txt  (pef -> pft)
injunctive  huet_conj_tables_inj.txt  aorist without augmentless

Currently,  only the results of Huet are used.
Later, we may include forms from Deshpande and or from local algorithms.

These files are converted to the 'manual' form, and then copied to the
parent directory for further use.

# benedictive
python huet_table.py 0 inj_exclude.txt ../../../../huetdata/mapextract/huet_conj_tables_inj.txt tables_inj_huet.txt 

cp tables_inj_huet.txt  ../tables_inj.txt

inj_exclude.txt contains roots which we exclude.

