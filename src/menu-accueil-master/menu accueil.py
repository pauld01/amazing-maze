import pygame, sys
from pygame.locals import *

pygame.init()

"""constante"""
nombre_sprite_cote = 15
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite

continuer = 1
continuer_jeu = 1
continuer_accueil = 1

titre_fenetre = "labyrinthe"

"""images du jeu"""
image_icone = "images/DVD.png"              #icone
image_accueil = "images/accueil.png"        #accueil
image_fond = "images/DVD.png"               #fond du jeu
image_mur = "images/mur.png"                #sprite du mur
image_depart = "images/depart.png"          #image case départ
image_arrivee = "images/arrivee.png"        #image arrivée

"""musique"""
musique = "son.wav"

"""debut, lancement de la fenêtre"""

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

icone = pygame.image.load(image_icone)          #chargement image pour l'icon du jeu
pygame.display.set_icon(icone)

pygame.display.set_caption(titre_fenetre)       #titre de la fenêtre

accueil = pygame.image.load(image_accueil)      #affichage image d'accueil
fenetre.blit(accueil, (0,0))

son = pygame.mixer.Sound(musique)               #chargement de la musique
son.play()                                      #lecture de la musique

pygame.display.flip()                           #Rafraichissement pour afficher les images


while continuer:                                #boucle pour charger et affichée la page d'accueil

    for event in pygame.event.get():            # On parcourt la liste de tous les événements reçus
        if event.type == QUIT:                  # Si un de ces événements est de type QUIT
            continuer = 0                       # On arrête la boucle
        elif event.type == KEYDOWN:             #si on appuie sur une touche
            if event.key == K_ESCAPE:           #si cette touche est echap
                pygame.quit()                   #la fenêtre se ferme
                continuer = 0
        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] >= 134 and event.pos[0] <= 320 and event.pos[1] >= 427 and event.pos[1] <= 445:
            pygame.quit()
            continuer = 0

#ici il faudra mettre le code du jeu
    #while continuer_jeu:
        #if event.type == KEYDOWN:
            #if event.key == K_F1:
                #image2 = pygame.image.load(image_fond)
                #fenetre.blit(image2, (0,0))


#pygame.display.flip()                       #Rafraichissement



pygame.quit()                                   #fermeture du programe