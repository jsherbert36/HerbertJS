import pygame,random,sys,FileIO,MazeGenerator,random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
RED = (255, 0, 0)
YELLOW = (230,230,0)

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
            
class Wall(pygame.sprite.Sprite):
    def __init__(self,dimension,block_width,colour = BLUE):
        super().__init__()
        self.colour = colour
        self.image = pygame.Surface([block_width, block_width])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.y = dimension[1]
        self.rect.x = dimension[0]
    #end procedure
#end class
class Ghost(pygame.sprite.Sprite):
    def __init__(self,block_width,dimension):
        super().__init__()
        self.width = block_width - 1
        self.image = pygame.Surface([self.width, self.width])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = dimension[1]
        self.rect.x = dimension[0]
        self.speed = 1
        self.direction = 'stop'
        self.count = 0
        self.node_queue = []
        self.next_node = None

    def update(self):
        if self.direction == 'right': self.rect.x += self.speed
        elif self.direction == 'left': self.rect.x -= self.speed
        elif self.direction == 'up': self.rect.y -= self.speed
        elif self.direction == 'down': self.rect.y += self.speed
        if self.direction == 'stop' and self.node_queue:
            self.next_node = self.node_queue.pop(0)
        if self.next_node != None:
            Next_X = Node_List[self.next_node][0]
            Next_Y = Node_List[self.next_node][1]
            if self.direction == 'right':
                Current_X = self.rect.left//block_width
                Current_Y = self.rect.y//block_width
            elif self.direction == 'left':
                Current_X = self.rect.right//block_width
                Current_Y = self.rect.y//block_width
            elif self.direction == 'down':
                Current_X = self.rect.x//block_width
                Current_Y = self.rect.top//block_width
            elif self.direction == 'up': 
                Current_X = self.rect.x//block_width
                Current_Y = self.rect.bottom//block_width
            else:
                Current_X = self.rect.x//block_width
                Current_Y = self.rect.y//block_width
            if Current_X < Next_X:
                self.direction = 'right'
            elif Current_X > Next_X:
                self.direction = 'left'
            elif Current_Y > Next_Y:
                self.direction = 'up'
            elif Current_Y < Next_Y:
                self.direction = 'down'
            if Next_X == Current_X and Next_Y == Current_Y:
                self.direction = 'stop'
    def move(self,Path_List):
        self.direction = 'stop'
        self.node_queue = Path_List[1:]

class Player(pygame.sprite.Sprite):
    def __init__(self,block_width,dimension):
        super().__init__()
        self.width = block_width - 3
        self.image = pygame.Surface([self.width, self.width])
        self.image.fill(YELLOW)
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
block_width = 30
pygame.init()
x = 700 - (700 % block_width)
y = 700 - (700 % block_width)
size = (x,y)
maze_x = size[0]//block_width
maze_y = size[1]//block_width
Wall_List = FileIO.input_list('PacMan-Maze.json')
wall_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
Node_List = MazeGenerator.getNodes(Wall_List)
pos = (Node_List[0][0]*block_width,Node_List[0][1]*block_width)
currentplayer = Node_List[0]
ghost1 = Ghost(block_width,pos)
generate_wall(Wall_List,block_width)
screen = pygame.display.set_mode(size)
game_over = False
clock = pygame.time.Clock()
all_sprites_group.add(ghost1)
player1 = Player(block_width,pos)
all_sprites_group.add(player1)
Temp_Node_List = []
# -------- Main Program Loop ----------- #
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
        
    x = player1.rect.x//block_width
    y = player1.rect.y//block_width
    if currentplayer != [x,y]:
        currentplayer = [x,y]
        for i in Temp_Node_List:
            index = Node_List.index(i)
            del Node_List[index]
        Temp_Node_List = []
        if currentplayer not in Node_List:
            Node_List.append(currentplayer)
            Temp_Node_List.append(currentplayer)
        End_Index = Node_List.index(currentplayer)
        Start = [ghost1.rect.x//block_width,ghost1.rect.y//block_width]
        if Start not in Node_List:
            Node_List.append(Start)
        Start_Index = Node_List.index(Start)
        Connection_Dict = MazeGenerator.getConnections(Wall_List,Node_List)
        Path_List = MazeGenerator.Dijkstra(Connection_Dict,Start_Index,End_Index)
        ghost1.move(Path_List)
            
    
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
    ghost1.update()
    all_sprites_group.draw(screen)
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
