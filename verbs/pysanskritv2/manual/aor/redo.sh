echo "reformat huet, making tables_aorist_huet.txt"
python huet_table.py AP ../../../../huetdata/huet_conj_tables_aor.txt tables_aorist_huet.txt huet_table_aorist_log.txt
echo "make ../tables_aorist.txt"
python merge_tables.py ../tables_aorist.txt merge_tables_aorist_log.txt  tables_aorist_huet.txt tables_aorist_deshpande.txt
echo "reformat huet, making tables_aorist_passive_huet.txt"
python huet_table.py Q ../../../../huetdata/huet_conj_tables_aor.txt tables_aorist_passive_huet.txt huet_table_aorist_passive_log.txt
echo "make ../tables_aorist_passive.txt"
python merge_tables.py ../tables_aorist_passive.txt merge_tables_aorist_passive_log.txt  tables_aorist_passive_huet.txt tables_aorist_passive_deshpande.txt
