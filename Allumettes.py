import os
from typing import Tuple # Initialisation des variables

def nb_al(allumettes: int) -> str:
    """
    Fonction qui génère une chaîne de caractères représentant les allumettes restantes
    entree : un entier correspondant au nb d'allumettes
    sortie : une chaine de caracteres
    """
    resultat: str
    resultat = '|' * allumettes  # Crée une chaîne avec autant de "|" que d'allumettes restantes
    return resultat

def allumettes(ScoreJ1:int, ScoreJ2:int, Joueur1 : str, Joueur2 : str)->Tuple[int]:
    """
    Fonction principale du jeu
    entree : 2 entiers qui correspond aux scores des joueurs
    sortie : un tuple avec en premiere position le nouveau score du joueur 1 et en deuxieme position le nouveau score du joueur 2
    """
    nb_allumettes: int  # Nombre d'allumettes restantes dans le jeu
    Joueur: int  # Indique le joueur en cours (1 ou 2)
    decr_nb_al: int  # Nombre d'allumettes à retirer
    null : str # Variable pour quitter le jeu quand une partie est fini
    Sortie: bool  # Variable pour gérer la fin du tour

    nb_allumettes = 20  # Le jeu commence avec 20 allumettes

    # Choisir quel joueur commence (1 ou 2)
    print("Qui joue en 1er ?")
    print(f"1- {Joueur1}")
    print(f"2- {Joueur2}")
    Joueur = int(input(">>"))
    while Joueur < 1 or Joueur > 2:  # Validation du choix
        os.system('clear')  # Nettoie l’écran (sous Windows)
        print("Erreur de saisie, veuillez réessayer")
        print("Qui joue en 1er ?")
        print(f"1- {Joueur1}")
        print(f"2- {Joueur2}")
        Joueur = int(input(">>"))

    # Boucle principale du jeu, qui continue jusqu'à ce qu'il n'y ait plus d'allumettes
    while nb_allumettes != 0:
        os.system("clear")
        if Joueur == 1:
            Sortie = True  # Variable pour gérer la fin du tour
            print(nb_al(nb_allumettes))  # Affiche les allumettes restantes
            print(f"Il reste {nb_allumettes} allumettes")
            decr_nb_al = int(input(f"{Joueur1}, combien d'allumettes voulez-vous retirer ? (1-3)  "))

            # Validation de l'entrée pour s'assurer que le joueur retire 1 à 3 allumettes
            while decr_nb_al < 1 or decr_nb_al > 3:
                os.system("clear") # # # # # # # # """""""""""""""""""""""""
                print("Erreur de saisie, veuillez réessayer")
                print(nb_al(nb_allumettes))
                print(f"Il reste {nb_allumettes} allumettes")
                decr_nb_al = int(input(f"{Joueur1}, combien d'allumettes voulez-vous retirer ? (1-3)  "))

            # Gestion du retrait des allumettes pour le joueur 1
            while Sortie:
                if decr_nb_al == 1:
                    nb_allumettes -= 1  # Retire 1 allumette
                    if nb_allumettes == 0:  # Si plus d'allumettes, joueur 2 gagne
                        print(f"{Joueur2} a gagné")
                        ScoreJ2 += 50
                    Sortie = False  # Fin du tour
                elif decr_nb_al == 2:
                    if (nb_allumettes - 2) < 0:  # Vérifie qu'il reste assez d'allumettes
                        print("Impossible")
                        decr_nb_al = int(input(f"{Joueur1}, combien d'allumettes voulez-vous retirer ? (1-3)  "))
                        print(nb_al(nb_allumettes))
                    else:
                        nb_allumettes -= 2  # Retire 2 allumettes
                        if nb_allumettes == 0:
                            print(f"{Joueur2} a gagné")
                            ScoreJ2 += 50
                        Sortie = False
                elif decr_nb_al == 3:
                    if (nb_allumettes - 3) < 0:  # Vérifie qu'il reste assez d'allumettes
                        print("Impossible")
                        decr_nb_al = int(input(f"{Joueur1}, combien d'allumettes voulez-vous retirer ? (1-3)  "))
                        print(nb_al(nb_allumettes))
                    else:
                        nb_allumettes -= 3  # Retire 3 allumettes
                        if nb_allumettes == 0:
                            print(f"{Joueur2} a gagné")
                            ScoreJ2 += 50
                        Sortie = False
            Joueur = 2  # Passe au joueur 2

        elif Joueur == 2:
            Sortie = True
            print(nb_al(nb_allumettes))  # Affiche les allumettes restantes
            print(f"Il reste {nb_allumettes} allumettes")
            decr_nb_al = int(input(f"{Joueur2}, combien d'allumettes voulez-vous retirer ? (1-3)  "))

            # Validation de l'entrée pour s'assurer que le joueur retire 1 à 3 allumettes
            while decr_nb_al < 1 or decr_nb_al > 3:
                os.system("clear") # # # # # # # # """""""""""""""""""""""""
                print("Erreur de saisie, veuillez réessayer")
                print(nb_al(nb_allumettes))
                print(f"Il reste {nb_allumettes} allumettes")
                decr_nb_al = int(input(f"{Joueur2}, combien d'allumettes voulez-vous retirer ? (1-3)  "))

            # Gestion du retrait des allumettes pour le joueur 2
            while Sortie:
                if decr_nb_al == 1:
                    nb_allumettes -= 1  # Retire 1 allumette
                    if nb_allumettes == 0:  # Si plus d'allumettes, joueur 1 gagne
                        print(f"{Joueur1} a gagné")
                        ScoreJ1 += 50
                    Sortie = False
                elif decr_nb_al == 2:
                    if (nb_allumettes - 2) < 0:  # Vérifie qu'il reste assez d'allumettes
                        print("Impossible")
                        decr_nb_al = int(input(f"{Joueur2}, combien d'allumettes voulez-vous retirer ? (1-3)  "))
                        print(nb_al(nb_allumettes))
                    else:
                        nb_allumettes -= 2  # Retire 2 allumettes
                        if nb_allumettes == 0:
                            print(f"{Joueur1} a gagné")
                            ScoreJ1 += 50
                        Sortie = False
                elif decr_nb_al == 3:
                    if (nb_allumettes - 3) < 0: # Vérifie qu'il reste assez d'allumettes
                        print("Impossible")
                        decr_nb_al = int(input(f"{Joueur2}, combien d'allumettes voulez-vous retirer ? (1-3)  "))
                        print(nb_al(nb_allumettes))
                    else:
                        nb_allumettes -= 3  # Retire 3 allumettes
                        if nb_allumettes == 0:
                            print(f"{Joueur1} a gagné")
                            ScoreJ1 += 50
                        Sortie = False
            Joueur = 1  # Passe au joueur 1
    null = input("Pour quitter, appuyez sur entree...")


    return ScoreJ1, ScoreJ2  # Retourne les scores finaux des deux joueurs
