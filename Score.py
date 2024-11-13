# Créé par henzo, le 09/11/2024 avec Python 3.7 en UTF-8

from typing import List # typage

class Scores_joueur:
    """
    Structure qui prend en memtoire la listes des points des differents jeux d'un joueur
    n_joueur : int -> numero du joueur
    liste_score_devinette : List[int] -> liste de score du jeu de la devinette
    liste_score_allumettes : List[int] -> liste de score du jeu des allumettes
    liste_score_morpion : List[int] -> liste de score du jeu du morpion
    """
    n_joueur : int # numero du joueur
    liste_score_devinette : List[int] # liste de score du jeu de la devinette
    liste_score_allumettes : List[int] # liste de score du jeu des allumettes
    liste_score_morpion : List[int] # liste de score du jeu du morpion

class Rang_score:
    """
    Structure qui prend en memoir la position du score (n_partie) et sa valeur (valeur)
    n_partie : int -> numero de la partie
    valeur   : int -> valeur du score
    """
    n_partie : int # numero de la partie
    valeur : int # valeur du score

def initialisation_score(n_joueur:int, ls_devinette:List[int], ls_allumettes:List[int], ls_morpion:List[int])->Scores_joueur:
    """
    fonction qui initialise les scores d'un joueur dans la strucuture Scores_joueur

    entree : un entier qui correspond au numéro d'un joueur soit 1, soit 2
             trois liste d'entier qui correspond seccessivement aux listes des scores du jeu des devinettes, des allumettes et du mopion
    sortie : une structure Scores_joueur
    """
    score_j : Scores_joueur

    assert n_joueur == 1 or n_joueur == 2 # verification que le numero du joueur est soit 1, soit 2

    score_j = Scores_joueur() # initialisation de la structure
    # affectation des donnees :
    score_j.n_joueur = n_joueur
    score_j.liste_score_allumettes = ls_allumettes
    score_j.liste_score_devinette = ls_devinette
    score_j.liste_score_morpion = ls_morpion

    return score_j

def score_update(jeu:str, scores_joueur:Scores_joueur, nouveau_score:int):
    """
    procedure qui met a jour les donnees d'une strucure Score_joueur en fonction du jeu et du nouveau score a enregister

    entree : une chaine de caracteres qui correspond soit à "Devinette", "Allumettes" ou a "Morpion
             une sctucure Scores_joueur
             un entier qui correspond au nouveau score qui doit etre enregiste
    """

    jeu = jeu.lower()

    assert jeu == "allumettes" or jeu == "morpion" or jeu == "devienette" # verification du jeu

    # ajout du score a la liste de scores en fonction du jeu :
    if jeu == "allumettes":
        scores_joueur.liste_score_allumettes.append(nouveau_score)
    elif jeu == "morpion":
        scores_joueur.liste_score_morpion.append(nouveau_score)
    else:
        scores_joueur.liste_score_devinette.append(nouveau_score)

def get_last_score(jeu:str, scores_joueur:Scores_joueur)->int:
    """
    fonction qui renvoie le dernier score d'un jeu qui a ete ajoute dans une struture Scores_joueur donnee

    entree : une chaine de caracteres qui correspond soit à "Devinette", "Allumettes" ou a "Morpion
             une sctucure Scores_joueur
    sortie : un entier qui correspond au dernier score enregistre dans la structure
    """
    score : int
    score = 0

    jeu = jeu.lower()

    assert jeu == "allumettes" or jeu == "morpion" or jeu == "devinette" # verification du jeu

    if jeu == "allumettes" and len(scores_joueur.liste_score_allumettes) > 0:
        score = scores_joueur.liste_score_allumettes[-1]
    elif jeu == "dorpion" and len(scores_joueur.liste_score_morpion) > 0:
        score = scores_joueur.liste_score_morpion[-1]
    elif len(scores_joueur.liste_score_devinette) > 0:
        score = scores_joueur.liste_score_devinette[-1]

    return score

def get_score(jeu:str, scores_joueur:Scores_joueur)->List[int]:
    """
    fonction qui renvoie la liste des scores d'un jeu

    entree : une chaine de caracteres qui correspond soit à "Devinette", "Allumettes" ou a "Morpion
             une sctucure Scores_joueur
    sortie : un liste d'entier qui correspond a la liste des scores du jeu
    """
    l_score : List[int]
    l_score = []

    jeu = jeu.lower()

    assert jeu == "allumettes" or jeu == "morpion" or jeu == "devinette" # verification du jeu

    if jeu == "allumettes" and len(scores_joueur.liste_score_allumettes) > 0:
        l_score = scores_joueur.liste_score_allumettes
    elif jeu == "morpion" and len(scores_joueur.liste_score_morpion) > 0:
        l_score = scores_joueur.liste_score_morpion
    elif len(scores_joueur.liste_score_devinette) > 0:
        l_score = scores_joueur.liste_score_devinette

    return l_score

def somme_score(l_score:List[int])->int:
    """
    fonction qui fait la somme des scores d'une liste de scores

    entree : une liste de scores
    sortie : un entier qui reprensente la somme des scores
    """
    i : int
    score_tt : int

    for i in range(len(l_score)):
        score_tt = score_tt + l_score[i]

    return score_tt

def meilleur_score(l_score:List[int])->int:
    """
    fonction qui revoie le meilleur score d'une liste de scores

    entree : une liste de scores
    sortie : un entier qui reprensente le meilleur des scores de la liste des scores
    """
    i : int
    score_m : int

    score_m = l_score[0]

    for i in range(1, len(l_score)):
        if score_m < l_score[i]:
            score_m[i] = l_score[i]

    return score_m

def trie_score(l_score:List[int])->List[Rang_score]:
    """
    fonction faisant un tri par selection par odre decroissant et revoie une liste de structure Rang_score

    entree : une liste de score
    sortie : une liste de structure Rang_score
    """
    l_score_trie : List[Rang_score] = []
    score_rang : Rang_score
    score : int
    i : int
    j : int

    # on transforme les valeurs de l_score en structure Rang_score (numero de position, valeur) et on les met dans l_score_trie
    for i in range(len(l_score)):
        score_rang = Rang_score()
        score_rang.n_partie = i + 1
        score_rang.valeur = l_score[i]
        l_score_trie.append(score_rang)

    # tri par selection par odre decroissant
    for i in range(1, len(l_score_trie)):
        score = l_score_trie[i]

        j = i
        while j > 0 and l_score_trie[j - 1].valeur < score.valeur:
            l_score_trie[j] = l_score_trie[j - 1]
            j = j - 1

        l_score_trie[j] = score

    return l_score_trie