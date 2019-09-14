table,answer = -1,'C'
def entertable():
    global table,Rows
    while table != -1:
        print("Enter which times table you want from 1 to 20")
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

