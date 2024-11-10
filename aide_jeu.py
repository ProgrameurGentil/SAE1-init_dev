# Créé par henzo, le 07/11/2024 avec Python 3.7 en UTF-8

from os.path import exists
from os import system

def aide(chemin_aide:str):
    """
    procedure qui affiche l'aide des jeux en fonction du fichier d'aide mis en parametre
    si le chemin d'acces est enexistant alors une erreur est levé
    entree : une chaine de caractere
    """
    fichier : ...
    fichier_ouvert : str
    nul : str

    if not exists(chemin_aide):
        raise FileExistsError("§§ le fichier d'aide n'est pas trouvé §§")

    system('cls')
    with open(chemin_aide) as fichier:
        fichier_ouvert = fichier.read()

    print(fichier_ouvert)
    nul = input("Pour quitter, appuyez sur entree...")
    system('cls')

def aide_morpion():
    """
    procedure qui affiche l'aide du jeu morpion
    """
    chemin_acces : str
    chemin_acces = "aide_morpion.txt"
    print("e:", exists(chemin_acces), chemin_acces)

    aide(chemin_acces)

def aide_allumettes():
    """
    procedure qui affiche l'aide du jeu des allumettes
    """
    chemin_acces : str
    chemin_acces = "aide_allumettes.txt"
##    print("e:", exists(chemin_acces), chemin_acces)
    aide(chemin_acces)

def aide_devinette():
    """
    procedure qui affiche l'aide du jeu de la devinette
    """
    chemin_acces : str
    chemin_acces = "aide_devinette.txt"

    aide(chemin_acces)

##
##print(exists("aide_allumettes.txt"), "aide_allumettes.txt")
##aide_allumettes()