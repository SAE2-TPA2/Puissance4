from Jeton import Rond, Croix


class Joueur:
    def __init__(self, pseudo: str, jeton: Rond | Croix, est_humain: bool = True):
        self.pseudo = pseudo
        self.jeton = jeton
        self.est_humain = est_humain

    def __str__(self):
        return f"{self.pseudo} avec le jeton {self.jeton}"
