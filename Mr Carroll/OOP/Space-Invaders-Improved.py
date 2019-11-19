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
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.x = random.randrange(90,(size[0]-120),invader.dimension+10)
        self.rect.y = random.randrange(-300,-20,invader.dimension+10)
 
    def update(self):
        self.rect.x += self.direction 
        for invader in invader_group:
            if invader.rect.x > size[0] - self.dimension*2:
                self.direction = -1
                self.rect.y += 3
            elif invader.rect.x < self.dimension:
                self.direction = 1
                self.rect.y += 3
        
 
class Player(Invader):
    def __init__(self):
        super().__init__(20)
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.speed = 7
        self.rect.x = size[0]//2
        self.rect.y = size[1] - 50
    def update(self):
        if self.rect.x > size[0] - 20:
            self.rect.x = size[0] - 20
        elif self.rect.x < 0:
            self.rect.x = 0
    def move(self,val):
        if val == 'right':
            self.rect.x += self.speed
        elif val == 'left':
            self.rect.x -= self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self,X,Y):
        super().__init__()
        self.image = pygame.Surface([8, 8])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.y = Y
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            bullet_group.remove(self)

# Initialize Pygame
pygame.init()
size = (1280,720)
screen = pygame.display.set_mode(size)
invader_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
bullets_hit_group = pygame.sprite.Group()
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
bullet_num = 75
# -------- Main Program Loop ----------- #
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_SPACE and bullet_num > 0:
                bullet = Bullet(player.rect.centerx,player.rect.y)
                bullet_group.add(bullet)
                all_sprites_group.add(bullet)
                bullet_num -= 1
            #endif
        #endif
    #next event
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.move('right')
    elif keys[pygame.K_LEFT]:
        player.move('left')
    screen.fill(BLACK)    
    all_sprites_group.update()
    
    if not invader_group:
        game_over = True
    
    bullets_hit_dict = pygame.sprite.groupcollide(bullet_group, invader_group, True,True)
    bullet_list = []
    for key,val in bullets_hit_dict.items():
        bullet_list.append(val)
    for bullet in bullet_list:
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
    Bullets = font.render('Bullets: ' + str(bullet_num), True, WHITE)
    BulletsRect = Bullets.get_rect()
    BulletsRect.topleft = (20,60)
    screen.blit(Lives, LivesRect)
    screen.blit(Score, ScoreRect)
    screen.blit(Bullets,BulletsRect) 
    all_sprites_group.draw(screen) 
    clock.tick(40)
    pygame.display.flip()
 
pygame.quit()
