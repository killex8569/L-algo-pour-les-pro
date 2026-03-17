from jeuDeLaVie import JDLV as jdlv


def menu():
    while True:
        try:
            print("1 - Lancer la simulation\n2 - Définir des paramètres")
            rep_user = int(input("Votre choix : "))

        except ValueError:
            print("Erreur, veuillez recommencer")
            continue
        match rep_user:
            case 1:
                JDLV = jdlv()
                print(JDLV)

menu()