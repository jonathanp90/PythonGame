import pygame

class Player:
    def __init__(self, x:int,y:int ,width:int ,height:int , speed:int):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.velocity_x = 0
        self.velocity_y = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()

        self.velocity_x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])* self.speed
        self.velocity_y = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * self.speed

    def update(self):
            self.rect.x += self.velocity_x
            self.rect.y += self.velocity_y

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (0,255,9), self.rect)