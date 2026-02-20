import pygame
posx = 400
posy = 300
width = 50
height = 50
speed = 5

player_rect = pygame.Rect(posx,posy,width,height)

def Update():
    player_rect.x = posx
    player_rect.y = posy