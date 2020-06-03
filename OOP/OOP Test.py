import pygame
import random
from typing import Tuple
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

### What is a class?

# A class is the blueprint for an object. It defines what an object
# will look like (its properties and attributes) and what the object will do (its methods)

 
class Block(pygame.sprite.Sprite):
    def __init__(self, colour:Tuple[int], width:int, height:int): ### What is this subroutine known as? -- This is known as the constructor method
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour) 
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-300, -20)
    #end method
 
    def reset_pos(self):
        self.rect.y = -20
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
    #end method

    def update(self):
        self.rect.y += 4
        if self.rect.y > screen_height: self.reset_pos()
    #end method
#end class


### Fix this class so that it inherits Block and is the colour RED
class Player(Block):
    def __init__(self):
        super().__init__(RED,20,20)
    #end method
        
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]
     #end method
#end class
        
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
 

### Create 50 random positioned blocks that will be displayed

block_list.add([Block(BLACK,20,20) for _ in range(50)])
 
# Create a red player
red_player = Player()

all_sprites_list.add(red_player,block_list)
 

game_over = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #end if
    #next event
            
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Calls update() method on every sprite in the list
    
    all_sprites_list.update() ### What OOP concept is being used here? -- This is the OOP concept of polymorphism
 
    # See if the player has collided with a block.
    block_hit_list = pygame.sprite.spritecollide(red_player,block_list,True)

    # Update the score +1 for every block collision
    score += len(block_hit_list)
    map(Block.reset_pos,block_hit_list)

    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()
