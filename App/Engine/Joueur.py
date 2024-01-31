class Joueur:
    def __init__(self, pseudo:str, jeton):
        self.pseudo = pseudo
        self.jeton = jeton

    def __str__(self):
        return f"{self.pseudo} avec {self.jeton} jetons"
    