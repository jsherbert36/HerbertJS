### SRC - Excellent work
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
    CircleSize = 17
    CenterX = size[0]//2
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
        PongRect.center = (CenterX, size[1] // 3) 
        screen.blit(Pong, PongRect) 
        mouse = pygame.mouse.get_pos()      
        Single = font2.render('SINGLEPLAYER', True, SingleColour)
        SingleRect = Single.get_rect()
        SingleRect.center = (CenterX, size[1] // 2) 
        screen.blit(Single, SingleRect) 
        if SingleRect.collidepoint(mouse):    
            SingleColour = RED
        else:
            SingleColour = WHITE  
        #endif
        Multi = font2.render('MULTIPLAYER', True, MultiColour)
        MultiRect = Multi.get_rect()
        MultiRect.center = (CenterX, int(size[1] // 1.7)) 
        screen.blit(Multi, MultiRect) 
        if MultiRect.collidepoint(mouse):
            MultiColour = RED
        else:
            MultiColour = WHITE
        #endif
        Score = font2.render('SCOREBOARD', True, ScoreColour)
        ScoreRect = Score.get_rect()
        ScoreRect.center = (CenterX, int(size[1] // 1.46)) 
        screen.blit(Score, ScoreRect) 
        if ScoreRect.collidepoint(mouse):
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
        MessageRect.center = (CenterX, int(size[1]//1.2)) 
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
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if SingleRect.collidepoint(mouse):
                        choice = True
                        return 'single'
                    elif MultiRect.collidepoint(mouse):
                        choice = True
                        return 'multi'
                    elif ScoreRect.collidepoint(mouse):
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
    font = pygame.font.Font('freesansbold.ttf', size[0]//15) 
    font2 = pygame.font.Font('freesansbold.ttf',size[0]//20)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (204,0,0)
    CenterX = size[0]//2
    circlesize = 17
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
        DifficultyRect.center = (CenterX, int(size[1]//2.88)) 
        screen.blit(Difficulty, DifficultyRect) 
        mouse = pygame.mouse.get_pos()    
        
        Easy = font2.render('EASY', True, EasyColour)
        EasyRect = Easy.get_rect()
        EasyRect.center = (CenterX, int(size[1]//1.94)) 
        screen.blit(Easy, EasyRect) 
        if EasyRect.collidepoint(mouse):
            EasyColour = RED
        else:
            EasyColour = WHITE      
        #end if
        Medium = font2.render('MEDIUM', True, MediumColour)
        MediumRect = Medium.get_rect()
        MediumRect.center = (CenterX, int(size[1]//1.6)) 
        screen.blit(Medium, MediumRect) 
        if MediumRect.collidepoint(mouse):
            MediumColour = RED
        else:
            MediumColour = WHITE
        #end if
        Hard = font2.render('HARD', True, HardColour)
        HardRect = Hard.get_rect()
        HardRect.center = (CenterX, int(size[1]//1.35)) 
        screen.blit(Hard, HardRect) 
        if HardRect.collidepoint(mouse):
            HardColour = RED
        else:
            HardColour = WHITE
        #end if
        for i in range(5):
            circle_x[i] += round(direction_x[i])
            circle_y[i] += round(direction_y[i])
            if circle_y[i] > size[1] - circlesize:
                direction_y[i] *= -1
            elif circle_y[i] < circlesize:
                direction_y[i] *= -1
            elif circle_x[i] < circlesize:
                direction_x[i] *= -1
            elif circle_x[i] > size[0] - circlesize:
                direction_x[i] *= -1
            #endif
            pygame.draw.circle(screen, WHITE, (circle_x[i],circle_y[i]), circlesize)
        #next i
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if EasyRect.collidepoint(mouse):
                        choice = True
                        return 'Easy'
                    elif MediumRect.collidepoint(mouse):
                        choice = True
                        return 'Medium'
                    elif HardRect.collidepoint(mouse):
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

    
def ScoreBoard():
    choice = False
    font = pygame.font.Font('freesansbold.ttf', size[0]//20) 
    font2 = pygame.font.Font('freesansbold.ttf',size[0]//25)
    font3 = pygame.font.Font('freesansbold.ttf',size[0]//30)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (204,0,0)
    CenterX = size[0]//2
    TextX = int(size[0] //3.6)
    circlesize = 15
    BackColour = WHITE
    global game_over
    circle_x = [90,200,600,1200,1100] 
    circle_y = [600,100,450,550,50]
    direction_x = [-8,2,7,8,-9]
    direction_y = [7,-8,10,-9,5]
    while not game_over and not choice:
        screen.fill(BLACK) 
        Scoreboard = font.render('SCOREBOARD', True, WHITE)
        ScoreboardRect = Scoreboard.get_rect()
        ScoreboardRect.center = (CenterX, int(size[1]//5)) 
        screen.blit(Scoreboard, ScoreboardRect) 
        
        f = open('highscore.txt','rt')
        highscore = f.read()
        f.close
        mouse = pygame.mouse.get_pos()      
        Score = font2.render('HIGHEST SCORE: ' + highscore , True, WHITE)
        ScoreRect = Score.get_rect()
        ScoreRect.center = (CenterX, int(size[1]//3)) 
        screen.blit(Score, ScoreRect) 
        
        s = open('highestrally.txt','rt')
        highrally = s.read()
        s.close
        Rally = font2.render('LONGEST RALLY: ' + highrally, True, WHITE)
        RallyRect = Rally.get_rect()
        RallyRect.topleft = (ScoreRect.left, ScoreRect.bottom + size[1]//30) 
        screen.blit(Rally, RallyRect) 

        p = open('mostrounds.txt','rt')
        mostrounds = p.read()
        p.close
        Round = font2.render('MOST ROUNDS: ' + mostrounds, True, WHITE)
        RoundRect = Round.get_rect()
        RoundRect.topleft = (ScoreRect.left, RallyRect.bottom + size[1]//30) 
        screen.blit(Round, RoundRect) 

        Back = font3.render('BACK', True, BackColour)
        BackRect = Back.get_rect()
        BackRect.topleft = (int(size[0]//10), size[1] - (size[1] // 7.2)) 
        screen.blit(Back, BackRect) 
        if BackRect.collidepoint(mouse):
            BackColour = RED
        else:
            BackColour = WHITE
        #end if

        for i in range(5):
            circle_x[i] += round(direction_x[i])
            circle_y[i] += round(direction_y[i])
            if circle_y[i] > size[1] - circlesize:
                direction_y[i] *= -1
            elif circle_y[i] < circlesize:
                direction_y[i] *= -1
            elif circle_x[i] < circlesize:
                direction_x[i] *= -1
            elif circle_x[i] > size[0] - circlesize:
                direction_x[i] *= -1
            #endif
            pygame.draw.circle(screen, WHITE, (circle_x[i],circle_y[i]), circlesize)
        #next i
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if BackRect.collidepoint(mouse):
                        choice = True
                        global restart
                        restart = False
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
    CenterX = size[0]//2
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
                SingleRect.center = (CenterX, size[1] // 2) 
                screen.blit(Single, SingleRect) 
                Message = font2.render('PRESS SPACEBAR TO PAUSE/EXIT', True, WHITE)
                MessageRect = Message.get_rect()
                MessageRect.center = (CenterX, 620) 
                screen.blit(Message, MessageRect) 
                pygame.display.flip()
            #endif
            count -= 1
            clock.tick(60)
    #endwhile
#end procedure
def outputscore(num,filename):
    f = open(filename,'wt')
    f.write(str(num))
    f.close()

def gameplay(speed,paddle_height,mode,comp_speed,refresh):
    #initialise variables
    paddlewidth = 24
    left_x = int(size[0]//42.6)
    left_y = size[1]//2
    right_x = size[0] - (int(size[0]//42.6))
    right_y = size[1]//2 - paddlewidth
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (204,0,0)
    GREEN = (8,184,6)
    circlesize = 17
    PlayColour = BLACK
    ExitColour = BLACK
    RestartColour = BLACK
    global game_over
    game_end = False
    score1 = 0
    score2 = 0
    currentrally = 0
    font = pygame.font.Font('freesansbold.ttf', int(size[1]//7.2))
    font2 = pygame.font.Font('freesansbold.ttf',int(size[1]//14.4))
    font3 = pygame.font.Font('freesansbold.ttf',int(size[1]//23))
    f = open('highscore.txt','rt')
    highscore = int(f.read())
    f.close
    p = open('mostrounds.txt','rt')
    mostrounds = int(p.read())
    p.close
    roundcount = 0
    while not game_over:
        if game_end:
                clock.tick(1)   
        #endif
        game_end = False
        direction_x = speed 
        direction_y = speed
        count = 0
        roundcount += 1
        if (score1 + score2) % 2 == 0:
            circle_x = 100
        else:
            circle_x = size[0] - 100
            direction_x *= -1
        #endif
        circle_y = random.randint(5,size[1]-30)
        if score1 > highscore:
            highscore = score1
            outputscore(highscore,'highscore.txt')
        elif score2 > highscore:
            highscore = score2
            outputscore(highscore,'highscore.txt')
        s = open('highestrally.txt','rt')
        highrally = int(s.read())
        s.close
        if currentrally > highrally:
            outputscore(currentrally,'highestrally.txt')
        currentrally = 0
        while not game_over and not game_end:
            count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if roundcount > mostrounds:
                        outputscore(roundcount,'mostrounds.txt')
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if roundcount > mostrounds:
                            outputscore(roundcount,'mostrounds.txt')
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
                    PlayRect.center = (size[0] // 2, int(size[1]//2.4)) 
                    screen.blit(Play, PlayRect) 
                    if PlayRect.collidepoint(mouse):
                        PlayColour = RED
                    else:
                        PlayColour = BLACK
                    #end if
                    Exit = font2.render('EXIT GAME', True, ExitColour)
                    ExitRect = Exit.get_rect()
                    ExitRect.center = (size[0] // 2, int(size[1]//1.95)) 
                    screen.blit(Exit, ExitRect) 
                    if ExitRect.collidepoint(mouse):
                        ExitColour = RED
                    else:
                        ExitColour = BLACK
                    #endif
                    Restart = font2.render('MAIN MENU', True, RestartColour)
                    RestartRect = Restart.get_rect()
                    RestartRect.center = (size[0] // 2, int(size[1]//1.63)) 
                    screen.blit(Restart, RestartRect) 
                    if RestartRect.collidepoint(mouse):
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
                            if PlayRect.collidepoint(mouse):
                                Continue = True
                            elif ExitRect.collidepoint(mouse):
                                if roundcount > mostrounds:
                                    outputscore(roundcount,'mostrounds.txt')
                                game_over = True
                            elif RestartRect.collidepoint(mouse):
                                if roundcount > mostrounds:
                                    outputscore(roundcount,'mostrounds.txt')
                                global restart
                                restart = False
                                game_over = True
                            #endif
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                if roundcount > mostrounds:
                                    outputscore(roundcount,'mostrounds.txt')
                                game_over = True
                                Continue = True
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
                if circle_x < size[0]//2:
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
                currentrally = 0
                if circle_x > size[0]//2:
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
            if (circle_x < left_x + paddlewidth + circlesize + 5):
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
            if (circle_x > right_x - circlesize):
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
            if count > 20 and circle_x > right_x - circlesize: 
                if circle_y < paddle_height + right_y and circle_y > right_y:
                    currentrally += 1
                    count = 0
            if count > 20 and circle_x < left_x + circlesize + paddlewidth + 6: 
                if circle_y < paddle_height + left_y and circle_y > left_y:
                    currentrally += 1
                    count = 0
            #endif

    
            if circle_y > size[1] - circlesize:
                direction_y *= -1
            elif circle_y < circlesize:
                direction_y *= -1
            elif circle_x < circlesize:
                game_end = True
                score2 += 1
            elif circle_x > size[0] - circlesize:
                game_end = True
                score1 += 1
            #endif 
            Single1 = font2.render(str(score1), True, WHITE)
            Single1Rect = Single1.get_rect()
            Single1Rect.center = (paddlewidth + 70, 80) 
            screen.blit(Single1, Single1Rect)
            Single2 = font2.render(str(score2), True, WHITE)
            Single2Rect = Single2.get_rect()
            Single2Rect.center = (size[0] - paddlewidth - 70, 80) 
            screen.blit(Single2, Single2Rect)
            if currentrally > highrally:
                rallycolour = GREEN
            else:
                rallycolour = WHITE
            if currentrally > 5:
                Rally = font3.render('RALLY: ' + (str(currentrally)), True, rallycolour)
                RallyRect = Rally.get_rect()
                RallyRect.center = (size[0]//2, 80) 
                screen.blit(Rally, RallyRect)

            pygame.draw.rect(screen, WHITE, (right_x, right_y, paddlewidth, paddle_height))
            pygame.draw.rect(screen, WHITE, (left_x, left_y, paddlewidth, paddle_height))
            pygame.draw.circle(screen, WHITE, (circle_x,circle_y), circlesize)

            pygame.display.flip()
            clock.tick(refresh)
        #endwhile
    #endwhile
#end procedure


# -- Initialise PyGame
pygame.init()
clock = pygame.time.Clock()

# -- Blank Screen
infoObject = pygame.display.Info()
size = (infoObject.current_w, infoObject.current_h)
size2 = (1280,720)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

pygame.display.set_caption("Pong")

restart = False
while not restart:
    restart = True
    mode = Menu1()
    if mode == 'special':
        gameplay(13,130,'special',12,150)
    elif mode == 'score':
        ScoreBoard()
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
