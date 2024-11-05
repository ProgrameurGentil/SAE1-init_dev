def nb_al(allumettes : int) -> str:
    resultat : str
    resultat = '|' * allumettes
    return resultat


def allumettes(ScoreJ1 : int, ScoreJ2 : int):
    nb_allumettes : int
    Joueur : int
    decr_nb_al : int
    Sortie : bool
    nb_allumettes = 20

    Joueur = int(input("Choissisez quel joueur Commence (1/2)  "))
    while Joueur < 1 or Joueur > 2:
        print("Erreur de saisie, veuillez réessayer")
        Joueur = int(input("Choissisez quel joueur Commence (1/2)  "))
    while nb_allumettes != 0:
        if Joueur == 1:
            Sortie = True
            print(nb_al(nb_allumettes))
            print(f"Il reste {nb_allumettes} allumettes")
            decr_nb_al = int(input("Joueur 1, combien d'allumettes voulez-vous retirer ?  "))
            while decr_nb_al < 1 or decr_nb_al > 3:
                print("Erreur de saisie, veuillez réessayer")
                print(nb_al(nb_allumettes))
                print(f"Il reste {nb_allumettes} allumettes")
                decr_nb_al = int(input("Joueur 1, combien d'allumettes voulez-vous retirer ?  "))
            while Sortie == True:
                
                if decr_nb_al == 1:
                    nb_allumettes = nb_allumettes - 1
                    if nb_allumettes == 0:
                        print("Le joueur 2 a gagné")
                        ScoreJ2 = ScoreJ2 + 50
                    Sortie = False
                elif decr_nb_al == 2:
                    if (nb_allumettes -2) < 0:
                        print("Impossible")
                        decr_nb_al = int(input("Joueur 1, combien d'allumettes voulez-vous retirer ?  "))
                    else:
                        nb_allumettes = nb_allumettes - 2
                        if nb_allumettes == 0:
                            print("Le joueur 2 a gagné")
                            ScoreJ2 = ScoreJ2 + 50
                        Sortie = False
                elif decr_nb_al == 3:
                    if (nb_allumettes -3) < 0:
                        print("Impossible")
                        decr_nb_al = int(input("Joueur 1, combien d'allumettes voulez-vous retirer ?  "))
                    else:
                        nb_allumettes = nb_allumettes - 3
                        if nb_allumettes == 0:
                            print("Le joueur 2 a gagné")
                            ScoreJ2 = ScoreJ2 + 50
                        Sortie = False
            Joueur = 2
        elif Joueur == 2:
            Sortie = True
            print(nb_al(nb_allumettes))
            print(f"Il reste {nb_allumettes} allumettes")
            decr_nb_al = int(input("Joueur 2, combien d'allumettes voulez-vous retirer ?  "))
            while decr_nb_al < 1 or decr_nb_al > 3:
                print("Erreur de saisie, veuillez réessayer")
                print(nb_al(nb_allumettes))
                print(f"Il reste {nb_allumettes} allumettes")
                decr_nb_al = int(input("Joueur 2, combien d'allumettes voulez-vous retirer ?  "))
            while Sortie == True:
                
                if decr_nb_al == 1:
                    nb_allumettes = nb_allumettes - 1
                    if nb_allumettes == 0:
                        print("Le joueur 1 a gagné")
                        ScoreJ1 = ScoreJ1 + 50
                    Sortie = False
                elif decr_nb_al == 2:
                    if (nb_allumettes -2) < 0:
                        print("Impossible")
                        decr_nb_al = int(input("Joueur 2, combien d'allumettes voulez-vous retirer ?  "))
                    else:
                        nb_allumettes = nb_allumettes - 2
                        if nb_allumettes == 0:
                            print("Le joueur 1 a gagné")
                            ScoreJ1 = ScoreJ1 + 50
                        Sortie = False
                elif decr_nb_al == 3:
                    if (nb_allumettes -3) < 0:
                        print("Impossible")
                        decr_nb_al = int(input("Joueur 2, combien d'allumettes voulez-vous retirer ?  "))
                    else:
                        nb_allumettes = nb_allumettes - 3
                        if nb_allumettes == 0:
                            print("Le joueur 1 a gagné")
                            ScoreJ1 = ScoreJ1 + 50
                        Sortie = False
            Joueur = 1
    return ScoreJ1, ScoreJ2