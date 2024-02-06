from app.engine import Grille
from app.engine.Jeton import Jeton


def min_max(grille: Grille, mon_pion: Jeton, pion_adverse: Jeton, pion_qui_joue: Jeton, profondeur: int = 7) -> int:
    """
    Méthode min-max pour choisir la colonne à jouer
    :param pion_adverse:
    :param profondeur: La profondeur de recherche
    :param pion_qui_joue:
    :param mon_pion:
    :param grille: la grille du jeu
    :return: L'indice de la colonne à jouer
    """
    pass


def evaluation(grille: Grille, mon_pion: Jeton, pion_qui_joue: Jeton) -> int:
    """
    Fonction d'évaluation pour la méthode min-max
    :param pion_qui_joue: Le pion qui joue
    :param mon_pion: Mon pion
    :param grille: la grille du jeu
    :return: la valeur de la grille
    """
    resultat = grille.est_gagnee()
    if resultat == mon_pion:  # J'ai gagné
        return 100
    elif resultat is not None:  # L'adversaire a gagné
        return -100

    if grille.grille_est_pleine():
        return 0  # Match nul

    return 0  # STUB


def etat_suivant(grille: Grille, pion: Jeton) -> list[Grille]:
    """
    Retourne l'état de la grille après avoir joué un coup
    :param grille: la grille du jeu
    :param pion: le pion à jouer
    :return: la grille après avoir joué le coup
    """
    resultat: list[Grille] = []
    for coup in grille.coups_possible():
        grille_copie = grille.__deepcopy__()
        grille_copie.jouer_pion(coup, pion)
        resultat.append(grille_copie)
    return resultat
