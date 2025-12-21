import pygame
import Player
import Enemy
import Text

pygame.init()

txt = Text
#Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D game")

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
    Enemy.X += Enemy.speed
    if Enemy.X < 0 or Enemy.X > WIDTH - 50:
        Enemy.speed *= -1

    if keys[pygame.K_LEFT]:
        Player.posx -= Player.speed
    if keys[pygame.K_RIGHT]:
        Player.posx += Player.speed
    if keys[pygame.K_UP]:
        Player.posy -= Player.speed
    if keys[pygame.K_DOWN]:
        Player.posy += Player.speed

    player_rect = pygame.Rect(Player.posx, Player.posy,  Player.width, Player.height)
    enemy_rect = pygame.Rect(Enemy.X, Enemy.Y, 50, 50)

    if player_rect.colliderect(enemy_rect):
        game_mode = 2
        #running = False

    #draw
    screen.fill((0,0,0))

    pygame.draw.rect(screen,(250,0,0),player_rect)
    pygame.draw.rect(screen, (0,0,255),  enemy_rect)
    pygame.display.flip()

    if game_mode == 2:
        txt.message = "Game Over"
        txt.text_source = txt.font.render(txt.message, True, txt.WHITE)
        txt.text_rect = txt.text_source.get_rect()
        # txt.update()
        txt.text_rect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(txt.text_source, txt.text_rect)
        Enemy.speed = 0
        Player.speed = 0
        pygame.display.flip()
#pygame.quit()