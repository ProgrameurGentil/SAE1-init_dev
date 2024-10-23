# Créé par henzo, le 23/10/2024 avec Python 3.7 en UTF-8
def saisie_entier_borne(msg_saisie:str, msg_erreur:str, borninf:int, bornsup:int)->int:
    """
    fonction de saisie de variable entiere entre la borne inferieur et la borne superieur
    un message de demande de saisie et un message d'erreur est demande
    un message d'erreur est affiche si le type est mauvais (type entier -> int)

    entree : msg_saisie -> message affiche lors de la saisie de l'utilisateur
             msg_erreur -> message affiche lors d'une erreur de saisie ( si la valeur n'est pas dans les bornes )
             borninf -> un entier qui represente la borne inferieur
             bornsup -> un entier qui represente la borne superieur. peut etre deffinit par la valeur MAXINT present dans le module (represente le plus grand chiffre pouvant etre contenu dans sur 4 bits)
    sortie : une valeur entiere compris entre une borne superieur et une borne inferieur
    """
    var : int
    var = int(input(msg_saisie))
    while (var < borninf) or (var > bornsup): # verifiaction entre bornes
        print(msg_erreur)
        var = saisie_entier_borne(msg_saisie, msg_erreur, borninf, bornsup)
    return var

MAXINT = 2147483647