import pygame
from src.entities import Player
from src.entities.Enemy import Enemy
from src.entities.Player import Player
from src.ui.Text import Text
from src.core.Screen import Screen

pygame.init()

player = Player(300,200, 50,50,5)
enemy = Enemy(100, 100, 50, 50, 5)
txt = Text("Game Over")
#Window
window = Screen(600,800)

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
    enemy.update(window.Scene)



    if player.rect.colliderect(enemy.rect):
        game_mode = 2
        #running = False

    #draw
    window.Scene.fill((0,0,0))


    player.draw(window.Scene)
    enemy.draw(window.Scene)
    window.draw()

    if game_mode == 2:
        txt.set_message( "Game Over")
        
        # txt.update()
        txt.set_position(window.Width // 2, window.Height // 2)
        txt.draw(window.Scene)
        enemy.speed = 0
        player.speed = 0
        window.draw()
        
#pygame.quit()