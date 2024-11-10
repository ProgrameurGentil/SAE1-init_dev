# Créé par henzo, le 10/11/2024 avec Python 3.7 en UTF-8

from enregistrement import sauvegarde, chargement_nb_pnts_j1, chargement_nb_pnts_j2 # sauvegarde et chargement des donnees
from Score import Scores_joueur, initialisation_score, score_update, get_last_score, get_score # gestion des scores
from Menu import menu # menu principal
from typing import List # typage
import os # systeme

if __name__ == '__main__':
    mat_pnts_j1 : List[List[int]]
    mat_pnts_j2 : List[List[int]]
    structure_joueur1 : Scores_joueur
    structure_joueur2 : Scores_joueur

    mat_pnts_j1 = chargement_nb_pnts_j1()
    mat_pnts_j2 = chargement_nb_pnts_j2()

    structure_joueur1 = initialisation_score(1, mat_pnts_j1[0], mat_pnts_j1[1], mat_pnts_j1[2])
    structure_joueur2 = initialisation_score(2, mat_pnts_j2[0], mat_pnts_j2[1], mat_pnts_j2[2])

    os.system("cls")
    menu(structure_joueur1, structure_joueur2) # lancement du menu
    os.system("cls")