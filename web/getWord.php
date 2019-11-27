<?php
/*

*/

$dir = dirname(__FILE__); //directory containing this php file
require_once('dal.php');
require_once('dbgprint.php');
require_once('utilities/transcoder.php');
global $filter0,$filterin0,$filterin,$word_slp1;
 list($filter0,$filterin0) = getParameters_orig();
$filter = transcoder_standardize_filter($filter0); // in transcoder
$filterin = transcoder_standardize_filter($filterin0);

 if (isset($_GET['word'])) {
  $keyin = $_GET['word'];
 }else if (isset($argv[1])) {
  $keyin=$argv[1];
 }else {
  $keyin='rAmaH';
 }

$keyin1 = preprocess_unicode_input($keyin,$filterin);
$key = transcoder_processString($keyin1,$filterin,"slp1");
$word = $key;
$word_slp1=$word;
#$dbg=true;
#$dbg=false;
$info = process1_word($word);
if ($dbg) {echo "\n<!-- debug info \n";}
if ($dbg) {echo " word='$word',transLit='$transLit',filter='$filter'\n";}
if ($dbg) {echo count($info) . " records returned\n";}
$info1 = array();
for($i=0;$i<count($info);$i++) {
 list($table,$x,$y) = $info[$i];
 $xtext = join(',',$x);
 $key = $x[0];
 $model = $x[1];
 $stem = $x[2];
 dbgprint($dbg,"info[$i]: $table\n");
 dbgprint($dbg,"{$table}2: $key,$model,$stem\n");
 $model1 = $y[0]; # model1 and stem1 are stem as model and stem
 $stem1 =  $y[1];  
 $refstr = $y[2];  # citation1,Lnum1:citation2,Lnum2 ...
 $inflstr = $y[3]; #inflection string

 dbgprint($dbg,"{$table}1: $model1  $stem1  $refstr\n  $inflstr\n");
 
 if ($dbg) {echo "$table:$i: $xtext\n";}
 $nmatches = count($matches[0]);
  $citation = get_citation($table,$stem,$refstr);
  $form = $inflstr;
  $pn = lgtab_pn($key,$model,$form);
  if ($dbg) {echo "   $pn\n";}
  # set $id to first Lnum in refstr
  $id = first_Lnum($refstr);
  if($pn != "") { 
   // not sure why this is required
   // got false match on aMSayizyati otherwise
   $info1[] = array($citation,$model,$pn,$form,$id,$refstr);
  }

 if ($dbg) {echo "---------------\n";}
}
if ($dbg) {echo "end debug info -->\n";}
// Now, construct html
$ans = "";
$ans2 = "";
// Nov 27, 2011.  Remove 'duplicates' from $info1 before generating html
$info2 = array();
$info2vals=array();
foreach($info1 as $info) {
 list($citation,$model,$detail,$formlist,$id,$refstr) = $info;
 $mwkey1_slp = $citation;
 $info2arr=array($citation,$model,$detail,$formlist,$mwkey1_slp);
 $info2val = join(',',$info2arr);
 if(!$info2vals[$info2val]) {
  $info2vals[$info2val]=true;
  $info2[]=$info;
 }
}
for($n=0;$n<count($info2);$n++) {
 list($a,$b) = display_info($info2[$n],$n);
 $ans .= $a;
 $ans2 .= "$b";
}
$ans = transcoder_processElements($ans,"slp1",$filter,"SA");
$ans2 = transcoder_processElements($ans2,"slp1",$filter,"SA");
echo "$ans\n";
echo "<disp1>\n";  // separator for ajax caller
echo "$ans2\n";
exit; 

function get_citation($table,$stem,$refstr){
 # refstr: citation1,Lnum1:citation2,Lnum2
 # $table = 'lgtab' or 'vlgtab'
 if ($table =='lgtab') {
  $citation = preg_replace('/-/','',$stem); # ok for nouns.
 }else  {
  $a = preg_split('/:/',$refstr);
  list($L,$citation) = preg_split('/,/',$a[0]);
 }
 return $citation;
}
function process1_word($word) {
    #$dbg = true;
    $info=array();
    $tables  = array("lgtab","vlgtab");
    for($itable=0;$itable<count($tables);$itable++) {
     $table=$tables[$itable];
     $table2=$table . "2";
     $table1=$table . "1";
     $xarr = process_word($word,$table2);
     for($i=0;$i<count($xarr);$i++) {
      $x = $xarr[$i];
      $model = $x[1];
      $stem = $x[2];
      dbgprint($dbg,"$table2 entry $i: $model, $stem\n");
      $yarr = process_form($model,$stem,$table1);
      dbgprint($dbg,"$table1 returns " . count($yarr) . " items\n");
      for($j=0;$j<count($yarr);$j++) {
       $y=$yarr[$j];
       $info[] = array($table,$x,$y);
       #dbgprint($dbg,"$table , $x, $y\n");
      }
     }
    }
    return $info;
}
function process_word($key,$table) {
 $dal = new Dal("None","$table");

$sql = "select * from `$table` where `key`=\"$key\"";
$ansarr = $dal->get($sql);

$dal->close();
return $ansarr;
}
function process_form($model,$stem,$table) {
 $dal = new Dal("None","$table");
$sql = "select * from `$table` where `stem`=\"$stem\" and `model`=\"$model\"";
$ansarr = $dal->get($sql);

return $ansarr;  // 11-18-2019
if (0 < count($ansarr)) {
 $ans1 = array();
 foreach ($ansarr as $line) {
  #$ans1[] = $line[0];
 }
 $ansarr = $ans1;
}
return $ansarr;
}
function lgtab_pn($key,$model,$formdata) {
 $ans="";
 $forms = preg_split('/:/',$formdata);
 $dispforms_mfn= array("1s","1d","1p","2s","2d","2p","3s","3d","3p","4s","4d","4p","5s","5d","5p","6s","6d","6p","7s","7d","7p","8s","8d","8p");
 $dispforms_ind= array("ind");
 $dispforms_verb = array("3s","3d","3p","2s","2d","2p","1s","1d","1p" );
 for($n=0;$n<count($forms);$n++) {
  $form = $forms[$n];
  // may have multiple forms separated by forward slash
  $forms1 = preg_split('/\//',$form);
  foreach($forms1 as $form1) {
   if ($key != $form1) {continue;}
   if(preg_match('/^fut/',$model)) {
    $ans1 = $dispforms_verb[$n];
   }else if (preg_match('/^[mfn]/',$model)) {
    $ans1 = $dispforms_mfn[$n];
   }else if($model == "ind") {
    $ans1 = $dispforms_ind[$n];
   }else { // assume verb conjugation
    $ans1 = $dispforms_verb[$n];
   }
   if ($ans == "") {
    $ans = $ans1;
   }else {
    $ans .= "/" . $ans1;
   }
  }
 }
 return $ans;
}
function display_info($info,$n) {
 list($key,$model,$detail,$formin,$id,$refstr) = $info;
 $x = sprintf("%03d",$n);
 $lb="#";
 $formdata = "$key $model $formin";
 #dbgprint(true,"display_info: key=$key\n");
 $temp = display_lgtab1($key,$detail,$formdata,$n);
 return $temp;
}
function display_lgtab1($citation,$detail,$formdata,$nmodels) {
global $filter0,$filterin0,$filterin,$word_slp1;
 $filter=$filter0;
 $transLit = $filterin0;
   $lb = "#";
    list($stem,$model,$formlist) = preg_split('/ /',$formdata);
    $ans = "";
    $n = $nmodels+1;
    $ans .= "<a id=\"model_$n\" />\n";
    $ans .= "<table class=\"tabmain\">\n";
    if (preg_match('/^ind/',$model)) {
	$type = "indeclinable";
    }else if(preg_match('/^fut/',$model)) {
       //this needed since 'fut' starts with f.
	$type = "verb";
    }else if(preg_match('/^[mfn]/',$model)) {
	$type = "noun/adj";
    }else {
	$type = "verb";
    }
    $x = sprintf("%03d",$n);
    $mwkey1_slp = $citation;
    $mwkey1 = transcoder_processString($mwkey1_slp,"slp1",$filterin);
    $mwurl = getMonierKey1url($mwkey1,$transLit,$filter);
    $aid = 	"<a class='idinfo' " . 
	"onclick=\"id_info('" . $mwurl . "');\">$mwkey1</a>";

    $ans2 = "<a href=\"$lb" . "model_" . "$n\">" .
	$x . "</a> " . $model .
	" " . $detail . " " .
	" " . $aid . " " . 
	"<br/>";
    
    $modelurl=getModelurl($model);
    $ans .= "<tr><td>$x $type: <SA>$stem</SA> , model: " .
	"<a class='modelinfo' " . 
	"onclick=\"model_info('" . $modelurl . "');\">$model</a>"
	. "</td></tr>\n";
    
    $ans .= "<tr>\n";
    $ans .= "<td>\n";
    if($type == 'verb') {
     $ans .= "<table class='conj'>\n";
    }else {
     $ans .= "<table class='decl'>\n";
    }
    if ($type == "indeclinable") {
	$rowtitles = array("ind");
    }else if ($type == "noun/adj") {
	$rowtitles = array("Nom","Acc","Inst","Dat","Abl","Gen","Loc","Voc");
	$ans .= "<tr>";
	$coltitles = array("Sg","Du","Pl");
	$ans .= "<th></th>";
	foreach ($coltitles as $ct) {
	    $ans .= "<th>$ct</th>";
	}
	$ans .= "</tr>\n";
    }else if ($type == "verb") {
	$rowtitles = array("3rd","2nd","1st");
	$ans .= "<tr>";
	$coltitles = array("Sg","Du","Pl");
	$ans .= "<th></th>";
	foreach ($coltitles as $ct) {
	    $ans .= "<th>$ct</th>";
	}
	$ans .= "</tr>\n";
    }
    $forms1 = preg_split('/:/',$formlist);
    $n = 0;
    
    foreach($forms1 as $form1) {
	if (($n % 3) == 0) {
	    $irow = $n / 3;
	    $ans .= "<tr>";
	    $ans .= "<th>$rowtitles[$irow]</th>";
	    $ans .= "\n";
	}
	$ans .= "<td>";
	$forms = preg_split('/\//',$form1);
	$i = 0;
	$td = array();
	foreach($forms as $form) {
	    $td[$i] = "<SA>$form</SA>";
	    // Nov 27, 2011.  
	    if($form == $word_slp1) {
	      $td[$i] = "<span style='color:red;font-weight:bold'>" . $td[$i] . "</span>";
	    }
	    $i++;
	}
	$ans1 = join(" / ",$td);
	$ans .= $ans1;
	$ans .= "</td>\n";
	if ((($n+1) % 3) == 0) {
	    $ans .= "</tr>\n";
	}
	$n++;
    }
    $ans .= "</table>";
    $ans .= "</td>";
    $ans .= "</tr>";
    $ans .= "</table>";
    return array($ans,$ans2);
}
function getidref($id) {
 $ans = preg_replace('/^MW-/','',$id);
 $ans = preg_replace('/^[0]+/','',$ans);
 $ans = preg_replace('/[.]00$/','',$ans);
 //echo("getidref: $id -> $ans<br/>\n");
 return $ans;
}
function getMonierKey1($lnum){
 global $lnums;
 if (!$lnums) {$lnums = array();}
 $ans = $lnums[$lnum];
 if ($ans){return $ans;}
 $dal = new Dal('mw','mw');
 $sql = "select `key` from `mw` where `lnum`=\"$lnum\"";
 $ansarr = $dal->get($sql);
 $dal->close();
 if (count($ansarr) == 0) {
  return "$lnum ?";
 }else {
  $key = $ansarr[0]['key'];
  $ans=$key;
  $lnums[$lnum]=$ans;
  return $ans;
 }
/*
  $ans=$key;
  $lnums[$lnum]=$ans;
 return 'mw??';  // not implemented 09-14-2018
 if (!$lnums) {$lnums = array();}
 $ans = $lnums[$lnum];
 if ($ans){return $ans;}
 $sql = "select `key` from `monier` where `lnum`=\"$lnum\"";
 $result=mysql_query($sql) or die('mysql query failed: ' . mysql_error());
 
 if ($line = mysql_fetch_array($result,MYSQL_NUM)) {
  $key=$line[0];
  $ans=$key;
  $lnums[$lnum]=$ans;
 }
 return $ans;
*/
}
function getMonierKey1url($key1,$transLit,$filter) {
 $dictinfowhich = get_DictinfoWhich();
 if ($dictinfowhich == "cologne") {
    $ans = "http://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/mw/web/webtc/indexcaller.php?key=$key1&filter=$filter&translit=$transLit";
 } else {
    $ans = "../../mw/web/webtc/indexcaller.php?key=$key1&filter=$filter&translit=$transLit";
 }
    return $ans;
}

function getModelurl($model) {
 $sql = "select `ref` from `lgmodel` WHERE `model`=\"$model\" ";
 $dal = new Dal("None","lgmodel");
 $ansarr = $dal->get($sql);
 $ans="";
 if (count($ansarr) > 0) {
  $line = $ansarr[0];
  $data = $line[0];
  if (preg_match('/Kale +([0-9]+)/',$data,$matches)) {
   $page = $matches[1];
   $ans = getKaleUrl($page);
  }
 }
 return $ans;
}
function getKaleUrl($page) {
//    $ans = "http://www.sanskrit-lexicon.uni-koeln.de/scans/KALEScan/disp1/index1.php?sfx=png&pageua=" . $page;
 $dictinfowhich = get_DictinfoWhich();
 if ($dictinfowhich == "cologne") {
    $ans = "http://www.sanskrit-lexicon.uni-koeln.de/scans/csl-kale/disp/index.php?sfx=png&pageua=$page";
 } else {
    $ans = "../../csl-kale/disp/index.php?sfx=png&pageua=$page";
 }
 return $ans;
}
function get_DictinfoWhich() {
 if (preg_match("|^/[an]fs/|",dirname(__DIR__))) {
  $dictinfowhich = "cologne"; 
 }else {
  $dictinfowhich = "xampp";
 }
 return $dictinfowhich;
}
function getParameters_orig() {
 $filter = $_GET['filter'];
 $filterin = $_GET['transLit']; 
 if(!$filterin) {$filterin = $_GET['translit']; }
 if (! $filterin) {$filterin = 'SLP2SLP';};
 return array($filter,$filterin);
}
function preprocess_unicode_input($x,$filterin) {
 // when a unicode form is input in the citation field, for instance
 // rAma (where the unicode roman for 'A' is used), then,
 // the value present as 'keyin' is 'r%u0101ma' (a string with 9 characters!).
 // The transcoder functions assume a true unicode string, so keyin must be
 // altered.  This is what this function aims to accomplish.
 $hex = "0123456789abcdefABCDEF";
 $x1 = $x;
 if ($filterin == 'roman') {
  $x1 = preg_replace("/\xf1/","%u00f1",$x);
 }
 $ans = preg_replace_callback("/(%u)([$hex][$hex][$hex][$hex])/",
     "preprocess_unicode_callback_hex",$x1);
 return $ans;
}
function preprocess_unicode_callback_hex($matches) {
 $x = $matches[2]; // 4 hex digits
 $y = unichr(hexdec($x));
 return $y;
}

function first_Lnum($refstr) {
 $parts = preg_split('/:/',$refstr);
 list($hw,$L) = preg_split('/,/',$parts[0]);
 return $L;
}
?>
