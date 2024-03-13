from app.engine.grille import Grille
from app.engine.jeton import Jeton, Rond, Croix

VALEUR_X = -5
VALEUR_O = 5


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


def min_max(grille: Grille, profondeur: int, mon_pion: Rond | Croix, pion_adverse: Rond | Croix, qui_joue: Rond | Croix,
            coup_joue: int | None = None, methode_evaluation: str = "v2")->int:
    """
    Méthode min-max pour choisir la colonne à jouer
    :param grille: La grille du jeu
    :param profondeur: La profondeur de recherche
    :param mon_pion: Mon pion
    :param pion_adverse: Le pion de l'adversaire
    :param qui_joue: Le pion qui joue
    :param coup_joue: Le coup joué qui a mené à cette grille
    :param methode_evaluation: La méthode d'évaluation à utiliser v2 ou v3
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
            if methode_evaluation == "v3":
                return evaluation_v3(grille)
            return evaluation_v2(grille)

    coups_possible = grille.coups_possible()
    
    if qui_joue == mon_pion:
        valeur_max: tuple[int, int] = (3, -1000)
        for coup in coups_possible:
            grille_temp = grille.__deepcopy__()
            grille_temp.placer_pion(coup, qui_joue)

            valeur = min_max(grille_temp, profondeur - 1, mon_pion, pion_adverse,
                             pion_adverse, coup, methode_evaluation=methode_evaluation)

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

        valeur = min_max(grille_temp, profondeur - 1, mon_pion, pion_adverse,
                         mon_pion, coup, methode_evaluation=methode_evaluation)

        valeur_min = min_tuple([(coup, valeur), valeur_min])

    if coup_joue is None:  # Si on est à la racine, on retourne le coup à jouer
        return valeur_min[0]
    # else: # Sinon on retourne la valeur de la grille
    return valeur_min[1]


def evaluation_v2(grille: Grille) -> int:
    """
    Fonction d'évaluation renvoi un int correspondant au score de la grille
    :param grille: la grille du jeu évalué
    :return: la valeur correspondant au score de la grille
    """
    score_initial = 0
    score_initial -= lecture_score_alignement(grille, Croix())
    score_initial += lecture_score_alignement(grille, Rond())
    return score_initial

def lecture_score_alignement(grille: Grille, pionObserve: Rond | Croix) -> int:
    """
    Obeservation de chaque pion de la grille est donne un nombre
    représentant le score du pion

    Args:
        grille (Grille): grille du jeu à évaluer
        pionObserve (Jeton): point de vu du jeu

    Returns:
        int: entier indiquant l'avantage du point de vu passé en paramètre
    """
    score_a_renvoiyer = 0

    symbole_observe = pionObserve.get_caractere()
    for i in range(6):#parcours de toute la grille
        for j in range(7):
            if grille.get_case(i, j) is not None:
                if grille.get_case(i, j).get_caractere() == symbole_observe:
                    # récupéation de la valeur du pion
                    score_a_renvoiyer += get_score_pion(grille, i, j, symbole_observe)
    return score_a_renvoiyer

def get_score_pion(grille: Grille, ligne: int, colonne: int, symboleObserve: Jeton) -> int:
    """
    Renvoie la valeur des alignements du pion %10 correspond au nombre de pion aligné
    /10 correspond au emplacement libre dans l'alignement du joueur

    Args:
        grille (Grille): grille du jeu evaluer
        ligne (int): ligne du pion observé
        colonne (int): colonne du pion observé
        symboleObserve (Jeton): symbole observé

    Returns:
        int: entier corrspondant au score du pion
    """
    score_to_add = 0

    score_horizontal = 0
    score_vertical = 0
    score_diagonale_nose = 0
    score_diagonale_sone = 0

    symboleAdverse = get_pion_adverse(symboleObserve)

    for i in range(4):# lecture de l'ensemble des 4 directions du pion
        match i:
            case 0:  # DIRECTION EST
                score_horizontal += lecture_alignement(grille, ligne, colonne, 1, 0, symboleObserve)
            case 1:  # DIRECTION SUD-EST
                score_diagonale_nose += lecture_alignement(grille, ligne, colonne, 1, -1, symboleObserve)
            case 2:  # DIRECTION SUD
                score_vertical += lecture_alignement(grille, ligne, colonne, 0, -1, symboleObserve)
            case 3:  # DIRECTION SUD-OUEST
                score_diagonale_sone += lecture_alignement(grille, ligne, colonne, -1, -1, symboleObserve)

    scores = [score_horizontal, score_vertical, score_diagonale_nose, score_diagonale_sone]

    for score in scores:
        # 1 seul pion détecté dans l'alignement avec possibilité de placer 3 autres
        if score % 10 == 1 and score / 10 >= 3:
            score_to_add += 1 # score attribué 1 car peu avantageux
        # 2 pions détectés dans l'alignement avec possibilité de placer au moins 2 autres
        elif score % 10 == 2 and score / 10 >= 2:
            score_to_add += 2  # score attribué 2 car peu avantageux mais interéssant
        # 3 pions détectés dans l'alignement avec possibilité de placer 1 autre
        elif score % 10 == 3 and score / 10 == 1:
            score_to_add += 3 # score attribué 3 avantageux mais reste limité
        # 3 pions détectés dans l'alignement avec possibilité de placer au moins 2 autres
        elif score % 10 == 3 and score / 10 >= 2:
            score_to_add += 5 # score attribué 5 avantageux et non blocable au prochain tour

    return score_to_add


def lecture_alignement(grille: Grille, ligne: int, colonne: int, direction_h: int, direction_v: int,
                       mon_pion: Jeton) -> int:
    """
    Renvoie la valeur d'un alignement précis sur un pion donné

    Args:
        grille (Grille): grille du jeu evaluer
        ligne (int): ligne du pion observé
        colonne (int): colonne du pion observé
        mon_pion (Jeton): symbole observé

    Returns:
        int: entier modifiant le score
    """
    add_to_ligne = 0
    add_to_colonne = 0
    score_a_return = 0

    symbole_adverse = get_pion_adverse(mon_pion)
    fin = True
    while fin:
        try:
            if grille.get_case(ligne + add_to_ligne, colonne + add_to_colonne) is None:
                score_a_return += 10
            elif grille.get_case(ligne + add_to_ligne, colonne + add_to_colonne).get_caractere() == symbole_adverse.get_caractere():
                fin = False
            else: score_a_return += 1

        except IndexError:
            fin = False

        add_to_ligne += direction_v
        add_to_colonne += direction_h

    fin = True
    add_to_ligne = 0
    add_to_colonne = 0

    while fin:
        try:
            if grille.get_case(ligne + add_to_ligne, colonne + add_to_colonne) is None:
                score_a_return += 10
            elif grille.get_case(ligne + add_to_ligne, colonne + add_to_colonne).get_caractere() == symbole_adverse.get_caractere():
                fin = False
            else: score_a_return += 1

        except IndexError:
            fin = False

        add_to_ligne -= direction_v
        add_to_colonne -= direction_h

    return score_a_return


def get_pion_adverse(mon_pion: Jeton) -> Rond | Croix:
    """
        renvoi le caractère du pion adverse

    Args:
        mon_pion (str): caractere du pion observe

    Returns:
        str: caractère du pion adverse
    """
    symbole_adverse = Croix()
    if mon_pion == "X":
        symbole_adverse = Rond()
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


def evaluation_v3(grille: Grille) -> int:
    """
    Fonction d'évaluation de la grille.
    L'évaluation est calculé indépendamment de la pièce qui vient d'être déposée.
    :param grille: La Grille avec les pièces
    :return: l'évaluation de la grille
    """

    score = 0
    # Evaluation de la colonne centrale
    colonne_central = [i for i in list(grille.grille[3][:])]

    # Evaluation Horizontal -
    for ligne in range(6):
        contenu_ligne = [i for i in list(grille.get_ligne(ligne))]
        for colonne in range(4):
            # une portion de 4 jetons de la ligne
            segment = contenu_ligne[colonne: colonne + 4]
            score += evaluate_segment(segment)

    # Evaluation Vertical |
    for colonne in range(7):
        contenu_colonne = [i for i in list(grille.get_colonne(colonne))]
        for ligne in range(4):
            segment = contenu_colonne[ligne: ligne + 4]
            score += evaluate_segment(segment)

    # Evaluation Diagonale NO-SE /
    for ligne in range(3):
        for colonne in range(4):
            segment = [grille.grille[colonne + i][ligne + i] for i in range(4)]
            score += evaluate_segment(segment)

    # Evaluation Diagonale NE-SO \
    for ligne in range(3):
        for colonne in range(4):
            segment = [grille.grille[colonne + i][ligne + 3 - i] for i in range(4)]
            score += evaluate_segment(segment)

    return score


def evaluate_segment(segment: list[Rond | Croix | None]) -> int:
    """
    Évalue le score d'une partie de la grille
    :param segment: partie du plateau avec toutes les pièces qui ont été placées
    :return: le score de la partie de la grille
    """
    global VALEUR_X, VALEUR_O
    score = 0

    nb_rond = segment.count(Rond())
    nb_croix = segment.count(Croix())
    nb_case_vide = 4 - (nb_rond + nb_croix)

    if nb_rond == 4:
        # 4 pièces alignées → victoire
        score += 20 * VALEUR_O

    elif nb_rond == 3 and nb_case_vide == 1:
        # 3 pièces alignées et une case vide → avantage
        score += 3 * VALEUR_O

    elif nb_rond == 2 and nb_case_vide == 2:
        # 2 pièces alignées et deux cases vides
        score += VALEUR_O

    if nb_croix == 4:
        score += 20 * VALEUR_X

    elif nb_croix == 3 and nb_case_vide == 1:
        score += 3 * VALEUR_X

    elif nb_croix == 2 and nb_case_vide == 2:
        score += VALEUR_X

    return score
