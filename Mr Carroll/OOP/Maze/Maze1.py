import pygame,random,sys,FileIO,MazeGenerator
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
def generate_wall(List,Dimension):
    for i in range(len(List)):
        for j in range(len(List[i])):
            if List[i][j] == 1:
                wall1 = Wall(((j*Dimension),(i*Dimension)),Dimension)
                wall_group.add(wall1)
                all_sprites_group.add(wall1)
            else:
                false_block = ((j*Dimension),(i*Dimension))
            #end if
        #next j
    #next i
    return false_block
#end function
    
class Wall(pygame.sprite.Sprite):
    def __init__(self,dimension,block_width):
        super().__init__()
        self.image = pygame.Surface([block_width, block_width])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = dimension[1]
        self.rect.x = dimension[0]
    #end procedure
#end class
class Player(pygame.sprite.Sprite):
    def __init__(self,block_width,dimension):
        super().__init__()
        self.width = block_width - 3
        self.image = pygame.Surface([self.width, self.width])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = dimension[1]
        self.rect.x = dimension[0]
        self.speed = 3
    def update(self):
        if self.rect.x > size[0] - 20:
            self.rect.x = size[0] - 20
        elif self.rect.x < 0:
            self.rect.x = 0
    def move(self,val):
        if val == 'right': self.rect.x += self.speed
        elif val == 'left': self.rect.x -= self.speed
        elif val == 'up': self.rect.y -= self.speed
        elif val == 'down': self.rect.y += self.speed
        wall_hit_group = pygame.sprite.spritecollide(self, wall_group, False)
        for block in wall_hit_group:
            if val == 'right': self.rect.right = block.rect.left
            elif val == 'left': self.rect.left = block.rect.right
            elif val == 'down': self.rect.bottom = block.rect.top
            elif val == 'up': self.rect.top = block.rect.bottom
                
# Initialize Pygame
User_Choice = input('Generate new maze? (Y/N): ')
block_width = int(input('Enter Block Size (integer):'))
pygame.init()
x = 1000 + (1000 % block_width)
y = 700 + (700 % block_width)
size = (x,y)
maze_x = size[0]//block_width
maze_y = size[1]//block_width
if User_Choice.upper() == 'Y':
    Wall_List = (MazeGenerator.generate(maze_x,maze_y)).tolist()
    FileIO.output_list(Wall_List)
else:
    Wall_List = FileIO.input_list()
#endif
Node_List = MazeGenerator.getNodes(Wall_List)
FileIO.output_list(Wall_List)
FileIO.output_list(Node_List)
Connection_List = MazeGenerator.getConnections(Wall_List,Node_List)
Connection_Dict = {tuple(i):[] for i in Node_List}
for i in range(len(Connection_List)):
    for j in Connection_List[i]:
        temp = tuple(Node_list[i])
        Connection_Dict[temp].append({(j[0],j[1]):j[2]})
    #next j
#next i
screen = pygame.display.set_mode(size)
wall_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
pos = generate_wall(Wall_List,block_width)
game_over = False
clock = pygame.time.Clock()
player1 = Player(block_width,pos)
all_sprites_group.add(player1)
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
        player1.move('right')
    elif keys[pygame.K_LEFT]:
        player1.move('left')
    elif keys[pygame.K_DOWN]:
        player1.move('down')
    elif keys[pygame.K_UP]:
        player1.move('up')
    screen.fill(BLACK)    
    all_sprites_group.draw(screen) 
    clock.tick(50)
    pygame.display.flip()
 
pygame.quit()
