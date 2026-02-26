import pygame
from src.entities import Player
from src.entities.Enemy import Enemy
from src.entities.Player import Player
from src.ui import Text
from src.core import Screen

pygame.init()

player = Player(300,200, 50,50,5)
enemy = Enemy(100, 100, 50, 50, 5)
txt = Text
#Window
scene = Screen

clock = pygame.time.Clock()

running = True
game_mode = 1




while running:
    clock.tick(60) #60 FPS
    keys = pygame.key.get_pressed()




    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Update


    player.handle_input()



    player.update()
    enemy.update(scene.screen)



    if player.rect.colliderect(enemy.rect):
        game_mode = 2
        #running = False

    #draw
    scene.screen.fill((0,0,0))

    player.draw(scene.screen)
    enemy.draw(scene.screen)
    pygame.display.flip()

    if game_mode == 2:
        txt.message = "Game Over"
        txt.text_source = txt.font.render(txt.message, True, txt.WHITE)
        txt.text_rect = txt.text_source.get_rect()
        # txt.update()
        txt.text_rect.center = (scene.WIDTH // 2, scene.HEIGHT // 2)
        scene.screen.blit(txt.text_source, txt.text_rect)
        enemy.speed = 0
        player.speed = 0
        pygame.display.flip()
#pygame.quit()