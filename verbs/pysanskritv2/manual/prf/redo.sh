echo "reformat huet, making tables_prf_huet.txt"
python huet_table.py AP ../../../../huetdata/mapextract/huet_conj_tables_prf.txt tables_prf_huet.txt huet_table_prf_log.txt

echo "make ../tables_prf.txt"
python merge_tables.py ../tables_prf.txt merge_tables_prf_log.txt  tables_prf_huet.txt tables_prf_deshpande.txt
