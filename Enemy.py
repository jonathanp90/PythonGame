import pygame

X = 100
Y = 100
speed = 5





enemy_rect = pygame.Rect(X, Y , 50 , 50)

def Update():
    enemy_rect.x = X
    enemy_rect.y = Y