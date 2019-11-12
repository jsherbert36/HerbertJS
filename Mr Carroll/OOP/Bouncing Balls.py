import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (51, 51, 255)
YELLOW = (255, 255, 51)
RED = (255, 51, 51)
PINK = (255, 51, 133)
GREEN = (51, 255, 51)
PURPLE = (153, 51, 255)
LIGHTBLUE = (51, 255, 255)
ORANGE = (255, 51, 51)
BALLCOLOURS = (WHITE,BLUE,YELLOW,RED,PINK,GREEN,PURPLE,LIGHTBLUE,ORANGE)
class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction_y = random.randint(8,12) * random.choice([1,-1])
        self.direction_x = random.randint(8,12) * random.choice([1,-1])
        self.colour = BALLCOLOURS[random.randint(0,8)]
        self.size = 15
        
    def move(self):
        if self.y > size[1] - self.size:
            self.direction_y *= -1
        elif self.y < self.size:
            self.direction_y *= -1
        elif self.x < self.size:
            self.direction_x *= -1
        elif self.x > size[0] - self.size:
            self.direction_x *= -1
                
        #End if
        self.y += self.direction_y 
        self.x += self.direction_x 

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x,self.y), self.size)

# -- Initialise PyGame
pygame.init()
clock = pygame.time.Clock()
info = pygame.display.Info()
size = (info.current_w, info.current_h)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

pygame.display.set_caption("Bouncing Balls")

game_over = False
ball_size = 15
circles = []
for i in range(50):
    X = random.randint(2,size[0])
    Y = random.randint(2,size[1])
    circles.append(Ball(X,Y))
#endfor 

### -- Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_SPACE:
                for i in range(20):
                    X = random.randint(2,size[0])
                    Y = random.randint(2,size[1])
                    circles.append(Ball(X,Y))
                #endfor 
            elif event.key == pygame.K_UP:
                ball_size += 3
            elif event.key == pygame.K_DOWN:
                ball_size -= 3
            #End If
        #End If
    #Next event
    screen.fill (BLACK)
    if ball_size < 2:
        ball_size = 2
    for circle in circles:
        circle.move()
        circle.size = ball_size
        circle.draw()

    pygame.display.flip()

    clock.tick(50)

#End While - End of game loop

pygame.quit()
