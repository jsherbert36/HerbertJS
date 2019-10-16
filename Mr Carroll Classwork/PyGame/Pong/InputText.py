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
    Text = 'TEST'
    Active = False
    BackWidth = 10
    BackHeight = 10
    while not game_over and not choice:
        screen.fill(BLACK) 
        
        mouse = pygame.mouse.get_pos()      
        BOXRect = pygame.draw.rect(screen, BOXColour, (CenterX,size[1]//2, BackWidth, BackHeight))
        BOXRect.center = (CenterX,size[1]//2)
        Score = font2.render(Text, True, WHITE)
        ScoreRect = Score.get_rect()
        ScoreRect.center = (CenterX, size[1]//2) 
        screen.blit(Score, ScoreRect)
        BackWidth = ScoreRect.width + 10
        BackHeight = ScoreRect.height + 10
        
        
        if ScoreRect.collidepoint(mouse):
            BOXColour = WHITE
        else:
            BOXColour = BLACK
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    
                elif event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if ScoreRect.collidepoint(mouse):
                        Active = True
                        
                elif Active == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_RETURN:
                            Active = False
                        else:
                            Text += event.unicode
                    
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




