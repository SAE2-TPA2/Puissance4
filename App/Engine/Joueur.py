from Jeton import Rond, Croix

class Joueur:
    def __init__(self, pseudo: str, jeton: Rond | Croix):
        self.pseudo = pseudo
        self.jeton = jeton

    def __str__(self):
        return f"{self.pseudo} avec le jeton {self.jeton}"
