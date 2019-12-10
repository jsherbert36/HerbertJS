import pygame,random,sys,MazeGenerator,random,os,math,json
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0,0,210)
RED = (204, 0, 0)
YELLOW = (230,230,0)
SCRIPT_PATH = sys.path[0]

def Menu(screen):
    font = pygame.font.Font('freesansbold.ttf', 70) 
    PlayColour = YELLOW
    CenterX = 350
    CenterY = 350
    game_over = False
    while not game_over:
        screen.fill(BLACK) 
        Logo = pygame.image.load(os.path.join(SCRIPT_PATH,"images","logo.bmp")).convert()
        Logo = pygame.transform.smoothscale(Logo, (550,293))
        LogoRect = Logo.get_rect()
        LogoRect.center = (CenterX, CenterY - 100) 
        screen.blit(Logo, LogoRect) 
        Play = font.render('PLAY', True, PlayColour)
        PlayRect = Play.get_rect()
        PlayRect.center = (CenterX, CenterY)
        screen.blit(Play, PlayRect) 
        mouse = pygame.mouse.get_pos()
        if PlayRect.collidepoint(mouse): PlayColour = BLUE
        else: PlayColour = YELLOW
        pygame.display.flip()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    return 'gameover'
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        return 'gameover'
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if PlayRect.collidepoint(mouse):
                        return 'play'    
        clock.tick(60)
        
def move_ghost(ghost,dimension):
    if dimension not in Node_List:
        Node_List.append(dimension)
        print('new end node')
    End_Index = Node_List.index(dimension)
    Start = [ghost.rect.x//block_width,ghost.rect.y//block_width]
    if Start not in Node_List:
        Node_List.append(Start)
        print('new start node')
    Start_Index = Node_List.index(Start)
    Connection_Dict = MazeGenerator.getConnections(Wall_List,Node_List)
    try:
        Path_List = MazeGenerator.Dijkstra(Connection_Dict,Start_Index,End_Index)
    except:
        Path_List = []
    ghost.move(Path_List)

def random_place():
    Cage_List = [[10,11],[11,11],[12,11]]
    Random_Node = random.choice(Cage_List)
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
        self.speed = 1
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
            elif self.next == None:
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
        self.next = val
        
# Initialize Pygame
block_width = 30
pygame.init()
x = 700 - (700 % block_width)
y = 700 - (700 % block_width)
size = (x,y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('PACMAN')
maze_x = size[0]//block_width
maze_y = size[1]//block_width



f = open(os.path.join(SCRIPT_PATH,'PacMan-Maze.json'),"rt")
Wall_List = json.load(f)
f.close()



temp_node_list = []
wall_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
Node_List = MazeGenerator.getNodes(Wall_List)
currentplayer = Node_List[0]
temp = (11*block_width,10*block_width)
blinky = Ghost(block_width,temp,'blinky')
temp = (10*block_width,11*block_width)
inky = Ghost(block_width,temp,'inky')
temp = (11*block_width,11*block_width)
pinky = Ghost(block_width,temp,'pinky')
temp = (12*block_width,11*block_width)
sue = Ghost(block_width,temp,'sue')
ghost_group.add(blinky,inky,pinky,sue)
all_sprites_group.add(blinky,inky,pinky,sue)
left_portal,right_portal = generate_wall(Wall_List,block_width)
all_sprites_group.add(left_portal,right_portal)
game_over = False
clock = pygame.time.Clock()
Random_Node = random.choice(Node_List[-10:-1])
temp = (Random_Node[0]*block_width,Random_Node[1]*block_width)
pacman = Player(block_width,temp)
all_sprites_group.add(pacman)
Temp_Node_List = []
portal_active = True
start_menu = Menu(screen)
if start_menu == 'gameover': game_over = True
count = 0
cage = pygame.Surface([3*block_width,block_width])
cage_rect = cage.get_rect()
cage_rect.topleft = (10*block_width,11*block_width)
Open = True
ghost_mode = 'scatter'
ghost_mode_count = 0
# -------- Main Program Loop ----------- #
while not game_over:
    count += 1
    ghost_mode_count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
    if ghost_mode_count > 500 and ghost_mode == 'hunt':
        ghost_mode = 'scatter'
        ghost_mode_count = 0 
    elif ghost_mode_count > 200 and ghost_mode == 'scatter':
        ghost_mode = 'hunt'
        ghost_mode_count = 0
        
    x = pacman.rect.centerx//block_width
    y = pacman.rect.centery//block_width
    if currentplayer != [x,y] and ghost_mode == 'hunt':
        currentplayer = [x,y]
        Blinky_Start = [blinky.rect.x//block_width,blinky.rect.y//block_width]
        if Blinky_Start in Node_List: move_ghost(blinky,currentplayer)
        if math.hypot(abs(pacman.rect.x - left_portal.rect.x), abs(pacman.rect.y - left_portal.rect.y)) < 150:
            inky_x = (right_portal.rect.x - 100)//block_width
            inky_y = (right_portal.rect.y//block_width)
        elif math.hypot(abs(pacman.rect.x - right_portal.rect.x), abs(pacman.rect.y - right_portal.rect.y)) < 150:
            inky_x = (left_portal.rect.x + 100)//block_width
            inky_y = (left_portal.rect.y//block_width)
        else:
            inky_x = x
            inky_y = y
        Inky_Start = [inky.rect.x//block_width,inky.rect.y//block_width]
        if Inky_Start in Node_List: move_ghost(inky,[inky_x,inky_y])
        if pacman.direction == 'up':
            pinky_x = x
            if pacman.rect.y > block_width + 130:
                pinky_y = (pacman.rect.y - 130)//block_width
            else:
                pinky_y = y
        elif pacman.direction == 'down':
            pinky_x = x
            if pacman.rect.y < size[1] - block_width - 130:
                pinky_y = (pacman.rect.y + 130)//block_width
            else:
                pinky_y = y
        elif pacman.direction == 'right':
            if pacman.rect.x < size[0]-130-block_width:
                pinky_x = (pacman.rect.x + 130)//block_width
            else:
                pinky_x = x
            pinky_y = y
        elif pacman.direction == 'left':
            if pacman.rect.x > block_width + 130:
                pinky_x = (pacman.rect.x - 130)//block_width
            else:
                pinky_x = x
            pinky_y = y
        else:
            pinky_x = x
            pinky_y = y
        Pinky_Start = [pinky.rect.x//block_width,pinky.rect.y//block_width]
        if Pinky_Start in Node_List: move_ghost(pinky,[pinky_x,pinky_y])
        if sue.next_node == None: move_ghost(sue,random.choice(Node_List))


    elif ghost_mode == 'scatter':
        if sue.next_node == None: move_ghost(sue,random.choice(Node_List))
        if pinky.next_node == None and count > 400: move_ghost(pinky,random.choice(Node_List))
        if blinky.next_node == None: move_ghost(blinky,random.choice(Node_List))
        if inky.next_node == None and count > 150: move_ghost(inky,random.choice(Node_List))

        

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

    if Open == False:
        collide = False
        for ghost in ghost_group:
            if pygame.Rect.colliderect(cage_rect,ghost.rect):
                collide = True
        if pygame.sprite.spritecollide(gate,ghost_group,False) or collide == True:
            Open = True
            gate.kill()
        else:
            gate = Wall(((11*block_width),(10*block_width)),block_width)
            Open = False
            all_sprites_group.add(gate)
            wall_group.add(gate)
    elif Open == True:
        collide = False
        for ghost in ghost_group:
            if pygame.Rect.colliderect(cage_rect,ghost.rect):
                collide = True
        if collide == False:
            Open = False
            gate = Wall(((11*block_width),(10*block_width)),block_width)
            all_sprites_group.add(gate)
            wall_group.add(gate)

            
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
    clock.tick(150)
    pygame.display.flip()
 
pygame.quit()
