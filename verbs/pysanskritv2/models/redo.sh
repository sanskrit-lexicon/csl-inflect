echo "Begin verbs/pysanskritv2/models/redo.sh"
rm calc_models_*.txt
python3 root_model.py 1 ../inputs/verb_cp.txt calc_models_1.txt
python3 root_model.py 2 ../inputs/verb_cp.txt calc_models_2.txt
python3 root_model.py 3,fut ../inputs/verb_cp.txt calc_models_fut.txt
python3 root_model.py 3,pft ../inputs/verb_cp.txt calc_models_pft.txt
python3 root_model.py 3,con ../inputs/verb_cp.txt calc_models_con.txt
python3 root_model.py 3,ben ../inputs/verb_cp_deshpande_330.txt calc_models_ben.txt
python3 root_model.py 4,ppf ../inputs/verb_cp_deshpande_305.txt calc_models_ppf.txt
python3 root_model.py 4,prf ../inputs/verb_cp_deshpande_305.txt calc_models_prf.txt
cat calc_models_*.txt > calc_models.txt
