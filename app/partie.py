from random import shuffle
from app.engine.jeton import Croix, Rond
from app.engine.joueur import Joueur
from app.engine.grille import Grille
import plotly.graph_objects as go


class Partie:
    def __init__(self, joueur_1_est_ia: bool = False, joueur_2_est_ia: bool = False):
        self.nb_tour: int = 0

        methode_evaluation_ia1 = ""
        methode_evaluation_ia2 = ""
        # Si les joueurs sont des IA, demande à l'utilisateur de saisir la méthode d'évaluation
        if joueur_1_est_ia:
            methode_evaluation_ia1 = input("Nom méthode d'évaluation (v2 ou v3) du joueur IA 1 : ")
        if joueur_2_est_ia:
            methode_evaluation_ia2 = input("Nom méthode d'évaluation (v2 ou v3) du joueur IA 2 : ")

        self.joueur_1: Joueur = Joueur("", Croix(), est_humain=not joueur_1_est_ia,
                                       methode_evaluation=methode_evaluation_ia1)
        self.joueur_2: Joueur = Joueur("", Rond(), est_humain=not joueur_2_est_ia,
                                       methode_evaluation=methode_evaluation_ia2)
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

            if joueur_du_tour.get_est_humain():
                print(self.grille)
            else:
                print(f"L'IA {joueur_du_tour.get_pseudo()}({joueur_du_tour.get_jeton()}) réfléchit...")

            # Demande au joueur de choisir une colonne
            numero_colonne_joue = joueur_du_tour.choisir_colonne(self.grille)
            while numero_colonne_joue not in self.grille.coups_possible():
                print("Erreur : Colonne pleine ou inexistante, veuillez choisir une autre colonne")
                numero_colonne_joue = joueur_du_tour.choisir_colonne(self.grille)

            if not joueur_du_tour.get_est_humain():
                print(f"L'IA {joueur_du_tour.get_pseudo()} a choisi la colonne {numero_colonne_joue}")

            # Place le jeton du joueur
            jeton_joue: Rond | Croix = joueur_du_tour.get_jeton()

            # Place le jeton du joueur dans la colonne choisie
            self.grille.placer_pion(numero_colonne_joue, jeton_joue)
            self.nb_tour += 1

            grille_est_gagnee = self.grille.est_gagnee(numero_colonne_joue)

            partie_terminee = grille_est_gagnee is not None or self.grille.grille_est_pleine()

        if grille_est_gagnee == self.joueur_1.get_jeton():
            print("Le joueur", self.joueur_1, "remporte la partie !")
        elif grille_est_gagnee == self.joueur_2.get_jeton():
            print("Le joueur", self.joueur_2, "remporte la partie !")
        else:
            print("Égalité, aucun joueur ne remporte la partie")
        print(self.grille)

        self.affichage_temps_reflexion()

    def affichage_temps_reflexion(self):
        """
        Affiche le temps de réflexion pour chaque joueur sur un graphique.
        On utilise la librairie plotly pour afficher le graphique.
        Le graphique sera afficher dans le navigateur par défaut.
        """
        # Affiche le temps de réflexion pour chaque joueur
        print(
            f"Temps de réflexion pour {self.joueur_1.get_pseudo()} : {sum(self.joueur_1.temp_reflexion) / len(self.joueur_1.temp_reflexion)} secondes")
        print(
            f"Temps de réflexion pour {self.joueur_2.get_pseudo()} : {sum(self.joueur_2.temp_reflexion) / len(self.joueur_2.temp_reflexion)} secondes")

        # Prepare the data
        rounds = list(range(1, self.nb_tour + 1))
        reflection_times_1 = self.joueur_1.temp_reflexion
        reflection_times_2 = self.joueur_2.temp_reflexion
        # Create a line chart for each player
        line_chart_1 = go.Scatter(x=rounds, y=reflection_times_1, mode='lines', name=self.joueur_1.get_pseudo())
        line_chart_2 = go.Scatter(x=rounds, y=reflection_times_2, mode='lines', name=self.joueur_2.get_pseudo())
        # Create a figure and add the line charts to it
        fig = go.Figure(data=[line_chart_1, line_chart_2])
        # Display the figure
        fig.show()
