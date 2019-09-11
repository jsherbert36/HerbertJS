table,answer = -1,'N'
while (table < 1 or table > 20):
    print("Enter which times table you want from 1 to 20")
    try:
        table = int(input())
    except typeerror:
        print('Please enter an integer next time')
    print('Enter how many rows you want:')
    try:
        rows = int(input())
    except typeerror:
        print('Please enter an integer next time')
#endwhile
print("You entered the ",table," for ",rows," rows"
[print(i*int(table)) for i in range(int(rows))]
