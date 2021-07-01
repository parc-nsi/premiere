"""Macros de Franck Chambon, Guillaume Connan et autres participants du forum NSI
Merci à eux
Voir https://mooc-forums.inria.fr/moocnsi/t/mkdocs-une-solution-ideale/1758

"""
from mkdocs_macros import fix_url 
import os

def pyodide():
    #macro de Guillaume Connan
    s =" <div> Code Python:</div><textarea id='code' style='width: 100%;'rows='10' ></textarea><button onclick='evaluatePython()' class='execution'>Exécuter</button><br><div>Résultat:</div><textarea id='output' style='width: 100%;' rows='10' disabled></textarea><script>const output = document.getElementById(\"output\");const code = document.getElementById(\"code\");let cpt = 0;function addToOutput(s) {cpt += 1;output.value += 'In  ['+ cpt+ ']: ' + code.value + '\\n';output.value += 'Out [' + cpt+ ']: ' + s + '\\n\\n'; }output.value = 'Je me prépare...\\n'; async function main(){  await loadPyodide({ indexURL : 'https://cdn.jsdelivr.net/pyodide/v0.17.0/full/' });  output.value += 'Prêt!\\n';} let pyodideReadyPromise = main(); async function evaluatePython() {  await pyodideReadyPromise;  try { let output = await pyodide.runPythonAsync(code.value); addToOutput(output);  } catch(err) { addToOutput(err);}} </script>"
    return s


def define_env(env):
    "Hook function"
    
    # activate trace
    chatter = env.start_chatting("Simple module")# activate trace
    #voir https://mkdocs-macros-plugin.readthedocs.io/en/latest/troubleshooting/
    env.variables['compteur_exo'] = 0
    env.variables['compteur_enigme'] = 0
    env.variables['term_counter'] = 0
    env.variables['IDE_counter'] = 0   

    @env.macro
    def exercice(): #G Connan
       env.variables['compteur_exo'] += 1
       return f"tip \"Exercice { env.variables['compteur_exo']}\""

    @env.macro
    def enigme(): 
       env.variables['compteur_enigme'] += 1
       return f"question \"Énigme { env.variables['compteur_enigme']}\""

    @env.macro
    def console(): #G Connan
        return pyodide()
    

    @env.macro
    def console_perso(url_code_test, url_code_template, url_pyodid = f"../../javascripts/pyodid.js"):        
        code_test = f"""
        --8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{url_code_test}"
        """    
        code_template =  f"""
        --8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{url_code_template}"
        """              
        s = "<div>Code:</div><textarea id='code' class='txta' autofocus></textarea>"          
        s = s + "<button onclick='evaluatePythonPerso()'  class='execution'>Exécuter le code</button> <button class='execution' onclick='clearOutput()'>Nettoyer Console</button>"
        s = s + "<div>Évaluation du code :</div><textarea id='output' class='txta common'></textarea><br><br><button onclick='executeTestPerso(code_test)'  class='execution'>Exécuter les tests unitaires</button>  <button class='execution' onclick='clearSortieTest()'>Nettoyer tests</button><div>Évaluation des tests :</div><textarea id='sortie_test' style='width: 100%;' rows='6' disabled></textarea>" 
        s = s + f"<script src='{url_pyodid}'></script>"   
        s = s +  "<script>var code_template =`" + code_template + "`;" + "code_template = desindente(code_template);code.innerHTML = code_template </script>"
        s = s +  "<script>var code_test =`" + code_test + "`;" + "code_test = desindente(code_test);</script>"
        return s  

   

    @env.macro
    def basthon(exo: str, hauteur: int) -> str: #F Chambon
        "Renvoie du HTML pour embarquer un fichier `exo` dans Basthon"
        return f"""<iframe src="https://console.basthon.fr/?from={env.variables.io_url}{env.variables.page.url}../{exo}" width=100% height={hauteur}></iframe>
[Lien dans une autre page](https://console.basthon.fr/?from={env.variables.io_url}{env.variables.page.url}../{exo})
"""

    @env.macro
    def script(lang: str, nom: str) -> str: #F Chambon
        "Renvoie le script dans une balise bloc avec langage spécifié"
        return f"""```{lang}
--8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
```"""
    #voir https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#snippets

    @env.macro
    def py(nom: str) -> str: #F Chambon
        "macro python rapide"
        return script('python', "scripts/" + nom + ".py")

    @env.macro
    def html_fig(num: int) -> str: #F Chambon
        "Renvoie le code HTML de la figure n° `num`"
        return f'--8<-- "docs/' + os.path.dirname(env.variables.page.url.rstrip('/')) + f'/figures/fig_{num}.html"'


   

    @env.macro
    def table_a():  #F Chambon
        a = [1, 1, 2, 3]
        b = [1, 1, 3, 4]
        c = [1, 1, 2, 3]
        for n in range(4, 24):
            # On ajoute a[n], puis b[n], puis c[n]
            a.append(a[n-1] + a[n-2] + a[n-4] + 2*b[n-4] + c[n-4])
            b.append(a[n] + b[n-2])
            c.append(a[n] + c[n-4])

        def markdown(a, ni, nf):
            """Renvoie un joli tableau markdown des valeurs de
            la suite a_n pour n dans [ni, nf["""
            ans = "|$n$|"
            for n in range(ni, nf): ans += f"${n}$|"
            ans += "\n|:---:|"
            for n in range(ni, nf): ans += ":---:|"
            ans+= "\n|$a_n$|"
            for n in range(ni, nf): ans += f"${a[n]}$|"
            return ans + "\n\n"

        return markdown(a, 0, 24)

    #Macros terminal et REPL Vincent Bouillot
    @env.macro
    def terminal() -> str:
        """   
        Purpose : Create a Python Terminal.
        Methods : Two layers to avoid focusing on the Terminal. 1) Fake Terminal using CSS 2) A click hides the fake 
        terminal and triggers the actual Terminal.
        """        
        tc = env.variables['term_counter']
        env.variables['term_counter'] += 1
        return f"""<div onclick='start_term("id{tc}")' id="fake_id{tc}" class="terminal_f"><label class="terminal"><span>>>> </span></label></div><div id="id{tc}" class="hide"></div>"""

    def read_ext_file(nom_script : str) -> str:
        """
        Purpose : Read a Python file that is uploaded on the server.
        Methods : The content of the file is hidden in the webpage. Replacing \n by a string makes it possible
        to integrate the content in mkdocs admonitions.
        """
        short_path = f"""docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}"""
        try: 
            f = open(f"""{short_path}/scripts/{nom_script}.py""")
            content = ''.join(f.readlines())
            f.close()
            content = content+ "\n"
            # Hack to integrate code lines in admonitions in mkdocs
            return content.replace('\n','backslash_newline')
        except :
            return
        
    def generate_content(nom_script : str) -> str:
        """
        Purpose : Return content and current number IDE {tc}.
        """
        tc = env.variables['IDE_counter']
        env.variables['IDE_counter'] += 1

        content = read_ext_file(nom_script)

        if content is not None :
            return content, tc
        else : return "", tc

    def create_upload_button(tc : str) -> str:
        """
        Purpose : Create upoad button for a IDE number {tc}.
        Methods : Use an HTML input to upload a file from user. The user clicks on the button to fire a JS event
        that triggers the hidden input.
        """
        return f"""<button class="emoji" onclick="document.getElementById('input_editor_{tc}').click()">⤴️</button>\
                <input type="file" id="input_editor_{tc}" name="file" enctype="multipart/form-data" class="hide"/>"""

    def create_unittest_button(tc: str, nom_script: str, mode: str) -> str:
        """
        Purpose : Generate the button for IDE {tc} to perform the unit tests if a valid test_script.py is present.
        Methods : Hide the content in a div that is called in the Javascript
        """
        stripped_nom_script = nom_script.split('/')[-1]
        relative_path = '/'.join(nom_script.split('/')[:-1])
        nom_script = f"{relative_path}/test_{stripped_nom_script}"
        content = read_ext_file(nom_script)
        if content is not None: 
            return f"""<span id="test_term_editor_{tc}" class="hide">{content}</span><button class="emoji_dark" onclick=\'executeTest("{tc}","{mode}")\'>🛂</button><span class="compteur">5/5</span>"""
        else: 
            return ''


    def blank_space() -> str:
        """ 
        Purpose : Return 5em blank spaces. Use to spread the buttons evenly
        """
        return f"""<span style="indent-text:5em"> </span>"""

    @env.macro
    def IDEv(nom_script : str ='') -> str:
        """
        Purpose : Easy macro to generate vertical IDE in Markdown mkdocs.
        Methods : Fire the IDE function with 'v' mode.
        """
        return IDE(nom_script, 'v')


    @env.macro
    def IDE(nom_script : str ='', mode : str = 'h') -> str:
        """
        Purpose : Create a IDE (Editor+Terminal) on a Mkdocs document. {nom_script}.py is loaded on the editor if present. 
        Methods : Two modes are available : vertical or horizontal. Buttons are added through functioncal calls.
        Last span hides the code content of the IDE if loaded.
        """
        content, tc = generate_content(nom_script)
        corr_content, tc = generate_content(f"""{'/'.join(nom_script.split('/')[:-1])}/corr_{nom_script.split('/')[-1]}""")
        div_edit = f'<div class="ide_classe">'
        if mode == 'v':
            div_edit += f'<div class="wrapper"><div class="interior_wrapper"><div id="editor_{tc}"></div></div><div id="term_editor_{tc}" class="term_editor"></div></div>'
        else:
            div_edit += f'<div class="wrapper_h"><div class="line" id="editor_{tc}"></div><div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div>'
        div_edit += f"""<button class="emoji" onclick='interpretACE("editor_{tc}","{mode}")'>▶️</button>"""
        div_edit += f"""{blank_space()}<button class="emoji" onclick=\'download_file("editor_{tc}","{nom_script}")\'>⤵️</button>{blank_space()}"""
        div_edit += create_upload_button(tc)
        div_edit += create_unittest_button(tc, nom_script, mode)
        div_edit += '</div>'

        div_edit += f"""<span id="content_editor_{tc}" class="hide">{content}</span>"""
        div_edit += f"""<span id="corr_content_editor_{tc}" class="hide">{corr_content}</span>"""
        return div_edit
