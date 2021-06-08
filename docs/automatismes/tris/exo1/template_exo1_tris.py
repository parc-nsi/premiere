def index_minimum_partiel(tab:[int], debut:int)->int:
        #votre code
    
t = list(range(4))
assert [index_minimum_partiel(t,k) == k for k in range(len(t))]  #postcondition

def tri_selection_croissant(tab:[int])->[int]:
    #votre code

t2 = [3 - k for k in range(4)]    
assert tri_selection_croissant(t2) == t
t3 = []    
assert tri_selection_croissant(t3) == t3