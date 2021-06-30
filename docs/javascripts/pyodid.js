/////////////////////////////////////////////////////
//
//        P Y O D I D E
//
//
////////////////////////////////////////////////////////

//////   POUR AVOIR DES textareas QUI S'ÉTENDENT AVEC LE TEXTE


// Targets all textareas with class "txta"
var textareas = document.querySelectorAll('.txta');
var hiddenDiv = document.createElement('div');
var content = null;

// Adds a class to all textareas
for (let j of textareas) {
  j.classList.add('txtstuff');
}

// Build the hidden div's attributes

// The line below is needed if you move the style lines to CSS
hiddenDiv.classList.add('hiddendiv');

// Add the "txta" styles, which are common to both textarea and hiddendiv
// If you want, you can remove those from CSS and add them via JS
hiddenDiv.classList.add('txta');

// Loop through all the textareas and add the event listener
for(let i of textareas) {
  (function(i) {
    // Note: Use 'keyup' instead of 'input'
    // if you want older IE support
    i.addEventListener('input', function() {
      
      // Append hiddendiv to parent of textarea, so the size is correct
      i.parentNode.appendChild(hiddenDiv);
      
      // Remove this if you want the user to be able to resize it in modern browsers
      i.style.resize = 'none';
      
      // This removes scrollbars
      i.style.overflow = 'hidden';

      // Every input/change, grab the content
      content = i.value;

      // Add the same content to the hidden div
      
      // This is for old IE
      content = content.replace(/\n/g, '<br>');
      
      // The <br ..> part is for old IE
      // This also fixes the jumpy way the textarea grows if line-height isn't included
      hiddenDiv.innerHTML = content + '<br style="line-height: 3px;">';

      // Briefly make the hidden div block but invisible
      // This is in order to read the height
      hiddenDiv.style.visibility = 'hidden';
      hiddenDiv.style.display = 'block';
      i.style.height = hiddenDiv.offsetHeight + 'px';

      // Make the hidden div display:none again
      hiddenDiv.style.visibility = 'visible';
      hiddenDiv.style.display = 'none';
    });
  })(i);
}


////////  PYODIDE

var output = document.getElementById("output");
var code = document.getElementById("code");
var sortie_test = document.getElementById("sortie_test");
var cpt = 0;
var reussite = 0; //nombre de séries de tests réussies

//désindenter un bloc de code Python
function desindente(chaine){
  let tab = chaine.split('\n')
  let chaine2 = "";  
  let start = 0;
  while ((start < tab.length ) && (tab[start].trim() == '')){
    start++;
  }
  let decalage = 0;
  while (tab[start][decalage] == ' '){
    decalage++;
  }
  for (let k = start; k < tab.length;k++){
    chaine2 = chaine2 +  tab[k].slice(decalage) + "\n"
  }
  return chaine2  
}


function addToOutput(sortie) {
    cpt += 1;
    // output.value += 'In  ['+ cpt+ ']: ' + code.value + '\n';
    output.value += 'Out [' + cpt+ ']: ' + sortie + '\n';
}

function addToSortieTest(sortie) {
    sortie_test.value +=  sortie + '\n';
}


function clearOutput() {
  // output.value += 'In  ['+ cpt+ ']: ' + code.value + '\n';
  output.value = '';
}

function clearSortieTest() {
  // output.value += 'In  ['+ cpt+ ']: ' + code.value + '\n';
  sortie_test.value = '';
}

// pour avoir des tabulations dans le textarea du code
document.getElementById('code').addEventListener('keydown', function(e) {
  if (e.key == 'Tab') {
    e.preventDefault();
    var start = this.selectionStart;
    var end = this.selectionEnd;

    // set textarea value to: text before caret + tab + text after caret
    this.value = this.value.substring(0, start) +
      "\t" + this.value.substring(end);

    // put caret at right position again
    this.selectionStart =
      this.selectionEnd = start + 1;
  }
});


output.value = 'Un instant...\n';


// init Pyodide
async function main(){
  await loadPyodide({ indexURL : 'https://cdn.jsdelivr.net/pyodide/v0.17.0/full/' });
  output.value += 'Prêt !\n';
}

if (typeof pyodideReadyPromise === "undefined"){
  var pyodideReadyPromise = main();
}
else {
  console.log("Pyodide déjà chargé");
  output.value += 'Prêt !\n';
}


async function evaluatePythonPerso() {
  await pyodideReadyPromise;
  try {
      let output = await pyodide.runPythonAsync(code.value);
      addToOutput(output);
      }
  catch(err) {
  addToOutput(err);
  }
}

async function executeTestPerso(c) {
  evaluatePythonPerso(); 
  await pyodideReadyPromise;
  try {
    let sortie = await pyodide.runPythonAsync(c);
    addToSortieTest(sortie);} 
  catch(err) {addToSortieTest(err);}}
///////////////////////////////////////////////////////
//
//         fin Pyodide
//
////////////////////////////////////////////////////////
