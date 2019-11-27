dbname="vlgtab1"
dbfile="$dbname.sqlite"
smfile="../../verbs/pysanskritv2/tables/calc_tables.txt"
if [ -f "$dbfile" ]; then
 rm $dbfile
fi
python3 make_input.py  $smfile temp_input.txt
echo "remaking $dbfile ..."
sqlite3 $dbfile < $dbname.sql
mv $dbfile ../db/

