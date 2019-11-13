import pygame,random,sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class Invader(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.x = random.randrange(0,(size[0]-30),30)
        self.rect.y = random.randrange(-300,-20,30)
 
    def update(self):
        self.rect.y += 1
        if self.rect.y > size[1] + 10:
            self.reset_pos()
 
class Player(Invader):
    def __init__(self):
        super().__init__()
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
        self.speed = 3

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            bullet_group.remove(self)

# Initialize Pygame
pygame.init()
size = (900,650)
screen = pygame.display.set_mode(size)
# This is a group of 'sprites.' Each invader in the program is
# added to this group. The group is managed by a class called 'Group.'
invader_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
bullets_hit_group = pygame.sprite.Group()
invaders_hit_group = pygame.sprite.Group()
 
for i in range(75):
    invader = Invader()
    invader.rect.x = random.randrange(0,(size[0]-30),30)
    invader.rect.y = random.randrange(-200,50,30)
    # Add the invader to the group of objects
    invader_group.add(invader)
    all_sprites_group.add(invader)

player = Player()
all_sprites_group.add(player)
game_over = False
clock = pygame.time.Clock()
score = 0
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

    Score = font.render('Score: '+ str(score), True, WHITE)
    ScoreRect = Score.get_rect()
    ScoreRect.topleft = (20,20)
    Bullets = font.render('Bullets: ' + str(bullet_num), True, WHITE)
    BulletsRect = Bullets.get_rect()
    BulletsRect.topleft = (20,60)
    
    screen.blit(Score, ScoreRect)
    screen.blit(Bullets,BulletsRect) 
    all_sprites_group.draw(screen) 
    clock.tick(50)
    pygame.display.flip()
 
pygame.quit()
