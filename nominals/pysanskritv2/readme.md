# nominals/pysanskritv2

The identification and declension of nominals (and indeclineables) proceeds
in several steps in the subdirectories.
Each of these subdirectories has further details in `readme.md` files.

* inputs : nominals with gender specifications from MW1899 dictionary
* stems  : assignment of declension models and stems from the `inputs`
* tables : declension based on the stems.  
* analysis : various analyses of the declensions.

## redo.sh
This script goes through all the steps needed to calculate declensions.
The final result is tables/calc_tab.txt.
