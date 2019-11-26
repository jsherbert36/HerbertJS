import pygame,random,sys,FileIO

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
def generate_wall(List,Dimension):
    for i in range(len(List)):
        for j in range(len(List[i])):
            if List[i][j] == True:
                wall1 = Wall(((j*Dimension),(i*Dimension)),Dimension)
                wall_group.add(wall1)
                all_sprites_group.add(wall1)
            #end if
        #next j
    #next i 
    
class Wall(pygame.sprite.Sprite):
    def __init__(self,dimension,block_width):
        super().__init__()
        self.image = pygame.Surface([block_width, block_width])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = dimension[1]
        self.rect.x = dimension[0]
# Initialize Pygame
Wall_List = FileIO.input_list()
pygame.init()
size = (1000,700)
block_width = 15
screen = pygame.display.set_mode(size)
wall_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
generate_wall(Wall_List,block_width)
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
    #all_sprites_group.update()
 
    all_sprites_group.draw(screen) 
    clock.tick(50)
    pygame.display.flip()
 
pygame.quit()
