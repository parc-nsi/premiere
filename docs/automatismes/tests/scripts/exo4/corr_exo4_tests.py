#Solution 1
# doit fonctionner pour tout triplet de valeurs de (a,b,c) de type int
a = 841
b = 841
c = 842
if a == b or a == c or b == c:
    print("Au moins deux égales")
else:
    print("Au moins deux différentes")

#Solution 2 : on inverse les blocs en prenant la négation de la condition
# doit fonctionner pour tout triplet de valeurs de (a,b,c) de type int
a = 841
b = 841
c = 842
if a != b and a != c and b != c:
    print("Au moins deux différentes")    
else:
   print("Au moins deux égales")

