#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:52:02 2021

@author: fjunier
"""
"""
Référence :
On a 3 piles de 11, 7 et 6 assiettes
On ne peut déplacer des assiettes qu'en diminuant la taille d'une pile
pour doubler la taille d'une autre
Nombre minimal de coups pour avoir 3 piles de même taille
"""

memo = dict()

def minimum_coups(a, b, c, p, chemin):    
    #print(a,b,c)
    memo[(a,b,c)] = p
    if a == b and b == c:  
        print(chemin)
        return 0
    m = float('inf')
    if a >= b and ((a - b, 2 * b, c) not in memo or memo[(a - b, 2 * b, c)] > p):
        m = min(m, 1 + minimum_coups(a - b, 2 * b, c, p + 1, chemin[:] + [(a - b, 2 * b, c)]))
    if b >= a and ((2*a, b - a, c) not in memo or memo[(2*a, b - a, c)] > p):
        m = min(m, 1 + minimum_coups(2*a, b - a, c, p + 1, chemin[:] +[(2*a, b - a, c)]))
    if a >= c and ((a - c, b, 2*c) not in memo or memo[(a - c, b, 2*c)] > p):
        m = min(m, 1 + minimum_coups(a - c, b, 2*c, p + 1, chemin[:] + [(a - c, b, 2*c)]))
    if c >= a and ((2*a, b, c - a) not in memo or memo[(2*a, b, c - a)] > p):
        m = min(m, 1 + minimum_coups(2*a, b, c - a, p + 1, chemin[:] + [(2*a, b, c - a)]))
    if b >= c and ((a, b - c, 2*c) not in memo or memo[(a, b - c, 2*c)] > p ):
        m = min(m, 1 + minimum_coups(a, b - c, 2*c, p + 1, chemin[:] + [(a, b - c, 2*c)]))
    if c >= b and ((a, 2*b, c - b) not in memo or memo[(a, 2*b, c - b)] > p):      
        m = min(m, 1 + minimum_coups(a, 2*b, c - b, p + 1, chemin[:] + [(a, 2*b, c - b)]))
    return m


print(minimum_coups(4,14,6, 0, []))


"""
def minimum_coups(a, b, c, p):
    if p >=  15:
        if a == b and b == c:
            print(True)
        return 0
    if a == b and b == c:
        print(True)
        return 0
    m = float('inf')
    if a >= b:
        m = min(m, 1 + minimum_coups(a - b, 2 * b, c, p + 1))
    if b >= a:
        m = min(m, 1 + minimum_coups(2*a, b - a, c, p + 1))
    if a >= c:
        m = min(m, 1 + minimum_coups(a - c, b, 2*c, p + 1))
    if c >= a:
        m = min(m, 1 + minimum_coups(2*a, b, c - a, p + 1))
    if b >= c:
        m = min(m, 1 + minimum_coups(a, b - c, 2*c, p + 1))
    if c >= b:      
        m = min(m, 1 + minimum_coups(a, 2*b, c - b, p + 1))
    return m


print(minimum_coups(14,16, 30, 0))
"""