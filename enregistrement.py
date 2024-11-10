# Créé par henzo, le 24/10/2024 avec Python 3.7 en UTF-8

import pickle
from os.path import exists
import os

# ----------------------------- # fonction interne

def lecture()->tuple:
    """
    procedure (interne) qui lit le fichier sauvegarde_score.bu où sont stokés les scores du joueur 1 et joueur 2
    entree : rien
    sortie : un tuple (liste des nombres de points du joueur 1 , liste des nombres de points du joueur 2)
    """
    liste_score : list
    sauvgarde : pickle.io.BufferedReader

    if not exists(f'{os.getcwd()}\\sauvegarde_score.bu'):
        return ""
    with open(f'{os.getcwd()}\\sauvegarde_score.bu', 'rb') as sauvgarde:
        liste_score = list(pickle.load(sauvgarde))
    return liste_score

def ecriture(score:tuple):
    """
    procedure (interne) qui ecrit dans le fichier sauvegarde_score.bu les scores des joueur 1 et 2
    entree : un tuple (liste des nombres de points du joueur 1 , liste des nombres de points du joueur 2)
    sortie : rien
    """
    f1 : pickle.io.BufferedWriter

    with open(f'{os.getcwd()}\\sauvegarde_score.bu', 'wb') as f1:
        pickle.dump(score, f1)

# ----------------------------- # fonction d'utilisation

def saugarde(liste_point_j1 : list, liste_point_j2 : list):
    """
    procedure qui sauvgarde les scores des joueur 1 et 2
    entree : liste_point_j1 -> liste des points du joueur 1
             liste_point_j2 -> liste des points du joueur 2
    sortie : rien
    """
    liste_saugarde : tuple

    ecriture( (liste_point_j1, liste_point_j2) )

def chargement_nb_pnts_j1() -> list:
    """
    fonction qui donne la liste du nombre de pnts du joueur 1
    entree : rien
    sortie : une liste
    """
    donnees : tuple

    donnees = lecture()
    return donnees[0]

def chargement_nb_pnts_j2() -> list:
    """
    fonction qui donne la liste du nombre de pnts du joueur 2
    entree : rien
    sortie : une liste
    """
    donnees : tuple

    donnees = lecture()
    return donnees[1]