from random import randint
Cscore = 0
Uscore= 0
userinput = 0
choice = ['rock','paper','scissors','finish']
def score():
    print('SCORE:')
    print('Computer:',Cscore,'Player:',Uscore,sep=' ')
#end procedure
    
def result(WinOrLose):
    print('The computer chose '+ choice[comp] + ', you '+ WinOrLose + ' !')
    score()
#end procedure

    
while userinput != -1:
    print('============================================================================') ### SRC - Do you need these print statements? could you have used the input below
    print('NEW ROUND: Enter rock, paper or scissors. Enter finish to end the game.')
    userinput = input() ### SRC - do you need str here?
    comp = randint(0,2)  ### SRC - meaningful variable names please!!!
    if userinput in choice:
        i = choice.index(userinput)
        if i == comp:
            print('The computer also chose '+ choice[i] + ' so you draw!')
            score()
        elif (i == 0 and comp == 1) or (i == 1 and comp == 2) or (i == 2 and comp == 0):
            Cscore += 1
            result('lose') 
        elif (i == 0 and comp == 2) or (i == 1 and comp == 0) or (i == 2 and comp == 1):
            Uscore += 1
            result('win')
        elif i == 3:
            print('Thanks for playing!')
            score()
            userinput = -1
    else:
        print('invalid input')
#endwhile


        


    
