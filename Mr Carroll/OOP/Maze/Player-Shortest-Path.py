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

def follow_path(Path_List,Dimension,Node_List):
    player1.move_queue = []
    for i in range(len(Path_List)-1):
        Next_X = Node_List[Path_List[i+1]][0]
        Next_Y = Node_List[Path_List[i+1]][1]
        x = Node_List[Path_List[i]][0]
        y = Node_List[Path_List[i]][1]
        if x < Next_X:
            player1.move('right')
            print('right')
            print(player1.move_queue)
        if x > Next_X:
            player1.move('left')
            print('left')
            print(player1.move_queue)
        if y > Next_Y:
            player1.move('up')
            print('up')
            print(player1.move_queue)
        if y < Next_Y:
            player1.move('down')
            print('down')
            print(player1.move_queue)
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
        self.speed = 2
        self.direction = 'stop'
        self.move_queue = []
        self.count = 0
    def update(self):
        x = self.rect.centerx//block_width
        y = self.rect.centery//block_width
        if [x,y] in Node_List and self.move_queue:
            
            if self.move_queue[0] == 'right' and Wall_List[y][x+1] == 0:
                    self.direction = 'stop'
                    self.rect.y = y*block_width + 1
                    self.rect.right = (x+1) * block_width
            elif self.move_queue[0] == 'left' and Wall_List[y][x-1] == 0:
                    self.direction = 'stop'
                    self.rect.y = y*block_width + 1
                    self.rect.x = x * block_width
            elif self.move_queue[0] == 'up' and Wall_List[y-1][x] == 0:
                    self.direction = 'stop'
                    self.rect.x = x*block_width + 1
                    self.rect.y = y * block_width 
            elif self.move_queue[0] == 'down' and Wall_List[y+1][x] == 0:
                    self.direction = 'stop'
                    self.rect.x = x*  block_width + 1
                    self.rect.y = (y+1) * block_width
            
        #if self.direction == 'right' and Wall_List[y][x+1] == 1: self.direction = 'stop'
        #elif self.direction == 'left' and Wall_List[y][x-1] == 1: self.direction = 'stop'
        #elif self.direction == 'up' and Wall_List[y-1][x] == 1: self.direction = 'stop'
        #elif self.direction == 'down' and Wall_List[y+1][x] == 1: self.direction = 'stop'
        if self.direction == 'stop' and self.move_queue:
            self.direction = self.move_queue.pop(0)
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
            pass
        
    def move(self,direction):
        if direction == 'right' or direction == 'left' or direction == 'down' or direction == 'up':
            self.move_queue.append(direction)

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
pos = (Node_List[0][0]*block_width,Node_List[0][1]*block_width)
player1 = Player(block_width,pos)
Start = [player1.rect.x//block_width,player1.rect.y//block_width]
if Start not in Node_List:
    Node_list.append(Start)
Start_Index = Node_List.index(Start)
End_Index = Node_List.index(End)
Connection_Dict = MazeGenerator.getConnections(Wall_List,Node_List)
Path_List = MazeGenerator.Dijkstra(Connection_Dict,Start_Index,End_Index)
generate_wall(Wall_List,block_width)
generate_path(Path_List,block_width,Node_List)
screen = pygame.display.set_mode(size)
game_over = False
clock = pygame.time.Clock()


all_sprites_group.add(player1)
follow_path(Path_List,block_width,Node_List)
# -------- Main Program Loop ----------- #
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #elif event.type == pygame.KEYDOWN:
         #   if event.key == pygame.K_ESCAPE:
          #      game_over = True
           # if event.key == pygame.K_RIGHT:
            #    player1.move('right')
            #if event.key == pygame.K_LEFT:
            #    player1.move('left')
            #if event.key == pygame.K_DOWN:
            #    player1.move('down')
            #if event.key == pygame.K_UP:
            #    player1.move('up')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            x = mouse[0]//block_width
            y = mouse[1]//block_width
            if Wall_List[y][x] == 0:
                if [x,y] not in Node_List:
                    Node_List.append([x,y])
                if event.button == 1:
                    End_Index = Node_List.index([x,y])
                Start_Index = [player1.rect.x//block_width,player1.rect.y//block_width]
                if Start not in Node_List:
                    Node_list.append(Start)
                Start_Index = Node_List.index(Start)
                Connection_Dict = MazeGenerator.getConnections(Wall_List,Node_List)
                Path_List = MazeGenerator.Dijkstra(Connection_Dict,Start_Index,End_Index)
                generate_path(Path_List,block_width,Node_List)
                follow_path(Path_List,block_width,Node_List)
            #endif
        #endif
    #next event
    
    screen.fill(BLACK)
    player1.update()
    path_group.draw(screen)
    all_sprites_group.draw(screen)
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
