input=$1
#input="../models/models_1_3.txt"

IFS='	' # tab is set as delimiter
while read -r line
do
  if [[ $line =~ ^";" ]]
   then
    x="1" # dummy
   else
    read -ra ADDR <<< "$line"
    #echo "$line"
    #echo "     "
    #echo "     "
    #python3 ../analysis/conjugate_one_v2.py ${ADDR[0]}  ${ADDR[1]}
    python3 ../../pysanskritv1/conjugate_one_v1.py ${ADDR[0]}  ${ADDR[1]}
  fi
done < "$input"