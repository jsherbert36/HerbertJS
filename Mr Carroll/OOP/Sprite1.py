import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load("Snowflake.jpg").convert()
        self.image = pygame.transform.smoothscale(self.image, (30,30))
        self.image.set_colorkey(BLACK)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, size[0])
 
    def update(self):
        # Move block down one pixel
        self.rect.y += 1
        # If block is too far down, reset to top of screen.
        if self.rect.y > size[1] + 10:
            self.reset_pos()
 
class Player(Block):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
# Initialize Pygame
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(60):
    block = Block()
    block.rect.x = random.randrange((size[0]-30))
    block.rect.y = random.randrange(size[1])
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
player = Player()
all_sprites_list.add(player)
game_over = False
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font('freesansbold.ttf', 30)

# -------- Main Program Loop ----------- #
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
    screen.fill(BLACK)
    all_sprites_list.update()
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    for block in blocks_hit_list:
        score += 1
        block.reset_pos()

    # Draw all the sprites
    all_sprites_list.draw(screen) 
    Score = font.render(str(score), True, WHITE)
    ScoreRect = Score.get_rect()
    ScoreRect.center = (size[0]//2, size[1] - 50) 
    screen.blit(Score, ScoreRect)
    
    clock.tick(20)
    pygame.display.flip()
 
pygame.quit()
