# Solution 1

age = int(input('Votre âge ?')) #doit fonctionner pour toute valeur de type float de note
if age < 0 or age > 130:
    print("Valeur incohérente")
elif  age < 18:
    print("mineur")
elif  age == 18:
    print("Majeur dans l'année")
else:
    print("Majeur")

# Solution 2 (à éviter)

age = int(input('Votre âge ?')) #doit fonctionner pour toute valeur de type float de note
if age < 0 or age > 130:
    print("Valeur incohérente")
else:
    if  age < 18:
        print("mineur")
    else:
        if  age == 18:
            print("Majeur dans l'année")
        else:
            print("Majeur")
