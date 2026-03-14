import somme_liste as sl
import MinMaxList as minmaxl

liste_exemple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, -5]
liste_erreur = [1, 2, 3, 4, 5, "Test", 6, 7, 8, 9, 10, 5, -5]

# Exo Somme liste
print("resultat attendu : 55 ==>", sl.somme(liste_exemple))
print("resultat attendu : None ==>", sl.somme(liste_erreur))


# Exo minmaxl
print("resultat attendu : -5 ==>", minmaxl.minListe(liste_exemple))
print("resultat attendu : None ==>", minmaxl.minListe(liste_erreur))
print("resultat attendu : 10 ==>", minmaxl.maxListe(liste_exemple))
print("resultat attendu : None ==>", minmaxl.maxListe(liste_erreur))