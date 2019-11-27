echo "Begin nominals/pysanskritv2/redo.sh"
echo "computing calc_stems.txt"
cd stems
sh redo.sh
cd ../
echo "computing calc_tables.txt"
cd tables
sh redo.sh
cd ../
