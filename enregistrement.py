# Créé par henzo, le 24/10/2024 avec Python 3.7 en UTF-8

import pickle # module d'enregistrement
from os.path import exists # systeme
from typing import List, Tuple # typage
import os # systeme
from pathlib import Path # systeme
from Score import Scores_joueur # gestion des scores

# ----------------------------- # fonction interne

def lecture()->tuple:
    """
    fonction (interne) qui lit le fichier sauvegarde_score.bu où sont stokés les scores du joueur 1 et joueur 2

    sortie : un tuple ( matrice [liste_score_jeu 1, liste_score_jeu 2,liste_score_jeu 3] ) ,
                      ( matrice [liste_score_jeu 1, liste_score_jeu 2,liste_score_jeu 3] )
                -> sous la forme (joueur1, joueur2)
    """
    liste_score : list = [[[], [], []], [[], [], []]]
    sauvgarde : pickle.io.BufferedReader

    if exists(f'{os.getcwd()}/sauvegarde_score.bu'):
        with open(f'{os.getcwd()}/sauvegarde_score.bu', 'rb') as sauvgarde:
            liste_score = list(pickle.load(sauvgarde))

        if len(liste_score) != 2 or len(liste_score[0]) != 3 or len(liste_score[1]) != 3:
            liste_score  = [[[], [], []], [[], [], []]]

    return liste_score

def ecriture(score:tuple):
    """
    procedure (interne) qui ecrit dans le fichier sauvegarde_score.bu les scores des joueur 1 et 2

    entree : un tuple (liste des nombres de points du joueur 1 , liste des nombres de points du joueur 2)
    """
    f1 : pickle.io.BufferedWriter
    print(os.getcwd())
    with open(f'{os.getcwd()}/sauvegarde_score.bu', 'wb') as f1:
        pickle.dump(score, f1)

# ----------------------------- # fonction d'utilisation

def sauvegarde(scores_j1 : Scores_joueur, scores_j2 : Scores_joueur):
    """
    procedure qui sauvgarde les scores des joueur 1 et 2

    entree : deux structures Scores_joueur representant successivement celle du joueur 1 et du joueur 2
    """
    liste_sauvegarde : List[List[int]]

    liste_sauvegarde = [[scores_j1.liste_score_devinette, scores_j1.liste_score_allumettes, scores_j1.liste_score_morpion],
                        [scores_j2.liste_score_devinette, scores_j2.liste_score_allumettes, scores_j2.liste_score_morpion]]

    ecriture( liste_sauvegarde )

def chargement_nb_pnts_j1() -> list:
    """
    fonction qui donne la liste du nombre de pnts du joueur 1

    sortie : une matrice
                -> liste de scores jeu 1, liste de scores jeu 2, liste de scores jeu 3
    """
    donnees : tuple

    donnees = lecture()
    return donnees[0]

def chargement_nb_pnts_j2() -> list:
    """
    fonction qui donne la liste du nombre de pnts du joueur 2

    sortie : une matrice
                -> liste de scores jeu 1, liste de scores jeu 2, liste de scores jeu 3
    """
    donnees : tuple

    donnees = lecture()
    return donnees[1]