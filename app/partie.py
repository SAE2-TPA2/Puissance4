from app.engine.jeton import Croix, Rond
from app.engine.joueur import Joueur
from app.engine.grille import Grille
from random import shuffle


class Partie:
    def __init__(self, joueur_1_est_ia: bool = False, joueur_2_est_ia: bool = False):
        self.nb_tour: int = 0
        self.joueur_1: Joueur = Joueur("Alice", Croix(), est_humain=not joueur_1_est_ia)
        self.joueur_2: Joueur = Joueur("Bob", Rond(), est_humain=not joueur_2_est_ia)
        self.grille: Grille = Grille()

    def get_nb_tour(self):
        return self.nb_tour

    def get_joueur_1(self):
        return self.joueur_1

    def get_joueur_2(self):
        return self.joueur_2

    def get_grille(self):
        return self.grille

    def boucle_jeu(self):
        """Le jeu se déroule tant que la grille n'est pas pleine ou 
        que le jeu est considéré comme terminé (gagné, perdu, égalité)
        les joueurs vont jouer à tour de rôle jusqu'à la fin du jeu
        """
        ordre_joueurs = [self.joueur_1, self.joueur_2]
        shuffle(ordre_joueurs)

        numero_colonne_joue = 0
        partie_terminee = False
        grille_est_gagnee = False

        while not partie_terminee:
            joueur_du_tour = ordre_joueurs[self.nb_tour % 2]

            print(self.grille)
            # Demande au joueur de choisir une colonne
            numero_colonne_joue = joueur_du_tour.choisir_colonne(self.grille)
            while numero_colonne_joue not in self.grille.coups_possible():
                print("Erreur : Colonne pleine ou inexistante, veuillez choisir une autre colonne")
                numero_colonne_joue = joueur_du_tour.choisir_colonne(self.grille)

            # Place le jeton du joueur
            jeton_joue: Rond | Croix = joueur_du_tour.get_jeton()

            # Place le jeton du joueur dans la colonne choisie
            self.grille.placer_pion(numero_colonne_joue, jeton_joue)
            self.nb_tour += 1

            grille_est_gagnee = self.grille.est_gagnee(numero_colonne_joue)

            partie_terminee = grille_est_gagnee is not None or self.grille.grille_est_pleine()

        if grille_est_gagnee == self.joueur_1.get_jeton():
            print("Le joueur", self.joueur_1.get_pseudo(), "remporte la partie !")
        elif grille_est_gagnee == self.joueur_2.get_jeton():
            print("Le joueur", self.joueur_2.get_pseudo(), "remporte la partie !")
        else:
            print("Égalité, aucun joueur ne remporte la partie")
        print(self.grille)
