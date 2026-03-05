import pygame

class Screen:
    def __init__(self, height:int, width:int):
        self.Height = height
        self.Width = width
        self.Scene = pygame.display.set_mode((self.Width,self.Height))
        pygame.display.set_caption("2D game")


    def draw(self):
        pygame.display.flip()
