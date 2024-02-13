from app.engine.grille import Grille
from app.engine.jeton import Jeton, Rond, Croix


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
            coup_joue: int | None = None)->int:
    """
    Méthode min-max pour choisir la colonne à jouer
    :param grille: La grille du jeu
    :param profondeur: La profondeur de recherche
    :param mon_pion: Mon pion
    :param pion_adverse: Le pion de l'adversaire
    :param qui_joue: Le pion qui joue
    :param coup_joue: Le coup joué qui a mené à cette grille
    :return: Si coup_joue est None, on retourne le coup à jouer, sinon on retourne l'évaluation de la grille
    """
    if coup_joue is not None:  # Au premier appel coup_joue est None.
        jeton_gagnant = grille.est_gagnee(coup_joue)
        if jeton_gagnant == mon_pion:
            return 100
        if jeton_gagnant == pion_adverse:
            return -100

        if grille.grille_est_pleine():
            return 0

        if profondeur == 0:
            return evaluation(grille, coup_joue)

    coups_possible = grille.coups_possible()

    if qui_joue == mon_pion:
        valeur_max: tuple[int, int] = (3, -1000)
        for coup in coups_possible:
            grille_temp = grille.__deepcopy__()
            grille_temp.placer_pion(coup, qui_joue)
            valeur = min_max(grille_temp, profondeur - 1, mon_pion, pion_adverse, pion_adverse, coup)
            valeur_max = max_tuple([(coup, valeur), valeur_max])

        if coup_joue is None:  # Si on est à la racine, on retourne le coup à jouer
            return valeur_max[0]
        # else: # Sinon on retourne la valeur de la grille
        return valeur_max[1]

    # else qui_joue == pion_adverse
    valeur_min: tuple[int, int] = (3, 1000)
    for coup in coups_possible:
        grille_temp = grille.__deepcopy__()
        grille_temp.placer_pion(coup, qui_joue)
        valeur = min_max(grille_temp, profondeur - 1, mon_pion, pion_adverse, mon_pion, coup)
        valeur_min = min_tuple([(coup, valeur), valeur_min])

    if coup_joue is None:  # Si on est à la racine, on retourne le coup à jouer
        return valeur_min[0]
    # else: # Sinon on retourne la valeur de la grille
    return valeur_min[1]


def evaluation(grille: Grille, indice_colonne_jeton_joue: int) -> int:
    """
    Fonction d'évaluation pour la méthode min-max
    :param indice_colonne_jeton_joue: l'indice de la colonne où le jeton a été joué
    :param grille: la grille du jeu à évaluer
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


def evaluation_v2(grille: Grille, mon_pion: Jeton) -> int:
    """
    Fonction d'évaluation pour la méthode min-max
    :param pion_qui_joue: Le pion qui joue
    :param mon_pion: Mon pion
    :param grille: la grille du jeu
    :return: la valeur de la grille
    """
    # pass
    score_initial = 50
    caractere_increment_score = mon_pion.get_caractere()
    caractere_decrement_score = get_pion_adverse(caractere_increment_score)
    resultat_gagner = grille.est_gagnee()
    if resultat_gagner is not None:
        score_initial += evaluation_placement(grille, caractere_increment_score)
        score_initial -= evaluation_placement(grille, caractere_decrement_score)
        score_initial += lecture_score_alignement(grille, caractere_increment_score)
        score_initial -= lecture_score_alignement(grille, caractere_decrement_score)
    elif resultat_gagner.getcaractere() == caractere_increment_score:
        score_initial = 100
    else:
        score_initial = 0
    return score_initial


def evaluation_placement(grille: Grille, caractere_observe: str) -> int:
    """
    Donne le score initial avec l'emplacement des pions sans prendre en compte
    les alignements

    Args :
        caractere_observe :
        grille (Grille) : grille de jeu
        score_montant (_str_): caractère du pion correspondant au score de 100


    Returns :
        int : entier correspondant à un avantage si positif pour le joueur ayant le caractère montant
        et un désavantage si le caractère est négatif cela correspond à un désanvatage
    """

    score_a_ajouter = 0
    score_emplacement = [0, 0, 0, 2, 0, 0, 0,
                         0, 0, 2, 3, 2, 0, 0,
                         0, 2, 3, 4, 3, 2, 0,
                         0, 2, 3, 4, 3, 2, 0,
                         0, 0, 2, 3, 2, 0, 0,
                         0, 0, 0, 2, 0, 0, 0]
    nb_colonne = 1
    nb_ligne = 1
    indice_lecture = 0

    while nb_ligne != 6:
        while nb_colonne != 7:
            if grille.get_case(nb_ligne, nb_colonne).get_caractere() == caractere_observe:
                score_a_ajouter += score_emplacement[indice_lecture]
            else:
                score_a_ajouter -= score_emplacement[indice_lecture]
            nb_colonne += 1
        nb_colonne = 1
        nb_ligne += 1

    return score_a_ajouter


def lecture_score_alignement(grille: Grille, pionObserve: Rond | Croix) -> int:
    """
    Obeservation de chaque pion de la grille est donne un nombre
    final positif ou négatif

    Args:
        grille (Grille): grille du jeu à évaluer
        pionObserve (Jeton): point de vu du jeu

    Returns:
        int: entier indiquant l'avantage du point de vu passé en paramètre
    """
    score_a_renvoiyer = 0

    indice_lecture_colonne = 0
    indice_lecture_ligne = 0
    symbole_observe = pionObserve.get_caractere()
    while indice_lecture_ligne < 7:
        while indice_lecture_colonne < 6:
            if grille.get_case(indice_lecture_colonne, indice_lecture_ligne).get_caractere() == symbole_observe:
                score_a_renvoiyer += get_score_pion(grille, indice_lecture_ligne, indice_lecture_colonne)
            indice_lecture_colonne += 1
        indice_lecture_ligne += 1


def get_score_pion(grille: Grille, ligne: int, colonne: int, symboleObserve: str) -> int:
    """
    Renvoie la valeur des alignement du pion

    Args:
        grille (Grille): grille du jeu evaluer
        ligne (int): ligne du pion observé
        colonne (int): colonne du pion observé
        symboleObserve (str): symbole observé

    Returns:
        int: entier modifiant le score
    """
    score_to_add = 0
    direction_verifie = 0
    score_horizontal = 0
    score_vertical = 0
    score_diagonale_nose = 0
    score_diagonale_sone = 0

    symboleAdverse = get_pion_adverse(symboleObserve)

    while direction_verifie < 8:
        match direction_verifie:
            case 0:  # EST
                score_horizontal += lecture_alignement(grille, ligne, colonne, 1, 0, symboleObserve)
            case 1:  # SUD-EST
                score_diagonale_nose += lecture_alignement(grille, ligne, colonne, 1, -1, symboleObserve)
            case 2:  # SUD
                score_vertical += lecture_alignement(grille, ligne, colonne, 0, -1, symboleObserve)
            case 3:  # SUD-OUEST
                score_diagonale_sone += lecture_alignement(grille, ligne, colonne, -1, -1, symboleObserve)
            case 4:  # OUEST
                score_horizontal += lecture_alignement(grille, ligne, colonne, -1, 0, symboleObserve)
            case 5:  # NORD-OUEST
                score_diagonale_nose += lecture_alignement(grille, ligne, colonne, -1, 1, symboleObserve)
            case 6:  # NORD
                score_vertical += lecture_alignement(grille, ligne, colonne, 0, 1, symboleObserve)
            case 7:  # NORD-EST
                score_diagonale_sone += lecture_alignement(grille, ligne, colonne, 1, 1, symboleObserve)
        direction_verifie += 1

    scores = [score_horizontal, score_vertical, score_diagonale_nose, score_diagonale_sone]
    for score in scores:
        if score % 10 == 2 and score / 10 >= 2:
            score_to_add += 1
        elif score % 10 == 3 and score / 10 == 1:
            score_to_add += 2
        elif score_to_add == 3 and score / 10 >= 2:
            score_to_add == 3 # Ce n'est pas += plutôt ?

    return score_to_add


def lecture_alignement(grille: Grille, ligne: int, colonne: int, direction_h: int, direction_v: int,
                       monPion: str) -> int:
    add_to_ligne = 0
    add_to_colonne = 0
    score_a_return = 0

    symbole_adverse = get_pion_adverse(monPion)

    try:
        if grille.get_case(ligne,colonne).get_caractere() == monPion:
            score_a_return += 1
    except IndexError:
        return score_a_return
    fin = False

    while (grille.get_case(ligne + add_to_ligne, colonne + add_to_colonne).get_caractere()) != symbole_adverse or fin:
        add_to_ligne += direction_v
        add_to_colonne += direction_h
        try:
            if grille.get_case(ligne + add_to_ligne, colonne + add_to_colonne) is None:
                score_a_return += 10
            else:
                score_a_return += 1
        except IndexError:
            score_a_return += 0
            fin = True

    return score_a_return


def get_pion_adverse(mon_pion: str) -> str:
    """
        renvoi le caractère du pion adverse

    Args:
        mon_pion (str): caractere du pion observe

    Returns:
        str: caractère du pion adverse
    """
    symbole_adverse = "X"
    if mon_pion == "X":
        symbole_adverse = "O"
    return symbole_adverse


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
