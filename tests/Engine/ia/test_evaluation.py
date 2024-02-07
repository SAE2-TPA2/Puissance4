import unittest

from app.engine.grille import Grille
from app.engine.jeton import Croix, Rond
from app.engine.ai.ai import evaluation


class TestPartie(unittest.TestCase):
    def test_partie_ingagnable(self):
        print("=== TEST PARTIE INGAGNABLE ===")

        grille = Grille()
        croix = Croix()
        rond = Rond()

        grille.placer_pion(0, rond)
        grille.placer_pion(1, rond)
        grille.placer_pion(2, rond)
        grille.placer_pion(3, croix)

        eval_jeton = evaluation(grille, 2)
        print("SCORE OBTENU POUR ROND[2] => ", eval_jeton)

        print("=== ====================== ===")

    def test_partie_gagnable(self):
        print("=== TEST PARTIE GAGNABLE ===")

        grille = Grille()
        croix = Croix()
        rond = Rond()

        grille.placer_pion(0, rond)

        grille.placer_pion(1, croix)
        grille.placer_pion(1, rond)

        grille.placer_pion(2, rond)
        grille.placer_pion(2, croix)
        grille.placer_pion(2, rond)

        grille.placer_pion(3, croix)
        grille.placer_pion(3, rond)
        grille.placer_pion(3, croix)
        grille.placer_pion(3, rond)

        eval_jeton = evaluation(grille, 2)
        print("SCORE OBTENU POUR ROND[3] => ", eval_jeton)

        print("=== ====================== ===")

    def test_partie_ingagnable_deux_series(self):
        print("=== TEST PARTIE GAGNABLE ===")

        grille = Grille()
        croix = Croix()
        rond = Rond()

        grille.placer_pion(0, rond)

        grille.placer_pion(1, rond)
        grille.placer_pion(1, rond)

        grille.placer_pion(2, rond)
        grille.placer_pion(2, croix)
        grille.placer_pion(2, rond)

        grille.placer_pion(3, rond)
        grille.placer_pion(3, rond)
        grille.placer_pion(3, croix)
        grille.placer_pion(3, rond)

        eval_jeton = evaluation(grille, 0)
        print("SCORE OBTENU POUR ROND[3] => ", eval_jeton)

        print("=== ====================== ===")