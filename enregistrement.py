# Créé par henzo, le 23/10/2024 en Python 3.7

import pickle
from os.path import exists
import os

def lecture()->str:
    liste_score : list
    sauvgarde : pickle.io.BufferedReader

    if not exists(f'{os.getcwd()}\\sauvegarde_score.bu'):
        return ""
    with open(f'{os.getcwd()}\\sauvegarde_score.bu', 'rb') as sauvgarde:
        liste_score = list(pickle.load(sauvgarde))
    return liste_score

def ecriture(liste_score:list):
    f1 : pickle.io.BufferedWriter

    with open(f'{os.getcwd()}\\sauvegarde_score.bu', 'wb') as f1:
        pickle.dump(liste_score, f1)

