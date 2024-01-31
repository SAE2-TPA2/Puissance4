import unittest
from App.Engine.Grille import Grille


class TestGrille(unittest.TestCase):

    def test_get_grille(self):
        grille = Grille()
        self.assertEqual(grille.getGrille(), [[None for x in range(7)] for y in range(6)])

    def test_get_colonne(self):
        grille = Grille()
        self.assertEqual(grille.getColonne(4), [None for x in range(6)])
        with self.assertRaises(IndexError):
            grille.getColonne(7)
        with self.assertRaises(IndexError):
            grille.getColonne(-1)



