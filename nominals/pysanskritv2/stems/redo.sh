python3 stems.py ../inputs/lexnorm-all2.txt calc_stems_0.txt calc_lexnorm_models.txt calc_models.txt calc_stems_todo.txt

# two types of duplicates are removed.
# First, those where the model and (un-hyphenated) stems are the same
python3 remove_dups.py calc_stems_0.txt calc_stems_1.txt  calc_stems_dup.txt >  calc_stems_dup_log.txt

# Second, feminines where the (un-hyphenated) stems are the same
# Note the log file which identifies these cases
python3 remove_gdups.py calc_stems_1.txt calc_stems_2.txt  calc_stems_gdup.txt > calc_stems_gdup_log.txt

# remove problems
python3 stem_model_diff.py calc_stems_2.txt stems_problem.txt calc_stems.txt

