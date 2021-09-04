#Définition de fonctions
def f(x):
    return x ** 2 - 3

## Programme principal

#entrées
a = float(input('Borne inférieure ? '))
b = float(input('Borne supérieure ? '))
s = float(input("Seuil de l'encadrement ?"))

#traitement 
while b - a > s: #boucle conditionnelle
    m = (a+b)/2  #affectation
    if f(m) < 0: #branchement
        a = m
    else:
        b = m

#sorties
print(a, "<= racine(3) <= ", b)