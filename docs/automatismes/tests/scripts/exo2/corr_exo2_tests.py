# Solution 1

note = 5 #doit fonctionner pour toute valeur de type float de note
if 0 <= note < 8:
    print("Recalé")
elif  note < 10:
    print("Second groupe")
elif  note < 12:
    print("Reçu")
elif  note < 14:
    print("Assez bien")
elif  note < 16:
    print("Bien")
elif note <= 20:
    print("Très bien")
else:
    print("Valeur incohérente")

# Solution 2 (à éviter)

note = 5 #doit fonctionner pour toute valeur de type float de note
if 0 <= note < 8:
    print("Recalé")
else:
    if  note < 10:
        print("Second groupe")
    else:
        if  note < 12:
            print("Reçu")
        else:
            if  note < 14:
                print("Assez bien")
            else:
                if  note < 16:
                    print("Bien")
                else:
                    if note <= 20:
                        print("Très bien")
                    else:
                        print("Valeur incohérente")

