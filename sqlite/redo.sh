echo "Begin sqlite/redo.sh"
for dbname in lgmodel lgtab1 lgtab2 vlgtab1 vlgtab2 
do
 cd $dbname
 echo "redoing $dbname"
 sh redo_$dbname.sh
 cd ../
done