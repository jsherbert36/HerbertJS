from random import randint
from sys import exit
Cscore,Uscore,userinput,choice = 0,0,0,['rock','paper','scissors','finish']  ### SRC - I really don't like multiple assignments!
def score():
    print('SCORE:')
    print('Computer:',Cscore,'Player:',Uscore,sep=' ')
### SRC - I'd like to see an end procedure here
    
def result(WinOrLose):
    print('The computer chose '+ choice[j] + ', you '+ WinOrLose + ' !')
    score()

    
while userinput != -1:
    print('============================================================================') ### SRC - Do you need these print statements? could you have used the input below
    print('NEW ROUND: Enter rock, paper or scissors. Enter finish to end the game.')
    userinput = str(input()) ### SRC - do you need str here?
    j = randint(0,2)  ### SRC - meaningful variable names please!!!
    if userinput in choice:
        i = choice.index(userinput)
        if i == j:
            print('The computer also chose '+ choice[i] + ' so you draw!')
            score()
        elif (i == 0 and j == 1) or (i == 1 and j == 2) or (i == 2 and j == 0):
            Cscore += 1
            result('lose') 
        elif (i == 0 and j == 2) or (i == 1 and j == 0) or (i == 2 and j == 1):
            Uscore += 1
            result('win')
        elif i == 3:
            print('Thanks for playing!')
            score()
            userinput = -1
    else:
        print('invalid input')

        


    
