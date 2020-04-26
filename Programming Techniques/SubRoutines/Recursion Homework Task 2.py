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
    startTime = time.time()
    print(fib_recursive(num))
    print(time.time() - startTime)
elif type == 'iterative':
    startTime = time.time()
    Number = fib_iterative(num)
    print(Number[-1])
    print(time.time() - startTime)
else:
    print("Invalid input")
