import unittest

from app.engine.grille import Grille
from app.engine.jeton import Rond, Croix


class TestGrille(unittest.TestCase):

    def test_get_grille(self):
        grille = Grille()
        self.assertEqual(grille.get_grille(), [[None for x in range(6)] for y in range(7)])

    def test_get_colonne(self):
        grille = Grille()
        self.assertEqual(grille.get_colonne(4), [None for x in range(6)])
        with self.assertRaises(IndexError):
            grille.get_colonne(7)
        with self.assertRaises(IndexError):
            grille.get_colonne(-1)

    def test_get_ligne(self):
        grille = Grille()
        self.assertEqual(grille.get_ligne(4), [None for x in range(7)])
        with self.assertRaises(IndexError):
            grille.get_ligne(6)
        with self.assertRaises(IndexError):
            grille.get_ligne(-1)

    def test_get_case(self):
        grille = Grille()
        self.assertEqual(grille.get_case(4, 4), None)
        with self.assertRaises(IndexError):
            grille.get_case(6, 4)
        with self.assertRaises(IndexError):
            grille.get_case(-1, 4)
        with self.assertRaises(IndexError):
            grille.get_case(4, 7)
        with self.assertRaises(IndexError):
            grille.get_case(4, -1)

    def test_placer_pion(self):
        grille = Grille()
        rond = Rond()
        croix = Croix()

        # Test de placement d'un jeton dans une colonne vide
        grille.placer_pion(0, rond)
        self.assertEqual(grille.get_case(0, 0), rond)

        # Test de placement d'un jeton sur un autre jeton
        grille.placer_pion(0, croix)
        self.assertEqual(grille.get_case(1, 0), croix)

        # Test de placement d'un jeton dans une colonne pleine
        grille = Grille()
        rond = Rond()

        # Test de placement d'un jeton dans une colonne pleine
        for i in range(6):
            grille.placer_pion(0, rond)
        with self.assertRaises(Exception):
            grille.placer_pion(0, rond)

        # Test de placement d'un jeton en dehors de la grille
        with self.assertRaises(IndexError):
            grille.placer_pion(7, rond)
        with self.assertRaises(IndexError):
            grille.placer_pion(-1, rond)

    def test_est_gagnee_horizontal(self):
        rond = Rond()

        for decalage in range(4):
            grille = Grille()
            for colonne in range(4):
                grille.placer_pion(colonne + decalage, rond)

            self.assertEqual(rond, grille.est_gagnee(decalage + 3), "Les pion ronds doivent gagner")

    def test_est_gagnee_horizontal_seconde_ligne(self):
        grille = Grille()
        rond = Rond()
        croix = Croix()

        for colonne in range(2):
            grille.placer_pion(colonne, croix)

        for colonne in range(2, 4):
            grille.placer_pion(colonne, rond)

        for colonne in range(4):
            grille.placer_pion(colonne, rond)

        self.assertEqual(rond, grille.est_gagnee(3), "Les pion ronds doivent gagner")

    def test_est_gagnee_horizontal_seconde_ligne_droite(self):
        grille = Grille()
        rond = Rond()
        croix = Croix()

        grille.placer_pion(3, croix)
        grille.placer_pion(4, croix)
        grille.placer_pion(5, rond)
        grille.placer_pion(6, rond)

        grille.placer_pion(3, rond)
        grille.placer_pion(4, rond)
        grille.placer_pion(5, rond)
        grille.placer_pion(6, rond)

        self.assertEqual(rond, grille.est_gagnee(6), "Les pion ronds doivent gagner")

    def test_est_gagnee_vertical(self):
        rond = Rond()

        for colonne in range(7):
            grille = Grille()
            for _ in range(4):
                grille.placer_pion(colonne, rond)

            self.assertEqual(rond, grille.est_gagnee(colonne), "Les pion ronds doivent gagner")

    def test_est_gagnee_vertical_seconde_ligne(self):
        grille = Grille()
        rond = Rond()
        croix = Croix()

        grille.placer_pion(0, croix)

        for _ in range(4):
            grille.placer_pion(0, rond)

        self.assertEqual(rond, grille.est_gagnee(0), "Les pion ronds doivent gagner")

    def test_est_gagnee_no_se(self):
        grille = Grille()
        rond = Rond()
        croix = Croix()

        grille.placer_pion(0, rond)

        grille.placer_pion(1, croix)
        grille.placer_pion(1, rond)

        grille.placer_pion(2, croix)
        grille.placer_pion(2, croix)
        grille.placer_pion(2, rond)

        grille.placer_pion(3, croix)
        grille.placer_pion(3, rond)
        grille.placer_pion(3, croix)
        grille.placer_pion(3, rond)

        self.assertEqual(rond, grille.est_gagnee(3), "Les pion ronds doivent gagner")

    def test_est_gagnee_so_ne(self):
        grille = Grille()
        rond = Rond()
        croix = Croix()

        grille.placer_pion(5, rond)

        grille.placer_pion(4, croix)
        grille.placer_pion(4, rond)

        grille.placer_pion(3, croix)
        grille.placer_pion(3, croix)
        grille.placer_pion(3, rond)

        grille.placer_pion(2, croix)
        grille.placer_pion(2, rond)
        grille.placer_pion(2, croix)
        grille.placer_pion(2, rond)

        self.assertEqual(rond, grille.est_gagnee(2), "Les pion ronds doivent gagner")

    def test_est_gagnee(self):
        grille = Grille()
        rond = Rond()
        croix = Croix()

        # On remplie la première ligne pour faire une "base" pour la deuxième ligne que l'on va remplir
        for colonne in range(3, 6):
            grille.placer_pion(colonne, rond)
        grille.placer_pion(6, croix)

        # La ligne de la victoire est sur le deuxième ligne en partant du bas
        for colonne in range(3, 7):
            grille.placer_pion(colonne, rond)
        print(grille)
        self.assertEqual(rond, grille.est_gagnee(6), "Les pion ronds doivent gagner")

    def test_grille_est_pleine(self):
        grille = Grille()
        self.assertFalse(grille.grille_est_pleine())
        for colonne in range(7):
            for ligne in range(6):
                grille.placer_pion(colonne, Rond())
        self.assertTrue(grille.grille_est_pleine())

    def test_dernier_pion_colonne(self):
        grille = Grille()

        self.assertEqual(None, grille.dernier_pion_colonne(1))

        for _ in range(5):
            grille.placer_pion(1, Rond())

        grille.placer_pion(1, Croix())

        self.assertEqual(5, grille.dernier_pion_colonne(1))
        
    def test_coups_possible(self):
        grille = Grille()
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], grille.coups_possible())

        for i in range(6):
            grille.placer_pion(1, Rond())
        self.assertTrue(1 not in grille.coups_possible())
        