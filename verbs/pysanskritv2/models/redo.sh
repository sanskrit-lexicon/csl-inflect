echo "Begin verbs/pysanskritv2/models/redo.sh"
rm calc_models_*.txt
#python3 root_model.py 1 ../inputs/verb_cp.txt calc_models_1.txt
#python3 root_model.py 2 ../inputs/verb_cp.txt calc_models_2.txt
#python3 root_model.py 3,fut ../inputs/verb_cp.txt calc_models_fut.txt
python3 root_model.py 3,pft ../inputs/verb_cp.txt calc_models_pft.txt
cat calc_models_*.txt > calc_models.txt
