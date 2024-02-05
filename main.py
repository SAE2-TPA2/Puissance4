from App.Partie import Partie

if __name__ == '__main__':

    # Affichage menu principal et choix de l'utilisateur
    # 1. Joueur vs Joueur
    # 2. Joueur vs IA
    # 3. IA vs IA
    # 4. Quitter

    print("Bienvenue dans le jeu du Puissance 4 !")
    print("Sélectionnez le mode de jeu :")
    print("1. Joueur vs Joueur")
    print("2. Joueur vs IA")
    print("3. IA vs IA")
    print("4. Quitter")

    choix = input("Votre choix : ")
    while choix not in ["1", "2", "3", "4"]:
        print("Choix invalide, veuillez choisir un nombre entre 1 et 4")
        choix = input("Votre choix : ")

    partie = None

    match choix:
        case "1":
            print("Joueur vs Joueur")
            partie = Partie()
        case "2":
            print("Joueur vs IA")
            partie = Partie(joueur_2_est_ia=True)
        case "3":
            print("IA vs IA")
            partie = Partie(joueur_1_est_ia=True, joueur_2_est_ia=True)
        case "4":
            print("Au revoir !")
            exit(0)

    partie.boucle_jeu()
