import pygame

pygame.init()
fenetre = pygame.display.set_mode((300,300))
son = pygame.mixer.Sound("son.wav")
son.play()
