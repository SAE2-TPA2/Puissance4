import unittest

from app.engine.grille import Grille
from app.engine.jeton import Croix, Rond
from app.engine.ai.ai import lecture_alignement, evaluation_v2, get_pion_adverse, get_score_pion, \
    lecture_score_alignement


class TestEvaluationV2(unittest.TestCase):

    def test_evaluation_v2(self):

        grille_evalue = Grille()

        rond = Rond()
        croix = Croix()
        score_attendu = -14

        grille_evalue.placer_pion(0, rond)
        grille_evalue.placer_pion(1, rond)
        grille_evalue.placer_pion(2, rond)
        grille_evalue.placer_pion(3, croix)
        grille_evalue.placer_pion(4, rond)
        grille_evalue.placer_pion(5, rond)
        grille_evalue.placer_pion(6, rond)

        grille_evalue.placer_pion(0, rond)
        grille_evalue.placer_pion(1, rond)
        grille_evalue.placer_pion(2, croix)
        grille_evalue.placer_pion(3, croix)
        grille_evalue.placer_pion(4, croix)
        grille_evalue.placer_pion(5, rond)
        grille_evalue.placer_pion(6, rond)

        grille_evalue.placer_pion(0, rond)
        grille_evalue.placer_pion(1, rond)
        grille_evalue.placer_pion(2, rond)
        grille_evalue.placer_pion(3, croix)
        grille_evalue.placer_pion(4, rond)
        grille_evalue.placer_pion(5, rond)
        grille_evalue.placer_pion(6, rond)

        grille_evalue.placer_pion(1, croix)
        grille_evalue.placer_pion(5, croix)

        score_1 = evaluation_v2(grille_evalue)
        self.assertTrue(score_1 == score_attendu, "test 1 integration évaluation v2")

    def test_lecture_score_alignement(self):
        grille_a_lire = Grille()

        rond = Rond()
        croix = Croix()
        score_attendu = -14


        grille_a_lire.placer_pion(0, rond)
        grille_a_lire.placer_pion(1, rond)
        grille_a_lire.placer_pion(2, rond)
        grille_a_lire.placer_pion(3, croix)
        grille_a_lire.placer_pion(4, rond)
        grille_a_lire.placer_pion(5, rond)
        grille_a_lire.placer_pion(6, rond)

        grille_a_lire.placer_pion(0, rond)
        grille_a_lire.placer_pion(1, rond)
        grille_a_lire.placer_pion(2, croix)
        grille_a_lire.placer_pion(3, croix)
        grille_a_lire.placer_pion(4, croix)
        grille_a_lire.placer_pion(5, rond)
        grille_a_lire.placer_pion(6, rond)

        grille_a_lire.placer_pion(0, rond)
        grille_a_lire.placer_pion(1, rond)
        grille_a_lire.placer_pion(2, rond)
        grille_a_lire.placer_pion(3, croix)
        grille_a_lire.placer_pion(4, rond)
        grille_a_lire.placer_pion(5, rond)
        grille_a_lire.placer_pion(6, rond)

        grille_a_lire.placer_pion(1, croix)
        grille_a_lire.placer_pion(5, croix)

        score_1 = lecture_score_alignement(grille_a_lire, rond)
        score_2 = lecture_score_alignement(grille_a_lire, croix)

        self.assertTrue(score_1 - score_2 == score_attendu, "Test lecture grille NOk")

    def test_get_score_pion(self):
        score_attendu = 5

        grille_pion = Grille()
        rond = Rond()
        croix = Croix()

        grille_pion.placer_pion(2, rond)
        grille_pion.placer_pion(3, rond)
        grille_pion.placer_pion(4, rond)

        grille_pion.placer_pion(2, croix)
        grille_pion.placer_pion(3, rond)
        grille_pion.placer_pion(4, croix)

        grille_pion.placer_pion(3, rond)
        grille_pion.placer_pion(4, croix)

        score = get_score_pion(grille_pion,1,3,rond.get_caractere())

        self.assertTrue(score == score_attendu,"test get score pion ok")

    def test_lecture_alignement(self):

        rond = Rond()
        croix = Croix()

        # test Nord

        grilleN = Grille()
        score_attendu_1 = 4
        score_attendu_2 = 43
        score_attendu_3 = 0
        score_attendu_4 = 4

        grilleN.placer_pion(4, rond)
        grilleN.placer_pion(4, rond)
        grilleN.placer_pion(4, rond)
        grilleN.placer_pion(4, croix)
        grilleN.placer_pion(4, croix)
        grilleN.placer_pion(4, croix)
        grilleN.placer_pion(3, croix)
        grilleN.placer_pion(3, croix)

        score_1 = lecture_alignement(grilleN, 0, 4, 0, 1, rond.get_caractere())
        score_2 = lecture_alignement(grilleN, 0, 3, 0, 1, croix.get_caractere())
        score_3 = lecture_alignement(grilleN, 0, 3, 0, 1, rond.get_caractere())
        score_4 = lecture_alignement(grilleN, 5, 4, 0, 1, croix.get_caractere())

        self.assertTrue(score_attendu_1 == score_1, "test 1 Nord Nok")
        self.assertTrue(score_attendu_2 == score_2, "test 2 Nord Nok")
        self.assertTrue(score_attendu_3 == score_3, "test 3 Nord Nok")
        self.assertTrue(score_attendu_4 == score_4, "test 4 Nord Nok")

        # test Nord-Est

        grilleNE = Grille()
        score_attendu_1 = 2
        score_attendu_2 = 0
        score_attendu_3 = 13
        score_attendu_4 = 2

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

        # test Est

        grilleE = Grille()
        score_attendu_1 = 3
        score_attendu_2 = 23
        score_attendu_3 = 32

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

        # test Sud-Est

        grilleSE = Grille()
        score_attendu_1 = 43
        score_attendu_2 = 50
        score_attendu_3 = 52

        grilleSE.placer_pion(6, rond)
        grilleSE.placer_pion(5, rond)
        grilleSE.placer_pion(5, rond)

        score_1 = lecture_alignement(grilleSE, 0, 6, 1, -1, rond.get_caractere())
        score_2 = lecture_alignement(grilleSE, 0, 3, 1, -1, rond.get_caractere())
        score_3 = lecture_alignement(grilleSE, 5, 1, 1, -1, rond.get_caractere())

        self.assertTrue(score_attendu_1 == score_1, "test 1 Sud-Est Nok")
        self.assertTrue(score_attendu_2 == score_2, "test 2 Sud-Est Nok")
        self.assertTrue(score_attendu_3 == score_3, "test 3 Sud-Est Nok")

    def test_get_pion_adverse(self):
        caractere1 = "X"
        caractere2 = "O"
        if caractere2 == get_pion_adverse(caractere1):
            print("test get pion adverse ok")
        if caractere1 == get_pion_adverse(caractere2):
            print("test get pion adverse ok")
