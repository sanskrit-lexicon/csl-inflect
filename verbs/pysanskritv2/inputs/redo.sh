echo "Begin verbs/pysanskritv2/inputs/redo.sh"
python3 genuine_filter.py verb_cp_orig.txt mw_genuine_roots.txt verb_cp_orig_1.txt
python3 clean.py  verb_cp_orig_1.txt verb_cp.txt
