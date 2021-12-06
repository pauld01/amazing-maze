import pygame, sys
from pygame.locals import *
from timeit import default_timer
from tkinter import *

pygame.init()

fen=pygame.display.set_mode((1000,700))
im=pygame.image.load("foret.jpg")
fond = pygame.transform.scale(im, (1000, 700))
fen.blit(fond, (0, 0))
pas = pygame.image.load("imagepas.png").convert_alpha()
pas = pygame.transform.scale(pas, (50, 50))
pas_rect=pas.get_rect()
pas_rect.top=35
pas_rect.left=5
fen.blit(pas, pas_rect)
white=(255, 255, 255)
bandeau = pygame.draw.rect(fen, white, (0,0,1000,30))

pygame.key.set_repeat(400,30)
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_RIGHT :
                if pas_rect.left + pas_rect.width + 5 < 1000 :
                    fen.blit(fond, pas_rect, pas_rect)
                    pas_rect = pas_rect.move(5, 0)
                    fen.blit(pas, pas_rect)
                    pygame.display.update()
                    pygame.time.delay(20)
            if event.key==K_LEFT :
                if pas_rect.left - 5 > 0 :
                    fen.blit(fond, pas_rect, pas_rect)
                    pas_rect = pas_rect.move(-5, 0)
                    fen.blit(pas, pas_rect)
                    pygame.display.update()
                    pygame.time.delay(20)
            if event.key==K_DOWN :
                if pas_rect.top + pas_rect.height + 5 < 700 :
                    fen.blit(fond, pas_rect, pas_rect)
                    pas_rect = pas_rect.move(0, 5)
                    fen.blit(pas, pas_rect)
                    pygame.display.update()
                    pygame.time.delay(20)
            if event.key==K_UP :
                if pas_rect.top - 5 > 30 :
                    fen.blit(fond, pas_rect, pas_rect)
                    pas_rect = pas_rect.move(0, -5)
                    fen.blit(pas, pas_rect)
                    pygame.display.update()
                    pygame.time.delay(20)
    pygame.display.update()

pygame.init()