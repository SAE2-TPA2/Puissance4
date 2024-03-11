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


def min_max(grille: Grille, profondeur: int, mon_pion: Jeton, pion_adverse: Jeton, qui_joue: Rond | Croix,
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
            return evaluation_v3(grille)

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


def evaluation_v2(grille: Grille, mon_pion: Jeton) -> int:
    """
    Fonction d'évaluation renvoi un int correspondant au score de la grille
    :param mon_pion: Le pion qui joue (correspond au joueur maximisant
    son score)
    :param grille: la grille du jeu évalué
    :return: la valeur correspondant au score de la grille
    """
    score_initial = 0
    caractere_decrement_score = get_pion_adverse(mon_pion)
    resultat_gagner = grille.est_gagnee(5)

    if resultat_gagner is None: #verification que la grille est non gagnante
        score_initial += evaluation_placement(grille, mon_pion)
        score_initial += lecture_score_alignement(grille, mon_pion)
        score_initial -= lecture_score_alignement(grille, caractere_decrement_score)
    elif resultat_gagner.getcaractere() == mon_pion.get_caractere():
        score_initial = 100
    else:
        score_initial = -100
    return score_initial


def evaluation_placement(grille: Grille, caractere_observe: str) -> int:
    """
    Donne le score initial avec l'emplacement des pions sans prendre en compte
    les alignements

    Args :
        caractere_observe : permet de connaitre le
        caractère correspondant à la maximisation du score
        grille (Grille) : grille de jeu

    Returns :
        int : entier correspondant à un avantage si positif pour le joueur ayant le caractère
        cherchant a maximisé son score, désavantage si le int obtenu est négatif cela correspond
         à un désanvatage pour le joueur cherchant a minimisé son score
    """

    score_a_ajouter = 0
    score_emplacement = [-1, 0, 0, 1, 0, 0, -1,
                         0, 0, 1, 2, 1, 0, 0,
                         0, 1, 2, 3, 2, 1, 0,
                         0, 1, 2, 3, 2, 1, 0,
                         0, 0, 1, 2, 1, 0, 0,
                         -1, 0, 0, 1, 0, 0, -1] # tableau modulable pour augmenter
                                                # ou diminuer la précision de l'évaluation

    indice_lecture = 0

    for i in range(6): #parcour de la grille pour attribuer le score de placement
        for j in range(7):
            if grille.get_case(i, j) is not None:
                if grille.get_case(i, j).get_caractere() == caractere_observe:
                    score_a_ajouter += score_emplacement[indice_lecture]
                else:
                    score_a_ajouter -= score_emplacement[indice_lecture]
            indice_lecture += 1

    return score_a_ajouter

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
    for i in range(6):#parcour de toute la grille
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

    for i in range(8):# lecture de l'ensemble des 8 directions du pion
        match i:
            case 0:  # EST
                score_horizontal += lecture_alignement(grille, ligne, colonne, 1, 0, symboleObserve)
            case 1:  # SUD-EST
                score_diagonale_nose += lecture_alignement(grille, ligne, colonne, 1, -1, symboleObserve)
            case 2:  # SUD
                score_vertical += lecture_alignement(grille, ligne, colonne, 0, -1, symboleObserve)
            case 3:  # SUD-OUEST
                score_diagonale_sone += lecture_alignement(grille, ligne, colonne, -1, -1, symboleObserve)
            case 4:  # OUEST
                if score_horizontal != 0:
                    score_horizontal += -1
                score_horizontal += lecture_alignement(grille, ligne, colonne, -1, 0, symboleObserve)
            case 5:  # NORD-OUEST
                if score_diagonale_nose != 0:
                    score_diagonale_nose += -1
                score_diagonale_nose += lecture_alignement(grille, ligne, colonne, -1, 1, symboleObserve)
            case 6:  # NORD
                if score_vertical != 0:
                    score_vertical += -1
                score_vertical += lecture_alignement(grille, ligne, colonne, 0, 1, symboleObserve)
            case 7:  # NORD-EST
                if score_diagonale_sone != 0:
                    score_diagonale_sone += -1
                score_diagonale_sone += lecture_alignement(grille, ligne, colonne, 1, 1, symboleObserve)

    scores = [score_horizontal, score_vertical, score_diagonale_nose, score_diagonale_sone]
    for score in scores:
        if score % 10 == 1 and score / 10 >= 3:
            score_to_add += 1
        elif score % 10 == 2 and score / 10 >= 2:
            score_to_add += 2
        elif score % 10 == 3 and score / 10 == 1:
            score_to_add += 3
        elif score % 10 == 3 and score / 10 >= 2:
            score_to_add += 5

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

    return score_a_return


def get_pion_adverse(mon_pion: Jeton) -> str:
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
    :param piece: Rond ou Croix selon le joueur
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
    :param pion: Rond ou Croix selon le joueur
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
