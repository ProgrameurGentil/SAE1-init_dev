# Créé par henzo, le 23/10/2024 avec Python 3.7 en UTF-8

def saisie_oui_non(msg_saisie:str, msg_erreur:str, oui:str='o', non:str='n')->bool:
    """
    fonction de saisie ou l'on peut repondre par oui ou par non en conformite des parametre "oui" et "non"

    entree : msg_saisie -> message affiche lors de la saisie de l'utilisateur
             msg_erreur -> message affiche lors d'une erreur de saisie ( si la valeur n'est pas dans les bornes )
             oui : vaut 'o' par defaut -> chaine de caractere qui correspond a la valeur a saisir pour accecpter
             non : vaut 'n' par defaut -> chaine de caractere qui correspond a la valeur a saisir pour refuser
    sortie : un booleen
                -> vrai (True)  : l'utilisateur a repondu oui
                -> faux (Fasle) : l'utilisateur a repondu non
    """
    choix : str
    msg_saisie = msg_saisie + f" ({oui}/{non})"
    oui = oui.lower()
    non = non.lower()

    print(msg_saisie)
    choix = input(">> ").lower()

    while choix != oui or choix != non:
        print(msg_erreur)

        print(msg_saisie)
        choix = input(">> ").lower()

    return choix == oui

