from App.Engine.Jeton import Croix, Rond
from App.Engine.Joueur import Joueur
from App.Engine.Grille import Grille


class Partie:
    def __init__(self, joueur_1_ia: bool = False, joueur_2_ia: bool = False):
        self.nb_tour = 0
        self.joueur_1 = Joueur("", Croix(), joueur_1_ia)
        self.joueur_2 = Joueur("", Rond(), joueur_2_ia)
        self.grille = Grille()

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
        que le jeu est considéré comme terminé(gagné,perdu,égalité)
        les joueurs vont jouer à tour de rôle jusqu'a la fin du jeu 
        """

        while self.grille.est_gagnee() is None \
                or self.grille.grille_est_pleine():

            joueur_du_tour = self.joueur_1 if self.nb_tour % 2 == 0 else self.joueur_2

            while True:
                # try:
                numero_colonne_joue = self.grille.jouer_pion(joueur_du_tour)
                break
            # except nom_exception: TODO compléter avec le nom de l'exception correspondante
            # ...

            jeton_joue: Rond | Croix = joueur_du_tour.get_jeton()
            self.grille.placer_pion(numero_colonne_joue, jeton_joue)
            self.nb_tour += 1

        if self.grille.est_gagnee() == "Croix":
            print("Le joueur ", self.joueur_1.get_pseudo(), "remporte la partie !")
        elif self.grille.est_gagnee() == "Rond":
            print("Le joueur ", self.joueur_2.get_pseudo(), "remporte la partie !")
        else:
            print("Égalité, aucun joueur ne remporte la partie")
