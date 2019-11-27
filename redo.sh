echo "Begin calculations in 'nominals' directory"
cd nominals
sh redo.sh
cd ../
echo "End calculations in 'nominals' directory"
echo "Begin calculations in 'verbs' directory"
cd verbs
sh redo.sh
cd ../
echo "End calculations in 'verbs' directory"
echo "Begin calculations in 'sqlite' directory"
cd sqlite
sh redo.sh
echo "End calculations in 'sqlite' directory"

