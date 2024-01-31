from prettytable import PrettyTable

class Grille:

    # grille de jeu puissance 4 (6 lignes, 7 colonnes) initialisée à null
    grille = [[None for x in range(7)] for y in range(6)]

    def __init__(self):
        # constructeur vide
        pass

    def __str__(self):
        table = PrettyTable()
        for row in self.grille:
            table.add_row(row)
        print(table)

    def getGrille(self):
        return self.grille


    def getColonne(self, colonne: int):
        if colonne < 0 or colonne > 6:
            raise Exception("La colonne demandée n'existe pas")
        else:
            colonne = [row[colonne] for row in self.grille]
            return colonne

    def getLigne(self, ligne: int):
        if ligne < 0 or ligne > 5:
            raise Exception("La ligne demandée n'existe pas")
        else:
            ligne = self.grille[ligne]
            return ligne

