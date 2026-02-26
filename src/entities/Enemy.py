import pygame


class Enemy:
    def __init__(self, x:int , y:int, height:int, width:int, speed:int):
        self.rect = pygame.Rect(x , y , width, height)
        self.speed = speed
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self, scene: pygame.Surface):
        self.velocity_x += self.speed

        if self.rect.x < 0 or self.rect.x > scene.get_width() -50:
            self.speed = -1

        self.rect.x = self.velocity_x

    def draw(self, scene: pygame.Surface):
        pygame.draw.rect(scene, pygame.Color("blue"), self.rect)
