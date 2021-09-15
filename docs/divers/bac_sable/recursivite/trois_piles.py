"""
Référence :
On a 3 piles de 11, 7 et 6 assiettes
On ne peut déplacer des assiettes qu'en diminuant la taille d'une pile
pour doubler la taille d'une autre
Nombre minimal de coups pour avoir 3 piles de même taille
"""


def minimum_coups(a, b, c, p):
    if p >= 10:
        return 0
    if a == b and b == c:
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


print(minimum_coups(11,7, 6, 0))