from tokenize import String

import pygame

pygame.font.init()

WHITE = (255,255,255)

message = String
font = pygame.font.SysFont("Aerial", 30)
text_source = font.render(message, True, WHITE)
text_rect = text_source.get_rect()

def set_message(mess):
    message = mess

def update():
    text_source = font.render(message, True, WHITE)
    text_rect = text_source.get_rect()