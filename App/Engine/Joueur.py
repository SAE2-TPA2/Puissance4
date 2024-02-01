from App.Engine.Jeton import Rond, Croix

class Joueur:
    def __init__(self, pseudo: str, jeton: Rond | Croix, est_humain: bool = True):
        self.pseudo = pseudo
        self.jeton = jeton
        self.est_humain = est_humain

    def get_pseudo(self):
        return self.pseudo

    def get_jeton(self):
        return self.jeton

    def get_est_humain(self):
        return self.est_humain

    def __str__(self):
        return f"{self.pseudo} avec le jeton {self.jeton}"