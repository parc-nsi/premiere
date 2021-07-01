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
    def console_perso(url_code_test, url_code_template,  url_pyodid = "../../javascripts/pyodid.js"):
        code_test = f"""
        --8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{url_code_test}"
        """    
        code_template =  f"""
        --8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{url_code_template}"
        """              
        s = "<div>Code:</div><textarea id='code' class='txta' autofocus></textarea>"          
        s = s + "<button onclick='evaluatePython()'  class='execution'>Exécuter le code</button> <button class='execution' onclick='clearOutput()'>Nettoyer Console</button>"
        s = s + "<div>Évaluation du code :</div><textarea id='output' class='txta common'></textarea><br><br><button onclick='executeTest(code_test)'  class='execution'>Exécuter les tests unitaires</button>  <button class='execution' onclick='clearSortieTest()'>Nettoyer tests</button><div>Évaluation des tests :</div><textarea id='sortie_test' style='width: 100%;' rows='6' disabled></textarea>" 
        s = s + f"<script src='{url_pyodid}'></script>"   
        s = s +  "<script>var code_template =`" + code_template + "`;" + "code_template = desindente(code_template);code.innerHTML = code_template </script>"
        s = s +  "<script>var code_test =`" + code_test + "`;" + "code_test = desindente(code_test);</script>"
        return s  

    @env.macro
    def console_perso_old(url_code_test, url_pyodid = "../../javascripts/pyodid.js"): #very old version
        code_test = f"""
        --8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{url_code_test}"
        """      
        s = "<div>Code:</div><textarea placeholder='Tapez votre code ici' id='code' class='txta'></textarea>"
        s = s + "<button onclick='evaluatePython()'  class='execution'>Exécuter le code</button> <button class='execution' onclick='clearOutput()'>Nettoyer Console</button>"
        s = s + "<div>Évaluation du code :</div><textarea id='output' class='txta common'></textarea><br><br><button onclick='executeTest(code_test)'  class='execution'>Exécuter les tests unitaires</button>  <button class='execution' onclick='clearSortieTest()'>Nettoyer tests</button><div>Évaluation des tests :</div><textarea id='sortie_test' style='width: 100%;' rows='6' disabled></textarea>"
        s = s + f"<script src='{url_pyodid}'></script>"
        s = s +  "<script>var code_test =`" + code_test + "`;" + "code_test = desindente(code_test);</script>"
        return s 

    @env.macro
    def console_perso_very_old(url_code_test, url_pyodid = "../../javascripts/pyodid.js"): #very old version
        code_test = f"""
        --8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{url_code_test}"
        """ 
        s = "<div>Code:</div><textarea placeholder='Tapez votre code ici' id='code' class='txta'></textarea>"
        s = s + "<button onclick='evaluatePython()'  class='execution'>Exécuter le code</button> <button class='execution' onclick='clearOutput()'>Nettoyer Console</button>"
        s = s + "<div>Évaluation du code :</div><textarea id='output' class='txta common'></textarea><br><br><button onclick='executeTest()'  class='execution'>Exécuter les tests unitaires</button>  <button class='execution' onclick='clearSortieTest()'>Nettoyer tests</button><div>Évaluation des tests :</div><textarea id='sortie_test' style='width: 100%;' rows='6' disabled></textarea>"
        s = s + f"<script src='{url_pyodid}'></script>"
        s = s +  "<script>let code_test =`" + code_test + "`;" + "code_test = desindente(code_test);"
        s = s + "async function executeTest() {evaluatePython(); await pyodideReadyPromise;try {let sortie = await pyodide.runPythonAsync(code_test);addToSortieTest(sortie);} catch(err) {addToSortieTest(err);}}</script>"
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
    def terminal(prem = 0) -> str:
        tc = env.variables['term_counter']
        env.variables['term_counter'] += 1
        return f""""<div onclick='start_term("id{tc}")' id="fake_id{tc}" class="terminal_f"><label class="terminal"><span>>>> </span></label></div><div id="id{tc}" class="hide"></div>"""


    env.variables['REPL_counter'] = 0
    @env.macro
    def REPLv(nom_script='',last = 0, url_repljs = "../xtra/javascripts/repl.js") -> str:
        tc = env.variables['REPL_counter']
        if len(nom_script) > 0: 
            f = open(f"""docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}/scripts/{nom_script}.py""")
            content = ''.join(f.readlines())
            f.close()
            div_edit = f"""<div id="editor_{tc}">{content}</div>"""        
        else : div_edit = f'<div id="editor_{tc}"></div>'
        env.variables['REPL_counter'] += 1
        div_edit = f'<div class="wrapper"><div class="interior_wrapper">{div_edit}</div>\
        <div id="term_editor_{tc}" class="term_editor"></div></div><button onclick=\'interpretACE("editor_{tc}","vert")\' style="font-size:2em">⚙️</button>'
        return f"""{div_edit}<script src="{url_repljs}"></script> """ if last==-1 else div_edit
        #return f"""{div_edit}<script src="xtra/javascripts/repl.js"></script> """ if last==-1 else div_edit

    @env.macro
    def REPL(nom_script='', last = 0, url_repljs = "../xtra/javascripts/repl.js") -> str:
        tc = env.variables['REPL_counter']
        if len(nom_script) > 0: 
            f = open(f"""docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}/scripts/{nom_script}.py""")
            content = ''.join(f.readlines())
            f.close()
            div_edit = f"""<div class="line" id="editor_{tc}">{content}</div>"""        
        else : div_edit = f'<div class="line" id="editor_{tc}"></div>'
        env.variables['REPL_counter'] += 1
        div_edit = f'<div class="wrapper_h">{div_edit}<div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div><button onclick=\'interpretACE("editor_{tc}","hori")\' style="font-size:2em">⚙️</button>' 
        return f"""{div_edit}<script src="{url_repljs}"></script> """ if last==-1 else div_edit
        #return f"""{div_edit}<script src="xtra/javascripts/repl.js"></script> """ if last==-1 else div_edit