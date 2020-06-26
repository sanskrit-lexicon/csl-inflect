echo "Begin verbs/pysanskritv2/models/redo.sh"
rm calc_models_*.txt
# 4 special tenses for classes 1,4,6,10 active and middle voices
python3 root_model.py 1 ../inputs/verb_cp.txt calc_models_1.txt
# passive of 4 special tenses for all classes
python3 root_model.py 2 ../inputs/verb_cp.txt calc_models_2.txt
python3 root_model.py 3,fut ../inputs/verb_cp.txt calc_models_fut.txt
python3 root_model.py 3,pft ../inputs/verb_cp.txt calc_models_pft.txt
python3 root_model.py 3,con ../inputs/verb_cp.txt calc_models_con.txt
python3 root_model.py 3,ben ../inputs/verb_cp_deshpande_330.txt calc_models_ben.txt
python3 root_model.py 4,ppf ../inputs/verb_cp_deshpande_305.txt calc_models_ppf.txt
# prf models revised 05-24-2020 see below
#python3 root_model.py 4,prf ../inputs/verb_cp_deshpande_305.txt calc_models_prf.txt
#python3 root_model.py 3,ben ../inputs/verb_cp_deshpande_330.txt calc_models_ben.txt
# 4 special tenses (active/middle) for class 2 roots
#python3 root_model.py 1,2 ../inputs/verb_cp.txt calc_models_1_2.txt
# Instead, use models from models_1_2.txt
cp models_1_2.txt calc_models_1_2.txt
#python3 root_model.py 1,3 ../inputs/verb_cp.txt calc_models_1_3.txt
# Instead, use models from models_1_3.txt
cp models_1_3.txt calc_models_1_3.txt
#python3 root_model.py 1,5 ../inputs/verb_cp.txt calc_models_1_5.txt
# Instead, use models from models_1_5.txt
cp models_1_5.txt calc_models_1_5.txt
#python3 root_model.py 1,7 ../inputs/verb_cp.txt calc_models_1_7.txt
# Instead, use models from models_1_7.txt
cp models_1_7.txt calc_models_1_7.txt
#python3 root_model.py 1,8 ../inputs/verb_cp.txt models_1_8.txt
# Instead, use models from models_1_8.txt
cp models_1_8.txt calc_models_1_8.txt
#python3 root_model.py 1,9 ../inputs/verb_cp.txt models_1_9.txt
# Instead, use models from models_1_9.txt 
cp models_1_9.txt calc_models_1_9.txt
# Use models from models_aorist.txt 
# cp models_aorist.txt calc_models_aorist.txt
# cp models_aorist_passive.txt calc_models_aorist_passive.txt
# revised 4-23-2020
python3 root_model.py 5,aor ../inputs/verb_cp_aorist.txt ../manual/tables_aorist.txt calc_models_aorist.txt
python3 root_model.py 5,aor ../inputs/verb_cp_aorist_passive.txt ../manual/tables_aorist_passive.txt calc_models_aorist_passive.txt
# prf. Use manual
python3 root_model.py 5,prf ../inputs/verb_cp_prf.txt ../manual/tables_prf.txt calc_models_prf.txt

cat calc_models_*.txt > calc_models.txt
