from math import *
import os 
def points(lim : int, nombreDeCoups : int) -> int:
    nb_point : int
    nb_point = 1 + int((1-(nombreDeCoups / lim)) * 100)
    return nb_point



def Devinette(ScoreJ1 : int, ScoreJ2 : int)->tuple:
    nombre : int
    limit : int
    Joueur : int
    nb_a_faire_dev : int
    nb_coup : int
    reponse : str
    ScoreJ1 : int
    ScoreJ2 : int
    nb_coup = 0
    sortie1 : bool
    sortie1 = True
    
    joueur = int(input("Choissisez quel joueur va entrer un nombre et une limite (1/2) "))
    while (joueur > 2) or (joueur < 1):
        print("Erreur de saisie, veuillez réessayer")
        joueur = int(input("Choissisez quel joueur va entrer un nombre et une limite (1/2) "))

    if joueur == 1:
        limit = int(input("Joueur 1, veuillez choisir la limite maximum  "))
        nb_a_faire_dev = int(input("Joueur 1, veuillez choisir un nombre à faire deviner  "))
        os.system('cls')
        while (nb_a_faire_dev > limit) or (nb_a_faire_dev < 1):
            nb_a_faire_dev = int(input("Erreur de saisie, veuillez rentrer un nouveau nombre à faire deviner  "))
            os.system('cls')
        while sortie1 :
            print("Le nombre de coups max est:  ", 1 + int(log2(limit)))
            nombre = int(input(f"Joueur 2, veuillez choisir un nombre, la limite est {limit} et ton nombre d'essai actuel est {nb_coup}   "))
            nb_coup = nb_coup + 1
            reponse = str(input(f"Esque le nombre {nombre} est plus grand (+), plus petit (-), ou est égale (=) au nombre choisi ?  "))
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
                        print("Dommage, vous avez dépasser le nombre limite de coups pour gagner des points, vous avez donc perdu")                                       
                    else:
                        ScoreJ2 = points(limit, nb_coup)
                        sortie1 = False
                else:
                    print("Menteur")
            elif nb_coup == 1 + int(log2(limit)):
                print("Vous avez perdu, vous ne gagnerais pas de point, mais voulez vous continuer pour trouver le nombre ?  (o/n)")
                reponse2 = str(input())
                if reponse2 == 'o':
                    print("ok, comme vous voulez")
                elif reponse2 == 'n':
                    print("Le joueur 1 a gagné")
                    ScoreJ1 = ScoreJ1 + 50
                    sortie1 = False
    elif joueur == 2:
        limit = int(input("Joueur 2, veuillez choisir la limite maximum  "))
        nb_a_faire_dev = int(input("Joueur 2, veuillez choisir un nombre à faire deviner  "))
        os.system('cls')
        while (nb_a_faire_dev > limit) or (nb_a_faire_dev < 1):
            nb_a_faire_dev = int(input("Erreur de saisie, veuillez rentrer un nouveau nombre à faire deviner  "))
            os.system('cls')
        while sortie1 :
            print("Le nombre de coups max est:  ", 1 + int(log2(limit)))
            nombre = int(input(f"Joueur 1, veuillez choisir un nombre, la limite est {limit} et ton nombre d'essai actuel est {nb_coup}   "))
            nb_coup = nb_coup + 1
            reponse = str(input(f"Esque le nombre {nombre} est plus grand (+), plus petit (-), ou est égale (=) au nombre choisi ?  "))
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
                        print("Dommage, vous avez dépasser le nombre limite de coups pour gagner des points, vous avez donc perdu") 
                        ScoreJ2 = ScoreJ1 + 50
                        sortie2 = False

                    else:
                        ScoreJ1 = points(limit, nb_coup)
                        sortie1 = False
                else:
                    print("Menteur")
            elif nb_coup == 1 + int(log2(limit)):
                print("Vous avez perdu, vous ne gagnerais pas de point, mais voulez vous continuer pour trouver le nombre ?  (o/n)")
                reponse2 = str(input())
                if reponse2 == 'o':
                    print("ok, comme vous voulez")
                elif reponse2 == 'n':
                    print("Le joueur 2 a gagné")
                    ScoreJ2 = ScoreJ1 + 50
                    sortie2 = False
                
    print(f"Le score du joueur 1 est {ScoreJ1} et le score du joueur 2 est {ScoreJ2}")
    return ScoreJ1, ScoreJ2
