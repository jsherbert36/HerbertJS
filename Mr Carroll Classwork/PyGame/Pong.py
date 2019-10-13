import pygame
import random


def Menu1():
    choice = False
    font = pygame.font.Font('freesansbold.ttf', 100) 
    font2 = pygame.font.Font('freesansbold.ttf',60)
    font3 = pygame.font.Font('freesansbold.ttf',27)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (204,0,0)
    SingleColour = WHITE
    MultiColour = WHITE
    global game_over
    game_over = False
    circle_x = [90,200,600,1250,1900] 
    circle_y = [900,100,450,1070,50]
    direction_x = [-8,2,7,8,-9]
    direction_y = [7,-8,11,-9,5]
    while not game_over and not choice:
        
        
        screen.fill(BLACK) 
        Pong = font.render('PONG!', True, WHITE)
        PongRect = Pong.get_rect()
        PongRect.center = (size[0] // 2, 400) 
        screen.blit(Pong, PongRect) 
        mouse = pygame.mouse.get_pos()      
        Single = font2.render('SINGLEPLAYER', True, SingleColour)
        SingleRect = Single.get_rect()
        SingleRect.center = (size[0] // 2, 550) 
        screen.blit(Single, SingleRect) 
        if mouse[0]in range(SingleRect.x,SingleRect.x + SingleRect.width) and  mouse[1] in range(SingleRect.y,SingleRect.y + SingleRect.height):
            SingleColour = RED
        else:
            SingleColour = WHITE  
        #endif
        Multi = font2.render('MULTIPLAYER', True, MultiColour)
        MultiRect = Multi.get_rect()
        MultiRect.center = (size[0] // 2, 650) 
        screen.blit(Multi, MultiRect) 
        if mouse[0]in range(MultiRect.x,MultiRect.x + MultiRect.width) and  mouse[1] in range(MultiRect.y,MultiRect.y + MultiRect.height):
            MultiColour = RED
        else:
            MultiColour = WHITE
        #endif
        for i in range(5):
            circle_x[i] += round(direction_x[i])
            circle_y[i] += round(direction_y[i])
            if circle_y[i] > 1065:
                direction_y[i] *= -1
            elif circle_y[i] < 15:
                direction_y[i] *= -1
            elif circle_x[i] < 15:
                direction_x[i] *= -1
            elif circle_x[i] > 1905:
                direction_x[i] *= -1
            pygame.draw.circle(screen, WHITE, (circle_x[i],circle_y[i]), 20)
            #end if
        #next i

        Message = font3.render('PRESS ESC TO EXIT', True, WHITE)
        MessageRect = Message.get_rect()
        MessageRect.center = (size[0] // 2, 900) 
        screen.blit(Message, MessageRect) 
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    elif event.key == pygame.K_x:
                        return 'special'
                        choice == True
                    #end if
                elif event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0]in range(SingleRect.x,SingleRect.x + SingleRect.width) and  mouse[1] in range(SingleRect.y,SingleRect.y + SingleRect.height):
                        choice = True
                        return 'single'
                    elif mouse[0]in range(MultiRect.x,MultiRect.x + MultiRect.width) and  mouse[1] in range(MultiRect.y,MultiRect.y + MultiRect.height):
                        choice = True
                        return 'multi'
                    #endif
                #end if
        #next event      
        clock.tick(90)
    #endwhile
#end procedure


def Menu2():
    choice = False
    font = pygame.font.Font('freesansbold.ttf', 100) 
    font2 = pygame.font.Font('freesansbold.ttf',80)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (204,0,0)
    EasyColour = WHITE
    MediumColour = WHITE
    HardColour = WHITE
    global game_over
    circle_x = [90,200,600,1250,1900] 
    circle_y = [900,100,450,1070,50]
    direction_x = [-8,2,7,8,-9]
    direction_y = [7,-8,11,-9,5]
    while not game_over and not choice:
        
        
        screen.fill(BLACK) 
        Difficulty = font.render('DIFFICULTY:', True, WHITE)
        DifficultyRect = Difficulty.get_rect()
        DifficultyRect.center = (size[0] // 2, 400) 
        screen.blit(Difficulty, DifficultyRect) 
        mouse = pygame.mouse.get_pos()      
        Easy = font2.render('EASY', True, EasyColour)
        EasyRect = Easy.get_rect()
        EasyRect.center = (size[0] // 2, 550) 
        screen.blit(Easy, EasyRect) 
        if mouse[0]in range(EasyRect.x,EasyRect.x + EasyRect.width) and  mouse[1] in range(EasyRect.y,EasyRect.y + EasyRect.height):
            EasyColour = RED
        else:
            EasyColour = WHITE      
        #end if
        Medium = font2.render('MEDIUM', True, MediumColour)
        MediumRect = Medium.get_rect()
        MediumRect.center = (size[0] // 2, 650) 
        screen.blit(Medium, MediumRect) 
        if mouse[0]in range(MediumRect.x,MediumRect.x + MediumRect.width) and  mouse[1] in range(MediumRect.y,MediumRect.y + MediumRect.height):
            MediumColour = RED
        else:
            MediumColour = WHITE
        #end if
        Hard = font2.render('HARD', True, HardColour)
        HardRect = Hard.get_rect()
        HardRect.center = (size[0] // 2, 750) 
        screen.blit(Hard, HardRect) 
        if mouse[0]in range(HardRect.x,HardRect.x + HardRect.width) and  mouse[1] in range(HardRect.y,HardRect.y + HardRect.height):
            HardColour = RED
        else:
            HardColour = WHITE
        #end if
        for i in range(5):
            circle_x[i] += round(direction_x[i])
            circle_y[i] += round(direction_y[i])
            if circle_y[i] > 1065:
                direction_y[i] *= -1
            elif circle_y[i] < 15:
                direction_y[i] *= -1
            elif circle_x[i] < 15:
                direction_x[i] *= -1
            elif circle_x[i] > 1905:
                direction_x[i] *= -1
            #endif
            pygame.draw.circle(screen, WHITE, (circle_x[i],circle_y[i]), 20)
        #next i
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0]in range(EasyRect.x,EasyRect.x + EasyRect.width) and  mouse[1] in range(EasyRect.y,EasyRect.y + EasyRect.height):
                        choice = True
                        return 'Easy'
                    elif mouse[0]in range(MediumRect.x,MediumRect.x + MediumRect.width) and  mouse[1] in range(MediumRect.y,MediumRect.y + MediumRect.height):
                        choice = True
                        return 'Medium'
                    elif mouse[0]in range(HardRect.x,HardRect.x + HardRect.width) and  mouse[1] in range(HardRect.y,HardRect.y + HardRect.height):
                        choice = True
                        return 'Hard'
                    #end if
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    #end if
                #end if
        #next event
        clock.tick(90)
    #endwhile
#end function



def countdown(usercount):
    font = pygame.font.Font('freesansbold.ttf', 120) 
    font2 = pygame.font.Font('freesansbold.ttf',30)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    count = usercount * 60
    global game_over
    
    while count > -1 and not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    #endif
                #End If
            #next event
            if count % 60 == 0:
                screen.fill(BLACK) 
                Single = font.render(str(count // 60), True, WHITE)
                SingleRect = Single.get_rect()
                SingleRect.center = (size[0] // 2, size[1] // 2) 
                screen.blit(Single, SingleRect) 
                Message = font2.render('PRESS SPACEBAR TO PAUSE/EXIT', True, WHITE)
                MessageRect = Message.get_rect()
                MessageRect.center = (size[0] // 2, 800) 
                screen.blit(Message, MessageRect) 
                pygame.display.flip()
            #endif
            count -= 1
            clock.tick(60)
    #endwhile
#end procedure

def gameplay(speed,paddle_height,mode,comp_speed,refresh):
    #initialise variables
    left_x = 30
    left_y = 540
    right_x = 1860
    right_y = 540
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (204,0,0)
    PlayColour = BLACK
    ExitColour = BLACK
    RestartColour = BLACK
    global game_over
    game_end = False
    score1 = 0
    score2 = 0
    font = pygame.font.Font('freesansbold.ttf', 120)
    font2 = pygame.font.Font('freesansbold.ttf',100)
    while not game_over:
        if game_end:
                clock.tick(1)   
        #endif
        game_end = False
        direction_x = speed 
        direction_y = speed
        if (score1 + score2) % 2 == 0:
            circle_x = 100
        else:
            circle_x = 1880
            direction_x *= -1
        #endif
        circle_y = random.randint(5,1040)
        while not game_over and not game_end:
            # -- User input and controls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    #endif
                #endif
            #Next event
        
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_SPACE]:
                Continue = False
                while not game_over and not Continue:
                    screen.fill(WHITE) 
                    mouse = pygame.mouse.get_pos() 
                    Play = font2.render('CONTINUE PLAYING', True, PlayColour)
                    PlayRect = Play.get_rect()
                    PlayRect.center = (size[0] // 2, 500) 
                    screen.blit(Play, PlayRect) 
                    if mouse[0]in range(PlayRect.x,PlayRect.x + PlayRect.width) and  mouse[1] in range(PlayRect.y,PlayRect.y + PlayRect.height):
                        PlayColour = RED
                    else:
                        PlayColour = BLACK
                    #end if
                    Exit = font2.render('EXIT GAME', True, ExitColour)
                    ExitRect = Exit.get_rect()
                    ExitRect.center = (size[0] // 2, 600) 
                    screen.blit(Exit, ExitRect) 
                    if mouse[0]in range(ExitRect.x,ExitRect.x + ExitRect.width) and  mouse[1] in range(ExitRect.y,ExitRect.y + ExitRect.height):
                        ExitColour = RED
                    else:
                        ExitColour = BLACK
                    #endif
                    Restart = font2.render('MAIN MENU', True, RestartColour)
                    RestartRect = Restart.get_rect()
                    RestartRect.center = (size[0] // 2, 700) 
                    screen.blit(Restart, RestartRect) 
                    if mouse[0]in range(RestartRect.x,RestartRect.x + RestartRect.width) and  mouse[1] in range(RestartRect.y,RestartRect.y + RestartRect.height):
                        RestartColour = RED
                    else:
                        RestartColour = BLACK
                    #endif
                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_over = True
                        elif event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                            mouse = pygame.mouse.get_pos()
                            if mouse[0]in range(PlayRect.x,PlayRect.x + PlayRect.width) and  mouse[1] in range(PlayRect.y,PlayRect.y + PlayRect.height):
                                Continue = True
                            elif mouse[0]in range(ExitRect.x,ExitRect.x + ExitRect.width) and  mouse[1] in range(ExitRect.y,ExitRect.y + ExitRect.height):
                                game_over = True
                            elif mouse[0]in range(RestartRect.x,RestartRect.x + RestartRect.width) and  mouse[1] in range(RestartRect.y,RestartRect.y + RestartRect.height):
                                global restart
                                restart = False
                                game_over = True
                            #endif
                        #endif
                    #next event
                    clock.tick(60)
                #endwhile
            #endif
            if mode == 'multi':
                if keys[pygame.K_w]:
                    left_y = left_y - 13
                elif keys[pygame.K_s]:
                    left_y = left_y + 13
                #endif
            elif mode == 'single' or mode == 'special':
                if circle_x < 1000:
                    if circle_y < left_y + (paddle_height//4):
                        left_y -= comp_speed
                    elif circle_y > left_y + (paddle_height) - (paddle_height//4):
                        left_y += comp_speed
                    #endif
                #endif
            #endif
            
            if left_y > 1080 - paddle_height - 5:
                left_y = (1080 - paddle_height - 5) - 3
            elif left_y < 5:
                left_y = 7
            #endif
            if mode == 'single' or mode == 'multi':
                if keys[pygame.K_UP]:
                    right_y = right_y - 13
                elif keys[pygame.K_DOWN]:
                    right_y = right_y + 13
                #endif
            elif mode == 'special':
                if circle_x > 920:
                    if circle_y < right_y + (paddle_height//4):
                        right_y -= comp_speed
                    elif circle_y > right_y + (paddle_height) - (paddle_height//4):
                        right_y += comp_speed
                    #endif
                #endif
            #endif
            if right_y > 1080 - paddle_height - 5:
                right_y = (1080 - paddle_height - 5) - 3
            elif right_y < 5:
                right_y = 7
            #endif
        
            # -- Screen background is BLACK
            screen.fill (BLACK)

            if abs(direction_y/direction_x) > 1.5:
                direction_x *= 1.5
            circle_x += round(direction_x)
            circle_y += round(direction_y)
            #endif
            if (circle_x < left_x + 50):
                if (circle_y < (left_y + paddle_height)) and (circle_y > (left_y + paddle_height - 5)):     #corners
                    direction_x = speed
                    direction_y = speed
                elif (circle_y < (left_y + 5)) and (circle_y > (left_y)):     
                    direction_x = speed 
                    direction_y = speed * -1
                elif (circle_y < (left_y + paddle_height - (0.3*paddle_height))) and (circle_y > (left_y + (0.3*paddle_height))):     #sweet spot
                    direction_x = abs(direction_x) * 1.2
                elif (circle_y < (left_y + paddle_height -5)) and (circle_y > (left_y + paddle_height - (0.3*paddle_height))):     # slight angle
                    direction_x = abs(direction_x) * 0.8
                elif (circle_y < (left_y + (0.3*paddle_height))) and (circle_y > (left_y + 5)):     # slight angle
                    direction_x = abs(direction_x) * 0.8
                #end if
            #endif
            if (circle_x > right_x - 20):
                if (circle_y < (right_y + paddle_height)) and (circle_y > (right_y + paddle_height - 5)):     #corners
                    direction_x = speed * -1
                    direction_y = speed
                elif (circle_y < (right_y + 5)) and (circle_y > (right_y)):     
                    direction_x = speed * -1
                    direction_y = speed * -1
                elif (circle_y < (right_y + paddle_height - (0.3*paddle_height))) and (circle_y > (right_y + (0.3*paddle_height))):     #sweet spot
                    direction_x = abs(direction_x) * -1.2
                elif (circle_y < (right_y + paddle_height -5)) and (circle_y > (right_y + paddle_height - (0.3*paddle_height))):     # slight angle
                    direction_x = abs(direction_x) * -0.8
                elif (circle_y < (right_y + (0.3*paddle_height))) and (circle_y > (right_y + 5)):     # slight angle
                    direction_x = abs(direction_x) * -0.8
                #end if
            #endif

    
            if circle_y > 1065:
                direction_y *= -1
            elif circle_y < 15:
                direction_y *= -1
            elif circle_x < 15:
                game_end = True
                score2 += 1
            elif circle_x > 1905:
                game_end = True
                score1 += 1
            #endif
            font2 = pygame.font.Font('freesansbold.ttf', 50) 
            Single1 = font2.render(str(score1), True, WHITE)
            Single1Rect = Single1.get_rect()
            Single1Rect.center = (80, 80) 
            screen.blit(Single1, Single1Rect)
            Single2 = font2.render(str(score2), True, WHITE)
            Single2Rect = Single2.get_rect()
            Single2Rect.center = (1840, 80) 
            screen.blit(Single2, Single2Rect)

            pygame.draw.rect(screen, WHITE, (right_x, right_y, 30, paddle_height))
            pygame.draw.rect(screen, WHITE, (left_x, left_y, 30, paddle_height))
            pygame.draw.circle(screen, WHITE, (circle_x,circle_y), 20)

            pygame.display.flip()
            clock.tick(refresh)
        #endwhile
    #endwhile
#end procedure


# -- Initialise PyGame
pygame.init()
clock = pygame.time.Clock()

# -- Blank Screen
size = (1920,1080)
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("Pong")

restart = False
while not restart:
    restart = True
    mode = Menu1()
    if mode == 'special':
        gameplay(13,150,'special',12,150)
    else:
        difficulty = Menu2()
        countdown(3)
        if difficulty == 'Easy':
            gameplay(8,200,mode,6,100)
        elif difficulty == 'Medium':
            gameplay(9,150,mode,8,120)
        elif difficulty == 'Hard':
            gameplay(12,150,mode,11,130)
        #end if
    #end if
#endwhile

pygame.quit()
