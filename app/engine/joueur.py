import time

from app.engine.jeton import Rond, Croix, Jeton
from app.engine.grille import Grille
from app.engine.ai.ai import min_max


class Joueur:
    def __init__(self, pseudo: str, jeton: Jeton, est_humain: bool = True):
        self.pseudo = pseudo
        self.jeton = jeton
        self.est_humain = est_humain
        self.profondeur = 6

        self.temp_reflexion = []

    def get_pseudo(self):
        return self.pseudo

    def get_jeton(self):
        return self.jeton

    def get_est_humain(self):
        return self.est_humain

    def choisir_colonne(self, grille: Grille)->int:
        """
        Demande au joueur de choisir une colonne pour placer son pion
        Si le joueur n'est pas humain, la colonne est choisie grâce à la méthode min-max
        :param grille:
        :return:
        """
        if self.est_humain:
            t0 = time.time()
            colonne = input(f"Joueur {self.pseudo} choisissez une colonne : ")

            while not colonne.isdigit():
                print("Erreur : Veillez saisir un entier")
                colonne = input(f"Joueur {self.pseudo} choisissez une colonne : ")
            t1 = time.time()
            colonne = int(colonne)
            self.temp_reflexion.append(t1 - t0)
        else:
            nouveau_jeton = Rond() if self.jeton == Croix() else Croix()

            if len(grille.coups_possible()) < 4:
                self.profondeur += 1

            t0 = time.time()
            colonne = min_max(grille, self.profondeur, self.jeton, nouveau_jeton, self.jeton)
            t1 = time.time()

            if t1 - t0 < 4:
                self.profondeur += 1
                print("////Profondeur augmentée à ", self.profondeur, "////")

            print("Temps de calcul : ", t1 - t0, " secondes")
            self.temp_reflexion.append(t1 - t0)

        return colonne

    def __str__(self):
        return f"{self.pseudo} avec le jeton {self.jeton}"
