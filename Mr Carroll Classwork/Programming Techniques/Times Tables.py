table,rows = -1,-1
while table == -1 and rows == -1:
    print("what table?")
    table = input()
    print("How many rows?")
    rows = input()
[print(i*int(table)) for i in range(int(rows))]
