def NumberSum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + NumberSum(numbers[1:])
    #endif
#end function


N = [3,6,2,8,1,5,6,3,2,234,2346,54,2,2346,8,5,4,32,2,4,5,6,364364]
print(NumberSum(N))
