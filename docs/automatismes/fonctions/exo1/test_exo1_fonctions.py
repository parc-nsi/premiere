import io
import js

sortie = io.StringIO() 
benchmark = ['somme([]) == None', 'somme([1]) == 1', 'somme([1,2]) == 3', 'somme([-1,1]) == 0']
for k, test in enumerate(benchmark, 1):
    if eval(test):
        sortie.write(f'Test {k} réussi :  {test} \\n')
    else:
        sortie.write(f'Test {k} échoué :  {test} \\n')
        break
else:
    sortie.write("Bravo vous avez réussi tous les tests !!! \\n \\n")
    article = js.document.querySelector("article")
    div1 = js.document.createElement("div")
    div1.innerHTML = """
    <details class="help" open="">
    <summary>Solution 1</summary>
    <div class="highlight">
    <pre id="__code_solution">
    <span></span>
    <button class="md-clipboard md-icon" title="Copier dans le presse-papier" data-clipboard-target="#__code_solution"></button>
    def somme(tab):
        if len(tab) > 0:
            s = 0
            for e in s:
                s = s + e
            return s
        return None
    </pre>
    </details>
    """
    article.appendChild(div1)
    div2 = js.document.createElement("div")
    div2.innerHTML = """
    <details class="help" open="">
    <summary>Solution 2</summary>
    <div class="highlight">
    <pre id="__code_solution2">
    <span></span>
    <button class="md-clipboard md-icon" title="Copier dans le presse-papier" data-clipboard-target="#__code_solution2"></button>
    def somme(tab):
        if len(tab) > 0:
            s = 0
            for k in range(len(tab)):
                s = s + tab[k]
            return s
        return None
    </pre>
    </details>
    """
    article.appendChild(div2)

sortie.getvalue()
