import pygame
# -- Global Constants

BLACK = (131,226,255)
WHITE = (255,255,255)
BLUE = (191,81,21)
YELLOW = (255,220,0)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

# -- Blank Screen
size = (1080,720)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Sunrise")

game_over = False
x_pos = 40
y_pos = 300

### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
            
    # -- Game logic goes after this comment
    
    x_pos += 1
    if x_pos > 900 or x_pos < 0:
        x_pos = 40
    
    y_pos = (50 * ((x_pos - 540)**2)) + 3000000
    y_pos = y_pos // 50000
    
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, BLUE, (400,250,200,210))
    pygame.draw.circle(screen, YELLOW, (x_pos,y_pos),50,0)
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(200)

#End While - End of game loop

pygame.quit()
