def minListe(liste):
    if not isinstance(liste, list):
        return None
    else:
        for i in range(len(liste)):
            if not isinstance(liste[i], int):
                return None
        min = liste[0]
        for i in range(len(liste)):
            if liste[i] < min:
                min = liste[i]
        return min
    

def maxListe(liste):
    if not isinstance(liste, list):
        return None
    else:
        for i in range(len(liste)):
            if not isinstance(liste[i], int):
                return None
        max = liste[0]
        for i in range(len(liste)):
            if liste[i] > max:
                max = liste[i]
        return max