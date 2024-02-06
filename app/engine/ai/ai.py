from app.engine.grille import Grille
from app.engine.jeton import Jeton


def min_tuple(fils: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Retourne le minimum d'une liste de tuple
    Les tuples sont de la forme (coups, valeur)
    On recherche le minimum de la valeur
    :param fils:
    :return:
    """
    min_valeur = fils[0][1]
    min_coup = fils[0][0]
    for coup, valeur in fils:
        if valeur < min_valeur:
            min_valeur = valeur
            min_coup = coup
    return min_coup, min_valeur


def max_tuple(fils: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Retourne le maximum d'une liste de tuple
    Les tuples sont de la forme (coups, valeur)
    On recherche le maximum de la valeur
    :param fils:
    :return:
    """
    max_valeur = fils[0][1]
    max_coup = fils[0][0]
    for coup, valeur in fils:
        if max_valeur < valeur:
            max_valeur = valeur
            max_coup = coup
    return max_coup, max_valeur


def min_max(grille: Grille, mon_pion: Jeton, pion_qui_joue: Jeton) -> int:
    """
    Méthode min-max pour choisir la colonne à jouer
    :param pion_qui_joue:
    :param mon_pion:
    :param grille: la grille du jeu
    :return: L'indice de la colonne à jouer
    """
    pass


def evaluation(grille: Grille, indice_colonne_jeton_joue: int) -> int:
    """
    Fonction d'évaluation pour la méthode min-max
    :param pion_qui_joue: Le pion qui joue
    :param mon_pion: Mon pion
    :param grille: la grille du jeu
    :return: la valeur de la grille
    """
    POINTS_JETON_DANS_SERIE = 5
    POINTS_PARTIE_GAGNABLE = 100

    score_jeton = 0

    analyse_verticale = grille.verification_verticale(indice_colonne_jeton_joue)
    analyse_horizontale = grille.verification_horizontale(indice_colonne_jeton_joue)
    analyse_nose = grille.verification_diagonale_no_se(indice_colonne_jeton_joue)
    analyse_sone = grille.verification_diagonale_so_ne(indice_colonne_jeton_joue)

    if analyse_verticale[0] < 4:
        score_jeton += analyse_verticale[0] * POINTS_JETON_DANS_SERIE
    else:
        score_jeton += POINTS_PARTIE_GAGNABLE

    if analyse_horizontale[0] < 4:
        score_jeton += analyse_horizontale[0] * POINTS_JETON_DANS_SERIE
    else:
        score_jeton += POINTS_PARTIE_GAGNABLE

    if analyse_nose[0] < 4:
        score_jeton += analyse_nose[0] * POINTS_JETON_DANS_SERIE
    else:
        score_jeton += POINTS_PARTIE_GAGNABLE

    if analyse_sone[0] < 4:
        score_jeton += analyse_sone[0] * POINTS_JETON_DANS_SERIE
    else:
        score_jeton += POINTS_PARTIE_GAGNABLE

    return score_jeton
