import pygame
from random import randint
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

# -- My Classes
class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction_y = 1
        self.direction_x = 1
        self.colour = WHITE
        self.size
        
    def move(self):
        if circle_y > size[1] - self.size:
            self.direction_y *= -1
        elif circle_y < self.size:
            self.direction_y *= -1
        elif circle_x < self.size:
            self.direction_x *= -1
        elif circle_x > size[0] - self.size:
            self.direction_x *= -1
                
        #End if
        self.y += self.direction_y
        self.x += self.direction_x

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x,self.y), self.size)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My First Flipbook")

game_over = False
blocks = []
for i in range(10):
    blocks.append(Ball(randint(5,size[0]-5),randint(5,size[1]-5)))
#endfor 


### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event

            
            
    # -- Game logic goes after this comment
    for block in blocks:
        block.move()
    
    ## - the up key or down key has been pressed
    
        
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here

    # Make the mouse pointer appear in the middle of the square...
    for block in blocks:
        block.draw()

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
