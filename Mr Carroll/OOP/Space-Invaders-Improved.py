import pygame,random,sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class Invader(pygame.sprite.Sprite):
    direction = 1
    def __init__(self,dimension):
        self.dimension = dimension
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([self.dimension, self.dimension])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
 

    def update(self,count):
        self.rect.x += self.direction 
        for invader in invader_group:
            if invader.rect.x > size[0] - self.dimension*2:
                self.direction = -1
                self.rect.y += 3
            elif invader.rect.x < self.dimension:
                self.direction = 1
                self.rect.y += 3

    def shoot():
        i = random.randrange(i,len(invader_group))

        
 
class Player(Invader):
    def __init__(self):
        super().__init__(20)
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.speed = 7
        self.rect.x = size[0]//2
        self.rect.y = size[1] - 50
    def update(self,count):
        if self.rect.x > size[0] - 20:
            self.rect.x = size[0] - 20
        elif self.rect.x < 0:
            self.rect.x = 0
    def move(self,val):
        if val == 'right':
            self.rect.x += self.speed
        elif val == 'left':
            self.rect.x -= self.speed

class Player_Bullet(pygame.sprite.Sprite):
    def __init__(self,X,Y,speed):
        super().__init__()
        self.image = pygame.Surface([8, 8])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.y = Y
        self.speed = speed

    def update(self,count):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            player_bullet_group.remove(self)

# Initialize Pygame
pygame.init()
size = (1280,720)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

invader_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
player_bullets_hit_group = pygame.sprite.Group()
invaders_hit_group = pygame.sprite.Group()
player_hit_list = pygame.sprite.Group()
for i in range(20,300,40):
    for j in range(90,size[0]-120,size[0]//30):
        invader = Invader(30)
        invader.rect.x = j
        invader.rect.y = i
        # Add the invader to the group of objects
        invader_group.add(invader)
        all_sprites_group.add(invader)

player = Player()
all_sprites_group.add(player)
game_over = False
clock = pygame.time.Clock()
score = 0
lives = 5
font = pygame.font.Font('freesansbold.ttf', 20)
player_bullet_num = 75
count = 0
# -------- Main Program Loop ----------- #
while not game_over:
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_SPACE and player_bullet_num > 0:
                player_bullet = Player_Bullet(player.rect.centerx,player.rect.y,5)
                player_bullet_group.add(player_bullet)
                all_sprites_group.add(player_bullet)
                player_bullet_num -= 1
            #endif
        #endif
    #next event
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.move('right')
    elif keys[pygame.K_LEFT]:
        player.move('left')
    screen.fill(BLACK)    
    all_sprites_group.update(count)
    
    if not invader_group:
        game_over = True
    
    player_bullets_hit_dict = pygame.sprite.groupcollide(player_bullet_group, invader_group, True,True)
    player_bullet_list = []
    for key,val in player_bullets_hit_dict.items():
        player_bullet_list.append(val)
    for player_bullet in player_bullet_list:
        score += 5
    player_hit_list = pygame.sprite.spritecollide(player, invader_group, True)
    for invader in player_hit_list:
        lives -= 1
    if lives == 0:
        game_over = True

    Lives = font.render('Lives: '+ str(lives), True, WHITE) 
    LivesRect = Lives.get_rect()
    LivesRect.topleft = (20,100)
    Score = font.render('Score: '+ str(score), True, WHITE)
    ScoreRect = Score.get_rect()
    ScoreRect.topleft = (20,20)
    Player_Bullets = font.render('Player_Bullets: ' + str(player_bullet_num), True, WHITE)
    Player_BulletsRect = Player_Bullets.get_rect()
    Player_BulletsRect.topleft = (20,60)
    screen.blit(Lives, LivesRect)
    screen.blit(Score, ScoreRect)
    screen.blit(Player_Bullets,Player_BulletsRect) 
    all_sprites_group.draw(screen) 
    clock.tick(40)
    pygame.display.flip()
 
pygame.quit()
