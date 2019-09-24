# Basic function to calculate factorials recursively
def Factorial1(Num):
    if Num == 0:
        return 1
    else:
        return Num * Factorial1(Num - 1)
    #endif
#end function

# function to calculate factorials iteratively (without recursion)
def Factorial2(Num):
    if Num == 0:
        return 1
    else:
        total = 1 
        for i in range(1,Num + 1):
            total *= i
        return total 
    #endif
#end function 


# procedure to calculate factorials
def factorial3(Num):
    def fact(Num):
        if Num == 0:
            return 1
        else:
            return Num * Factorial1(Num - 1)
        #endif
    #endprocedure
    print (fact(Num))
#end procedure


Number = int(input('Enter a number: '))
print(Factorial1(Number))
print(Factorial2(Number))
factorial3(Number)