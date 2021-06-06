---
title: Thème Fonctions, somme d'un tableau
---

{% include 'abbreviations.md' %}

!!! tip "Exercice"

    Écrire une fonction de signature `somme(tab:[int])->int` qui prend en paramètre un tableau d'entiers et renvoie la somme de ses éléments. La fonction doit renvoyer `None` si le tableau est vide

    Signature de la fonction et deux  postconditions :

    ~~~python
    def somme(tab:[int])->int:
        #votre code
        
    assert somme([]) == None  #postcondition
    assert somme([1,2,3]) == 6  #postcondition
    ~~~

    _Patience, attendez l'affichage "Prêt" dans la console avant de commencer ! Rafraîchissez si le message n'apparaît pas au bout de quelques secondes._


{{console_perso("fonctions/exo1/test_exo1_fonctions.py")}} 