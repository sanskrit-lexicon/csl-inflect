echo "construct tables_prs_huet.txt "
python huet_table.py 0 AP ../../../../huetdata/mapextract/huet_conj_tables_prs.txt tables_prs_huet.txt 
echo "construct tables1_prs_huet.txt "
python huet_table.py 1 AP ../../../../huetdata/mapextract/huet_conj_tables_prs.txt tables1_prs_huet.txt 
echo "construct huet_prs_cv.txt"
python makecv.py  tables1_prs_huet.txt huet_prs_cv.txt
echo "construct compare_cv.txt"
python compare_cv.py H,huet_prs_cv.txt G,../../inputs/verb_cp.txt compare_cv.txt

echo "construct tables_passive_huet.txt "
python huet_table.py 0 Q ../../../../huetdata/mapextract/huet_conj_tables_prs.txt tables_passive_huet.txt 
echo "construct tables1_passive_huet.txt "
python huet_table.py 1 Q ../../../../huetdata/mapextract/huet_conj_tables_prs.txt tables1_passive_huet.txt 
