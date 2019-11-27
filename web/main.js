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
