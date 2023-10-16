#créé par Mikolai Szychowski
#créé le 19 septembre 2023
#TP2
import random     #fonction définit
def jeu():
    bornes=str(input('Voulez vous choisir les limites du nombres mystere? (y/n)'))   #limites
    borne_minimale=0    #bornes par défaut de 0 a 1000
    borne_maximale=1000
    if bornes == ('y'):
        borne_minimale=int(input('Quelle sera le minimum?'))
        borne_maximale=int(input('Quelle sera le maximum?'))
    chiffre_aléatoire = random.randint(borne_minimale,borne_maximale)    #definir chiffre_aleatoire
    print('Lordinateur a choisi un nombre, essayez de le deviner.')
    nb_essai=1

    while True:
        essai=int(input('Entrez votre premier essai:'))
        if essai>chiffre_aléatoire:          #si trop grand
            print('Le nombre est plus petit')
            nb_essai=nb_essai+1
        elif essai < chiffre_aléatoire:       #si trop petit
            print('le nombre est plus grand')
            nb_essai=nb_essai+1
        elif essai == chiffre_aléatoire:       #si le nombre est trouvé
            print('Bravo! Vous avez trouvez en',nb_essai,'essais,Bravo!')
            quit=str(input('Voulez vous réssayer? (y/n)'))    #pour ressayer
            if quit==('y'):
                jeu()
                break
            elif quit==('n'):
                print('A la prochaine!')
                False
                break

        else:             # en cas d'erreur, ca continue la boucle
            print('Erreur')

jeu()