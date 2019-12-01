echo "Begin verbs/pysanskritv2/models/redo.sh"
python3 root_model.py 1 ../inputs/verb_cp.txt calc_models_1.txt
python3 root_model.py 2 ../inputs/verb_cp.txt calc_models_2.txt
python3 root_model.py 3 ../inputs/verb_cp.txt calc_models_3.txt
cat calc_models_*.txt > calc_models.txt
