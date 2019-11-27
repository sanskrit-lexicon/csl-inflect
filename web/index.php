<?php
error_reporting( error_reporting() & ~E_NOTICE );
?>
<!DOCTYPE html>
<html>
 <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>inflected form lookup</title>
    <link rel="stylesheet" href="main.css" type="text/css"/>

  <script type="text/javascript" src="main.js"> </script>
 </head>
 <body  onload='loadFcn();'>
 <div id="leftpane" class="leftpane">
 <table width="100%">
   <tr>
    <td>
      <img id="unilogo" src="unilogo.gif"
           alt="University of Cologne" width="60" height="60" />
    </td>
      <td>
      <span style="font-size:larger;">inflected forms</span>
      <br/>
      <a href="help.html" target="_help">Help</a>
    </td>
   </tr>
 </table>
<?php init_inputs(); ?>
  <table width="100%" cellpadding="5">
   <tr>
   <td>word:&nbsp;</td>
   <td>
<?php
global $inithash;
 $init=$inithash['word'];
 echo '<input type="text" name="key" size="20" id="key" ';
 echo "value=\"$init\"";
 echo ' onkeypress="return queryInputChar(event);" />' . "\n";
?>

   </td>
   </tr>
   <tr>
   <td>input:&nbsp;</td>
   <td>
    <select name="transLit" id="transLit">
<?php
global $inithash;
 $init=$inithash['translit'];
 output_option("HK","Harvard-Kyoto",$init);
 output_option("SLP2SLP","SLP1",$init);
 output_option("ITRANS","ITRANS",$init);
?>
    </select>
   </td>
   </tr>
   <tr>
  </tr>

  <tr>
   <td>output:</td>
   <td>
    <select name="filter" id="filter">
<?php
global $inithash;
$init = $inithash['filter'];
output_option("SktDevaUnicode","Devanagari Unicode",$init);
 output_option("SLP2HK","Harvard-Kyoto",$init);
 output_option("SLP2SLP","SLP1",$init);
 output_option("SLP2ITRANS","ITRANS",$init);
 output_option("SktRomanUnicode","Roman Unicode",$init);
?>
    </select>
   </td>
  </tr>
</table>
   <td>
<input type="hidden" name="filterdir" value="../../../docs/filter" id="filterdir" />

    <input type="hidden" name="scandir" value="../..MWScan/MWScanpng" id="scandir" />
   </td>

</div>
<div id="disp1" class= "disp1">
</div>
 <div id="disp" class="disp">
 </div>
<script type="text/javascript" src="/js/piwik_analytics.js"></script>
</body>
</html>
<?php 
function init_inputs() {
global $inithash;
// foreach($_GET as $x=>$y) {
//  echo "GET: $x => $y <br/>\n";
// }
 // word = citation
 $x = $_GET['word'];
 if (!$x) {$x = $_GET['citation'];}
 if (!$x) {$x = $_GET['key'];}
 if (!$x) {$x = "";}
 $inithash['word'] = $x;

 // translit = input
 $x = $_GET['translit'];
 if (!$x) {$x = $_GET['input'];}
 if (!$x) {$x = "";}
 $x = strtoupper($x);
 if (preg_match('/^SLP/',$x)) {
  $x="SLP2SLP";
 }
 $inithash['translit'] = $x;
 
 // filter = output
 $x = $_GET['filter'];
 if (!$x) {$x = $_GET['output'];}
 if (!$x) {$x = "";}
 if (preg_match('/^SLP/',strtoupper($x))) {
  $x="SLP2SLP";
 }
 if (! $x) {
  $x="SktDevaUnicode";
 }else if ($x == "SLP2SLP") {
// $x="";
 }else if ($x == "HK") {
  $x = "SLP2HK";
 }else if ($x == "IRANS") {
  $x = "SLP2ITRANS";
 }
 
 $inithash['filter'] = $x;

}

 function output_option ($value,$display,$initvalue) {
  echo "  <option value='$value'";
  if ($initvalue == $value) {
   echo " selected='selected'";
  }
  echo ">$display</option>\n";
}

?>
