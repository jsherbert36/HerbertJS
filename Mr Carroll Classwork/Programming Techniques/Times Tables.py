
table = -1
answer = 'C'
Rows = -1 ### SRC - I added this line
def entertable():
    global table,Rows  ### SRC - No globals please!!!
    while table == -1:
        table = input("Enter which times table you want from 1 to 20: ")
        if table.isdigit() and Rows not in range(1,21):
            table = int(table)
        else:
            print('Try again next time!')
        Rows = input('Enter how many rows you want: ')
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
