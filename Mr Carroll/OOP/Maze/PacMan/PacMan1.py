import pygame,random,sys,FileIO,MazeGenerator,random,os,math
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
RED = (255, 0, 0)
YELLOW = (230,230,0)
SCRIPT_PATH = sys.path[0]

def move_ghost(ghost,dimension):
    if dimension not in Node_List:
        Node_List.append(dimension)
    End_Index = Node_List.index(dimension)
    Start = [ghost.rect.x//block_width,ghost.rect.y//block_width]
    if Start not in Node_List:
        Node_List.append(Start)
    Start_Index = Node_List.index(Start)
    Connection_Dict = MazeGenerator.getConnections(Wall_List,Node_List)
    try:
        Path_List = MazeGenerator.Dijkstra(Connection_Dict,Start_Index,End_Index)
    except:
        Path_List = []
    ghost.move(Path_List)

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
        self.width = block_width
        self.image = pygame.image.load(os.path.join(SCRIPT_PATH,"images","portal.png")).convert()
        self.image = pygame.transform.smoothscale(self.image, (self.width,self.width))
        self.rect = self.image.get_rect()
        self.rect.y = dimension[1]
        self.rect.x = dimension[0]

#end class
        
class Ghost(pygame.sprite.Sprite):
    def __init__(self,block_width,dimension,name):
        super().__init__()
        self.name = name
        self.width = block_width - 6
        self.image = pygame.image.load(os.path.join(SCRIPT_PATH,"images",name+".gif")).convert()
        self.image = pygame.transform.smoothscale(self.image, (self.width,self.width))
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
        self.width = block_width - 6
        self.stop_im = pygame.image.load(os.path.join(SCRIPT_PATH,"images","pacman.gif")).convert()
        self.image = self.stop_im
        self.image = pygame.transform.smoothscale(self.image, (self.width,self.width))
        self.next_x = None
        self.next_y = None
        self.next = None
        self.up_im = []
        self.down_im = []
        self.right_im = []
        self.left_im = []
        self.direction = 'stop'
        for i in range(1,9):
            self.up_im.append(pygame.image.load(os.path.join(SCRIPT_PATH,"images","pacman-u " + str(i) + ".gif")).convert())
        for i in range(1,9):
            self.down_im.append(pygame.image.load(os.path.join(SCRIPT_PATH,"images","pacman-d " + str(i) + ".gif")).convert())
        for i in range(1,9):
            self.right_im.append(pygame.image.load(os.path.join(SCRIPT_PATH,"images","pacman-r " + str(i) + ".gif")).convert())
        for i in range(1,9):
            self.left_im.append(pygame.image.load(os.path.join(SCRIPT_PATH,"images","pacman-l " + str(i) + ".gif")).convert())
        self.rect = self.image.get_rect()
        self.rect.y = dimension[1]
        self.rect.x = dimension[0]
        self.speed = 2
        self.count = 0

    def update(self):
        if self.count > 14:
            self.count = 0
        if self.direction == 'up':
            self.image = self.up_im[self.count//2]
            self.image = pygame.transform.smoothscale(self.image, (self.width,self.width))
            self.rect.y -= self.speed
            self.next_y = self.rect.bottom//block_width
            self.next_x = self.rect.x//block_width
        elif self.direction == 'down':
            self.image = self.down_im[self.count//2]
            self.image = pygame.transform.smoothscale(self.image, (self.width,self.width))
            self.rect.y += self.speed
            self.next_y = self.rect.top//block_width
            self.next_x = self.rect.x//block_width
        elif self.direction == 'right':
            self.image = self.right_im[self.count//2]
            self.image = pygame.transform.smoothscale(self.image, (self.width,self.width))
            self.rect.x += self.speed
            self.next_x = self.rect.left//block_width
            self.next_y = self.rect.y//block_width
        elif self.direction == 'left':
            self.image = self.left_im[self.count//2]
            self.image = pygame.transform.smoothscale(self.image, (self.width,self.width))
            self.rect.x -= self.speed
            self.next_x = self.rect.right//block_width
            self.next_y = self.rect.y//block_width
        elif self.direction == 'stop':
            self.image = self.stop_im
            self.image = pygame.transform.smoothscale(self.image, (self.width,self.width))
            self.next_x = self.rect.x//block_width
            self.next_y = self.rect.y//block_width
        self.count += 1
        wall_hit_group = pygame.sprite.spritecollide(self, wall_group, False)
        for block in wall_hit_group:
            if self.direction == 'right':
                self.rect.right = block.rect.left
            elif self.direction == 'left':
                self.rect.left = block.rect.right
            elif self.direction == 'down':
                self.rect.bottom = block.rect.top
            elif self.direction == 'up':
                self.rect.top = block.rect.bottom
            if self.next != None:
                self.direction = self.next
                self.next = None
            else:
                self.direction = 'stop'
        if self.next != None:
            if self.next == 'right':
                if Wall_List[self.next_y][self.next_x+1] == 0:
                    self.direction = 'right'
                    self.next = None
            elif self.next == 'left':
                if Wall_List[self.next_y][self.next_x-1] == 0:
                    self.direction = 'left'
                    self.next = None
            elif self.next == 'up':
                if Wall_List[self.next_y-1][self.next_x] == 0:
                    self.direction = 'up'
                    self.next = None
            elif self.next == 'down':
                if Wall_List[self.next_y+1][self.next_x] == 0:
                    self.direction = 'down'
                    self.next = None
            
    def move(self,val):
        if self.next == None:
            self.next = val
        
        
# Initialize Pygame
block_width = 30
pygame.init()
x = 700 - (700 % block_width)
y = 700 - (700 % block_width)
size = (x,y)
screen = pygame.display.set_mode(size)
maze_x = size[0]//block_width
maze_y = size[1]//block_width
Wall_List = FileIO.input_list(os.path.join(SCRIPT_PATH,'PacMan-Maze.json'))
wall_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
Node_List = MazeGenerator.getNodes(Wall_List)
currentplayer = Node_List[0]
temp = random_place()
blinky = Ghost(block_width,temp,'blinky')
temp = random_place()
inky = Ghost(block_width,temp,'inky')
temp = random_place()
pinky = Ghost(block_width,temp,'pinky')
temp = random_place()
sue = Ghost(block_width,temp,'sue')
ghost_group.add(blinky,inky,pinky,sue)
all_sprites_group.add(blinky,inky,pinky,sue)
left_portal,right_portal = generate_wall(Wall_List,block_width)
all_sprites_group.add(left_portal,right_portal)
game_over = False
clock = pygame.time.Clock()
temp = random_place()
pacman = Player(block_width,temp)
all_sprites_group.add(pacman)
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
        
    x = pacman.rect.centerx//block_width
    y = pacman.rect.centery//block_width
    if currentplayer != [x,y]:
        currentplayer = [x,y]
        move_ghost(blinky,currentplayer)
        if math.hypot(abs(pacman.rect.x - left_portal.rect.x), abs(pacman.rect.y - left_portal.rect.y)) < 150:
            inky_x = (right_portal.rect.x - 100)//block_width
            inky_y = (right_portal.rect.y//block_width)
        elif math.hypot(abs(pacman.rect.x - right_portal.rect.x), abs(pacman.rect.y - right_portal.rect.y)) < 150:
            inky_x = (left_portal.rect.x + 100)//block_width
            inky_y = (left_portal.rect.y//block_width)
        else:
            inky_x = x
            inky_y = y
        move_ghost(inky,[inky_x,inky_y])
        if pacman.direction == 'up':
            pinky_x = x
            if pacman.rect.y > block_width + 100:
                pinky_y = (pacman.rect.y - 100)//block_width
            else:
                pinky_y = y
        elif pacman.direction == 'down':
            pinky_x = x
            if pacman.rect.y < size[1] - block_width - 100:
                pinky_y = (pacman.rect.y + 100)//block_width
            else:
                pinky_y = y
        elif pacman.direction == 'right':
            if pacman.rect.x < size[0]-100-block_width:
                pinky_x = (pacman.rect.x + 100)//block_width
            else:
                pinky_x = x
            pinky_y = y
        elif pacman.direction == 'left':
            if pacman.rect.x > block_width + 100:
                pinky_x = (pacman.rect.x - 100)//block_width
            else:
                pinky_x = x
            pinky_y = y
        else:
            pinky_x = x
            pinky_y = y
        move_ghost(pinky,[pinky_x,pinky_y])
        move_ghost(sue,random.choice(Node_List))
        

    if pygame.sprite.collide_rect(pacman, right_portal) and portal_active == False:
        pacman.rect.left = left_portal.rect.right
        portal_active = True
    elif pygame.sprite.collide_rect(pacman, left_portal) and portal_active == False:
        pacman.rect.right = right_portal.rect.left
        portal_active = True
    if not pygame.sprite.collide_rect(pacman,left_portal) and not pygame.sprite.collide_rect(pacman,left_portal):
        portal_active = False
    if pygame.sprite.spritecollide(pacman,ghost_group,False):
        game_over = True
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        pacman.move('right')
    elif keys[pygame.K_LEFT]:
        pacman.move('left')
    elif keys[pygame.K_DOWN]:
        pacman.move('down')
    elif keys[pygame.K_UP]:
        pacman.move('up')

    screen.fill(BLACK)
    ghost_group.update()
    pacman.update()
    all_sprites_group.draw(screen)
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
