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


def min_max(grille: Grille, profondeur: int, mon_pion: Jeton, pion_adverse: Jeton, qui_joue: Jeton,
            coup_joue: int | None = None)->tuple[int, int]:
    """
    Méthode min-max pour choisir la colonne à jouer
    :param grille: La grille du jeu
    :param profondeur: La profondeur de recherche
    :param mon_pion: Mon pion
    :param pion_adverse: Le pion de l'adversaire
    :param qui_joue: Le pion qui joue
    :param coup_joue: Le coup joué qui a mené à cette grille
    :return: Un tuple qui contient le coup à jouer et la valeur de la grille.
    Sous la forme (coup, valeur)
    """
    if coup_joue is not None:  # Au premier appel coup_joue est None.
        jeton_gagnant = grille.est_gagnee(coup_joue)
        if jeton_gagnant == mon_pion:
            return coup_joue, 100
        if jeton_gagnant == pion_adverse:
            return coup_joue, -100

        if grille.grille_est_pleine():
            return coup_joue, 0

        if profondeur == 0:
            return coup_joue, evaluation(grille, coup_joue)

    coups_possible = grille.coups_possible()
    grille_fille: list[tuple[int, int]] = []

    if qui_joue == mon_pion:
        for coup in coups_possible:
            new_grille = grille.__deepcopy__()
            new_grille.placer_pion(coup, qui_joue)
            grille_fille.append(min_max(new_grille, profondeur - 1, mon_pion,
                                        pion_adverse, pion_adverse, coup))
        return max_tuple(grille_fille)

    # else qui_joue == pion_adverse
    for coup in coups_possible:
        new_grille = grille.__deepcopy__()
        new_grille.placer_pion(coup, qui_joue)
        grille_fille.append(min_max(new_grille, profondeur - 1, mon_pion,
                                    pion_adverse, mon_pion, coup))
    return min_tuple(grille_fille)


def evaluation(grille: Grille, indice_colonne_jeton_joue: int) -> int:
    """
    Fonction d'évaluation pour la méthode min-max
    :param indice_colonne_jeton_joue:
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
