from Engine.Jeton import Croix,Rond
from Engine.Joueur import Joueur
from Engine.Grille import Grille


class Partie:
    def __init__(self):
        self.nbTour = 0
        self.joueur1 = Joueur("",Croix())
        self.joueur2 = Joueur("",Rond())
        self.grille = Grille()

    def placerPion(self,colonne : int):
        """ Place un pion en fonction d'un numéro de colonne
        type de pion déterminer avec le numéro du tour


        Args:
            colonne (int): entier compris entre 1 et 7
        """
        pass

    def boucleJeu(self):
        """

        """
        pass