import pygame
import random
def InputName():
    clock = pygame.time.Clock()
    choice = False
    font = pygame.font.Font('freesansbold.ttf', size[1]//8) 
    font2 = pygame.font.Font('freesansbold.ttf',int(size[1]//14.4))
    font3 = pygame.font.Font('freesansbold.ttf',size[1]//36)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (204,0,0)
    BOXColour = BLACK
    CircleSize = 17
    CenterX = size[0]//2
    global game_over
    game_over = False
    Text = '_______'
    Active = False
    BackWidth = 10
    BackHeight = 10
    BOX_X = 30
    BOX_Y = 40
    TextColour = WHITE
    while not game_over and not choice:
        screen.fill(BLACK) 
        
        mouse = pygame.mouse.get_pos()
        Player1 = font2.render('PLAYER 1: ',True,WHITE)
        Player1Rect = Player1.get_rect()
        Player1Rect.x = 300
        Player1Rect.y = 300
        screen.blit(Player1,Player1Rect)
        BOXRect = pygame.draw.rect(screen, BOXColour, (BOX_X,BOX_Y, BackWidth, BackHeight))
        Score = font2.render(Text, True, TextColour)
        ScoreRect = Score.get_rect()
        ScoreRect.x = Player1Rect.x + Player1Rect.width
        ScoreRect.y = 300
        BOX_X = ScoreRect.x - 5
        BOX_Y = ScoreRect.y - 5
        screen.blit(Score, ScoreRect)
        BackWidth = ScoreRect.width + 10
        BackHeight = ScoreRect.height + 10
        
        
        if ScoreRect.collidepoint(mouse) or Active == True:
            BOXColour = WHITE
            TextColour = BLACK
        else:
            BOXColour = BLACK
            TextColour = WHITE
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    
                elif event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if BOXRect.collidepoint(mouse):
                        Active = True
                        
                if Active == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            Text = Text[:-1]
                        elif event.key == pygame.K_RETURN:
                            Active = False
                        else:
                            Text += (event.unicode).upper()
                    
                    #endif
                #end if
        #next event      
        clock.tick(90)
    #endwhile
#end procedure

pygame.init()
size = (1280,720)
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
InputName()
pygame.quit()




