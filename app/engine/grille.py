from app.engine.jeton import Rond, Croix, Jeton


class Grille:

    def __init__(self):
        # constructeur vide
        # grille de jeu puissance 4 (6 lignes, 7 colonnes) initialisée à null
        # la base de la grille commence à la ligne 0
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

    def grille_est_pleine(self):
        for colonne in range(len(self.grille) - 1):
            if not self.colonne_est_pleine(colonne):
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
            ligne_case_vide = 0
            while ligne_case_vide < 6 and self.get_case(ligne_case_vide, colonne) is not None:
                ligne_case_vide += 1

            if ligne_case_vide < 6:
                self.grille[colonne][ligne_case_vide] = jeton
            else:
                raise Exception(f"La colonne n° {ligne_case_vide} est pleine")

            # for ligne in range(6):
            #     if self.get_case(colonne, ligne) is None:
            #         self.grille[colonne][ligne] = jeton
            #         return

    def est_gagnee(self, indice_colonne_dernier_jeton: int) -> Jeton | None:
        """
        Détermine si la grille est dite gagnée : quatre
        jetons d'un joueur alignés.

        Analyse sur trois parties :
        - Analyse horizontale
        - Analyse verticale
        - Analyse diagonale

        TODO: appeler la méthode dans "jouer_pion()".

        :return: si la partie est gagnée par le pion joué
        """

        dernier_jeton = self.dernier_pion_colonne(indice_colonne_dernier_jeton)
        caractere_dernier_jeton = self.get_case(dernier_jeton, indice_colonne_dernier_jeton).get_caractere()
        nombre_pion_joue = 0

        # Analyse par ligne (verticale)
        for case in self.get_colonne(indice_colonne_dernier_jeton):
            if case is None:
                continue

            if case.get_caractere() == caractere_dernier_jeton:
                nombre_pion_joue += 1

                if nombre_pion_joue == 4:
                    return case
            else:
                break

        nombre_pion_joue = 0

        # Analyse par colonne (horizontale)
        for colonne in range(len(self.grille) - 1):
            case_analysee = self.get_case(dernier_jeton, colonne)

            if case_analysee is None:
                continue

            if case_analysee.get_caractere() == caractere_dernier_jeton:
                nombre_pion_joue += 1

                if nombre_pion_joue == 4:
                    return case_analysee

        # Analyse de la diagonale NO - SE (\)
        x = indice_colonne_dernier_jeton
        y = dernier_jeton
        nombre_pion_joue = 1

        while x < 0 and y > 5:
            x -= 1
            y += 1

            if self.get_case(y, x) is None \
                    or self.get_case(y, x).get_caractere() != caractere_dernier_jeton:

                break

            else:
                nombre_pion_joue += 1

        x = indice_colonne_dernier_jeton
        y = dernier_jeton

        while x < 5 and y > 0:
            x += 1
            y -= 1

            if self.get_case(y, x) is None \
                    or self.get_case(y, x).get_caractere() != caractere_dernier_jeton:

                break

            else:
                nombre_pion_joue += 1

        if nombre_pion_joue == 4:
            return self.get_case(dernier_jeton, indice_colonne_dernier_jeton)

        # TODO: analyse SO - NE
        # TODO: opti?
        
        return None  # TODO STUB

    def coups_possible(self) -> list[int]:
        """
        Retourne la liste des colonnes où un coup est possible
        :return: liste des colonnes où un coup est possible
        """
        return [i for i in range(len(self.grille) - 1) if not self.colonne_est_pleine(i)]

    def __str__(self):
        affichage = " ___" * (len(self.grille)) + "\n"

        for lig in range(len(self.get_colonne(0)) - 1, -1, -1):
            for col in range(len(self.get_grille())):
                pion = " "

                if self.get_case(lig, col) is not None:
                    pion = self.get_case(lig, col).get_caractere()

                affichage += f"| {pion} "

            affichage += "|\n" + ("|___" * len(self.grille)) + "|\n"

        return affichage

    def colonne_est_pleine(self, i) -> bool:
        """
        Retourne True si la colonne est pleine False sinon
        :param i: L'indice de la colonne à tester
        :return:
        """
        return self.get_case(len(self.get_colonne(0)) - 1, i) is not None

    def dernier_pion_colonne(self, indice_colonne: int):
        """
        retourne l'indice de la ligne du dernier pion dans la colonne
        :param indice_colonne:
        :return: indice du dernier pion dans la colonne
        """
        for i in range(5, -1, -1):
            if self.grille[indice_colonne][i] is not None:
                return i

        return None

    def __deepcopy__(self, memodict=None):
        if memodict is None:
            memodict = {}
        grille = Grille()
        grille.grille = [col.copy() for col in self.grille]
        return grille