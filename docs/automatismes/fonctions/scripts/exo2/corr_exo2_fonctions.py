# Solution 1

def secondes(h,m,s): 
    """Signature secondes(h:float,m:float,s:float)->float"""  
    #préconditions
    assert h >= 0 and m >= 0 and s >= 0            
    return h * 3600 + m * 60 + s 
