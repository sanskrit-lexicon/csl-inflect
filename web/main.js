// work/fflexphp/main.js
var request = null;
try {
  request = new XMLHttpRequest();
} catch (trymicrosoft) {
  try {
    request = new ActiveXObject("Msxml2.XMLHTTP");
  } catch (othermicrosoft) {
    try {
      request = new ActiveXObject("Microsoft.XMLHTTP");
    } catch (failed) {
      request = null;
    }
  }
}

if (request == null) {
  alert("Error creating request object!");
}
var requestActive=false;
var win_ls=null;
function loadFcn() {
 document.getElementById("disp").innerHTML = "";
 win_ls=null;
 var word = document.getElementById("key").value;
  if (word) {
    getWord();
  }

}
// Devanagari -> SLP1 transliteration, so users can type in Devanagari
// directly; the dal/getWord backend only understands the schemes it
// already supports (Harvard-Kyoto, SLP1, ITRANS), so this runs client-side
// before the request is sent and the "input" scheme is switched to SLP1.
var DEVA_TO_SLP1_VOWELS = {
 "अ":"a","आ":"A","इ":"i","ई":"I","उ":"u","ऊ":"U",
 "ऋ":"f","ॠ":"F","ऌ":"x","ॡ":"X","ए":"e","ऐ":"E","ओ":"o","औ":"O"
};
var DEVA_TO_SLP1_MATRAS = {
 "ा":"A","ि":"i","ी":"I","ु":"u","ू":"U",
 "ृ":"f","ॄ":"F","ॢ":"x","ॣ":"X","े":"e","ै":"E","ो":"o","ौ":"O"
};
var DEVA_TO_SLP1_CONSONANTS = {
 "क":"k","ख":"K","ग":"g","घ":"G","ङ":"N",
 "च":"c","छ":"C","ज":"j","झ":"J","ञ":"Y",
 "ट":"w","ठ":"W","ड":"q","ढ":"Q","ण":"R",
 "त":"t","थ":"T","द":"d","ध":"D","न":"n",
 "प":"p","फ":"P","ब":"b","भ":"B","म":"m",
 "य":"y","र":"r","ल":"l","व":"v",
 "श":"S","ष":"z","स":"s","ह":"h"
};
var DEVA_ANUSVARA = "M";  // ं
var DEVA_VISARGA = "H";   // ः
var DEVA_VIRAMA = "्";    // halant: suppresses the inherent 'a'
var DEVA_AVAGRAHA = "'";  // ऽ

function devanagariToSLP1(text) {
 var out = "";
 for (var i = 0; i < text.length; i++) {
  var c = text[i];
  var next = text[i + 1];
  if (DEVA_TO_SLP1_VOWELS[c]) {
   out += DEVA_TO_SLP1_VOWELS[c];
  } else if (DEVA_TO_SLP1_CONSONANTS[c]) {
   out += DEVA_TO_SLP1_CONSONANTS[c];
   if (next === DEVA_VIRAMA) {
    i++;  // consonant cluster continues, no inherent 'a'
   } else if (DEVA_TO_SLP1_MATRAS[next]) {
    out += DEVA_TO_SLP1_MATRAS[next];
    i++;
   } else {
    out += "a";  // inherent vowel
   }
  } else if (c === "ं") {
   out += DEVA_ANUSVARA;
  } else if (c === "ः") {
   out += DEVA_VISARGA;
  } else if (c === "ऽ") {
   out += DEVA_AVAGRAHA;
  } else {
   out += c;  // spaces, digits, punctuation pass through unchanged
  }
 }
 return out;
}

function getWord() {
  var word = "";
  if (document.getElementById("key").value) {
    word = document.getElementById("key").value;
  }
  if ((word.length < 1)) {
   alert('Please specify an L-number.');
   return;
  }
  var filter = document.getElementById("filter").value;
//  var filterdir = document.getElementById("filterdir").value;
  var transLit = document.getElementById("transLit").value;
  if (transLit === "DEVA") {
   word = devanagariToSLP1(word);
   transLit = "SLP2SLP";
  }
  var url = "getWord.php" +
   "?word=" +escape(word) +
   "&transLit=" + escape(transLit) +
   "&filter=" +escape(filter);

  request.open("GET", url, true);
  request.onreadystatechange = updatePage;
  request.send(null);
  requestActive=true;
 document.getElementById("disp").innerHTML = 
   '<p>working...</p>' ;
 return;

}

function updatePage() {
  if (request.readyState == 4) {
   requestActive=false;
   if (request.status == 200) {
    var response = request.responseText;
//    alert('response=' + response);
    var ansEl = document.getElementById("disp");
    var mark = response.lastIndexOf("<disp1>");
    var response1 = response.substring(0,mark);
    var response2 = response.substring(mark+7);
    ansEl.innerHTML = response1;
    ansEl = document.getElementById("disp1");
    ansEl.innerHTML = response2;
    return;
  } else {
    alert("Error! Request status is " + request.status);
  }
 }
}
function model_info (url) {
// alert ('model_info: url = ' + url);
var win_ls = window.open(url,"modelInfo","width=950,height=700,toolbar=yes,location=yes,directories=yes,status=yes,menubar=yes,scrollbars=yes,copyhistory=yes,resizable=yes");
win_ls.focus();
}
function id_info (url) {
// alert ('id_info: url = ' + url);
var win_ls = window.open(url,"idInfo","width=950,height=700,toolbar=yes,location=yes,directories=yes,status=yes,menubar=yes,scrollbars=yes,copyhistory=yes,resizable=yes");
win_ls.focus();
}
function queryInputChar(e){
var keynum;
var keychar;
var numcheck;

if(window.event) // IE
{
keynum = e.keyCode;
}
else if(e.which) // Netscape/Firefox/Opera
{
keynum = e.which;
}
keychar = String.fromCharCode(keynum);
if ((keynum == 10) || (keynum == 13)) { // newline or return
 getWord();
 return (1 == 1);
}
return keychar;
}
