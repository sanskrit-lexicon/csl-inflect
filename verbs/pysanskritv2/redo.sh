echo "Begin verbs/pysanskritv2/redo.sh"
for DIR in inputs models bases tables
 do
  echo "redo computation in directory $DIR"
  cd $DIR
  sh redo.sh
  cd ../
 done