import pygame
import random
import sys

def Menu1():
    choice = False
    font = pygame.font.Font('freesansbold.ttf', size[1]//8) 
    font2 = pygame.font.Font('freesansbold.ttf',int(size[1]//14.4))
    font3 = pygame.font.Font('freesansbold.ttf',size[1]//36)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (204,0,0)
    SingleColour = WHITE
    MultiColour = WHITE
    ScoreColour = WHITE
    CircleSize = 15
    global game_over
    game_over = False
    circle_x = [90,200,600,1200,1100] 
    circle_y = [600,100,450,160,50]
    direction_x = [-8,2,7,8,-9]
    direction_y = [7,-8,11,-9,5]
    while not game_over and not choice:
        
        
        screen.fill(BLACK) 
        Pong = font.render('PONG!', True, WHITE)
        PongRect = Pong.get_rect()
        PongRect.center = (size[0] // 2, size[1] // 3) 
        screen.blit(Pong, PongRect) 
        mouse = pygame.mouse.get_pos()      
        Single = font2.render('SINGLEPLAYER', True, SingleColour)
        SingleRect = Single.get_rect()
        SingleRect.center = (size[0] // 2, size[1] // 2) 
        screen.blit(Single, SingleRect) 
        if mouse[0]in range(SingleRect.x,SingleRect.x + SingleRect.width) and  mouse[1] in range(SingleRect.y,SingleRect.y + SingleRect.height):
            SingleColour = RED
        else:
            SingleColour = WHITE  
        #endif
        Multi = font2.render('MULTIPLAYER', True, MultiColour)
        MultiRect = Multi.get_rect()
        MultiRect.center = (size[0] // 2, int(size[1] // 1.7)) 
        screen.blit(Multi, MultiRect) 
        if mouse[0]in range(MultiRect.x,MultiRect.x + MultiRect.width) and  mouse[1] in range(MultiRect.y,MultiRect.y + MultiRect.height):
            MultiColour = RED
        else:
            MultiColour = WHITE
        #endif
        Score = font2.render('SCOREBOARD', True, ScoreColour)
        ScoreRect = Score.get_rect()
        ScoreRect.center = (size[0] // 2, int(size[1] // 1.46)) 
        screen.blit(Score, ScoreRect) 
        if mouse[0]in range(ScoreRect.x,ScoreRect.x + ScoreRect.width) and  mouse[1] in range(ScoreRect.y,ScoreRect.y + ScoreRect.height):
            ScoreColour = RED
        else:
            ScoreColour = WHITE
        #endif
        for i in range(5):
            circle_x[i] += round(direction_x[i])
            circle_y[i] += round(direction_y[i])
            if circle_y[i] > size[1] - CircleSize:
                direction_y[i] *= -1
            elif circle_y[i] < CircleSize:
                direction_y[i] *= -1
            elif circle_x[i] < CircleSize:
                direction_x[i] *= -1
            elif circle_x[i] > size[0] - CircleSize:
                direction_x[i] *= -1
            pygame.draw.circle(screen, WHITE, (circle_x[i],circle_y[i]), CircleSize)
            #end if
        #next i

        Message = font3.render('PRESS ESC TO EXIT', True, WHITE)
        MessageRect = Message.get_rect()
        MessageRect.center = (size[0] // 2, int(size[1]//1.2)) 
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
                    elif mouse[0]in range(ScoreRect.x,ScoreRect.x + ScoreRect.width) and  mouse[1] in range(ScoreRect.y,ScoreRect.y + ScoreRect.height):
                        choice = True
                        return 'score'
                    #endif
                #end if
        #next event      
        clock.tick(90)
    #endwhile
#end procedure


def Menu2():
    choice = False
    font = pygame.font.Font('freesansbold.ttf', 90) 
    font2 = pygame.font.Font('freesansbold.ttf',70)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (204,0,0)
    EasyColour = WHITE
    MediumColour = WHITE
    HardColour = WHITE
    global game_over
    circle_x = [90,200,600,1200,1100] 
    circle_y = [600,100,450,550,50]
    direction_x = [-8,2,7,8,-9]
    direction_y = [7,-8,10,-9,5]
    while not game_over and not choice:
        
        
        screen.fill(BLACK) 
        Difficulty = font.render('DIFFICULTY:', True, WHITE)
        DifficultyRect = Difficulty.get_rect()
        DifficultyRect.center = (size[0] // 2, 250) 
        screen.blit(Difficulty, DifficultyRect) 
        mouse = pygame.mouse.get_pos()      
        Easy = font2.render('EASY', True, EasyColour)
        EasyRect = Easy.get_rect()
        EasyRect.center = (size[0] // 2, 370) 
        screen.blit(Easy, EasyRect) 
        if mouse[0]in range(EasyRect.x,EasyRect.x + EasyRect.width) and  mouse[1] in range(EasyRect.y,EasyRect.y + EasyRect.height):
            EasyColour = RED
        else:
            EasyColour = WHITE      
        #end if
        Medium = font2.render('MEDIUM', True, MediumColour)
        MediumRect = Medium.get_rect()
        MediumRect.center = (size[0] // 2, 450) 
        screen.blit(Medium, MediumRect) 
        if mouse[0]in range(MediumRect.x,MediumRect.x + MediumRect.width) and  mouse[1] in range(MediumRect.y,MediumRect.y + MediumRect.height):
            MediumColour = RED
        else:
            MediumColour = WHITE
        #end if
        Hard = font2.render('HARD', True, HardColour)
        HardRect = Hard.get_rect()
        HardRect.center = (size[0] // 2, 530) 
        screen.blit(Hard, HardRect) 
        if mouse[0]in range(HardRect.x,HardRect.x + HardRect.width) and  mouse[1] in range(HardRect.y,HardRect.y + HardRect.height):
            HardColour = RED
        else:
            HardColour = WHITE
        #end if
        for i in range(5):
            circle_x[i] += round(direction_x[i])
            circle_y[i] += round(direction_y[i])
            if circle_y[i] > 705:
                direction_y[i] *= -1
            elif circle_y[i] < 15:
                direction_y[i] *= -1
            elif circle_x[i] < 15:
                direction_x[i] *= -1
            elif circle_x[i] > 1265:
                direction_x[i] *= -1
            #endif
            pygame.draw.circle(screen, WHITE, (circle_x[i],circle_y[i]), 15)
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
    font = pygame.font.Font('freesansbold.ttf', 100) 
    font2 = pygame.font.Font('freesansbold.ttf',20)
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
                MessageRect.center = (size[0] // 2, 620) 
                screen.blit(Message, MessageRect) 
                pygame.display.flip()
            #endif
            count -= 1
            clock.tick(60)
    #endwhile
#end procedure
def outputhighscore(num):
    f = open('highscore.txt','wt')
    f.write(str(num))
    f.close()
def gameplay(speed,paddle_height,mode,comp_speed,refresh):
    #initialise variables
    left_x = 30
    left_y = 340
    right_x = 1226
    right_y = 340
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
    font = pygame.font.Font('freesansbold.ttf', 100)
    font2 = pygame.font.Font('freesansbold.ttf',80)
    font3 = pygame.font.Font('freesansbold.ttf',40)
    f = open('highscore.txt','rt')
    highscore = int(f.read())
    f.close
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
            circle_x = 1240
            direction_x *= -1
        #endif
        circle_y = random.randint(5,700)
        if score1 > highscore:
            highscore = score1
            outputhighscore(highscore)
        elif score2 > highscore:
            highscore = score2
            outputhighscore(highscore)
        while not game_over and not game_end:
            # -- User input and controls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    elif event.key == pygame.K_p:
                        score2 += 1
                    elif event.key == pygame.K_t:
                        score1 += 1
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
                    PlayRect.center = (size[0] // 2, 300) 
                    screen.blit(Play, PlayRect) 
                    if mouse[0]in range(PlayRect.x,PlayRect.x + PlayRect.width) and  mouse[1] in range(PlayRect.y,PlayRect.y + PlayRect.height):
                        PlayColour = RED
                    else:
                        PlayColour = BLACK
                    #end if
                    Exit = font2.render('EXIT GAME', True, ExitColour)
                    ExitRect = Exit.get_rect()
                    ExitRect.center = (size[0] // 2, 370) 
                    screen.blit(Exit, ExitRect) 
                    if mouse[0]in range(ExitRect.x,ExitRect.x + ExitRect.width) and  mouse[1] in range(ExitRect.y,ExitRect.y + ExitRect.height):
                        ExitColour = RED
                    else:
                        ExitColour = BLACK
                    #endif
                    Restart = font2.render('MAIN MENU', True, RestartColour)
                    RestartRect = Restart.get_rect()
                    RestartRect.center = (size[0] // 2, 440) 
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
                if circle_x < 640:
                    if circle_y < left_y + (paddle_height//4):
                        left_y -= comp_speed
                    elif circle_y > left_y + (paddle_height) - (paddle_height//4):
                        left_y += comp_speed
                    #endif
                #endif
            #endif
            
            if left_y > size[1] - paddle_height - 5:
                left_y = (size[1] - paddle_height - 5) - 3
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
                if circle_x > 640:
                    if circle_y < right_y + (paddle_height//4):
                        right_y -= comp_speed
                    elif circle_y > right_y + (paddle_height) - (paddle_height//4):
                        right_y += comp_speed
                    #endif
                #endif
            #endif
            if right_y > size[1] - paddle_height - 5:
                right_y = (size[1] - paddle_height - 5) - 3
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
            if (circle_x < left_x + 40):
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
            if (circle_x > right_x - 15):
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

    
            if circle_y > 705:
                direction_y *= -1
            elif circle_y < 15:
                direction_y *= -1
            elif circle_x < 15:
                game_end = True
                score2 += 1
            elif circle_x > 1265:
                game_end = True
                score1 += 1
            #endif
            
            font2 = pygame.font.Font('freesansbold.ttf', 50) 
            Single1 = font2.render(str(score1), True, WHITE)
            Single1Rect = Single1.get_rect()
            Single1Rect.center = (100, 80) 
            screen.blit(Single1, Single1Rect)
            Single2 = font2.render(str(score2), True, WHITE)
            Single2Rect = Single2.get_rect()
            Single2Rect.center = (1180, 80) 
            screen.blit(Single2, Single2Rect)
            Single3 = font3.render(str(highscore), True, WHITE)
            Single3Rect = Single3.get_rect()
            Single3Rect.center = (size[0]//2, 80) 
            screen.blit(Single3, Single3Rect)

            pygame.draw.rect(screen, WHITE, (right_x, right_y, 24, paddle_height))
            pygame.draw.rect(screen, WHITE, (left_x, left_y, 24, paddle_height))
            pygame.draw.circle(screen, WHITE, (circle_x,circle_y), 15)

            pygame.display.flip()
            clock.tick(refresh)
        #endwhile
    #endwhile
#end procedure


# -- Initialise PyGame
pygame.init()
clock = pygame.time.Clock()

# -- Blank Screen
size = (1280,720)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption("Pong")

restart = False
while not restart:
    restart = True
    mode = Menu1()
    if mode == 'special':
        gameplay(13,130,'special',12,150)
    else:
        difficulty = Menu2()
        countdown(3)
        if difficulty == 'Easy':
            gameplay(7,160,mode,5,100)
        elif difficulty == 'Medium':
            gameplay(9,125,mode,8,120)
        elif difficulty == 'Hard':
            gameplay(12,125,mode,11,130)
        #end if
    #end if
#endwhile

pygame.quit()
