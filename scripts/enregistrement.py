# Créé par henzo, le 24/10/2024 avec Python 3.7 en UTF-8

import pickle # module d'enregistrement
from os.path import exists, dirname, realpath # systeme
from typing import List, Tuple, BinaryIO # typage
import os # systeme
from pathlib import Path # systeme
from Score import Scores_joueur # gestion des scores

# ----------------------------- # fonction interne

def lecture()->tuple:
    """
    fonction (interne) qui lit le fichier sauvegarde_score.bu où sont stokés les scores des joueurs

    sortie : un dictionnaire sous forme {<nom joueur> : {<jeu1>:<liste scores>, <jeu2>:<liste scores>, <jeu3>:<liste scores>}, ... }
                                 typage {chaine       : {chaine:liste         , chaine:liste         , chaine:liste          , ... }
    """
    scores : dict
    sauvgarde : pickle.io.BufferedReader # BinaryIO

    if exists(f'{dirname(realpath(__file__))}/sauvegarde_score.bu'):
        with open(f'{dirname(realpath(__file__))}/sauvegarde_score.bu', 'rb') as sauvgarde:
            scores = pickle.load(sauvgarde)

    else:
        scores = {}

    return scores

def ecriture(score:dict):
    """
    procedure (interne) qui ecrit dans le fichier sauvegarde_score.bu les scores des joueurs

    entree : un dictionnaire sous forme {<nom joueur> : {<jeu1>:<liste scores>, <jeu2>:<liste scores>, <jeu3>:<liste scores>}, ... }
                                 typage {chaine       : {chaine:liste         , chaine:liste         , chaine:liste          , ... }
    """
    f1 : pickle.io.BufferedWriter # BinaryIO

    with open(f'{dirname(realpath(__file__))}/sauvegarde_score.bu', 'wb') as f1:
        pickle.dump(score, f1)

# ----------------------------- # fonction d'utilisation

def sauvegarde(scores_j1 : Scores_joueur, scores_j2 : Scores_joueur):
    """
    procedure qui sauvgarde les scores des joueur 1 et 2

    entree : deux structures Scores_joueur representant successivement celle du joueur 1 et du joueur 2
    """
    dico_sauvegarde : dict

    dico_sauvegarde = lecture()
    dico_sauvegarde[scores_j1.pseudo] = {"Devinette":scores_j1.liste_score_devinette, "Allumettes":scores_j1.liste_score_allumettes, "Morpion":scores_j1.liste_score_morpion}
    dico_sauvegarde[scores_j2.pseudo] = {"Devinette":scores_j2.liste_score_devinette, "Allumettes":scores_j2.liste_score_allumettes, "Morpion":scores_j2.liste_score_morpion}

    ecriture( dico_sauvegarde )

def chargement_nb_pnts(pseudo:str) -> List[List[int]]:
    """
    fonction qui donne la liste du nombre de pnts d'un joueur en fonction de se pseudo

    entree : une chaine de caracteres qui represente le pseudo du joueur
    sortie : une matrice
                -> liste de scores jeu 1, liste de scores jeu 2, liste de scores jeu 3
    """
    donnees : dict
    dico_scores : dict
    scores : List[List[int]]

    donnees = lecture()
    if pseudo in donnees.keys():
        dico_scores = donnees[pseudo]

        scores = []
        if "Devinette" in dico_scores: # on verfie que les scores de la devinette sont presents
            scores.append(dico_scores["Devinette"])
        else:
            scores.append([])

        if "Allumettes" in dico_scores: # on verfie que les scores des allumettes sont presents
            scores.append(dico_scores["Allumettes"])
        else:
            scores.append([])

        if "Morpion" in dico_scores: # on verfie que les scores du morpion sont presents
            scores.append(dico_scores["Morpion"])
        else:
            scores.append([])

    else:
        scores = [[], [], []]

    return scores

def liste_pseudo_existant()->List[str]:
    """
    fonction qui retourne la liste des pseudo deja existant

    sortie : une liste de chaine de caractere qui represente les pseudo existant
    """
    donnees : dict

    donnees = lecture()

    return list(donnees.keys())


"""
la fonction lecture n'a pas de cas de test
la procedure d'ecriture n'a vraiment de cas de test mais on peut tester en mettant different tuple de longueur variable
la procedure sauvegarde peut etre teste en mettant differente structure Score_joueur en parametre
les fonctions chargement_nb_pnts_j1 et chargement_nb_pnts_j2 n'ont pas de cas de test
"""

# debug

##ecriture({"admin":{"Devinette":[], "Allumettes":[], "Morpion":[]}})

##print(lecture())
##print(chargement_nb_pnts("henzo"))
