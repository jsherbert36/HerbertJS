import pygame,random,sys,FileIO,MazeGenerator,random
from collections import deque
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
    #next i
#end function

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
    #next i
#end function
    
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
        self.direction = 'stop'
        self.move_queue = deque([])
    def update(self):
        if self.direction == 'stop' and not self.move_queue:
            self.direction = move_queue.popleft()
        if self.direction == 'right': self.rect.x += self.speed
        elif self.direction == 'left': self.rect.x -= self.speed
        elif self.direction == 'up': self.rect.y -= self.speed
        elif self.direction == 'down': self.rect.y += self.speed
        wall_hit_group = pygame.sprite.spritecollide(self, wall_group, False)
        for block in wall_hit_group:
            if self.direction == 'right': self.rect.right = block.rect.left
            elif self.direction == 'left': self.rect.left = block.rect.right
            elif self.direction == 'down': self.rect.bottom = block.rect.top
            elif self.direction == 'up': self.rect.top = block.rect.bottom
            self.direction = 'stop'
        x = self.rect.x//block_width
        y = self.rect.y//block_width
        if [x,y] in Node_List:
            if Wall_List                                                                        #needs completing

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
        player.move_queue.append('right')
    elif keys[pygame.K_LEFT]:
        player.move_queue.append('left')
    elif keys[pygame.K_DOWN]:
        player.move_queue.append('down')
    elif keys[pygame.K_UP]:
        player.move_queue.append('up')
    
    screen.fill(BLACK)
    path_group.draw(screen)
    all_sprites_group.draw(screen)
    clock.tick(50)
    pygame.display.flip()
 
pygame.quit()
