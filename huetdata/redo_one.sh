htense=$1
if [ ! $1 ]; then
 echo "huetdata/redo.sh requires tense parameter"
 exit 1
fi
if [ $htense == "aor" ] || [ $htense == "inj" ] ; then
 extractpy="verbs_tp.py"
elif [ $htense == "fut" ] || [ $htense == "cnd" ] ; then
 extractpy="verbs_tp.py"
elif [ $htense == "ben" ] [ $htense == "prf" ] ; then
 extractpy="verbs_tp.py"
elif [ $htense = "prs" ] || [ $htense == "pef" ]  ; then
 extractpy="verbs-prim-prs.py"
else 
 echo "Unknown htense=$htense"
 exit 1
fi

 echo "extract Huet forms for tense=$htense "
 stemfile="extract/huet_stems_${htense}.txt" 
 tabfile="extract/huet_conj_tables_${htense}.txt"
 echo $stemfile
 echo $tabfile
 python ${extractpy} download/SL_morph.xml $htense $stemfile $tabfile

 mapstemfile="mapextract/huet_stems_${htense}.txt" # unused
 maptabfile="mapextract/huet_conj_tables_${htense}.txt"

 echo "mapping verb spellings to MW form"
 python huet_mw_map.py $tabfile $maptabfile

