# Créé par henzo, le 10/11/2024 avec Python 3.7 en UTF-8
"""
d'empendance :
 typing
 os
 io
 pickle
 pathlib
 random
"""
from enregistrement import sauvegarde, chargement_nb_pnts, liste_pseudo_existant # sauvegarde et chargement des donnees
from Score import Scores_joueur, initialisation_score, score_update, get_last_score, get_score # gestion des scores
from Menu import menu # menu principal
from Login import connexion
from typing import List # typage
import os # systeme

if __name__ == '__main__':
    mat_pnts_j1 : List[List[int]]
    mat_pnts_j2 : List[List[int]]
    structure_joueur1 : Scores_joueur
    structure_joueur2 : Scores_joueur
    nom_j1 : str
    nom_j2 : str

    nom_j1 = connexion(liste_pseudo_existant(), 1)
    nom_j2 = connexion(liste_pseudo_existant(), 2, nom_j1)

    mat_pnts_j1 = chargement_nb_pnts(nom_j1)
    mat_pnts_j2 = chargement_nb_pnts(nom_j2)

    structure_joueur1 = initialisation_score(nom_j1, 1, mat_pnts_j1[0], mat_pnts_j1[1], mat_pnts_j1[2])
    structure_joueur2 = initialisation_score(nom_j2, 2, mat_pnts_j2[0], mat_pnts_j2[1], mat_pnts_j2[2])

    os.system("cls")
    menu(structure_joueur1, structure_joueur2) # lancement du menu
    os.system("cls")

"""
il n'y a aucun cas de test pour ce script
"""
