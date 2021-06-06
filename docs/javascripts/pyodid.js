/////////////////////////////////////////////////////
//
//        P Y O D I D E
//
//
////////////////////////////////////////////////////////

//////   POUR AVOIR DES TEXTAREAS QUI S'ÉTENDENT AVEC LE TEXTE


// Targets all textareas with class "txta"
let textareas = document.querySelectorAll('.txta'),
    hiddenDiv = document.createElement('div'),
    content = null;

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

const output = document.getElementById("output");
const code = document.getElementById("code");
const sortie_test = document.getElementById("sortie_test");
let cpt = 0;

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
let pyodideReadyPromise = main();

async function evaluatePython() {
  await pyodideReadyPromise;
  try {
      let output = await pyodide.runPythonAsync(code.value);
      addToOutput(output);
      }
  catch(err) {
  addToOutput(err);
  }
}


///////////////////////////////////////////////////////
//
//         fin Pyodide
//
////////////////////////////////////////////////////////
