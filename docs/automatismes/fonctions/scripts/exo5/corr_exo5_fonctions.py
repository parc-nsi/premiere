# Solution 1

def factorielle(n): 
    """Signature factorielle(n:int)->int
    Précondition : n >= 0
    Postcondition : 
    renvoie 1 si n == 0 ou le produit 
    des entiers successifs entre 1 et n    
    """  
    #précondition
    assert n >= 0
    p = 1
    for k in range(2, n + 1):
        p = p * k
    return p

# Solution 2 (Paradigme fonctionnel niveau terminale)
from functools import reduce 

def produit(x, y):
    return x * y

def factorielle2(n):
    assert n >= 0
    return reduce(produit, range(1, n + 1), 1)

