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

puissance = 1
exposant = 0
#invariant 2 ** exposant == puissance
while puissance <= 20000:
    puissance = puissance * 2
    exposant = exposant + 1
    #invariant 2 ** exposant == puissance
print("Puissance : ", puissance, " Exposant : ", exposant)