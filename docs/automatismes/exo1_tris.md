---
title: Thème Tris, tri par sélection
---

{% include 'abbreviations.md' %}

!!! tip "Exercice"

    Écrire deux fonctions :
    
    * `index_minimum_partiel(tab:[int], debut:int)->int` qui prend en paramètre un tableau d'entiers non vide et un index dans ce tableau et renvoie l'index du maximum dans `tab[debut:len(tab)]` 
    * `tri_selection_croissant(tab:[int])->[int]` qui prend en paramètre un tableau d'entiers, le trie en place avec l'algorithme de tri par sélection en utilisant la fonction `index_minimum_partiel` et renvoie le tableau trié.

    Signature des fonctions  et quelques postconditions :

    ~~~python
    def index_minimum_partiel(tab:[int], debut:int)->int:
        #votre code
    
    t = list(range(4))
    assert [index_minimum_partiel(t,k) == k for k in range(len(t))]  #postcondition

    def tri_selection_croissant(tab:[int])->[int]]:
        #votre code

    t2 = [3 - k for k in range(4)]    
    assert tri_selection_croissant(t2) == t
    t3 = []    
    assert tri_selection_croissant(t3) == t3
    ~~~

    _Patience, attendez l'affichage "Prêt" dans la console avant de commencer ! Rafraîchissez si le message n'apparaît pas au bout de quelques secondes._


{{console_perso("tris/exo1/test_exo1_tris.py")}} 