# Créé par henzo, le 23/10/2024 avec Python 3.7 en UTF-8

import os # systeme
from Morpion import morpion # jeu n3
from Allumettes import allumettes # jeu n2
from Devinette import Devinette as devienette # jeu n1
from aide_jeu import aide_morpion, aide_allumettes, aide_devinette # aide des jeu
from typing import List # typage
from typing import Callable as Function, Callable as Procedure # typage
from Score import Scores_joueur, Rang_score, score_update, get_score, somme_score, somme_score_interjeux, meilleur_score, trie_score # gestion des scores
from enregistrement import sauvegarde # sauvegarde des donnees

def affichage_nb_score(nom_joueur : str, l_score:List[int], nom_jeu:str):
    """
    procedure qui affiche les scores dans l'ordre decroissant du joueur

    entree : une liste d'entier qui correspond au score du joueur
             deux chaines de caracteres qui correspondent au du joueur et du nom du jeu
    """
    l_score_rang : List[Rang_score]
    i : int

    l_score_rang = trie_score(l_score)

    print(f"Voici la liste des scores dans l'orde decroissant du joueur {nom_joueur} dans le jeu {nom_jeu}: ")
    if len(l_score_rang) == 0: # si il n'y a pas de score enregistre
        print("Ah... Vous n'avez pas encore de points dans ce jeu...")
    else:
        print(f"Somme des scores : {somme_score(l_score)}")
        for i in range(len(l_score_rang)):
            print(f"{i+1} Position : partie n°{l_score_rang[i].n_partie} avec {l_score_rang[i].valeur} pnts")
    print()

def affichage_nb_score_total(scores:Scores_joueur):
    """
    procedure qui le score total (inter jeux) d'un joueur

    entree : une structure Scores_joueur
             une chaine de caracteres qui correspond au du nom du jeu
    """
    somme : int
    somme = somme_score_interjeux(scores)

    print(f"Voici la somme des scores du joueur {scores.pseudo} dans tout les jeux : ", end="")
    if somme == 0: # si il n'y a pas de score enregistre
        print("Ah... Vous n'avez aucun point enregisté...")
    else:
        print(f"{somme} pnts")
    print()

def menu(scores_j1:Scores_joueur, scores_j2:Scores_joueur):
    """
    procedure du menu principal :
        selection de jeu
        envoie dans le sous menu

    entree : scores_j1 & scores_j2 : stucture Scores_joueur du joueur 1 et 2
    """
    choix : int
    null : str
    choix = 0 # initilisation de la variable choix
    while choix != 5: # tant que le choix n'est pas de quitter le menu n'est pas choisi
        print("Quel jeu voulez-vous choisir ?")
        print("1) Devinette")
        print("2) Allumettes")
        print("3) Morpion")
        print("4) Score total (inter-jeux)")
        print("5) Quitter")
        choix = int(input(">> "))
        os.system("cls" if os.name == "nt" else "clear")

        if choix < 0 or choix > 5: # gestion des erreurs
            print("Erreur, le choix n'est pas valide")

        if choix == 1:
            sous_menu("Devinette", devienette, aide_devinette, scores_j1, scores_j2)

        elif choix == 2:
            sous_menu("Allumettes", allumettes, aide_allumettes, scores_j1, scores_j2)

        elif choix == 3:
            sous_menu("Morpion", morpion, aide_morpion, scores_j1, scores_j2)

        elif choix == 4: # affichage de la somme des scores de tout les jeux des joueurs
            os.system("cls" if os.name == "nt" else "clear")
            affichage_nb_score_total(scores_j1)
            affichage_nb_score_total(scores_j2)
            null = input("\n(taper sur entree pour continuer...)")
            os.system("cls" if os.name == "nt" else "clear")

    sauvegarde(scores_j1, scores_j2)

def sous_menu(nom_jeu:str, fonc_jeu:Function, fonc_aide:Procedure, scores_j1:Scores_joueur, scores_j2:Scores_joueur):
    """
    procedure affichant le sous menu. Possibilite de jouer, demander de l'aide et de quitter

    entree : nom_jeu   : chaine de caractere representant le nom du jeu choisi
             fonc_jeu  : procedure du jeu choisi
             fonc_aide : procedure d'aide pour la comprehention du jeu
             scores_j1 & scores_j2 : stucture Scores_joueur du joueur 1 et 2
    """
    null : str
    choix : int
    scores : tuple

    choix = 0 # initilisation de la variable choix
    while choix != 4: # tant que le choix n'est pas de quitter le sous menu du jeu choisi
        print("Vous avez choisi le jeu", nom_jeu, ". Que voulez-vois faire ?")
        print("1) Jouer")
        print("2) Aide")
        print("3) Scores precedent")
        print("4) Quitter et revenir au menu principal")
        choix = int(input(">> "))
        os.system("cls" if os.name == "nt" else "clear")

        if choix < 1 or choix > 4: # gestion des erreurs
            print("Erreur : le choix n'est pas valide.")

        if choix == 1: # Jouer
            os.system("cls" if os.name == "nt" else "clear")
            scores = fonc_jeu(0, 0, scores_j1.pseudo, scores_j2.pseudo)
            score_update(nom_jeu, scores_j1, scores[0])
            score_update(nom_jeu, scores_j2, scores[1])
            os.system("cls" if os.name == "nt" else "clear")

        elif choix == 2: # Aide
            os.system("cls" if os.name == "nt" else "clear")
            fonc_aide()
            os.system("cls" if os.name == "nt" else "clear")

        elif choix == 3: # Scores precedent
            os.system("cls" if os.name == "nt" else "clear")
            affichage_nb_score(scores_j1.pseudo, get_score(nom_jeu, scores_j1), nom_jeu)
            affichage_nb_score(scores_j2.pseudo, get_score(nom_jeu, scores_j2), nom_jeu)
            null = input("\n(taper sur entree pour continuer...)")
            os.system("cls" if os.name == "nt" else "clear")

"""
la procedure afffichage_nb_score peut etre teste en mettant un numero de joueur et un nom de jeu quelconque ainsi que differente liste d'entier (scores) trie ou non trie
la procedure menu peut etre teste en mettant differentes structures de joueurs remplie ou vide (mais avec de valeur initialise bien sur)
la procedure sous_menu peut etre teste en mettant un nom de jeu, une fonction et une procedure quelconque et avec differentes structures de joueurs remplie ou vide (mais avec de valeur initialise bien sur)
"""
