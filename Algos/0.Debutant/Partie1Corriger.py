"""
Auteur : Alexandre FAUBLADIER--ANETTE
Pseudo : Killex8569
Date : 14/03/2026
"""

import random

# Exo 1.1
def nb(n):
    if not isinstance(n, int):
        return None
    else:
        str = ""
        for i in range(n+1): 
            str += f' {i}' # On intègre i dans une chaine de caractère
        return str


# Exo 1.2
def table_multi(n):
    if not isinstance(n, int):
        return None
    else:
        str = ""
        for i in range(11):
            str += f' {i*n}'
        return str

# Exo 1.3
def affiche_nb_n_k(n, k):
    if not isinstance(n, int):
        return None
    else:
        str = ""
        for i in range(n, k+1):
            str += f" {i}"
        return str


# Exo 1.4

def puissance_2(k, n):
    if not isinstance(n, int):
        return None
    else:
        str = ""
        for i in range(k+1):
            str += f" puissance {i} : {n**i}"
        return str


# Exo 1.5
def random_nb(n, k):
    if not isinstance(n, int) or not isinstance(k, int):
        return None
    else:
        return random.randrange(n, k)


# Exo 1.6
def triangle(n):
    if not isinstance(n, int):
        return None
    else:
        str = ""
        for i in range(n+1):
            str += "\n"
            str += i*"*"
        return str
        
# Exo 1.7
def nb_paires(n):
    if not isinstance(n, int):
        return None
    else:
        liste_paire = []
        for i in range(n+1):
            if i % 2 == 0:
                liste_paire.append(i)
        return liste_paire

# Exo 1.8

def nb_impaire(n):
    if not isinstance(n ,int):
        return None
    else:
        liste_impaire = []
        for i in range(n+1):
            if i % 2 != 0:
                liste_impaire.append(i)
        return liste_impaire
    


# Exo 1.9

def space_letter(chaine):
    newChain = ""
    for i in chaine:
        newChain += f" {i}"
    return newChain

# Exo 1.10

def is_nb_paires(n):
    if not isinstance(n, int):
        return None
    else:
        if n % 2 == 0:
            return True
        return False
        