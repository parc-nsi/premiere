# Fonction de tri dans l'ordre croissant par sélection du maximum

def indice_maximum(tab, debut, fin):
    """
    Paramètres : 
        tab un tableau d'entiers
        debut un entier indice du début de la plage
        fin un entier indice de la fin de la plage (inclus)
    Valeur renvoyée : l'indice de la première occurence du maximum de tab 
    dans la plage  de valeurs entre les indice et debut et fin (inclus)
    """
    imax = "à modifier"
    for i in range(debut + 1, fin + 1):
        if "à modifier":
            imax = "à modifier"
    return imax
    
    
def tri_selection(tab):
    """
    Paramètre : tab un tableau de nombres
    Valeur renvoyée : tab
    Postcondition : valeur renvoyée de tab triée dans l'ordre croissant
    """
    i = len(tab) - 1
    while i >= 1:
        imax = indice_maximum(tab, "à modifier", "à modifier")
        tab[i], tab[imax] =  "à modifier"
        # assertion qui doit être vérifiée
        assert max(tab[:i+1]) == tab[i]
        i = "à modifier"
    return tab 
    
# Tests unitaires

import random


def test_indice_maximum(fonction_indice_maximum):
    #tableaux aléatoires
    for size in range(1, 10):
        tab = [random.randint(0, 100) for _ in range(size)]
        assert fonction_indice_maximum(tab, 0, len(tab) - 1) == tab.index(max(tab))
    print(f"Tests unitaires réussis pour {fonction_indice_maximum.__name__}")
    
def test_tri(fonction_tri):
    """Test unitaire d'une fonction de tri"""
    #tableaux déjà triés
    for size in range(0, 10):
        tab = list(range(0, size))
        assert fonction_tri(tab) == sorted(tab), f"echec sur {tab}"
    #tableaus triés dans l'ordre inverse
    for size in range(0, 11):
        tab = list(range(9 - size, -1, -1))
        assert fonction_tri(tab) == sorted(tab), f"echec sur {tab}"
    #tableaux aléatoires
    for size in range(0, 10):
        tab = [random.randint(0, 100) for _ in range(size)]
        assert fonction_tri(tab) == sorted(tab), f"echec sur {tab}"
    print(f"Tests unitaires réussis pour {fonction_tri.__name__}")

#désactiver pour effectuer les tests unitaire      
#test_indice_maximum(indice_maximum)
#test_tri(tri_selection)