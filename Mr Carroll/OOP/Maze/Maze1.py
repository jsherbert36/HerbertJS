import pygame,random,sys,FileIO

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class Wall(pygame.sprite.Sprite):
    def __init__(self,dimension):
        self.x = dimension[0]
        self.y = dimension[1]
        super().__init__()
        self.image = pygame.Surface([self.x, self.y])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

# Initialize Pygame
pygame.init()
size = (1000,700)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)



player = Player()
all_sprites_group.add(player)
game_over = False
clock = pygame.time.Clock()
# -------- Main Program Loop ----------- #
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            #endif
        #endif
    #next event
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.move('right')
    elif keys[pygame.K_LEFT]:
        player.move('left')
    screen.fill(BLACK)    
    all_sprites_group.update()
    
    if not invader_group:
        game_over = True
    
    bullets_hit_dict = pygame.sprite.groupcollide(bullet_group, invader_group, True,True)
    bullet_list = []
    for key,val in bullets_hit_dict.items():
        bullet_list.append(val)
    for bullet in bullet_list:
        score += 5
    player_hit_list = pygame.sprite.spritecollide(player, invader_group, True)
    for invader in player_hit_list:
        lives -= 1
    if lives == 0:
        game_over = True
 
    all_sprites_group.draw(screen) 
    clock.tick(50)
    pygame.display.flip()
 
pygame.quit()
