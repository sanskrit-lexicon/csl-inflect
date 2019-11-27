# temp1cons_todo.txt is a copy of temp_lexnorm_todo.txt created by
# running python3 stem_model.py lexnorm-all2.txt with
# the 1cons stuff commented out.
cp temp_lexnorm_todo.txt temp1cons_todo.txt
# write all to one file
python3 analyze_1cons.py 'all' slp1 temp1cons_todo.txt analyze_1cons.txt
python3 analyze_1cons.py 'all' roman temp1cons_todo.txt analyze_1cons_iast.txt
exit 0 # skip individual files. script ends here.
# write individual files (needed?)
python3 analyze_1cons.py t slp1 temp1cons_todo.txt temp_analyze_t.txt
python3 analyze_1cons.py T slp1 temp1cons_todo.txt temp_analyze_t1.txt
python3 analyze_1cons.py d slp1 temp1cons_todo.txt temp_analyze_d.txt
python3 analyze_1cons.py D slp1 temp1cons_todo.txt temp_analyze_d1.txt
#
python3 analyze_1cons.py '[kK]' slp1 temp1cons_todo.txt temp_analyze_k.txt
#python3 analyze_1cons.py K slp1 temp1cons_todo.txt temp_analyze_k1.txt
python3 analyze_1cons.py '[gG]' slp1 temp1cons_todo.txt temp_analyze_g.txt
#python3 analyze_1cons.py G slp1 temp1cons_todo.txt temp_analyze_g1.txt
#
python3 analyze_1cons.py '[wWqQ]' slp1 temp1cons_todo.txt temp_analyze_w.txt
#
python3 analyze_1cons.py j slp1 temp1cons_todo.txt temp_analyze_j.txt
python3 analyze_1cons.py c slp1 temp1cons_todo.txt temp_analyze_c.txt
python3 analyze_1cons.py '[CJ]' slp1 temp1cons_todo.txt temp_analyze_c1.txt
#
python3 analyze_1cons.py '[pPbB]' slp1 temp1cons_todo.txt temp_analyze_p.txt
#
python3 analyze_1cons.py '[S]' slp1 temp1cons_todo.txt temp_analyze_s1.txt
python3 analyze_1cons.py '[z]' slp1 temp1cons_todo.txt temp_analyze_z.txt
#
python3 analyze_1cons.py '[h]' slp1 temp1cons_todo.txt temp_analyze_h.txt
#
python3 analyze_1cons.py '[NYRnm]' slp1 temp1cons_todo.txt temp_analyze_n.txt
#
python3 analyze_1cons.py '[l]' slp1 temp1cons_todo.txt temp_analyze_l.txt
#
python3 analyze_1cons.py '[r]' slp1 temp1cons_todo.txt temp_analyze_r.txt
