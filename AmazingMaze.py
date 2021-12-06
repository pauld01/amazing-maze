import pygame, sys
from pygame.locals import *
from tkinter import*
from timeit import default_timer
from array import array

pygame.init()

"""Constantes"""
nombre_sprite_cote = 15
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite
FOG_distance = 2                                    # Distance du brouillard

continuer = 1           # Boucle du menu
continuer_jeu = 0       #   Boucle du jeu
niveau = 0              # Choix du niveau dans le menu
last_niveau = 0         # Dernier niveau pour affichage
status_level =""        # Derniere partie gagnée ou perdue
score = 0
debut = 0.0             # Temps du début d'un niveau
text_clock = "00:00:00"

titre_fenetre = "Amazing Maze"

structure = [[0 for j in range(15)] for i in range(15)]

"""Images du jeu"""
image_icone = "data/images/sprites/caisse.png"          #icone

image_accueil = "data/images/layout/accueil.png"        #accueil
image_fond = "data/images/layout/fond.jpg"              #fond du jeu

image_mur = "data/images/sprites/caisse.png"                #sprite du Mur
image_sol = "data/images/sprites/sol.png"                #sprite du Sol
image_depart = "data/images/sprites/depart.png"          #sprite case Départ
image_arrivee = "data/images/sprites/arrivee.png"        #sprite Arrivée
image_ennemi = "data/images/sprites/flammes.png"         #sprite Ennemi

"""musique"""
musique = "data/musics/Digital_Memories.wav"

"""Sound FX"""
son1 = "data/sounds/DK_SFX_1.wav"
son2 = "data/sounds/DK_SFX_2.wav"
son3 = "data/sounds/DK_SFX_3.wav"
son4 = "data/sounds/DK_SFX_4.wav"
son5 = "data/sounds/DK_SFX_5.wav"
son6 = "data/sounds/DK_SFX_6.wav"
son7 = "data/sounds/DK_SFX_7.wav"
son8 = "data/sounds/DK_SFX_8.wav"
son9 = "data/sounds/DK_SFX_9.wav"

"""debut, lancement de la fenêtre"""
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre + 2*taille_sprite)) # taille du jeu + deux lignes score et message
icone = pygame.image.load(image_icone)          #chargement image pour l'icone du jeu
pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)       #titre de la fenêtre
accueil = pygame.image.load(image_accueil)      #affichage image d'accueil
fenetre.blit(accueil, (0,0))
fond = pygame.image.load(image_fond)
sol = pygame.image.load(image_sol)
mur = pygame.image.load(image_mur)
depart = pygame.image.load(image_depart)
arrivee = pygame.image.load(image_arrivee)
ennemi = pygame.image.load(image_ennemi)


""" Sprite du debut """
pas = pygame.image.load("data/images/sprites/dk_bas.png").convert_alpha()
pas_rect = pas.get_rect()

"""debut, lancement du son"""
son = pygame.mixer.Sound(musique)
son.play(loops=-1, maxtime=0, fade_ms=0)        #lecture de la musique en boucle

""" Parametres """
pygame.time.Clock().tick(60)                    #Mettre le temps en route

def generer(fichier):
    with open(fichier, "r") as fichier:
        i = 0
        for ligne in fichier.readlines():
            j = 0
            for sprite in ligne:
                if sprite != '\n' :
                    structure[i][j] = sprite
                j += 1
            i += 1


def afficher(x,y,r):
    for i in range(nombre_sprite_cote) :
        for j in range(nombre_sprite_cote) :
            if (i-y<r and y-i<r) and (j-x<r and x-j<r) : # afficher le fog en fonction du déplacement
                if structure[j][i] == 'm':
                    fenetre.blit(mur, (i*taille_sprite, j*taille_sprite))   # Affiche un mur
                elif structure[j][i] == 'D':
                    fenetre.blit(depart, (i*taille_sprite, j*taille_sprite))  # Affiche le depart
                elif structure[j][i] == 'A':
                    fenetre.blit(arrivee, (i*taille_sprite, j*taille_sprite))   # Affiche l'arrivee
                elif structure[j][i] == 'E':
                    fenetre.blit(ennemi, (i*taille_sprite, j*taille_sprite))    # Affiche les ennemy
            else:
                fenetre.blit(sol, (i*taille_sprite, j*taille_sprite)) # Cache les sprites


def carreaux(x, y) :
    x = x/taille_sprite
    y = y/taille_sprite
    return structure[int(y)][int(x)] # m _ E A D

def init_sprite() :
    pas_rect.top=taille_sprite
    pas_rect.left=0

def message_display(TextMsg) :
    font = pygame.font.SysFont("Times New Roman", 22) # Choix de la police
    text = font.render(TextMsg,1,(255,255,255))       # Render la font en blanc
    fenetre.blit(text, (cote_fenetre/4, cote_fenetre ))
    pygame.display.update()

def chronometre():
    now = default_timer() - debut
    minutes,secondes = divmod (now, 60)
    heures,minutes = divmod(minutes,60)
    str_time = "%02d:%02d:%02d"%(heures,minutes,secondes)
    return str_time

while continuer:                                #boucle pour charger et affichée la page d'accueil

    fenetre.blit(accueil, (0,0))                # Affiche Accueil

    """ Affichage du Score """
    pygame.draw.rect(fenetre,(0,0,0),(0,450,450,60))           # affiche le rectangle noir
    message_display(status_level)                              # Affiche le message
    font = pygame.font.SysFont("Times New Roman", 22)           # Choix de la police
    text_Score = font.render("          Niv.: " + str(last_niveau) + " Temps : " + text_clock + "  Score : " + str(score) ,1,(255,255,255) )
    fenetre.blit(text_Score, (0 , cote_fenetre+taille_sprite))  # Affiche ligne en 0 / 480
    pygame.display.flip()

    for event in pygame.event.get():            # On parcourt la liste de tous les événements reçus
        if event.type == QUIT:                  # Si un de ces événements est de type QUIT
            continuer = 0                       # On arrête la boucle
            continuer_jeu = 0                   # On arrête la boucle
        elif event.type == KEYDOWN:             #si on appuie sur une touche
            pygame.time.delay(20)
            if event.key == K_ESCAPE:           #si cette touche est echap
                continuer = 0                   #la fenêtre se ferme
            elif event.key == K_F1:
                niveau = 1
            elif event.key == K_F2:
                niveau = 2
            elif event.key == K_F3:
                niveau = 3
            elif event.key == K_F4:
                niveau = 4
            elif event.key == K_F5:
                niveau = 5
            elif event.key == K_F6:
                niveau = 6
            elif event.key == K_F7:
                niveau = 7
            elif event.key == K_F8:
                niveau = 8
            elif event.key == K_F9:
                niveau = 9
        if niveau != 0 :        # Si K_FX alors niveau different de 0  alors Nouvelle Partie
            continuer = 1
            continuer_jeu = 1
            generer("data/levels/level"+str(niveau)+".txt") # on charge le niveau X
            init_sprite()                           # on met le sprite sur depart 0/30
            fenetre.blit(pas, pas_rect)
            debut = default_timer()                 # on init le chronometre
            status_level = ""
            score = 0                               # Score a 0

    while continuer_jeu:                                           #ici le code du jeu
        fenetre.blit(fond, (0,0))
        afficher(int(pas_rect.top/taille_sprite),int(pas_rect.left/taille_sprite),FOG_distance)
        fenetre.blit(pas, pas_rect)

        """ Affichage du Score """
        pygame.draw.rect(fenetre,(0,0,0),(0,450,450,60))
        message_display("Trouve les bananes !")
        font = pygame.font.SysFont("Times New Roman", 32)
        text_clock = chronometre()                                  # on met a jour la chaine du temps
        text_Score = font.render("           Niv.: " + str(niveau) + "  Temps : " + text_clock + "  Score : " + str(score) ,1,(255,255,255) )
        fenetre.blit(text_Score, (0 , cote_fenetre+taille_sprite))
        pygame.display.flip()

        for event in pygame.event.get():                            # on tests les evenements des touches du jeu
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 1
            if event.type == KEYDOWN:
                pygame.time.delay(20)
                if event.key==K_RIGHT :
                    if pas_rect.left + pas_rect.width + taille_sprite <= cote_fenetre and carreaux(pas_rect.left + taille_sprite, pas_rect.top) != "m":
                        pygame.mixer.Sound(son1).play(loops=1, maxtime=0, fade_ms=0) # On joue le son1
                        fenetre.blit(fond, pas_rect, pas_rect)
                        pas_rect = pas_rect.move(taille_sprite, 0)
                        pas = pygame.image.load("data/images/sprites/dk_droite.png").convert_alpha()
                        fenetre.blit(pas, pas_rect)
                    else:
                        pygame.mixer.Sound(son4).play(loops=1, maxtime=0, fade_ms=0) # On joue le son2
                elif event.key==K_LEFT :
                    if pas_rect.left - taille_sprite >= 0 and carreaux(pas_rect.left - taille_sprite, pas_rect.top) != "m":
                        pygame.mixer.Sound(son1).play(loops=1, maxtime=0, fade_ms=0)
                        fenetre.blit(fond, pas_rect, pas_rect)
                        pas_rect = pas_rect.move(-1*taille_sprite, 0)
                        pas = pygame.image.load("data/images/sprites/dk_gauche.png").convert_alpha()
                        fenetre.blit(pas, pas_rect)
                    else:
                        pygame.mixer.Sound(son2).play(loops=1, maxtime=0, fade_ms=0) # On joue le son2
                elif event.key==K_DOWN :
                    if pas_rect.top + pas_rect.height + taille_sprite <= cote_fenetre and carreaux(pas_rect.left, pas_rect.top + taille_sprite ) != "m" :
                        pygame.mixer.Sound(son1).play(loops=1, maxtime=0, fade_ms=0)
                        fenetre.blit(fond, pas_rect, pas_rect)
                        pas_rect = pas_rect.move(0, taille_sprite)
                        pas = pygame.image.load("data/images/sprites/dk_bas.png").convert_alpha()
                        fenetre.blit(pas, pas_rect)
                    else:
                        pygame.mixer.Sound(son2).play(loops=1, maxtime=0, fade_ms=0) # On joue le son2
                elif event.key==K_UP :
                    if pas_rect.top - taille_sprite >= 0 and carreaux(pas_rect.left , pas_rect.top - taille_sprite) != "m" :
                        pygame.mixer.Sound(son1).play(loops=1, maxtime=0, fade_ms=0)
                        fenetre.blit(fond, pas_rect, pas_rect)
                        pas_rect = pas_rect.move(0, -1*taille_sprite)
                        pas = pygame.image.load("data/images/sprites/dk_haut.png").convert_alpha()
                        fenetre.blit(pas, pas_rect)
                    else:
                        pygame.mixer.Sound(son2).play(loops=1, maxtime=0, fade_ms=0) # On joue le son2
                elif event.key == K_ESCAPE:           #si cette touche est echap
                    last_niveau = niveau
                    continuer = 1
                    continuer_jeu = 0
                    niveau = 0
                # Tests des collisions
                case = carreaux(pas_rect.left , pas_rect.top)
                if case == 'A':
                    pygame.mixer.Sound(son7).play(loops=1, maxtime=0, fade_ms=0) # on joue le son de la victoire
                    status_level = "Gagné"
                    last_niveau = niveau # on garde pour l'affichage le dernier niveau joué
                    niveau = 0
                    continuer_jeu = 0
                elif case == 'E':
                    pygame.mixer.Sound(son9).play(loops=1, maxtime=0, fade_ms=0) # on joue le son de la defaite
                    status_level = "Perdu"
                    last_niveau = niveau
                    niveau = 0
                    continuer_jeu = 0


pygame.quit()                                   #fermeture du programe
