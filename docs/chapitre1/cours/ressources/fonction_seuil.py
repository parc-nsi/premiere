"""
Problème :
    trouver la plus petite puissance de 2
    supérieure à 20000
    
Pseudo-code :

puissance = 1
exposant = 0
Tant que puissance <= 20000
    puissance = puissance * 2
    exposant = exposant + 1
Afficher puissance, exposant
"""

def seuil(n):
    """
    Paramètres : n de type int
    Valeur renvoyée : un entier naturel
    Postcondition : renvoie le plus petit exposant entier tel que 2 ** exposant > n    
    """
    puissance = 1
    exposant = 0
    #invariant 2 ** exposant == puissance
    while puissance <= n:
        puissance = puissance * 2
        exposant = exposant + 1
        #invariant 2 ** exposant == puissance
    return exposant

#un appel de fonction dans le print
res = seuil(20000)
#affichage du résultat
print(res)