# Créé par henzo, le 23/10/2024 avec Python 3.7 en UTF-8

def menu():
    choix : int
    while choix != 3: # tant que le choix n'est pas de quitter le menu n'est pas choisi
        print("Quel jeu voulez-vous choisir ?")
        print("1) Devinette")
        print("2) Allumettes")
        print("3) Morpion")
        print("4) Quitter")
        choix = int(input())

    if choix < 0 and choix > 4:
        print("Erreur, le choix n'est pas valide")

    if choix == 1:
        print("jeu 1")
        ...
    elif choix == 2:
        print("jeu 1")
        ...
    elif choix == 3:
        print("jeu 1")
        ...

def sous_menu(nom_jeu : str, fonc_jeu, fonc_aide):
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
        choix = int(input())

        while choix < 0 and choix > 3: # verification
            print("Erreur : le choix n'est pas valide.")
            print("1) Jouer")
            print("2) Aide")
            print("3) Quitter")
            choix = int(input())

        if choix == 1:
            fonc_jeu()
        elif choix == 2:
            fonc_aide()
