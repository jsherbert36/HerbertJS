Num = int(input("Please input a number: "))
def fib1(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fib1(n - 2) + fib1(n - 1)
#end function
my_list = []
def fib2(n):
    global my_list
    my_list.append(1)
    my_list.append(1)
    for i in range(2,n):
        my_list.append((my_list[i-1] + my_list[i-2]))
    #next
    [print(i,end=' ') for i in my_list]   
#end procedure

print(fib1(Num))
fib2(Num)
