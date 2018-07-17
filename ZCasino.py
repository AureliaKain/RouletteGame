# -*-coding:utf-8 -*
#Ce fichier contient le code du projet ZCasino, un jeu de roulette simplifié
from random import randrange
from math import ceil

argent = 1000
print('vous vous installez a table avec', argent, '$')
continuer_partie = True

while (argent > 0) and (continuer_partie == True):
    nb_mise = -1
    while nb_mise < 0 or nb_mise > 49:
        nb_mise = input("saisissez le nombre que vous misez : ")
        #raise exceptions
        try:
            nb_mise = int(nb_mise)
            assert (nb_mise > 0) and (nb_mise <= 50)
        except AssertionError:
            print("le nombre mise doit etre compris entre 0 et 50")
        except ValueError:
            print("vous n'avez pas saisi un nombre")


    somme_mise = -1
    while somme_mise < 0 or somme_mise > argent:
        somme_mise = input("saissiez la somme que vous misez : ")
        #raise exceptions
        try:
            somme_mise = int(somme_mise)
            assert (somme_mise > 0) and (somme_mise <= argent)
        except AssertionError:
            if somme_mise < 0:
                print("le nombre mise doit etre superieur a 0")
            elif somme_mise > argent:
                print("vous ne pouvez miser plus d'argent que ce que vous avez!")
        except ValueError:
            print("vous n'avez pas saisi un nombre ou un entier")

    nb_gagnant = randrange(0, 49)
    print("le nombre gagnant est:", nb_gagnant)

    if nb_mise == nb_gagnant:
        argent += somme_mise * 3
        gain = somme_mise * 3
    elif ((nb_gagnant % 2 == 0) and (nb_mise % 2 == 0)) or ((nb_gagnant % 2 == 1) and (nb_mise % 2 == 1)):
        argent += ceil(somme_mise * 0.5)
        gain = somme_mise * 0.5
    else:
        argent -= somme_mise
        gain = - somme_mise

    if gain > 0:
        print('vous avez gagne:', gain, '$')
        print('il vous reste:', argent, '$')
    else:
        print('vous avez perdu:', gain, '$')
        print('il vous reste:', argent, '$')

    if argent > 0:
        continuer_partie = input('voulez-vous continuer la partie (True or False)?')
if argent == 0:
    print('il ne vous reste plus d\'argent, la partie est finie!')
if continuer_partie == False:
    print('vous avez voulu arreter la partie, felicitations, vous partez avec', argent, '$')