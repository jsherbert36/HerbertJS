import pygame,random,sys,time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class Space():
    class Invader(pygame.sprite.Sprite):
        direction = 1
        def __init__(self,dimension):
            self.dimension = dimension
            # Call the parent class (Sprite) constructor
            super().__init__()
            self.image = pygame.image.load("Invader.jpg").convert()
            self.image = pygame.transform.smoothscale(self.image, (dimension,dimension))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
        def update(self,count):
            if count % 2 == 0:
                self.rect.x += self.direction 
            for invader in invader_group:
                if invader.rect.x > size[0] - self.dimension*2:
                    self.direction = -1
                    self.rect.y += 3
                elif invader.rect.x < self.dimension:
                    self.direction = 1
                    self.rect.y += 3

        def shoot(self):  
            if self.rect.x % random.randint(7,27) == 0 and self.rect.y % random.randint(5,25) == 0:
                print('Shoot')
                invader_bullet = Space.Invader_Bullet(self.rect.centerx,self.rect.y)
                invader_bullet_group.add(invader_bullet)
                all_sprites_group.add(invader_bullet)
        
 
    class Player(Invader):
        def __init__(self):
            super().__init__(20)
            self.image = pygame.image.load("player.png").convert()
            self.image = pygame.transform.smoothscale(self.image, (50,40))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
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
        def __init__(self,X,Y):
            super().__init__()
            self.image = pygame.image.load("bullet.png").convert()
            self.image = pygame.transform.smoothscale(self.image, (8,25))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = X
            self.rect.y = Y
            self.speed = 3

        def update(self,count):
            self.rect.y -= self.speed
            if self.rect.y < 0:
                player_bullet_group.remove(self)

    class Invader_Bullet(pygame.sprite.Sprite):
        def __init__(self,X,Y):
            super().__init__()
            self.image = pygame.image.load("Bullet.jpg").convert()
            self.image = pygame.transform.smoothscale(self.image, (12,20))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = X
            self.rect.y = Y
            self.speed = 6

        def update(self,count):
            self.rect.y += self.speed
            if self.rect.y > size[1] + 20:
                invader_bullet_group.remove(self)
    
    class Defence(pygame.sprite.Sprite):
        def __init__(self,X,Y,dimension):
            super().__init__()
            self.dimension = dimension
            self.image = pygame.image.load("Defence.jpg").convert()
            self.image = pygame.transform.smoothscale(self.image, (self.dimension,self.dimension))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = X
            self.rect.y = Y
        def update(self,count):
            pass
 

# Initialize Pygame
pygame.init()
size = (1280,720)
screen = pygame.display.set_mode(size)
invader_size = 55
invader_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
invader_bullet_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
player_bullets_hit_group = pygame.sprite.Group()
invader_bullets_hit_group = pygame.sprite.Group()
invaders_hit_group = pygame.sprite.Group()
player_hit_list = pygame.sprite.Group()
defence_group = pygame.sprite.Group()
for i in range(60,340,invader_size + 10):
    for j in range(250,size[0]-250 - invader_size,(size[0]//invader_size) + 50):
        invader = Space.Invader(invader_size)
        invader.rect.x = j
        invader.rect.y = i
        # Add the invader to the group of objects
        invader_group.add(invader)
        all_sprites_group.add(invader)
defence_dimension = 80
for i in range(200,size[0]-200,160):
    defence = Space.Defence(i,size[1]-170,defence_dimension)
    defence_group.add(defence)
    all_sprites_group.add(defence)

player = Space.Player()
all_sprites_group.add(player)
game_over = False
clock = pygame.time.Clock()
score = 0
lives = 3
font = pygame.font.Font('freesansbold.ttf', 20)
player_bullet_num = 100
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
                player_bullet = Space.Player_Bullet(player.rect.centerx,player.rect.y)
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
    
    if count % 50 == 0:
        for invader in invader_group:
             invader.shoot()

    player_bullets_hit_dict = pygame.sprite.groupcollide(player_bullet_group, invader_group, True,True)
    player_bullet_list = []
    for key,val in player_bullets_hit_dict.items():
        player_bullet_list.append(val)
    for player_bullet in player_bullet_list:
        score += 5
    pygame.sprite.groupcollide(player_bullet_group, defence_group, True,False)
    pygame.sprite.groupcollide(invader_bullet_group, defence_group, True,False)
    invader_bullets_hit_list = pygame.sprite.spritecollide(player, invader_bullet_group, True)
    for bullet in invader_bullets_hit_list:
        lives -= 1
        time.sleep(1)
    if lives == 0:
        game_over = True

    Lives = font.render('Lives: '+ str(lives), True, WHITE) 
    Score = font.render('Score: '+ str(score), True, WHITE)
    Player_Bullets = font.render('Bullets: ' + str(player_bullet_num), True, WHITE)
    screen.blit(Lives, (size[0]//2 - 150,17))
    screen.blit(Score, (size[0]//2 + 140,17))
    screen.blit(Player_Bullets,(size[0]//2 - 10,17)) 
    all_sprites_group.draw(screen) 
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
