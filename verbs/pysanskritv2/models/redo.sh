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
python3 root_model.py 4,prf ../inputs/verb_cp_deshpande_305.txt calc_models_prf.txt
python3 root_model.py 3,ben ../inputs/verb_cp_deshpande_330.txt calc_models_ben.txt
# 4 special tenses (active/middle) for class 2 roots
#python3 root_model.py 1,2 ../inputs/verb_cp.txt calc_models_1_2.txt
# Instead, use models from models_1_2.txt
cp models_1_2.txt calc_models_1_2.txt
#python3 root_model.py 1,3 ../inputs/verb_cp.txt calc_models_1_3.txt
# Instead, use models from models_1_2.txt
cp models_1_3.txt calc_models_1_3.txt
cat calc_models_*.txt > calc_models.txt
