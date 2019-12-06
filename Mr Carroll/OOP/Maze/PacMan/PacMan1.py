import pygame,random,sys,FileIO,MazeGenerator,random,os
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
RED = (255, 0, 0)
YELLOW = (230,230,0)
SCRIPT_PATH = sys.path[0]

def random_place():
    Random_Node = random.choice(Node_List)
    return(Random_Node[0]*block_width,Random_Node[1]*block_width)

def generate_wall(List,Dimension):
    for i in range(len(List)):
        for j in range(len(List[i])):
            if List[i][j] == 1:
                wall1 = Wall(((j*Dimension),(i*Dimension)),Dimension)
                wall_group.add(wall1)
                all_sprites_group.add(wall1)
        #next j
    #next i
    left = [0,len(List)//2]
    right = [len(List[0])-1,len(List)//2]
    for block in wall_group:
        if block.rect.collidepoint((0,left[1]*block_width)):
            block.kill()
            left_portal = Portal(Dimension,(0,left[1]*block_width))
        elif block.rect.collidepoint((right[0]*block_width,right[1]*block_width)):
            block.kill()
            right_portal = Portal(Dimension,(right[0]*block_width,right[1]*block_width))
    return left_portal,right_portal
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

class Portal(pygame.sprite.Sprite):
    def __init__(self,block_width,dimension):
        super().__init__()
        self.image = pygame.Surface([block_width, block_width])
        self.rect = self.image.get_rect()
        self.rect.y = dimension[1]
        self.rect.x = dimension[0]

#end class
        
class Ghost(pygame.sprite.Sprite):
    def __init__(self,block_width,dimension):
        super().__init__()
        self.width = block_width - 6
        self.image = pygame.Surface([self.width, self.width])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = dimension[1]
        self.rect.x = dimension[0]
        self.speed = 1  
        self.node_queue = []
        self.next_node = None

    def update(self):
        if self.next_node == None and self.node_queue:
            self.next_node = self.node_queue.pop(0)
        if self.next_node != None:
            Next_X = (Node_List[self.next_node][0] * block_width) + (block_width//2)
            Next_Y = (Node_List[self.next_node][1] * block_width) + (block_width//2)
            Current_X = self.rect.centerx
            Current_Y = self.rect.centery
            if Current_X < Next_X:
                 self.rect.x += self.speed
            if Current_X > Next_X:
                self.rect.x -= self.speed
            if Current_Y > Next_Y:
                self.rect.y -= self.speed
            if Current_Y < Next_Y:
                self.rect.y += self.speed
            if Next_X == Current_X and Next_Y == Current_Y:
                if self.node_queue:
                    self.next_node = self.node_queue.pop(0)
                else:
                    self.next_node = None

    def move(self,Path_List):
        self.node_queue = Path_List[1:]

class Player(pygame.sprite.Sprite):
    def __init__(self,block_width,dimension):
        super().__init__()
        self.width = block_width - 8
        self.image = pygame.image.load(os.path.join(SCRIPT_PATH,"images","pacman.gif")).convert()
        self.image = pygame.transform.smoothscale(self.image, (self.width,self.width))
        self.up_im = []
        for i in range(1,7):
            self.up_im.append(pygame.image.load(os.path.join(SCRIPT_PATH,"images","pacman-u " + str(i) + ".gif")).convert())
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
currentplayer = Node_List[0]
temp = random_place()
ghost1 = Ghost(block_width,temp)
ghost_group.add(ghost1)
all_sprites_group.add(ghost1)
left_portal,right_portal = generate_wall(Wall_List,block_width)
screen = pygame.display.set_mode(size)
game_over = False
clock = pygame.time.Clock()
temp = random_place()
player1 = Player(block_width,temp)
all_sprites_group.add(player1)
Temp_Node_List = []
portal_active = True
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

    if pygame.sprite.collide_rect(player1, right_portal) and portal_active == False:
        player1.rect.left = left_portal.rect.right
        portal_active = True
    elif pygame.sprite.collide_rect(player1, left_portal) and portal_active == False:
        player1.rect.right = right_portal.rect.left
        portal_active = True
    if not pygame.sprite.collide_rect(player1,left_portal) and not pygame.sprite.collide_rect(player1,left_portal):
        portal_active = False
        
            
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
    ghost_group.update()
    all_sprites_group.draw(screen)
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
