echo "Begin verbs/pysanskritv2/inputs/redo.sh"
python3 genuine_filter.py verb_cp_orig.txt mw_genuine_roots.txt verb_cp_orig_1.txt
python3 clean.py  verb_cp_orig_1.txt verb_cp.txt
echo "inputs for manual aorist (active/middle voices)"
python3 verb_cp_manual.py verb_cp.txt verb_cp_extra.txt ../manual/tables_aorist.txt verb_cp_aorist.txt
echo "inputs for manual aorist (passive voice)"
python3 verb_cp_manual.py verb_cp.txt verb_cp_extra.txt ../manual/tables_aorist_passive.txt verb_cp_aorist_passive.txt
echo "inputs for manual perfect (active/middle voices)"
python3 verb_cp_manual.py verb_cp.txt verb_cp_extra.txt ../manual/tables_prf.txt verb_cp_prf.txt

