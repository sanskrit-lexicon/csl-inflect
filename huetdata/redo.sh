echo "retrieving huet aorist conjugations"
cp ../temp_2020_huetcompare/verbs-tp-aor/huet_conj_tables_aor.txt .
echo "mapping verb spellings to MW form"
python huet_mw_map.py huet_conj_tables_aor.txt
