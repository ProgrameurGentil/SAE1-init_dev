# Créé par henzo, le 23/10/2024 avec Python 3.7 en UTF-8

import os # systeme
from Morpion import morpion # jeu n3
from Allumettes import allumettes # jeu n2
from Devinette import Devinette as devienette # jeu n1
from aide_jeu import aide_morpion, aide_allumettes, aide_devinette # aide des jeu
from typing import List # typage
from typing import Callable as Function, Callable as Procedure # typage
from Score import Scores_joueur, Rang_score, score_update, get_score, somme_score, meilleur_score, trie_score # gestion des scores
from enregistrement import sauvegarde # sauvegarde des donnees

def affichage_nb_score(n_joueur : int, l_score:List[int], nom_jeu:str):
    """
    procedure qui affiche les scores dans l'odre decroissant du joueur

    entree : un entier qui correspond au numero du joueur
             une liste d'entier qui correspond au score du joueur
             une chaine de caractere qui correspond au nom du jeu
    """
    null : str # varible ne servant à rien
    l_score_rang : List[Rang_score]
    i : int

    l_score_rang = trie_score(l_score)

    print(f"Voici la liste des scores dans l'orde decroissant du joueur {n_joueur} dans le jeu {nom_jeu}: ")
    for i in rang(len(l_score_rang)):
        print(f"{i+1} Position : partie n°{l_score_rang[i].n_partie} avec {l_score_rang[i].valeur} pnts")
    print()

def menu(scores_j1:Scores_joueur, scores_j2:Scores_joueur):
    """
    procedure du menu principal :
        selection de jeu
        envoie dans le sous menu

    entree : scores_j1 & scores_j2 : stucture Scores_joueur du joueur 1 et 2
    """
    choix : int
    choix = 0 # initilisation de la variable choix
    while choix != 4: # tant que le choix n'est pas de quitter le menu n'est pas choisi
        print("Quel jeu voulez-vous choisir ?")
        print("1) Devinette")
        print("2) Allumettes")
        print("3) Morpion")
        print("4) Quitter")
        choix = int(input(">> "))
        os.system("cls")

        if choix < 0 or choix > 4: # gestion des erreurs
            print("Erreur, le choix n'est pas valide")

        if choix == 1:
            print("jeu 1")
            sous_menu("Devinette", devinette, aide_devinette, scores_j1, scores_j2)
        elif choix == 2:
            print("jeu 2")
            sous_menu("Allumettes", allumettes, aide_allumettes, scores_j1, scores_j2)
        elif choix == 3:
            print("jeu 3")
            sous_menu("Morpion", morpion, aide_morpion, scores_j1, scores_j2)
    sauvegarde(scores_j1, scores_j2)

def sous_menu(nom_jeu:str, fonc_jeu:Function, fonc_aide:Procedure, scores_j1:Scores_joueur, scores_j2:Scores_joueur):
    """
    Procedure affichant le sous menu. Possibilite de jouer, demander de l'aide et de quitter
    Entree : nom_jeu   : chaine de caractere representant le nom du jeu choisi
             fonc_jeu  : procedure du jeu choisi
             fonc_aide : procedure d'aide pour la comprehention du jeu
             scores_j1 & scores_j2 : stucture Scores_joueur du joueur 1 et 2
    """
    null : str
    choix : int

    choix = 0 # initilisation de la variable choix
    while choix != 4: # tant que le choix n'est pas de quitter le sous menu du jeu choisi
        print("Vous avez choisi le jeu", nom_jeu, ". Que voulez-vois faire ?")
        print("1) Jouer")
        print("2) Aide")
        print("3) Scores precedent")
        print("4) Quitter")
        choix = int(input(">> "))
        os.system("cls")

        if choix < 1 or choix > 4: # gestion des erreurs
            print("Erreur : le choix n'est pas valide.")

        if choix == 1:
            fonc_jeu(0, 0)

        elif choix == 2:
            fonc_aide()

        elif choix == 3:
            os.system("cls")
            affichage_nb_score(scores_j1.n_joueur, get_score(nom_jeu, scores_j1), nom_jeu)
            affichage_nb_score(scores_j1.n_joueur, get_score(nom_jeu, scores_j1), nom_jeu)
            null = input("\n(taper sur entree pour continuer...)")
            os.system("cls")