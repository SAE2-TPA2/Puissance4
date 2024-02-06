from app.engine.jeton import Rond, Croix, Jeton


class Grille:
    """
    La classe Grille permet de gérer la grille de jeu du puissance 4
    """

    def __init__(self):
        """
        Constructeur de la classe Grille
        """
        # grille de jeu puissance 4 (6 lignes, 7 colonnes) initialisée à null
        # la base de la grille commence à la ligne 0
        self.grille: list[list[Rond | Croix | None]] = [[None for x in range(6)] for y in range(7)]

    def get_grille(self):
        """
        :return: la grille de jeu
        """
        return self.grille

    def get_colonne(self, colonne: int):
        """
        permet de récupérer une colonne de la grille
        :param colonne: l'indice de la colonne
        :return: la colonne demandée
        """
        if not 0 <= colonne < 7:
            raise IndexError("La colonne demandée n'existe pas")
        return self.grille[colonne]

    def get_ligne(self, ligne: int):
        """
        permet de récupérer une ligne de la grille
        :param ligne: l'indice de la ligne
        :return: la ligne demandée
        """
        if not 0 <= ligne < 6:
            raise IndexError("La ligne demandée n'existe pas")
        ligne = [col[ligne] for col in self.grille]
        return ligne

    def grille_est_pleine(self):
        """
        Vérifie si la grille est pleine
        :return: True si la grille est pleine, False sinon
        """
        for colonne in range(len(self.grille) - 1):
            if not self.colonne_est_pleine(colonne):
                return False
        return True

    def get_case(self, ligne: int, colonne: int):
        """
        Permet de récupérer une case de la grille
        :param ligne: l'indice de la ligne
        :param colonne: l'indice de la colonne
        :return: la case demandée
        """
        if not 0 <= ligne < 6:
            raise IndexError("La ligne demandée n'existe pas")
        if not 0 <= colonne < 7:
            raise IndexError("La colonne demandée n'existe pas")
        return self.grille[colonne][ligne]

    def placer_pion(self, colonne: int, jeton: Rond | Croix):
        """
        Permet de placer un jeton dans une colonne
        :param colonne: l'indice de la colonne
        :param jeton: le jeton à placer
        """
        if not 0 <= colonne < 7:
            raise IndexError("La colonne demandée n'existe pas")

        ligne_case_vide = 0
        while ligne_case_vide < 6 and self.get_case(ligne_case_vide, colonne) is not None:
            ligne_case_vide += 1

        if ligne_case_vide < 6:
            self.grille[colonne][ligne_case_vide] = jeton
        else:
            raise Exception(f"La colonne n° {ligne_case_vide} est pleine")

    def verification_verticale(self, indice_colonne_dernier_jeton: int) -> tuple[int, Jeton]:
        """
        Mesure d'une potentielle série verticale, à partir de l'indice de colonne
        du dernier jeton joué.

        :param indice_colonne_dernier_jeton:
        :return: La taille et le jeton de la potentielle série
        """
        dernier_jeton = self.dernier_pion_colonne(indice_colonne_dernier_jeton)
        caractere_dernier_jeton = self.get_case(dernier_jeton, indice_colonne_dernier_jeton)
        caractere_dernier_jeton = caractere_dernier_jeton.get_caractere()

        nombre_pion_joue = 1
        y = dernier_jeton

        while y > 0 and nombre_pion_joue < 4:
            y -= 1

            if (self.get_case(y, indice_colonne_dernier_jeton) is None
                    or self.get_case(y, indice_colonne_dernier_jeton)
                           .get_caractere() != caractere_dernier_jeton):

                break

            nombre_pion_joue += 1

        return nombre_pion_joue, self.get_case(y, indice_colonne_dernier_jeton)

    def verification_horizontale(self, indice_colonne_dernier_jeton: int) -> tuple[int, Jeton]:
        """
        Mesure d'une potentielle série horizontale, à partir de l'indice de colonne
        du dernier jeton joué.

        :param indice_colonne_dernier_jeton:
        :return: La taille et le jeton de la potentielle série
        """
        dernier_jeton = self.dernier_pion_colonne(indice_colonne_dernier_jeton)
        caractere_dernier_jeton = self.get_case(dernier_jeton, indice_colonne_dernier_jeton)
        caractere_dernier_jeton = caractere_dernier_jeton.get_caractere()

        nombre_pion_joue = 1
        x = indice_colonne_dernier_jeton

        while x > 0 and nombre_pion_joue < 4:
            x -= 1

            if self.get_case(dernier_jeton, x) is None \
                    or self.get_case(dernier_jeton, x).get_caractere() != caractere_dernier_jeton:
                break

            if self.get_case(dernier_jeton, x).get_caractere() == caractere_dernier_jeton:
                nombre_pion_joue += 1

        x = indice_colonne_dernier_jeton

        while x < 5 and nombre_pion_joue < 4:
            x += 1

            if self.get_case(dernier_jeton, x) is None \
                    or self.get_case(dernier_jeton, x).get_caractere() != caractere_dernier_jeton:
                break

            if self.get_case(dernier_jeton, x).get_caractere() == caractere_dernier_jeton:
                nombre_pion_joue += 1

        return nombre_pion_joue, self.get_case(dernier_jeton, x)

    def verification_diagonale_no_se(self, indice_colonne_dernier_jeton: int) -> tuple[int, Jeton]:
        """
        Mesure d'une potentielle série NO - SE, à partir de l'indice de colonne
        du dernier jeton joué.

        :param indice_colonne_dernier_jeton:
        :return: La taille et le jeton de la potentielle série
        """
        dernier_jeton = self.dernier_pion_colonne(indice_colonne_dernier_jeton)
        caractere_dernier_jeton = self.get_case(dernier_jeton, indice_colonne_dernier_jeton)
        caractere_dernier_jeton = caractere_dernier_jeton.get_caractere()

        x = indice_colonne_dernier_jeton
        y = dernier_jeton
        nombre_pion_joue = 1

        while x < 0 and y > 5 and nombre_pion_joue < 4:
            x -= 1
            y += 1

            if self.get_case(y, x) is None \
                    or self.get_case(y, x).get_caractere() != caractere_dernier_jeton:

                break

            nombre_pion_joue += 1

        x = indice_colonne_dernier_jeton
        y = dernier_jeton

        while x < 5 and y > 0 and nombre_pion_joue < 4:
            x += 1
            y -= 1

            if self.get_case(y, x) is None \
                    or self.get_case(y, x).get_caractere() != caractere_dernier_jeton:

                break

            nombre_pion_joue += 1

        return nombre_pion_joue, self.get_case(y, x)

    def verification_diagonale_so_ne(self, indice_colonne_dernier_jeton: int):
        """
        Mesure d'une potentielle série SO - NE, à partir de l'indice de colonne
        du dernier jeton joué.

        :param indice_colonne_dernier_jeton:
        :return: La taille et le jeton de la potentielle série
        """
        dernier_jeton = self.dernier_pion_colonne(indice_colonne_dernier_jeton)
        caractere_dernier_jeton = self.get_case(dernier_jeton, indice_colonne_dernier_jeton)
        caractere_dernier_jeton = caractere_dernier_jeton.get_caractere()

        x = indice_colonne_dernier_jeton
        y = dernier_jeton
        nombre_pion_joue = 1

        while x > 0 and y > 0 and nombre_pion_joue < 4:
            x -= 1
            y -= 1

            if self.get_case(y, x) is None \
                    or self.get_case(y, x).get_caractere() != caractere_dernier_jeton:

                break

            nombre_pion_joue += 1

        x = indice_colonne_dernier_jeton
        y = dernier_jeton

        while x < 5 and y < 4 and nombre_pion_joue < 4:
            x += 1
            y += 1

            if self.get_case(y, x) is None \
                    or self.get_case(y, x).get_caractere() != caractere_dernier_jeton:

                break
            nombre_pion_joue += 1

        return nombre_pion_joue, self.get_case(y, x)

    def est_gagnee(self, indice_colonne_dernier_jeton: int) -> Jeton | None:
        """
        Détermine si la grille est dite gagnée : quatre
        jetons d'un joueur alignés.

        Analyse sur quatre parties :
        - Analyse horizontale
        - Analyse verticale
        - Analyse diagonale NO - SE
        - Analyse diagonale SO - NE

        :return: si la partie est gagnée par le pion joué
        """

        dernier_jeton = self.dernier_pion_colonne(indice_colonne_dernier_jeton)
        caractere_dernier_jeton = self.get_case(dernier_jeton, indice_colonne_dernier_jeton)
        caractere_dernier_jeton = caractere_dernier_jeton.get_caractere()

        # Analyse par ligne (verticale)
        verticale = self.verification_verticale(indice_colonne_dernier_jeton)

        if verticale[0] == 4 and verticale[1] is not None:
            return verticale[1]

        # Analyse par colonne (horizontale)
        horizontale = self.verification_horizontale(indice_colonne_dernier_jeton)

        if horizontale[0] == 4 and horizontale[1] is not None:
            return horizontale[1]

        # Analyse de la diagonale NO - SE (\)
        nose = self.verification_diagonale_no_se(indice_colonne_dernier_jeton)

        if nose[0] == 4 and nose[1] is not None:
            return nose[1]

        # Analyse de la diagonale SO - NE (/)
        sone = self.verification_diagonale_so_ne(indice_colonne_dernier_jeton)

        if sone[0] == 4 and sone[1] is not None:
            return sone[1]

        # peut etre les boucles sont optimisables

    def coups_possible(self) -> list[int]:
        """
        Retourne la liste des colonnes où un coup est possible
        :return: liste des colonnes où un coup est possible
        """
        return [i for i in range(len(self.grille)) if not self.colonne_est_pleine(i)]

    def __str__(self):
        affichage = ""
        for i in range(len(self.grille)):
            affichage += f"  {i} "

        affichage += "\n" + " ___" * (len(self.grille)) + "\n"

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
