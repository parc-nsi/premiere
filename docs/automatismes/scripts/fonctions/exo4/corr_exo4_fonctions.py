# Solution 1

def somme1(n): 
    """Signature somme1(n:int)->int"""  
    s  = 0  #penser à l'initialisation
    for k in range(1, n + 1):
        s = s + k
    #return hors de la boucle
    return s


# Solution 3 : avec vérification de la précondition n >= 0

def somme1bis(n): 
    """Signature somme1bis(n:int)->int"""  
    assert n >= 0   #vérification de la précondition
    s  = 0  #penser à l'initialisation
    for k in range(1, n + 1):
        s = s + k
    #return hors de la boucle
    return s


# Solution 3 : avec la formule de Gauss

def somme1_gauss(n): 
    """Signature somme1bis(n:int)->int"""  
    return n * (n+1) // 2