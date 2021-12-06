import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((450, 450))
taille_sprite = 30
continuer = 1
structure = [[]]
sol = pygame.image.load("bloc1.png").convert()
mur = pygame.image.load("bloc2.png").convert()
position = (30, 0)


def generer(fichier):
    with open(fichier, "r") as fichier:
        i = 0
        for ligne in fichier.readlines():
            structure.append([])
            for sprite in ligne:
                if sprite != '\n' :
                    structure[i].append(sprite)
            i += 1
        del structure[-1]


generer('structurelab2')
print(structure)

def afficher():
    for i in range(len(structure)) :
        for j in range(len(structure[0])) :
            if structure[i][j] == 'm':
                fenetre.blit(mur, (i*taille_sprite, j*taille_sprite))
            else :
                fenetre.blit(sol, (i*taille_sprite, j*taille_sprite))



def get_tile_at(x, y) :
    x = x/30
    y = y/30
    return structure[int(x)][int(y)]

while continuer:
    pygame.time.Clock().tick(60)

    afficher()
    pygame.display.flip()
    pygame.display.update()

pygame.quit()