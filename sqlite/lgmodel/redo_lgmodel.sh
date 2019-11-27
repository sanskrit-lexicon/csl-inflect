dbname="lgmodel"
dbfile="$dbname.sqlite"
if [ -f "$dbfile" ]; then
 rm $dbfile
fi
echo "remaking $dbfile ..."
sqlite3 $dbfile < $dbname.sql
mv $dbfile ../db/
