# Créé par henzo, le 20/11/2024 avec Python 3.7 en UTF-8

from os import system
from typing import List
from Saisie_variable import saisie_oui_non

def pseudo_deja_cree(liste_pseudo:List[str], pseudo:str)->bool:
    """
    fonction qui revoie un booleen si le pseudo existe deje (se trouve dans la liste de pseudo)

    entree : liste_pseudo -> liste de pseudo existant
             pseudo -> pseudo sur lequel on se demande s'il existe deja
    sortie : un booleen
                -> vraai (True) : le pseudo existe
                -> faux (False) : le pseudo n'existe pas encore
    """

    i : int
    res : bool

    i = 0

    if len(liste_pseudo) == 0:
        res = False
    else:
        while i < len(liste_pseudo) - 1 and liste_pseudo[i] != pseudo:
            i = i + 1
        res = liste_pseudo[i] == pseudo

    return res

def verif_pseudo(pseudo:str)->bool:
    """
    fonction qui verifie si le pseudo est correcte ou pas

    entree : une chaine de caractere qui represente le pseudo
    sortie : un booleen
                -> vrai (True)  : le pseudo est valide
                -> faux (False) : le pseudo est invalide
    """
    i : int
    res : bool

    i = 0

    if len(pseudo) == 0 :
        res = False
    else:

        while i < len(pseudo) - 1 and pseudo[i] == ' ': # si le pseudo contient QUE des espaces alors il est invalide
            i = i + 1
        res = (pseudo[i] != ' ')

    return res

def connection(pseudo_existant:List[str], numero:int)->str:
    """
    fonction de connexion

    entree : une liste de pseudo existant
             un entier qui represente le numero du joueur
    sortie : une chaine de caracteres qui represente le pseudo du l'utilisateur
    """
    pseudo : str
    choix : str

    system("cls")

    pseudo = ""
    choix = False

    while pseudo == "":
        print(f"Joueur {numero}, quel est votre pseudo ?")
        pseudo = input(">> ")
        system("cls")

        if not verif_pseudo(pseudo):
            print("Erreur : votre nom doit contenir au moins un caractere et ne doit pas etre composé uniquement d'espace")

        elif pseudo_deja_cree(pseudo_existant, pseudo):
            choix = saisie_oui_non(f"Voulez vous connecter en tant que {pseudo} et ainsi reprendre les scores qui lui sont associés ?",
                                    "Erreur de saisie")
        else:
            choix = saisie_oui_non(f"Voulez vous connecter en tant que {pseudo} ?",
                                    "Erreur de saisie")

        if not choix:
            pseudo = ""

    return pseudo

