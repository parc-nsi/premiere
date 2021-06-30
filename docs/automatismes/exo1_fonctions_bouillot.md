---
title: Thème Fonctions, somme d'un tableau
---

{% include 'abbreviations.md' %}

Test de la console de [Vincent Bouillot](https://bouillotvincent.gitlab.io/pyodide-mkdocs/)

!!! tip "Exercice"

    Écrire une fonction de signature `somme(tab:[int])->int` qui prend en paramètre un tableau d'entiers et renvoie la somme de ses éléments. La fonction doit renvoyer `None` si le tableau est vide

    Signature de la fonction et deux  postconditions :

    ~~~python
    def somme(tab:[int])->int:
        #votre code
        
    assert somme([]) == None  #postcondition
    assert somme([1,2,3]) == 6  #postcondition
    ~~~


{{REPL("fonctions/exo1/exo1_fonctions")}} 