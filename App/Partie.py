from Engine.Jeton import Croix,Rond
from Engine.Joueur import Joueur
from Engine.Grille import Grille


class Partie:
    def __init__(self):
        self.nb_tour = 1
        self.joueur_1 = Joueur("",Croix())
        self.joueur_2 = Joueur("",Rond())
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
        nb_tour_joue = 1
        
        while self.grille.est_gagner() is None\
            or self.grille.grille_est_pleine():
            jeton_joue = ""    
            if(nb_tour_joue % 2 != 0):
                nb_tour_joue += 1
                while True:
                    #try:
                        numero_colonne_joue = jouer_pion(self.joueur_1)
                        break
                    #except nom_exception: TODO compléter avec le nom de l'exception correspondante
                        # ...    
                jeton_joue = "Croix"               
            else:
                nb_tour_joue += 1
                while True:
                    #try:
                        numero_colonne_joue = jouer_pion(self.joueur_2)
                        break
                    #except nom_exception: TODO compléter avec le nom de l'exception correspondante
                        # ...    
                jeton_joue = "Rond"
            
            self.grille.placer_pion(numero_colonne_joue,jeton_joue)
        if(self.est_gagner == "Croix"):
            print("Le joueur ",self.joueur_1.get_pseudo(), "remporte la partie !")
        else:
            if(self.est_gagner == "Rond"):
                print("Le joueur ",self.joueur_2.get_pseudo(), "remporte la partie !")
            else: 
                print("Égalité, aucun joueur ne remporte la partie")
        
