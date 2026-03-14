def somme(liste):
    if not isinstance(liste, list):
        return None
    else:
        for i in range(len(liste)):
            if not isinstance(liste[i], int):
                return None 
        s = 0
        for i in range(len(liste)):
            s += liste[i]
        return s
