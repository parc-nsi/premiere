def somme(tab):
    if len(tab) > 0:
        s = 0
        for k in range(len(tab)):
            s = s + tab[k]
        return s
    return None
