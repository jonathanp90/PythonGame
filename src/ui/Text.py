from tokenize import String

import pygame

class Text:

    def __init__(self, message: str):
        pygame.font.init()

        self.Color = (255,255,255)

        self.Message = message
        self.Font = pygame.font.SysFont("Aerial", 30)
        self.Source = self.Font.render(self.Message, True, self.Color)
        self.Position = self.Source.get_rect()

    def set_message(self, mess):
        self.Message = mess
        self.update()
    
    def set_position(self, x:int, y: int):
        self.Position.x = x
        self.Position.y = y
        self.update()

    def update(self):
        self.Source = self.Font.render(self.Message, True, self.Color)
        self.Position = self.Source.get_rect()

    def draw(self, scene:pygame.surface):
        scene.blit(self.Source, self.Position)