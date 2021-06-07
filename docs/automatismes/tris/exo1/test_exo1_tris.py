import io
import random
import js


def index_minimum_partiel_correction(tab:[int], debut:int)->int:
    imin = debut
    for k in range(debut + 1, len(tab)):
        if tab[k] < tab[imin]:
            imin = k
    return imin

def tri_selection_croissant_correction(tab:[int])->[int]:
    for k in range(len(tab) - 1):
        imin = index_minimum_partiel_correction(tab, k)
        tab[imin], tab[k] = tab[k], tab[imin]

sortie = io.StringIO() 
sortie.write('Tests de index_minimum_partiel \\n \\n')
tab_unitaire = [random.randint(1, 100)]
tab_croissant = [k for k in range(1, 4)]
tab_decroissant = [4 - k for k in range(1, 4)]
tab_aleatoire = [random.randint(1, 100) for _ in range(4)]
benchmark = [(0, tab_unitaire, f'index_minimum_partiel({tab_unitaire}, 0)', f'tri_selection_croissant({tab_unitaire})'),(0, tab_croissant, f'index_minimum_partiel({tab_croissant}, 1)',f'tri_selection_croissant({tab_croissant})'), (0, tab_decroissant, f'index_minimum_partiel({tab_decroissant}, 2)',f'tri_selection_croissant({tab_decroissant})'), (1, tab_aleatoire, f'index_minimum_partiel({tab_aleatoire}, 3)', f'tri_selection_croissant({tab_aleatoire})')]
for i, (j, tab, test, tri) in enumerate(benchmark, 1):
    if index_minimum_partiel(tab, i) == index_minimum_partiel_correction(tab, i):
        sortie.write(f"Test {i} réussi : {test} \\n")
    else:
        sortie.write(f"Test {i} échoué \\n")
        break
else:
    sortie.write("Bravo, tests réussis pour index_minimum_partiel \\n \\n")
    sortie.write('Tests de tri_selection_croissant \\n \\n')
    for i, (j, tab, test, tri) in enumerate(benchmark, 1):
        if tri_selection_croissant(tab) == tri_selection_croissant_correction(tab):
            sortie.write(f"Test {i} réussi : {tri} \\n")
        else:
            sortie.write(f"Test {i} échoué \\n")
            break
    else:        
        sortie.write("Bravo, tests réussis pour tri_selection_croissant !!! \\n \\n")
        sortie.write("Bravo vous avez réussi tous les tests !!! \\n \\n")
        article = js.document.querySelector("article")
        div1 = js.document.createElement("div")
        div1.innerHTML = """
        <details class="help" open="">
        <summary>Solution <code>index_minimum_partiel</code></summary>
        <div class="highlight">
        <pre id="__code_solution">
        <span></span>
        <button class="md-clipboard md-icon" title="Copier dans le presse-papier" data-clipboard-target="#__code_solution"></button>
        def index_minimum_partiel_correction(tab:[int], debut:int)->int:
            imin = debut
            for k in range(debut + 1, len(tab)):
                if tab[k] < tab[imin]:
                    imin = k
            return imin
        </pre>
        </details>
        """
        article.appendChild(div1)
        div2 = js.document.createElement("div")
        div2.innerHTML = """
        <details class="help" open="">
        <summary>Solution <code>tri_selection_croissant</code></summary>
        <div class="highlight">
        <pre id="__code_solution2">
        <span></span>
        <button class="md-clipboard md-icon" title="Copier dans le presse-papier" data-clipboard-target="#__code_solution2"></button>
        def tri_selection_croissant_correction(tab:[int])->[int]:
            for k in range(len(tab) - 1):
                imin = index_minimum_partiel_correction(tab, k)
                tab[imin], tab[k] = tab[k], tab[imin]
        </pre>
        </details>
        """
        article.appendChild(div2)
sortie.getvalue()
