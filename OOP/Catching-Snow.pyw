import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Snowflake.jpg").convert()
        self.image = pygame.transform.smoothscale(self.image, (30,30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, size[0])
 
    def update(self):
       
        self.rect.y += 1
       
        if self.rect.y > size[1] + 10:
            self.reset_pos()
 
class Player(Block):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
 
for i in range(60):
    block = Block()
    block.rect.x = random.randrange((size[0]-30))
    block.rect.y = random.randrange(size[1])
    block_list.add(block)
    all_sprites_list.add(block)
 
player = Player()
all_sprites_list.add(player)
game_over = False
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font('freesansbold.ttf', 30)

# -------- Main Program Loop ----------- #
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
    screen.fill(BLACK)
    all_sprites_list.update()
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    for block in blocks_hit_list:
        score += 1
        block.reset_pos()
    all_sprites_list.draw(screen) 
    Score = font.render(str(score), True, WHITE)
    ScoreRect = Score.get_rect()
    ScoreRect.center = (size[0]//2, size[1] - 50) 
    screen.blit(Score, ScoreRect)
    
    clock.tick(20)
    pygame.display.flip()
 
pygame.quit()
