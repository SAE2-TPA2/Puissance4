from App.Engine import Grille
from App.Engine.Jeton import Jeton


def est_terminal(grille)->bool:
    pass


def min_max(grille: Grille, mon_pion: Jeton, pion_qui_joue: Jeton) -> int:
    """
    Méthode min-max pour choisir la colonne à jouer
    :param pion_qui_joue:
    :param mon_pion:
    :param grille: la grille du jeu
    :return: L'indice de la colonne à jouer
    """
    if est_terminal(grille):
        return evaluation(grille, mon_pion, pion_qui_joue)
    else:
        coups_possible = grille.coups_possible()
        coups_possible_valeur = []
        for etat in coups_possible:
            coups_possible_valeur.append(min_max(etat, mon_pion, pion_qui_joue))
            
        if pion_qui_joue == mon_pion:
            return max(coups_possible_valeur)
        else:
            return min(coups_possible_valeur)


def evaluation(grille: Grille, mon_pion: Jeton, pion_qui_joue: Jeton) -> int:
    """
    Fonction d'évaluation pour la méthode min-max
    :param pion_qui_joue: Le pion qui joue
    :param mon_pion: Mon pion
    :param grille: la grille du jeu
    :return: la valeur de la grille
    """
    pass


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
