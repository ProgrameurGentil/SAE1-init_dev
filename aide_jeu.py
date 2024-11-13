# Créé par henzo, le 07/11/2024 avec Python 3.7 en UTF-8

from os.path import exists # systeme
from os import system, getcwd # systeme
from io import TextIOWrapper

# Les fichiers textes (.txt) doivent etre dans le meme repertoire que le script
# pour fonctionner.

def aide(chemin_aide:str):
    """
    procedure qui affiche l'aide des jeux en fonction du fichier d'aide mis en parametre
    si le chemin d'acces est enexistant alors une erreur est levé
    entree : une chaine de caractere
    """
    fichier : TextIOWrapper
    fichier_ouvert : str
    nul : str

    system('cls')
    if not exists(chemin_aide): # verification de l'existance du fichier
        print("Le fichier d'aide lié à ce jeu n'a pas été trouvé")
    else:
        with open(chemin_aide, encoding="UTF-8") as fichier: # l'encodage des fichiers textes est en UTF-8
            fichier_ouvert = fichier.read()

        print(fichier_ouvert) # affichage de l'aide

    nul = input("Pour quitter, appuyez sur entree...")
    system('cls')

def aide_morpion():
    """
    procedure qui affiche l'aide du jeu morpion
    """
    chemin_acces : str
    chemin_acces = f"{getcwd()}/aide_morpion.txt"
    print("e:", exists(chemin_acces), chemin_acces)

    aide(chemin_acces)

def aide_allumettes():
    """
    procedure qui affiche l'aide du jeu des allumettes
    """
    chemin_acces : str
    chemin_acces = f"{getcwd()}/aide_allumettes.txt"
    aide(chemin_acces)

def aide_devinette():
    """
    procedure qui affiche l'aide du jeu de la devinette
    """
    chemin_acces : str
    chemin_acces = f"{getcwd()}/aide_devinette.txt"

    aide(chemin_acces)

# debug
aide_morpion()