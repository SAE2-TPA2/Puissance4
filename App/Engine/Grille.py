from App.Engine.Exceptions import ColonnePleineException

from App.Engine.Jeton import Rond, Croix


class Grille:

    def __init__(self):
        # constructeur vide
        # grille de jeu puissance 4 (6 lignes, 7 colonnes) initialisée à null
        self.grille: list[list[Rond | Croix | None]] = [[None for x in range(7)] for y in range(6)]
        pass

    def get_grille(self):
        return self.grille

    def get_colonne(self, colonne: int):
        if not (0 <= colonne < 7):
            raise IndexError("La colonne demandée n'éxiste pas")
        colonne = [row[colonne] for row in self.grille]
        return colonne

    def get_ligne(self, ligne: int):
        if not (0 <= ligne < 6):
            raise IndexError("La ligne demandée n'éxiste pas")

        ligne = self.grille[ligne]
        return ligne

    def get_case(self, ligne: int, colonne: int):
        if not (0 <= ligne < 6):
            raise IndexError("La ligne demandée n'existe pas")
        elif not (0 <= colonne < 7):
            raise IndexError("La colonne demandée n'existe pas")
        else:
            return self.grille[ligne][colonne]

    def placer_pion(self, colonne: int, jeton: Rond | Croix):
        if not (0 <= colonne < 7):
            raise IndexError("La colonne demandée n'existe pas")
        else:
            for ligne in range(5):
                if self.grille[ligne][colonne] is None:
                    self.grille[ligne][colonne] = jeton.get_caractere()
                    return
            raise ColonnePleineException("La colonne demandée est pleine")

    def __str__(self):
        affichage = ""
        for col in range(len(self.grille[0]) - 1, 0, -1):
            for lig in range(len(self.grille)):
                pion = " "
                if self.grille[lig][col] is not None:
                    pion = self.grille[lig][col].get_caractere()
                affichage = "|" + pion
            affichage + "|\n"
        return affichage
