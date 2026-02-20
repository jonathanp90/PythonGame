import pygame
import Player
import Enemy
import Text
import Screen

pygame.init()

player = Player
enemy = Enemy
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
    enemy.X += enemy.speed
    if enemy.X < 0 or enemy.X > scene.WIDTH - 50:
        enemy.speed *= -1

    if keys[pygame.K_LEFT]:
        player.posx -= player.speed
    if keys[pygame.K_RIGHT]:
        player.posx += player.speed
    if keys[pygame.K_UP]:
        player.posy -= player.speed
    if keys[pygame.K_DOWN]:
        player.posy += player.speed

    player.Update()
    enemy.Update()



    if player.player_rect.colliderect(enemy.enemy_rect):
        game_mode = 2
        #running = False

    #draw
    scene.screen.fill((0,0,0))

    pygame.draw.rect(scene.screen,(250,0,0),player.player_rect)
    pygame.draw.rect(scene.screen, (0,0,255),  enemy.enemy_rect)
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