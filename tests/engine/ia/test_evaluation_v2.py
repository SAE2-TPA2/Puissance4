import unittest

from app.engine.grille import Grille
from app.engine.jeton import Croix, Rond
from app.engine.ai.ai import lecture_alignement,evaluation_v2,get_pion_adverse,evaluation_placement,get_score_pion


class TestEvaluationV2(unittest.TestCase):
    
    def test_evaluation_v2(self):
        pass

    def test_evaluation_placement(self):
        pass

    def test_lecture_score_alignement(self):
        grille = Grille()
        rond = Rond()
        croix = Croix()
        #test Nord
        score_attendu_1 = 3
        score_attendu_2 = 42
        score_attendu_3 = 0
        score_attendu_4 = 1
        grille.placer_pion(4,rond)
        grille.placer_pion(4, rond)
        grille.placer_pion(4, rond)
        grille.placer_pion(4, croix)
        grille.placer_pion(4, croix)
        grille.placer_pion(4, croix)
        grille.placer_pion(3, croix)
        grille.placer_pion(3, croix)

        score_1 = lecture_alignement(grille,0,4,0,1,rond.get_caractere())
        score_2 = lecture_alignement(grille, 0, 3, 0, 1, croix.get_caractere())
        score_3 = lecture_alignement(grille,0,3,0,1,rond.get_caractere())
        score_4 = lecture_alignement(grille,5,4,0,1,croix.get_caractere())

        print(score_1)
        print(score_2)
        print(score_3)
        print(score_4)

        self.assertTrue(score_attendu_1 == score_1, "test 1 Nord ok")
        self.assertTrue(score_attendu_2 == score_2, "test 2 Nord ok")
        self.assertTrue(score_attendu_3 == score_3, "test 3 Nord ok")
        self.assertTrue(score_attendu_4 == score_4, "test 4 Nord ok")

        #grille2 = Grille()
        #test Nord-Est
        #test Est
        #test Sud-Est
        #test Sud
        #test Sud-Ouest
        #test Ouest
        #test Nord-Ouest

    def test_get_pion(self):
        caractere1 = "X"
        caractere2 = "O"    
        if caractere2 == get_pion_adverse(caractere1):
            print("test get pion adverse ok")
        if caractere1 == get_pion_adverse(caractere2):
            print("test get pion adverse ok")
            
    def test_lecture_alignement(self):
        pass