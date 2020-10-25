echo "REDO DECLENSION TABLES BEGINS"
echo "calc_tables0"
python3 decline_file.py ../stems/calc_stems.txt calc_tables0.txt
echo "calc_tables (after corrections)"
python3 corrections.py calc_tables0.txt correction_inventory.txt calc_tables.txt
echo "REDO DECLENSION TABLES ENDS"
