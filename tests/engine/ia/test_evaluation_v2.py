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
        score_attendu = 51
        grille.placer_pion(4,rond)
        grille.placer_pion(4, rond)
        grille.placer_pion(4, rond)
        grille.placer_pion(4, croix)
        score = lecture_alignement(grille,0,4,0,1,rond.get_caractere())
        print(score)
        self.assertTrue(score_attendu == score,"test Nord ok")
        
        grille2 = Grille()
        score_attendu = 0 
        grille2.placer_pion(4,rond)
        grille2.placer_pion(3,rond)
        grille2.placer_pion(3,rond)
        grille2.placer_pion(5,rond)
        grille2.placer_pion(5,rond)
        score = lecture_alignement(grille,1,4,0,1,rond.get_caractere())
        self.assertTrue(score_attendu == score,"Test Nord ok")
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