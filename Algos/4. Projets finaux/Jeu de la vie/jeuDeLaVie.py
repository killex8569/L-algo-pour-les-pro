class JDLV:
    def __init__(self):
        self.n_grille = 20
        self.nb_cell = 6
        self.grp_cell = 2
        self.grille = self.create_grille()

    def SetParameter(self, taille_grille, nb_cell, ):
        pass

    def create_grille(self):
        grille = []
        for i in range(self.n_grille):
            ligne = []
            for j in range(self.n_grille):
                ligne.append(0)
            grille.append(ligne)
        return grille
    def __str__(self):
        affichage = ""
        for ligne in self.grille:
            affichage += " ".join(map(str, ligne)) + "\n"
        return affichage
    


