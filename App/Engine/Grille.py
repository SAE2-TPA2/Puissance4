from App.Engine.Exceptions import ColonnePleineException


class Grille:
    # grille de jeu puissance 4 (6 lignes, 7 colonnes) initialisée à null
    grille = [[None for x in range(7)] for y in range(6)]

    def __init__(self):
        # constructeur vide
        pass

    def getGrille(self):
        return self.grille

    def getColonne(self, colonne: int):
        if colonne < 0 or colonne > 6:
            raise IndexError("La colonne demandée n'existe pas")
        else:
            colonne = [row[colonne] for row in self.grille]
            return colonne

    def getLigne(self, ligne: int):
        if ligne < 0 or ligne > 5:
            raise IndexError("La ligne demandée n'existe pas")
        else:
            ligne = self.grille[ligne]
            return ligne

    def getCase(self, ligne: int, colonne: int):
        if ligne < 0 or ligne > 5:
            raise IndexError("La ligne demandée n'existe pas")
        elif colonne < 0 or colonne > 6:
            raise IndexError("La colonne demandée n'existe pas")
        else:
            case = self.grille[ligne][colonne]
            return case

    def placerPion(self, colonne:int):
        if colonne < 0 or colonne > 6:
            raise IndexError("La colonne demandée n'existe pas")
        else:
            for ligne in range(5, -1, -1):
                if self.grille[ligne][colonne] is None:
                    self.grille[ligne][colonne] = "X"
                    return
            raise ColonnePleineException("La colonne demandée est pleine")