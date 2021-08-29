---
title: Thème boucle while
---

{% include 'abbreviations.md' %}


!!! tip "Exercice"

    On donne ci-dessous la documentation de la fonction `randint` du module `random`.
    
    ~~~python
    In [1]: from random import randint

    In [2]: ??randint
    Signature: randint(a, b)
    Docstring:
    Return random integer in range [a, b], including both end points.
    ~~~

    On peut simuler le lancer d'un dé équilibré à 6 faces avec l'expression `randint(1,6)`.

    Compléter le programme ci-dessous pour qu'il simule une série de lancers  de dés à 6 face jusqu'à l'obtention d'un premier 6 et affiche le nombre de lancers effectués.

    ~~~python
    from random import randint
    compteur = 1
    #à compléter
    ~~~    


{{IDE("exo2/exo2_while")}} 


[Correction](scripts/exo2/corr_exo2_while.py)

