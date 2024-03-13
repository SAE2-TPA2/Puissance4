from app.partie import Partie


def affichage_menu() -> str:
    """
    Affiche le menu principal et demande à l'utilisateur de choisir un mode de jeu
    :return: le choix de l'utilisateur
    """
    # Affichage menu principal et choix de l'utilisateur
    # 1. Joueur vs Joueur
    # 2. Joueur vs IA
    # 3. IA vs IA
    # 4. Quitter
    print("""
    +----------------------------------------+
    | Bienvenue dans le jeu du Puissance 4 ! |
    | Sélectionnez le mode de jeu :          |
    |     1. Joueur vs Joueur                |
    |     2. Joueur vs IA                    |
    |     3. IA vs IA                        |
    |     4. Quitter                         |
    +----------------------------------------+
    """)
    choix_input = input("Votre choix : ")
    while choix_input not in ["1", "2", "3", "4"]:
        print("Choix invalide, veuillez choisir un nombre entre 1 et 4")
        choix_input = input("Votre choix : ")

    return choix_input


def joueur_vs_joueur():
    print("Joueur vs Joueur")
    return Partie()


def joueur_vs_ia():
    print("Joueur vs IA")
    return Partie(joueur_2_est_ia=True)


def ia_vs_ia():
    print("IA vs IA")
    return Partie(joueur_1_est_ia=True, joueur_2_est_ia=True)


if __name__ == '__main__':

    print("""
 _______             __                                                                   __    __ 
/       \\           /  |                                                                 /  |  /  |
$$$$$$$  | __    __ $$/   _______  _______   ______   _______    _______   ______        $$ |  $$ |
$$ |__$$ |/  |  /  |/  | /       |/       | /      \\ /       \\  /       | /      \\       $$ |__$$ |
$$    $$/ $$ |  $$ |$$ |/$$$$$$$//$$$$$$$/  $$$$$$  |$$$$$$$  |/$$$$$$$/ /$$$$$$  |      $$    $$ |
$$$$$$$/  $$ |  $$ |$$ |$$      \\$$      \\  /    $$ |$$ |  $$ |$$ |      $$    $$ |      $$$$$$$$ |
$$ |      $$ \\__$$ |$$ | $$$$$$  |$$$$$$  |/$$$$$$$ |$$ |  $$ |$$ \\_____ $$$$$$$$/             $$ |
$$ |      $$    $$/ $$ |/     $$//     $$/ $$    $$ |$$ |  $$ |$$       |$$       |            $$ |
$$/        $$$$$$/  $$/ $$$$$$$/ $$$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/  $$$$$$$/             $$/ 


""")

    # Créez un dictionnaire pour mapper les choix de l'utilisateur sur les fonctions correspondantes
    choices = {
        "1": joueur_vs_joueur,
        "2": joueur_vs_ia,
        "3": ia_vs_ia,
    }
    choix = 0
    while choix != "4":
        choix = affichage_menu()
        if choix != "4":
            # Récupérez la fonction dans le dictionnaire et appelez-la
            partie = choices.get(choix)()
            partie.boucle_jeu()

    print("Au revoir !")
