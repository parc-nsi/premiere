#Solution 1
# doit fonctionner pour tout triplet de valeurs de (a,b,c) de type int
a = 841
b = 841
c = 842
if a == b and b == c:
    print("Toutes égales")
else:
    print("Pas toutes égales")

#Solution 2 : on inverse les blocs en prenant la négation de la condition
# doit fonctionner pour tout triplet de valeurs de (a,b,c) de type int
a = 841
b = 841
c = 842
if a != b or b != c:
    print("Pas toutes égales")    
else:
    print("Toutes égales")