for DIR in inputs bases models tables
 do
  echo "redo computation in directory $DIR"
  cd $DIR
  sh redo.sh
  cd ../
 done