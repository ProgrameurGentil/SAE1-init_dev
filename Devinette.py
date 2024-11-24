from math import *  # Importe toutes les fonctions de la bibliothèque math
import os  # Importe le module OS pour nettoyer l’écran
from typing import Tuple # Initilisation des variables

def points(lim: int, nombreDeCoups: int) -> int:
    """
    Fonction pour calculer les points gagnés en fonction de la limite et du nombre de coups utilisés

    entree : un entier pour une qui indique la limite de recherche et un deuxieme entier representant le nombre de coup
    sortie : un entier qui represente le nombre de point en fonction de la limite et du nombre de coup
    """
    nb_max_coups : int
    nb_point: int
    nb_max_coups = 1 + int(log2(lim))
    # Calcule des points
    if nombreDeCoups == 1:
        nb_point = 100
    elif 1 < nombreDeCoups <= int(nb_max_coups / 4):
        nb_point = 90
    elif int(nb_max_coups / 4) < nombreDeCoups <= int(nb_max_coups / 3): 
        nb_point = 75
    elif int(nb_max_coups / 3) < nombreDeCoups <= int(nb_max_coups / 2): 
        nb_point = 50
    elif int(nb_max_coups / 2) < nombreDeCoups <= int(nb_max_coups / 1): 
        nb_point = 25
    elif nombreDeCoups == 1 + int(log2(lim)):
        nb_point = 10
    return nb_point


def Devinette(ScoreJ1: int, ScoreJ2: int, Joueur1 : str, Joueur2 : str)->Tuple[int]:
    """
    Fonction principale de la "Devinette" où un joueur doit deviner un nombre choisi par l'autre joueur

    entree : deux entiers qui correspondent successivement aux scores de depart du joueur 1 et du joueur 2
    sortie : un tuple de deux entiers qui correspondent successivement aux scores du joueur 1 et du joueur 2
    """
    # Initialisation des variables
    nombre: int  # Nombre que le joueur doit deviner
    limit: int  # Limite maximale pour le nombre
    joueur: int  # Joueur qui choisit le nombre et la limite
    nb_a_faire_dev: int  # Nombre à deviner
    nb_coup: int = 0  # Compteur de coups pour deviner
    sortie1: bool = True  # Flag pour contrôler la boucle principale
    ScoreAjout : int #Valeur à ajouter quand le joueur gagne
    reponse: str # Variable pour que le joueur réponde par '=' '+' ou '-' 
    null : str # Variable pour quitter le jeu quand une partie est fini
    echec : bool # Variable pour savoir si le joueur a dépasser le nombre de coups maximum
    echec = False # Le nombre de coups max n'a pas été atteint
    #Choix du nom des joueurs
    # Choix du joueur qui va entrer le nombre à deviner et la limite
    joueur = int(input("Choisissez quel joueur va entrer un nombre et une limite (1/2) "))
    while joueur > 2 or joueur < 1:  # Validation du choix de joueur
        print("Erreur de saisie, veuillez réessayer")
        joueur = int(input("Choisissez quel joueur va entrer un nombre et une limite (1/2) "))

    # Paramétrage selon le joueur choisi
    if joueur == 1:
        limit = int(input(f"{Joueur1}, veuillez choisir la limite maximum  "))  # Limite maximum pour le nombre à deviner
        while limit < 1:
            print("Erreur de syntaxe, la limite est inférieur à 1")
            limit = int(input(f"{Joueur1}, veuillez choisir la limite maximum  "))
        nb_a_faire_dev = int(input(f"{Joueur1}, veuillez choisir un nombre à faire deviner  "))

        os.system('cls')  # Nettoie l’écran (sous Windows)

        # Validation pour s'assurer que le nombre à deviner est dans les limites
        while nb_a_faire_dev > limit or nb_a_faire_dev < 1:
            nb_a_faire_dev = int(input("Erreur de saisie, veuillez rentrer un nouveau nombre à faire deviner  "))
            os.system('cls')

        # Boucle principale pour les tentatives de devinette
        while sortie1:
            print("Le nombre de coups max est:  ", 1 + int(log2(limit)))  # Affiche le nombre de coups maximum
            nombre = int(input(f"{Joueur2}, veuillez choisir un nombre, la limite est {limit} et ton nombre d'essai actuel est {nb_coup}   "))
            while 0 > nombre > limit:
                os.system('cls')
                print(f"Erreur de saisie, le nombre {nombre} n'est pas inclu dans la limite : ]0 {limit}]")
                nombre = int(input(f"{Joueur2}, veuillez choisir un nombre, la limite est {limit} et ton nombre d'essai actuel est {nb_coup}   "))

            nb_coup += 1  # Incrémente le compteur de coups
            os.system('cls')
            # Demande si le nombre deviné est plus grand, plus petit, ou égal
            reponse = str(input(f"Est-ce que le nombre {nombre} est plus grand (+), plus petit (-), ou égal (=) au nombre choisi ?  "))


            if reponse == '+':
                if echec == False: # Si le nombre de coup max n'a pas encore été atteint
                    if nombre > nb_a_faire_dev:
                        print("c'est moins")
                    else:
                        print(f"Menteur, {Joueur1} perd 5 points")  # Indique une réponse incorrecte intentionnelle
                        ScoreJ1 = ScoreJ1 - 5
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        if nombre == nb_a_faire_dev:
                            print(f"{Joueur2} a gagné")
                            ScoreAjout = points(limit, nb_coup)
                            ScoreJ2 = ScoreJ2 + ScoreAjout
                            sortie1 = False
                else:
                    if nombre > nb_a_faire_dev:
                        print("c'est moins")
                    else:
                        print("Menteur")  # Indique une réponse incorrecte intentionnelle
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        if nombre == nb_a_faire_dev:
                            print(f"{Joueur2} a quand même perdu")
                            ScoreJ1 += 50
                            sortie1 = False





            elif reponse == '-':
                if echec == False:
                    if nombre < nb_a_faire_dev:
                        print("c'est plus")
                    else:
                        print(f"Menteur, {Joueur1} perd 5 points")
                        ScoreJ1 = ScoreJ1 - 5
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        elif nombre == nb_a_faire_dev:
                            print(f"{Joueur2} a gagné")
                            ScoreAjout = points(limit, nb_coup)
                            ScoreJ2 = ScoreJ2 + ScoreAjout
                            sortie1 = False
                else:
                    if nombre < nb_a_faire_dev:
                        print("c'est plus")
                    else:
                        print("Menteur")
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        elif nombre == nb_a_faire_dev:
                            print(f"{Joueur2} a quand même perdu")
                            ScoreJ1 += 50
                            sortie1 = False




            elif reponse == '=':
                if echec == False:
                    if nb_a_faire_dev == nombre:  # Le joueur a deviné correctement
                        # Vérifie si le nombre de coups est dans la limite
                        if nb_coup > 1 + int(log2(limit)):
                            print("Dommage, vous avez dépassé le nombre limite de coups pour gagner des points, vous avez donc perdu")
                            ScoreJ1 += 50
                            sortie1 = False
                        else:
                            ScoreAjout = points(limit, nb_coup)
                            ScoreJ2 = ScoreJ2 + ScoreAjout  # Calcule et attribue les points
                            sortie1 = False  # Termine la boucle principale
                    else:
                        print(f"Menteur, {Joueur1} perd 5 points")
                        ScoreJ1 = ScoreJ1 - 5
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        elif nombre > nb_a_faire_dev:
                            print("C'est moins")
                else:
                    if nb_a_faire_dev == nombre:  # Le joueur a deviné correctement
                        # Vérifie si le nombre de coups est dans la limite
                        if nb_coup > 1 + int(log2(limit)):
                            print("Dommage, vous avez dépassé le nombre limite de coups pour gagner des points, vous avez donc perdu")
                            ScoreJ1 += 50
                            sortie1 = False
                        else:
                            ScoreAjout = points(limit, nb_coup)
                            ScoreJ2 = ScoreJ2 + ScoreAjout  # Calcule et attribue les points
                            sortie1 = False  # Termine la boucle principale
                    else:
                        print("Menteur")
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        elif nombre > nb_a_faire_dev:
                            print("C'est moins")




            if nb_coup == 1 + int(log2(limit)):  # Le joueur dépasse le nombre limite de coups
                echec = True # Echec devient Vrai Car le nombre de coup max a été atteint
                print("Vous avez perdu, vous ne gagnerez pas de point. Voulez-vous continuer pour trouver le nombre ?  (o/n)")
                reponse2 = str(input())
                if reponse2 == 'o':
                    print("Ok, comme vous voulez")
                elif reponse2 == 'n':
                    print(f"{Joueur1} a gagné")
                    ScoreJ1 += 50
                    sortie1 = False



    elif joueur == 2:  # Cas similaire mais pour le joueur 2 qui choisit le nombre et la limite
        limit = int(input(f"{Joueur2}, veuillez choisir la limite maximum  "))
        while limit < 1:
            print("Erreur de syntaxe, la limite est inférieur à 1")
        nb_a_faire_dev = int(input(f"{Joueur2}, veuillez choisir un nombre à faire deviner  "))
        os.system('cls')

        while nb_a_faire_dev > limit or nb_a_faire_dev < 1:
            nb_a_faire_dev = int(input("Erreur de saisie, veuillez rentrer un nouveau nombre à faire deviner  "))
            os.system('cls')



        while sortie1:

            print("Le nombre de coups max est:  ", 1 + int(log2(limit)))
            nombre = int(input(f"{Joueur1}, veuillez choisir un nombre, la limite est {limit} et ton nombre d'essai actuel est {nb_coup}   "))
            while 0 > nombre > limit:
                os.system('cls')
                print(f"Erreur de saisie, le nombre {nombre} n'est pas inclu dans la limite : ]0 {limit}]")
                nombre = int(input(f"{Joueur1}, veuillez choisir un nombre, la limite est {limit} et ton nombre d'essai actuel est {nb_coup}   "))
            nb_coup += 1
            os.system('cls')
            reponse = str(input(f"Est-ce que le nombre {nombre} est plus grand (+), plus petit (-), ou égal (=) au nombre choisi ?  "))

            if reponse == '+':
                if echec == False:
                    if nombre > nb_a_faire_dev:
                        print("c'est moins")
                    else:
                        print(f"Menteur, {Joueur2} perd 5 points")
                        ScoreJ2 = ScoreJ2 - 5
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        elif nombre == nb_a_faire_dev:
                            print(f"{Joueur2} a gagné")
                            ScoreAjout = points(limit, nb_coup)
                            ScoreJ1 = ScoreJ1 + ScoreAjout
                            sortie1 = False
                else:
                    if nombre > nb_a_faire_dev:
                        print("c'est moins")
                    else:
                        print("Menteur")
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        elif nombre == nb_a_faire_dev:
                            print(f"{Joueur2} a quand même perdu")
                            ScoreJ2 += 50
                            sortie1 = False




            elif reponse == '-':
                if echec == False:
                    if nombre < nb_a_faire_dev:
                        print("c'est plus")
                    else:
                        print(f"Menteur, {Joueur2} perd 5 points")
                        ScoreJ2 = ScoreJ2 - 5
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        elif nombre == nb_a_faire_dev:
                            print(f"{Joueur1} a gagné")
                            ScoreAjout = points(limit, nb_coup)
                            ScoreJ1 = ScoreJ1 + ScoreAjout
                            sortie1 = False
                else:
                    if nombre < nb_a_faire_dev:
                        print("c'est plus")
                    else:
                        print("Menteur")
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        elif nombre == nb_a_faire_dev:
                            print(f"{Joueur1} a quand même perdu")
                            ScoreJ2 += 50
                            sortie1 = False


            elif reponse == '=':
                if echec == False:
                    if nb_a_faire_dev == nombre:
                        if nb_coup > 1 + int(log2(limit)):
                            print("Dommage, vous avez dépassé le nombre limite de coups pour gagner des points, vous avez donc perdu")
                            ScoreJ1 += 50
                            sortie1 = False
                        else:
                            ScoreAjout = points(limit, nb_coup)
                            ScoreJ1 = ScoreJ1 + ScoreAjout
                            sortie1 = False

                    else:
                        print(f"Menteur, {Joueur2} perd 5 points")
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        elif nombre > nb_a_faire_dev:
                            print("C'est moins")
                        ScoreJ2 = ScoreJ2 - 5
                else:
                    if nb_a_faire_dev == nombre:
                        if nb_coup > 1 + int(log2(limit)):
                            print("Dommage, vous avez dépassé le nombre limite de coups pour gagner des points, vous avez donc perdu")
                            ScoreJ1 += 50
                            sortie1 = False
                        else:
                            ScoreAjout = points(limit, nb_coup)
                            ScoreJ1 = ScoreJ1 + ScoreAjout
                            sortie1 = False

                    else:
                        print("Menteur")
                        if nombre < nb_a_faire_dev:
                            print("C'est plus")
                        elif nombre > nb_a_faire_dev:
                            print("C'est moins")



            if nb_coup >= 1 + int(log2(limit)):
                echec = True
                print("Vous avez perdu, vous ne gagnerez pas de point. Voulez-vous continuer pour trouver le nombre ?  (o/n)")
                reponse2 = str(input())
                if reponse2 == 'o':
                    print("Ok, comme vous voulez")

                elif reponse2 == 'n':
                    print(f"{Joueur2} a gagné")
                    ScoreJ2 = ScoreJ2 + 50
                    sortie1 = False

    # Affiche les scores finaux
    print(f"Le score de {Joueur1} est {ScoreJ1} et le score de {Joueur2} est {ScoreJ2}")
    null = input("Pour quitter, appuyez sur entree...")
    return ScoreJ1, ScoreJ2 # Retourne les scores finaux

#debug
#Devinette(0,0)
