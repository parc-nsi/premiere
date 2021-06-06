import io 
sortie = io.StringIO() 
assert somme([]) == 0
assert somme([1]) == 1
assert somme([1,2]) == 3
assert somme([-1,1]) == 0
sortie.write("tests réussis") 
sortie.getvalue()
