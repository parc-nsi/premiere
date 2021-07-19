
#variable globale
chiffres_hexa = {str(k) : k for k in range(10) }
k = 10
for c in 'ABCDEF':
    chiffres_hexa[c] = k
    k = k + 1
#postcondition
assert chiffres_hexa == {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
'7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def hexa_vers_decimal(chaine_hexa):
    """
    Paramètre : chaine_hexa de type str
    Valeur renvoyée : decimal de type int, conversion en base dix de la représentation
    heaxdécimale d'un nombre
    """
    decimal = 0
    for c in chaine_hexa:
        decimal = decimal * 16 +  chiffres_hexa[c]
    return decimal

#test unitaire
assert [hexa_vers_decimal(c) for c in ['FF', '00', '0A', 'A9']] == [255,0,10,169]

def mac_adresse_vers_decimal(mac_adresse):
    """
    Paramètre : mac_adresse de type str, sous la forme '8D:A9:D5:67:E6:F3'
    Valeur renvoyée : tableau de six nombres de type int, conversion en base dix de chaque champ de l'adresse MAC
    """
    champs = mac_adresse.split(':')
    return [hexa_vers_decimal(chaine_hexa) for chaine_hexa in champs]

#test unitaire
assert mac_adresse_vers_decimal('8D:A9:D5:67:E6:F3') == [141, 169, 213, 103, 230, 243]
assert mac_adresse_vers_decimal('FF:FF:FF:FF:FF:FF') == [255, 255, 255, 255, 255, 255]
