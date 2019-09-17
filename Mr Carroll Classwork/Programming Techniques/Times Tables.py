#<<<<<<< HEAD
### SRC - Where has the line above come from?
table,answer = -1,'C'
Rows = -1 ### SRC - I added this line
def entertable():
    global table,Rows  ### SRC - No globals please!!!
    while table != -1:
        print("Enter which times table you want from 1 to 20") ### SRC - you can put the output text in your input statement
        table = input()
        if table.isdigit() and rows not in range(1,21):
            table = int(table)
        else:
            print('Try again next time!')
        print('Enter how many rows you want:')
        Rows = input()
        if Rows.isdigit() and Rows not in range(1,31):
            Rows = int(Rows)
        else:
            print('Try again next time!')
            continue
    #endwhile
entertable()
print("Did you enter the "+str(table)+" times table for "+str(Rows)+" rows")
print("If yes, type 'Yes', if no, type 'No'")
answer = input()
if answer == 'Yes':
    [print(i*table) for i in range(Rows)]
    answer = 'X'
else:
    entertable()

#=======
table,answer = -1,'N'
while (table < 1 or table > 20):
    print("Enter which times table you want from 1 to 20")
    try:
        table = int(input())
    except valueerror:
        print('Please enter an integer next time')
    print('Enter how many rows you want:')
    try:
        rows = int(input())
    except valueerror:
        print('Please enter an integer next time')
#endwhile
print("You entered the ",table," for ",rows," rows")
[print(i*int(table)) for i in range(int(rows))]  ### Can you do this as a standard for loop please.


#>>>>>>> 2cce926b124b281edd9b8c34d98353b513e8ed36
