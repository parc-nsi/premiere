# Solution 1

def valeur_absolue(x): 
    """Signature valeur_absolue(x:float)->float"""  
    if x >= 0:
        return x
    else:
        return -x


# Solution 2

def valeur_absolue(x): 
    """Signature valeur_absolue(x:float)->float"""  
    if x >= 0:
        return x
    #else inutile si return dans le if
    return -x
