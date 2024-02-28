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

        rond = Rond()
        croix = Croix()

        #test Nord

        grilleN = Grille()
        score_attendu_1 = 3
        score_attendu_2 = 42
        score_attendu_3 = 0
        score_attendu_4 = 1

        grilleN.placer_pion(4,rond)
        grilleN.placer_pion(4, rond)
        grilleN.placer_pion(4, rond)
        grilleN.placer_pion(4, croix)
        grilleN.placer_pion(4, croix)
        grilleN.placer_pion(4, croix)
        grilleN.placer_pion(3, croix)
        grilleN.placer_pion(3, croix)

        score_1 = lecture_alignement(grilleN,0,4,0,1,rond.get_caractere())
        score_2 = lecture_alignement(grilleN, 0, 3, 0, 1, croix.get_caractere())
        score_3 = lecture_alignement(grilleN,0,3,0,1,rond.get_caractere())
        score_4 = lecture_alignement(grilleN,5,4,0,1,croix.get_caractere())

        self.assertTrue(score_attendu_1 == score_1, "test 1 Nord Nok")
        self.assertTrue(score_attendu_2 == score_2, "test 2 Nord Nok")
        self.assertTrue(score_attendu_3 == score_3, "test 3 Nord Nok")
        self.assertTrue(score_attendu_4 == score_4, "test 4 Nord Nok")

        #test Nord-Est

        grilleNE = Grille()
        score_attendu_1 = 1
        score_attendu_2 = 0
        score_attendu_3 = 12
        score_attendu_4 = 1

        grilleNE.placer_pion(5, rond)
        grilleNE.placer_pion(6, rond)
        grilleNE.placer_pion(4, rond)
        grilleNE.placer_pion(5, rond)
        grilleNE.placer_pion(6, croix)

        score_1 = lecture_alignement(grilleNE, 0, 6, 1, 1, rond.get_caractere())
        score_2 = lecture_alignement(grilleNE, 0, 6, 1, 1, croix.get_caractere())
        score_3 = lecture_alignement(grilleNE, 0, 4, 1, 1, rond.get_caractere())
        score_4 = lecture_alignement(grilleNE, 0, 5, 1, 1, rond.get_caractere())

        self.assertTrue(score_attendu_1 == score_1, "test 1 Nord-Est Nok")
        self.assertTrue(score_attendu_2 == score_2, "test 2 Nord-Est Nok")
        self.assertTrue(score_attendu_3 == score_3, "test 3 Nord-Est Nok")
        self.assertTrue(score_attendu_4 == score_4, "test 4 Nord-Est Nok")

        #test Est

        grilleE = Grille()
        score_attendu_1 = 2
        score_attendu_2 = 2
        score_attendu_3 = 22

        grilleE.placer_pion(0, rond)
        grilleE.placer_pion(1, rond)
        grilleE.placer_pion(6, rond)
        grilleE.placer_pion(5, rond)
        grilleE.placer_pion(2, croix)

        score_1 = lecture_alignement(grilleE, 0, 0, 1, 0, rond.get_caractere())
        score_2 = lecture_alignement(grilleE, 0, 5, 1, 0, rond.get_caractere())
        score_3 = lecture_alignement(grilleE, 0, 3, 1, 0, rond.get_caractere())

        self.assertTrue(score_attendu_1 == score_1, "test 1 Nord-Est Nok")
        self.assertTrue(score_attendu_2 == score_2, "test 2 Nord-Est Nok")
        self.assertTrue(score_attendu_3 == score_3, "test 3 Nord-Est Nok")

        #test Sud-Est

        grilleSE = Grille()
        score_attendu_1 = 1
        score_attendu_2 = 10
        score_attendu_3 = 42

        grilleSE.placer_pion(6, rond)
        grilleSE.placer_pion(5, rond)
        grilleSE.placer_pion(5, rond)

        score_1 = lecture_alignement(grilleSE, 0, 6, 1, -1, rond.get_caractere())
        score_2 = lecture_alignement(grilleSE, 0, 3, 1, -1, rond.get_caractere())
        score_3 = lecture_alignement(grilleSE, 5, 1, 1, -1, rond.get_caractere())

        self.assertTrue(score_attendu_1 == score_1, "test 1 Sud-Est Nok")
        self.assertTrue(score_attendu_2 == score_2, "test 2 Sud-Est Nok")
        self.assertTrue(score_attendu_3 == score_3, "test 3 Sud-Est Nok")

        #test Sud

        grilleS = Grille()
        score_attendu_1 = 6
        score_attendu_2 = 60
        score_attendu_3 = 22

        grilleS.placer_pion(5, rond)
        grilleS.placer_pion(5, rond)
        grilleS.placer_pion(5, rond)
        grilleS.placer_pion(5, rond)
        grilleS.placer_pion(5, rond)
        grilleS.placer_pion(5, rond)
        grilleS.placer_pion(2, croix)
        grilleS.placer_pion(2, rond)
        grilleS.placer_pion(2, rond)

        score_1 = lecture_alignement(grilleS, 5, 5, 0, -1, rond.get_caractere())
        score_2 = lecture_alignement(grilleS, 5, 0, 0, -1, rond.get_caractere())
        score_3 = lecture_alignement(grilleS, 4, 2, 0, -1, rond.get_caractere())

        self.assertTrue(score_attendu_1 == score_1, "test 1 Sud Nok")
        self.assertTrue(score_attendu_2 == score_2, "test 2 Sud Nok")
        self.assertTrue(score_attendu_3 == score_3, "test 3 Sud Nok")

        #test Sud-Ouest

        grilleSO = Grille()
        score_attendu_1 = 22
        score_attendu_2 = 60
        score_attendu_3 = 2

        grilleSO.placer_pion(4, croix)
        grilleSO.placer_pion(5, rond)
        grilleSO.placer_pion(6, rond)
        grilleSO.placer_pion(4, rond)
        grilleSO.placer_pion(5, croix)
        grilleSO.placer_pion(6, rond)
        grilleSO.placer_pion(4, rond)
        grilleSO.placer_pion(5, rond)
        grilleSO.placer_pion(6, rond)


        score_1 = lecture_alignement(grilleSO, 3, 6, -1, -1, rond.get_caractere())
        score_2 = lecture_alignement(grilleSO, 5, 6, -1, -1, rond.get_caractere())
        score_3 = lecture_alignement(grilleSO, 1, 5, -1, -1, rond.get_caractere())

        print(score_1)
        print(score_2)
        print(score_3)

        self.assertTrue(score_attendu_1 == score_1, "test 1 Sud Ouest Nok")
        self.assertTrue(score_attendu_2 == score_2, "test 2 Sud Ouest Nok")
        #self.assertTrue(score_attendu_3 == score_3, "test 3 Sud Ouest Nok")

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