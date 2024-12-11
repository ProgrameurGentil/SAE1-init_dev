# Créé par henzo, le 07/11/2024 avec Python 3.7 en UTF-8

from os.path import exists, dirname, realpath # systeme
from os import system, getcwd, name # systeme
from io import TextIOWrapper

# Les fichiers textes (.txt) doivent etre dans le meme repertoire que le script
# pour fonctionner.

# taille minimum pour la fenetre cmd : Colonnes : 125, Lignes : 30

def aide(chemin_aide:str):
    """
    procedure qui affiche l'aide des jeux en fonction du fichier d'aide mis en parametre
    si le chemin d'acces est enexistant alors une erreur est levé
    entree : une chaine de caractere
    """
    fichier : TextIOWrapper
    fichier_ouvert : str
    nul : str

    system("cls" if name == "nt" else "clear")
    #if not exists(chemin_aide): # verification de l'existance du fichier
    #    print("Le fichier d'aide lié à ce jeu n'a pas été trouvé")
    #else:
    with open(chemin_aide, encoding="UTF-8") as fichier: # l'encodage des fichiers textes est en UTF-8
        fichier_ouvert = fichier.read()

    print(fichier_ouvert) # affichage de l'aide

    nul = input("Pour quitter, appuyez sur entree...")
    system("cls" if name == "nt" else "clear")

def aide_morpion():
    """
    procedure qui affiche l'aide du jeu morpion
    """
    chemin_acces : str
    chemin_acces = f"{dirname(realpath(__file__))}/aide_morpion.txt"
    ##print("e:", exists(chemin_acces), chemin_acces) # debug

    aide(chemin_acces)

def aide_allumettes():
    """
    procedure qui affiche l'aide du jeu des allumettes
    """
    chemin_acces : str
    chemin_acces = f"{dirname(realpath(__file__))}/aide_allumettes.txt"
    aide(chemin_acces)

def aide_devinette():
    """
    procedure qui affiche l'aide du jeu de la devinette
    """
    chemin_acces : str
    chemin_acces = f"{dirname(realpath(__file__))}/aide_devinette.txt"

    aide(chemin_acces)

# debug
##aide_morpion()
##print(dirname(realpath(__file__)))

"""
il n'y a aucun cas de test pour les procedure aide_morpion, aide_allumettes et aide_devinette
pour la procedure aide on peut tester un fichier texte non valide (chemin qui n'existe pas)
"""