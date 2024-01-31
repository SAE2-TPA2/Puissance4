import unittest
from Engine.Grille import Grille

class TestGrille(unittest.TestCase):

    def test_getColonne(self):
        grille = Grille()
        grille.getColonne(0)
        grille.getColonne(6)
        with self.assertRaises(Exception):
            grille.getColonne(-1)
        with self.assertRaises(Exception):
            grille.getColonne(7)

