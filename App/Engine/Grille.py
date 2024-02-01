from App.Engine.Jeton import Rond, Croix
from App.Engine.Joueur import Joueur


class Grille:

    def __init__(self):
        # constructeur vide
        # grille de jeu puissance 4 (6 lignes, 7 colonnes) initialisée à null
        self.grille: list[list[Rond | Croix | None]] = [[None for x in range(6)] for y in range(7)]
        pass

    def get_grille(self):
        return self.grille

    def get_colonne(self, colonne: int):
        if not (0 <= colonne < 7):
            raise IndexError("La colonne demandée n'éxiste pas")
        return self.grille[colonne]

    def get_ligne(self, ligne: int):
        if not (0 <= ligne < 6):
            raise IndexError("La ligne demandée n'éxiste pas")
        ligne = [col[ligne] for col in self.grille]
        return ligne

    def est_pleine(self):
        for colonne in self.grille:
            for case in colonne:
                if case is None:
                    return False
        return True

    def get_case(self, ligne: int, colonne: int):
        if not (0 <= ligne < 6):
            raise IndexError("La ligne demandée n'existe pas")
        elif not (0 <= colonne < 7):
            raise IndexError("La colonne demandée n'existe pas")
        else:
            return self.grille[colonne][ligne]

    def placer_pion(self, colonne: int, jeton: Rond | Croix):
        if not (0 <= colonne < 7):
            raise IndexError("La colonne demandée n'existe pas")
        else:
            for ligne in range(6):
                if self.grille[colonne][ligne] is None:
                    self.grille[colonne][ligne] = jeton.get_caractere()
                    return
            raise Exception("La colonne est pleine")

    def jouer_pion(self, joueur: Joueur):
        # TODO: colonne = joueur.choisir_colonne()
        # self.placer_pion(colonne, joueur.get_jeton())
        pass

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

    def est_gagnee(self):
        """
        Détermine si la grille est dite gagnée : quatre
        jetons d'un joueur alignés.

        Analyse sur trois parties :
        - Analyse horizontale
        - Analyse verticale
        - Analyse diagonale

        TODO: appeler la méthode dans "jouer_pion()".

        :return:
        - FALSE si la partie n'est pas encore gagnée
        - ou 'X' ou 'O' en fonction du jeton gagnant
        """
        partie_gagnee = False

        # 1. Analyse horizontale

        for y in self.get_grille():
            for x in y:
                print(f"{x}\t{y}")

        return False  # TODO STUB
