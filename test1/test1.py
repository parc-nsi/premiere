import io 
sortie = io.StringIO() 
assert somme(1,2) == 3 
sortie.write("tests réussis") 
sortie.getvalue()
