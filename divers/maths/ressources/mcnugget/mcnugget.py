#!/usr/bin/python3

def est_decomposable(n, a, b):
    """Renvoie un booléen indiquant si n décomposable
    comme n = a * x + b * y
    """
    while n >= 0 and n % 7 != 0:
        n = n - 5
    return n >= 0

def liste_decomposable(a, b, bsup):
    """Renvoie la liste des entiers <= bsup non décomposables
    sous la forme a*x + b * y"""
    return [n for n in range(bsup) if not est_decomposable(n,a,b) ]

print(liste_decomposable(5, 7, 100))
