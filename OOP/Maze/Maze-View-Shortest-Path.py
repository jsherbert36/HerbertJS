import pygame,random,sys,FileIO,MazeGenerator,random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
RED = (255, 0, 0)
def generate_wall(List,Dimension):
    for i in range(len(List)):
        for j in range(len(List[i])):
            if List[i][j] == 1:
                wall1 = Wall(((j*Dimension),(i*Dimension)),Dimension)
                wall_group.add(wall1)
                all_sprites_group.add(wall1)
        #next j
#end procedure

def generate_path(Path_List,Dimension,Node_List):
    for block in path_group:
        block.kill()
    for i in range(len(Path_List)-1):
        Next = Node_List[Path_List[i+1]]
        x = Node_List[Path_List[i]][0]
        y = Node_List[Path_List[i]][1]
        while [x,y] != Next:
            if x < Next[0]: x += 1
            elif x>Next[0]: x -= 1
            if y < Next[1]: y +=1
            elif y>Next[1]: y -= 1
            path1 = Wall(((x*Dimension),(y*Dimension)),Dimension,BLUE)
            path_group.add(path1)
        #next j
    #nexti
#end procedure
    
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
width = 1000
height = 700
x = width - (width % block_width)
y = height - (height % block_width)
size = (x,y)
maze_x = size[0]//block_width
maze_y = size[1]//block_width
if User_Choice.upper() == 'Y':
    Wall_List = (MazeGenerator.generate(maze_x,maze_y)).tolist()
    FileIO.output_list(Wall_List)
else:
    Wall_List = FileIO.input_list()
#endif
wall_group = pygame.sprite.Group()
path_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
Node_List = MazeGenerator.getNodes(Wall_List)
End = random.choice(Node_List)
Start_Index = 0
End_Index = Node_List.index(End)
Connection_Dict = MazeGenerator.getConnections(Wall_List,Node_List)
Path_List = MazeGenerator.Dijkstra(Connection_Dict,Start_Index,End_Index)
generate_wall(Wall_List,block_width)
generate_path(Path_List,block_width,Node_List)
screen = pygame.display.set_mode(size)
game_over = False
clock = pygame.time.Clock()
pos = (Node_List[0][0]*block_width,Node_List[0][1]*block_width)
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            x = mouse[0]//block_width
            y = mouse[1]//block_width
            if Wall_List[y][x] == 0:
                if [x,y] not in Node_List:
                    Node_List.append([x,y])
                if event.button == 1:
                    End_Index = Node_List.index([x,y])
                elif event.button == 3:
                    Start_Index = Node_List.index([x,y])
                Connection_Dict = MazeGenerator.getConnections(Wall_List,Node_List)
                Path_List = MazeGenerator.Dijkstra(Connection_Dict,Start_Index,End_Index)
                generate_path(Path_List,block_width,Node_List)
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
    path_group.draw(screen)
    all_sprites_group.draw(screen)
    clock.tick(50)
    pygame.display.flip()
 
pygame.quit()
