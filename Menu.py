# Créé par henzo, le 23/10/2024 avec Python 3.7 en UTF-8

#import <module du 1er jeu>
#import <module du 2e jeu>
#import <module du 3e jeu>
import os
from morpion import morpion
from Allumettes import allumettes
from aide_jeu import aide_morpion, aide_allumettes, aide_devinette

def somme_score(l_score:list):
    _l_score = l_score
    if len(_l_score) == 1:
        return _l_score[-1]
    return _l_score.pop() + somme_score(_l_score)

def menu():
    choix : int
    choix = 0 # initilisation de la variable choix
    while choix != 4: # tant que le choix n'est pas de quitter le menu n'est pas choisi
        print("Quel jeu voulez-vous choisir ?")
        print("1) Devinette")
        print("2) Allumettes")
        print("3) Morpion")
        print("4) Quitter")
        choix = int(input(">> "))
        os.system('cls')

        if choix < 0 or choix > 4:
            print("Erreur, le choix n'est pas valide")

        if choix == 1:
            print("jeu 1")
            sous_menu("Devinette", ..., aide_devinette, ..., ...)
        elif choix == 2:
            print("jeu 2")
            sous_menu("Allumettes", allumettes, aide_allumettes, ..., ...)
        elif choix == 3:
            print("jeu 3")
            sous_menu("Morpion", morpion, aide_morpion, ..., ...)

def sous_menu(nom_jeu : str, fonc_jeu, fonc_aide, l_score_j1, l_score_j2):
    """
    Procedure affichant le sous menu. Possibilite de jouer, demander de l'aide et de quitter
    Entree : nom_jeu   : chaine de caractere representant le nom du jeu choisi
             fonc_jeu  : procedure du jeu choisi
             fonc_aide : procedure d'aide pour la comprehention du jeu
    """
    choix : int
    choix = 0 # initilisation de la variable choix
    while choix != 3: # tant que le choix n'est pas de quitter le sous menu du jeu choisi
        print("Vous avez choisi le jeu", nom_jeu, ". Que voulez-vois faire ?")
        print("1) Jouer")
        print("2) Aide")
        print("3) Quitter")
        choix = int(input(">> "))
        os.system('cls')

        if choix < 1 or choix > 3:
            print("Erreur : le choix n'est pas valide.")

        if choix == 1:
            fonc_jeu()
        elif choix == 2:
            fonc_aide()
