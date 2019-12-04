echo "Begin verbs/pysanskritv2/models/redo.sh"
rm calc_models_*.txt
python3 root_model.py 1 ../inputs/verb_cp.txt calc_models_1.txt
python3 root_model.py 2 ../inputs/verb_cp.txt calc_models_2.txt
python3 root_model.py 3,fut ../inputs/verb_cp.txt calc_models_fut.txt
python3 root_model.py 3,pft ../inputs/verb_cp.txt calc_models_pft.txt
python3 root_model.py 3,con ../inputs/verb_cp.txt calc_models_con.txt
python3 root_model.py 3,ben ../inputs/verb_cp_deshpande_330.txt calc_models_ben.txt
cat calc_models_*.txt > calc_models.txt
