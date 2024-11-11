from math import *  # Importe toutes les fonctions de la bibliothèque math
import os  # Importe le module OS pour nettoyer l’écran

# Fonction pour calculer les points gagnés en fonction de la limite et du nombre de coups utilisés
def points(lim: int, nombreDeCoups: int) -> int:
    nb_point: int
    # Calcule les points basés sur le ratio entre coups utilisés et limite de coups
    nb_point = 1 + int((1 - (nombreDeCoups / lim)) * 100)
    return nb_point


# Fonction principale de la "Devinette" où un joueur doit deviner un nombre choisi par l'autre joueur
def Devinette(ScoreJ1: int, ScoreJ2: int):
    # Initialisation des variables
    nombre: int  # Nombre que le joueur doit deviner
    limit: int  # Limite maximale pour le nombre
    joueur: int  # Joueur qui choisit le nombre et la limite
    nb_a_faire_dev: int  # Nombre à deviner
    nb_coup: int = 0  # Compteur de coups pour deviner
    sortie1: bool = True  # Flag pour contrôler la boucle principale
    reponse: str

    # Choix du joueur qui va entrer le nombre à deviner et la limite
    joueur = int(input("Choisissez quel joueur va entrer un nombre et une limite (1/2) "))
    while joueur > 2 or joueur < 1:  # Validation du choix de joueur
        print("Erreur de saisie, veuillez réessayer")
        joueur = int(input("Choisissez quel joueur va entrer un nombre et une limite (1/2) "))

    # Paramétrage selon le joueur choisi
    if joueur == 1:
        limit = int(input("Joueur 1, veuillez choisir la limite maximum  "))  # Limite maximum pour le nombre à deviner
        nb_a_faire_dev = int(input("Joueur 1, veuillez choisir un nombre à faire deviner  "))
        os.system('cls')  # Nettoie l’écran (sous Windows)

        # Validation pour s'assurer que le nombre à deviner est dans les limites
        while nb_a_faire_dev > limit or nb_a_faire_dev < 1:
            nb_a_faire_dev = int(input("Erreur de saisie, veuillez rentrer un nouveau nombre à faire deviner  "))
            os.system('cls')

        # Boucle principale pour les tentatives de devinette
        while sortie1:
            print("Le nombre de coups max est:  ", 1 + int(log2(limit)))  # Affiche le nombre de coups maximum
            nombre = int(input(f"Joueur 2, veuillez choisir un nombre, la limite est {limit} et ton nombre d'essai actuel est {nb_coup}   "))
            nb_coup += 1  # Incrémente le compteur de coups

            # Demande si le nombre deviné est plus grand, plus petit, ou égal
            reponse = str(input(f"Est-ce que le nombre {nombre} est plus grand (+), plus petit (-), ou égal (=) au nombre choisi ?  "))
            if reponse == '+':
                if nombre > nb_a_faire_dev:
                    print("c'est moins")
                else:
                    print("Menteur")  # Indique une réponse incorrecte intentionnelle
            elif reponse == '-':
                if nombre < nb_a_faire_dev:
                    print("c'est plus")
                else:
                    print("Menteur")
            elif reponse == '=':
                if nb_a_faire_dev == nombre:  # Le joueur a deviné correctement
                    # Vérifie si le nombre de coups est dans la limite
                    if nb_coup > 1 + int(log2(limit)):
                        print("Dommage, vous avez dépassé le nombre limite de coups pour gagner des points, vous avez donc perdu")
                    else:
                        ScoreJ2 = points(limit, nb_coup)  # Calcule et attribue les points
                        sortie1 = False  # Termine la boucle principale
                else:
                    print("Menteur")
            elif nb_coup == 1 + int(log2(limit)):  # Le joueur dépasse le nombre limite de coups
                print("Vous avez perdu, vous ne gagnerez pas de point. Voulez-vous continuer pour trouver le nombre ?  (o/n)")
                reponse2 = str(input())
                if reponse2 == 'o':
                    print("Ok, comme vous voulez")
                elif reponse2 == 'n':
                    print("Le joueur 1 a gagné")
                    ScoreJ1 += 50
                    sortie1 = False

    elif joueur == 2:  # Cas similaire mais pour le joueur 2 qui choisit le nombre et la limite
        limit = int(input("Joueur 2, veuillez choisir la limite maximum  "))
        nb_a_faire_dev = int(input("Joueur 2, veuillez choisir un nombre à faire deviner  "))
        os.system('cls')
        while nb_a_faire_dev > limit or nb_a_faire_dev < 1:
            nb_a_faire_dev = int(input("Erreur de saisie, veuillez rentrer un nouveau nombre à faire deviner  "))
            os.system('cls')

        while sortie1:
            print("Le nombre de coups max est:  ", 1 + int(log2(limit)))
            nombre = int(input(f"Joueur 1, veuillez choisir un nombre, la limite est {limit} et ton nombre d'essai actuel est {nb_coup}   "))
            nb_coup += 1
            reponse = str(input(f"Est-ce que le nombre {nombre} est plus grand (+), plus petit (-), ou égal (=) au nombre choisi ?  "))

            if reponse == '+':
                if nombre > nb_a_faire_dev:
                    print("c'est moins")
                else:
                    print("Menteur")
            elif reponse == '-':
                if nombre < nb_a_faire_dev:
                    print("c'est plus")
                else:
                    print("Menteur")
            elif reponse == '=':
                if nb_a_faire_dev == nombre:
                    if nb_coup > 1 + int(log2(limit)):
                        print("Dommage, vous avez dépassé le nombre limite de coups pour gagner des points, vous avez donc perdu")
                        ScoreJ2 = ScoreJ1 + 50
                        sortie1 = False
                    else:
                        ScoreJ1 = points(limit, nb_coup)
                        sortie1 = False
                else:
                    print("Menteur")
            elif nb_coup == 1 + int(log2(limit)):
                print("Vous avez perdu, vous ne gagnerez pas de point. Voulez-vous continuer pour trouver le nombre ?  (o/n)")
                reponse2 = str(input())
                if reponse2 == 'o':
                    print("Ok, comme vous voulez")
                elif reponse2 == 'n':
                    print("Le joueur 2 a gagné")
                    ScoreJ2 = ScoreJ1 + 50
                    sortie1 = False

    # Affiche les scores finaux
    print(f"Le score du joueur 1 est {ScoreJ1} et le score du joueur 2 est {ScoreJ2}")
    return ScoreJ1, ScoreJ2  # Retourne les scores finaux
