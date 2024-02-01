import unittest

from App.Engine.Grille import Grille
from App.Engine.Jeton import Rond, Croix


class TestGrille(unittest.TestCase):

    def test_get_grille(self):
        grille = Grille()
        self.assertEqual(grille.get_grille(), [[None for x in range(7)] for y in range(6)])

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
        self.assertEqual(grille.get_case(0, 0), rond.get_caractere())

        # Test de placement d'un jeton sur un autre jeton
        grille.placer_pion(0, croix)
        self.assertEqual(grille.get_case(1, 0), croix.get_caractere())

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

    def test_est_gagnee(self):
        grille = Grille()
        rond = Rond()
        croix = Croix()

        for colonne in range(4):
            grille.placer_pion(colonne, rond)

        print(grille)

    def test_grille_est_pleine(self):
        grille = Grille()
        self.assertFalse(grille.grille_est_pleine())
        for i in range(6):
            for j in range(7):
                grille.placer_pion(j, Rond())
        self.assertTrue(grille.grille_est_pleine())
