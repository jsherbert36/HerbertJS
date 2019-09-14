from random import randint
from sys import exit
Cscore,Uscore,userinput,choice = 0,0,0,['rock','paper','scissors','finish']
def score():
    print('SCORE:')
    print('Computer:',Cscore,'Player:',Uscore,sep=' ')
def result(WinOrLose):
    print('The computer chose '+ choice[j] + ', you '+ WinOrLose + ' !')
    score()
while userinput != -1:
    print('============================================================================')
    print('NEW ROUND: Enter rock, paper or scissors. Enter finish to end the game.')
    userinput = str(input())
    j = randint(0,2)
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

        


    
