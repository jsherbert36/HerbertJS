import time
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 2) + fib_recursive(n - 1)
    #end if
#end function


def fib_iterative(n):  
    fibNumbers = [0,1]
    for i in range(2,n):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    #next i   
    return fibNumbers
#endfunction

num = int(input("Please input a number: "))
type = input("Enter recursive or iterative: ")

if type == 'recursive':
    print(fib_recursive(num))
elif type == 'iterative':  
    [print(i,end=' ') for i in fib_iterative(num)]
else:
    print("Invalid input")