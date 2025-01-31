# Créé par henzo, le 24/10/2024 avec Python 3.7 en UTF-8

from random import randint
from typing import List # typage
import os # systeme

# fonction interne

def menu()->bool:
    """
    fonction du sous menu du jeu du morpion
    options -> 1- rejouer ; 2- quitter

    sortie : un booleen qui correspond au choix de l'utilisateur
                -> vrai (True)  : veut rejouer
                -> faux (False) : veut quitter le jeu
    """
    choix : int
    res : bool

    choix = 0 # initialistion de la variable de choix
    os.system("cls" if os.name == "nt" else "clear")

    while choix < 1 or choix > 2: # tant que le choix
        print("Que voulez-vous faire ?")
        print("1) Re-jouer")
        print("2) Quitter")
        choix = int(input(">> "))
        os.system("cls" if os.name == "nt" else "clear")

        if choix < 1 or choix > 2: # si la saisie est mauvaise, afficher un message d'erreur
            print("Erreur de saisie...")

    if choix == 1: # choix = 1 -> l'utilisateur veut rejouer
        res = True
    else : # choix = 2 -> l'utilisateur veut quitter le jeu
        res = False
    return res

def affichage(plateau:List[List[str]]):
    """
    procedure qui affichage le plateau de jeu du morpion

    entree : une matrice qui represente le plateau de jeu du morpion
    """
    ligne : list
    colone : str
    i : int
    j : int

    print("   A B C ") # affichage des noms de colones

    for i in range(len(plateau)): # la varible 'i' represente les lignes
        print(i + 1, '|', end = '')
        for j in range(len(plateau[i])):  # la varible 'j' represente les colones
            if plateau[i][j] == '': # si il n'y a pas de symbole sur la place [i][j]
                print("_|", end = '')
            else: # si il y a un symbole sur la place [i][j]
                print(f"{plateau[i][j]}|", end = '') # affichage du symbole
        print() # saut de ligne

def verif_morpion(mat:List[List[str]])->bool:
    """
    fonction qui verifie si il y a un alligement sur le plateau de jeu du morpion et revoie un booleen vrai si c'est le cas

    entree : une matrice qui represent le plateau de jeu du morpion
    sortie : un booleen
                -> vrai (True)  : il y a un alignement de symboles
                -> faux (False) : il n'y a pas un alignement de symboles
    """
    i : int = 0
    alignement : bool = False

    while i < len(mat) and not alignement: # verifiaction ligne et colone
        if ( ( (mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2]) and mat[i][0] != '') or ( (mat[0][i] == mat[1][i] and mat[1][i] == mat[2][i]) and mat[0][i] != '') ):
            alignement = True
        i = i + 1

    # verication diagonal
    return alignement or ( (mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[0][0] != '') or (mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0] and mat[0][2] != '') )


def symbole_gagnant_morpion(mat:List[List[str]])->str:
    """
    fonction qui renvoie un caractere qui correspond au symbole qui alligne sur le plateau de jeu du morpion

    entree : une matrice qui represente le plateau de jeu du morpion
    sortie : un caractere qui represente le symbole qui est alligne ;
             si aucun symbole alligne, retourne un caractere vide -> ''
    """
    i : int = 0
    alignement : bool = False
    res : str = ''

    while i < len(mat) and not alignement: # verification des lignes et des colones
        if ( ( (mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2]) and mat[i][0] != '') or ( (mat[0][i] == mat[1][i] and mat[1][i] == mat[2][i]) and mat[0][i] != '') ):
            alignement = True
        i = i + 1

    i = i - 1

    if alignement : # si alignement est sur vrai (alignement trouve)
        if ( (mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2]) and mat[i][0] != '' ): # ligne
            res = mat[i][0]

        elif ( (mat[0][i] == mat[1][i] and mat[1][i] == mat[2][i]) and mat[0][i] != ''): # colone
            res = mat[0][i]

    if ( (mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[0][0] != '') or (mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0] and mat[0][2] != '') ): # diagonal
        res = mat[1][1]

    return res

def placement_plateau(plateau:List[List[str]], position:str, symbole:str)->bool:
    """
    fonction qui place un sybole sur le platrau de jeu au coordonne qu'on lui donne et renvoie un booleen en fonction de la reussite du placement

    entree : une matrice qui represente le plateau de jeu du morpion ;
             une chaine de caractere qui represente la position sous la forme colone+ligne (ex : A2, B1, C3) ;
             une chaine de caractere qui correspond au symbole a placer
    sortie : un booleen qui correspond a la reussite du placement
                -> vrai (True)  : placement reussi
                -> faux (False) : place deja prise
    """
    colone : int
    ligne : int
    res : bool

    position = position.upper() # on met la postion en majuscule pour eviter les erreurs

    # verification ...
    assert len(symbole) == 1 # ... de la longueur du symoble (longueur max = 1)
    assert len(plateau) == len(plateau[0]) # ... de la taille de la matrice, si elle correspond a la bonne taille d'un plateau
    assert len(position) == 2 and position[0] in ['A', 'B', 'C'] and position[1] in ['1', '2', '3'] # ... de la correspondance de la position

    if position[0] == 'A':
        colone = 0
    elif position[0] == 'B':
        colone = 1
    else:
        colone = 2
    ligne = int(position[1]) - 1

    if plateau[ligne][colone] == '': # si la position [ligne][colone] est vide
        plateau[ligne][colone] = symbole
        res = True
    else:
        res = False

    return res

def verif_placement(position:str)->bool:
    """
    fonction qui verifie si l'ecriture d'une position est bonne ou non en retournant un booleen

    entree : une chaine de caractere qui correspond a un position de la forme colone+ligne (ex: A1, B2, C3)
    sortie : un booleen qui correpond à la bonne syntaxe de la position
                -> vrai (True)  : la syntaxe est bonne
                -> faux (False) : la syntaxe est mauvaise
    """
    res : bool
    res = True

    if len(position) != 2: # verification de la taille
        res = False
    elif not (position[0] in ['A', 'B', 'C'] and position[1] in ['1', '2', '3']): # correspondance de la position
        res = False

    return res

def saisie_placement(plateau:List[List[str]])->str:
    """
    fonction pour la saisie sur le placement de jeu du mopion

    entree : une matrice representant le plateaud de jeu du morpion
    sortie : une chaine de caractere qui repesente la position du placement
    """
    position : str

    position = input("où voulez-vous vous placer ? (col, lig => lettre+chiffre)\n>>").upper()

    while not verif_placement(position): # on repose la question tant que le placement est mauvais
        os.system("cls" if os.name == "nt" else "clear")
        affichage(plateau)
        print("Erreur d'entrée : le placement doit etre de la forme nb+chiffre (ex: A1, B3, C2)")
        position = input("où voulez-vous vous placer ? (col, lig => lettre+chiffre)\n>> ").upper()

    return position

def verif_remplissage(plateau:List[List[str]])->bool:
    """
    fonction qui renvoie un booleen en fonction du remplissage du plateau :
        vrai -> le plateau est rempli
        faux -> la plateau n'est pas rempli

    entree : une matrice correspondant au plateau de jeu du morpion
    sortie : un booleen qui correpond au taux de replissage du plateau
                -> vrai (True)  : le plateau est rempli
                -> faux (False) : le plateau n'est pas encore rempli
    """
    res : bool
    i : int # ligne
    j : int # colone

    i = 0
    j = 0

    res = True
    while i < len(plateau) and res:
        j = 0
        while j < len(plateau) and res:
            if plateau[i][j] == '': # si une case n'est pas remplie
                res = False
            j = j + 1
        i +=1

    return res

# ########################################################### #

# fonction principal

def morpion(score_j1:int, score_j2:int, nom_j1:str, nom_j2)->tuple:
    """
    fonction principal du jeu du morpion

    entree: deux entiers correspondant successivement au score de depart du joueur 1 et du joueur 2
    sortie : un tuple de score
                -> indice 0 : score joueur 1
                -> indice 1 : score joueur 2
    """
    plateau : list
    joueur_gagnant : int
    joueur_jouant : int
    symbole_joueur : str
    placement : str
    null : str # varible ne servant à rien
    jouer : bool = True

    symbole_joueur = ['O', 'X']
    joueur_gagnant = -1

    while jouer: # tant que l'utilisateur veut faire une partie
        os.system("cls" if os.name == "nt" else "clear")
        plateau = [['','',''], 
                   ['','',''],
                   ['','','']] 

        if joueur_gagnant < 1 or joueur_gagnant > 2: # on choisi le joueur qui comment aléatoirement s'il n'y a pas de gagnant
            joueur_gagnant = randint(1,2)
        joueur_jouant = joueur_gagnant

        while not verif_morpion(plateau) and not verif_remplissage(plateau): # tant qu'il n'y a pas d'allignement et que le plateau n'est pas rempli
            os.system("cls" if os.name == "nt" else "clear")
            if joueur_jouant == 1: # on indique a l'utilisateur de jouer
                print(f"{nom_j1}, à vous de jouer !! (Vous etes {symbole_joueur[joueur_jouant - 1]})")
            else:
                print(f"{nom_j2}, à vous de jouer !! (Vous etes {symbole_joueur[joueur_jouant - 1]})")
            affichage(plateau)

            placement = saisie_placement(plateau)

            while not placement_plateau(plateau, placement, symbole_joueur[joueur_jouant - 1]): # si le placement est deja pris
                os.system("cls" if os.name == "nt" else "clear")
                affichage(plateau)
                print("Ah... je crois que la place est deja prise...")
                placement = saisie_placement(plateau)

            if joueur_jouant == 1: # on inverse les roles
                joueur_jouant = 2
            else:
                joueur_jouant = 1


        if verif_remplissage(plateau): # si le plateau est rempli on indique une egalite
            os.system("cls" if os.name == "nt" else "clear")
            affichage(plateau)
            print("Stoooopp !! Egalité !")
        else: # sinon, il y a un gagant
            os.system("cls" if os.name == "nt" else "clear")
            affichage(plateau)
            joueur_gagnant = symbole_joueur.index(symbole_gagnant_morpion(plateau)) + 1 # on regarde qui est le gagnant on fonction de son symboles

            if joueur_gagnant == 1: # on indique au joueur son nombre point gagne
                print(f"Bravo {nom_j1}, tu as gagné 25 pnts !!")
            else:
                print(f"Bravo {nom_j2}, tu as gagné 25 pnts !!")

            # incrementation du score du joueur gagnant
            if joueur_gagnant == 1:
                score_j1 = score_j1 + 25
            else:
                score_j2 = score_j2 + 25

        null = input("\n(taper sur entree pour continuer...)")
        os.system("cls" if os.name == "nt" else "clear")
        jouer = menu() # on demmande s'il veut re joueur
    os.system("cls" if os.name == "nt" else "clear")

    return score_j1, score_j2


# debug
##
##plateau =     [['o','','x'],
##               ['x','x','o'],
##               ['o','','']]
##
##affichage(plateau)

##plateau = [['X', 'O', 'X'], ['', 'O', ''], ['X', 'X', 'O']]
##print(verif_remplissage(plateau))

##morpion(0,0, "Jonate", "huge")


"""
la procedure menu n'a pas de cas de test
la procedure affichage peut etre teste en mettant des matice quelconque -> le seul point qui ne serait pas bon est le nommage des colones qui affichera tjrs A B C
la fontion verif_moprion ne fonction qu'avec une grille de morpion 3x3. on peut la tester avec
"""
