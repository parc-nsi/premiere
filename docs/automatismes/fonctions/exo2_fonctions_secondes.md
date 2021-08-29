---
title: Thème Fonctions, opérations arithmétiques
---

{% include 'abbreviations.md' %}

Exercice tiré de  [Progalgo](https://progalgo.fr/) de Julien de Villèle.

!!! tip "Exercice"

    Compléter la fonction `secondes` ci-dessous pour qu'elle convertisse en secondes un triplet (heure h, minutes m, secondes s). 
    On donne :
        * des préconditions que doivent vérifier les valeurs de h, m et s
        * un jeu de tests unitaires : des postconditions sur les valeurs renvoyées
        par la fonction dans certains cas.        
        
    ~~~python
    def secondes(h,m,s): 
        """Signature secondes(h:float,m:float,s:float)->float"""  
        #préconditions
        assert h >= 0 and m >= 0 and s >= 0            
        return "à compléter"

    assert secondes(1,1,1) == 3661
    assert secondes(1,0,1) == 3601
    ~~~


{{IDE("exo2/exo2_fonctions")}} 