import pygame,random,sys,FileIO
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
class Wall(pygame.sprite.Sprite):
    def __init__(self,dimension,block_width,colour = WHITE):
        super().__init__()
        self.colour = colour
        self.image = pygame.Surface([block_width, block_width])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.y = dimension[1]
        self.rect.x = dimension[0]
    #end procedure
#end class

# Initialize Pygame
block_width = int(input('Enter Block Size (integer):'))
width = int(input('Enter the screen width: '))
height = int(input('Enter the screen height: '))
pygame.init()
x = width - (width % block_width)
y = height - (height % block_width)
size = (x,y)
maze_x = size[0]//block_width
maze_y = size[1]//block_width
Wall_List = [[0 for j in range(maze_x)] for i in range(maze_y)]
wall_group = pygame.sprite.Group()
screen = pygame.display.set_mode(size)
game_over = False
clock = pygame.time.Clock()
last_pressed = []
# -------- Main Program Loop ----------- #
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_SPACE:
                FileIO.output_list(Wall_List)
                game_over = True
    if pygame.mouse.get_pressed()[0]:
        mouse = pygame.mouse.get_pos()
        x = mouse[0]//block_width
        y = mouse[1]//block_width
        if [x,y] != last_pressed:
            if Wall_List[y][x] == 0:
                Wall_List[y][x] = 1
                wall1 = Wall(((x*block_width),(y*block_width)),block_width)
                wall_group.add(wall1)
            elif Wall_List[y][x] == 1:
                Wall_List[y][x] = 0
                for block in wall_group:
                    if block.rect.collidepoint(mouse):
                        block.kill()
            last_pressed = [x,y]
    screen.fill(BLACK)
    wall_group.draw(screen)
    clock.tick(100)
    pygame.display.flip()
pygame.quit()
