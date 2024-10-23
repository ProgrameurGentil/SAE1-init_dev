def jeu1 ():
    nombre : int
    limit : int
    Joueur : int
    nb : int
    nb_coup : int
    reponse : str
    nb_coup = 0


    
    joueur = int(input("Choissisez quel joueur va entrer un nombre et une limite (1/2)"))
    while (joueur > 2) or (joueur < 1):
        print("Erreur de saisie, veuillez réessayer")
        joueur = int(input("Choissisez quel joueur va entrer un nombre et une limite (1/2)"))



    if joueur == 1:
        limit = int(input("Joueur 1, veuillez choisir la limite maximum"))
        nb = int(input("Joueur 1, veuillez choisir un nombre à faire deviner"))
        while (nb > limit) or (nb < 1):
            nb = int(input("Erreur de saisie, veuillez rentrer un nouveau nombre à faire deviner"))
        nombre = int(input("Joueur 2, veuillez choisir un nombre"))
        nb_coup = nb_coup + 1
        reponse = str(input("Esque le nombre", nombre, "est plus grand (+), plus petit (-), ou est égale (=) au nombre choisi ?"))
        if reponse == '+':
        if reponse == '-':
        if reponse == '=':


    else:
