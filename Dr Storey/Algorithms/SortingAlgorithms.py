import random,time,sys,os,json
def insertionsort(num_list):
    for i in range(1,len(num_list)):
        next = num_list[i]
        while i > 0 and num_list[i-1] > next:
            num_list[i] = num_list[i-1]
            i -= 1
        num_list[i] = next
    return(num_list)

def bubblesort(List):
    n = len(List)
    for i in range(n):
        for j in range(0, n - i -1):
            if List[j] > List[j + 1]:
                List[j], List[j+1] = List[j+1],List[j]
    return List

def quicksort(List,low = 0,high = ''):
    if high == '':
        high = len(List) - 1
    if low < high:
        Q,List = partition(List,low,high)
        quicksort(List,low,Q-1)
        quicksort(List,Q+1,high)
    return List

def partition(List,low,high):
    pivot = List[high]
    i = low 
    for j in range(low,high):
        if List[j] <= pivot:
            List[i],List[j] = List[j],List[i]
            i += 1
    List[i],List[high] = List[high],List[i]
    return i,List

def mergesort(List):
    n = len(List)
    if n <= 1:
        return List
    Left = []
    Right = []
    for i in range(n):
        if i < n//2:
            Left.append(List[i])
        else:
            Right.append(List[i])
    Left = mergesort(Left)
    Right = mergesort(Right)
    return merge(Left,Right)

def merge(Left,Right):
    Result = []
    while Left and Right:
        if Left[0] <= Right[0]:
            Result.append(Left[0])
            Left = Left[1:]
        else:
            Result.append(Right[0])
            Right = Right[1:]
    while Left:
        Result.append(Left[0])
        Left = Left[1:]
    while Right:
        Result.append(Right[0])
        Right = Right[1:]
    return Result

def JacobSort(num_list):
    n = len(num_list)
    RUN = 32
    List,Rest = [],[]
    if n > RUN*2:
        X = n//RUN
        if X%2 == 1:
            X = (X-1)*32
        else:
            X *= 32
        for i in range(0,X-1,RUN):
            List += insertionsort(num_list[i:i+RUN])
    else:
        X = 0
    if n!= X:
        Rest = insertionsort(num_list[X:])
    size = RUN
    while size < X:
        Temp = []
        for LeftIndex in range(0,X-3,2*size):
            MidIndex = LeftIndex + size -1
            RightIndex = LeftIndex + (2*size) 
            Left = List[LeftIndex:MidIndex+1]
            Right = List[MidIndex+1:RightIndex]
            Temp += merge(Left,Right)
        List = Temp
        size *= 2
    final = merge(List,Rest)
    return final

def input_list(name = ''):
    finish = False
    while finish == False:
        if name == '':
            file = input("Please enter the input file name i.e input.json: ")
        else:
            file = str(name)
        try:
            f = open(file,"rt")
            finish = True
        except FileNotFoundError:
            print('File not found - try again')
            name = ''
    return (json.load(f))
    f.close()

def output_list(List):
    file = input("Please enter the .json output file name: ")    
    f = open(file,"wt")        
    json.dump(List, f)
    f.close()

if __name__ == "__main__":
    arr = input_list()
    assert type(arr) == list
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Choose which sorting algorithm to use:\n',
          'QuickSort\n','Bubble Sort\n','Insertion Sort\n','MergeSort\n',
          'JacobSort',sep = '')
    Type = input()
    Type = ''.join([i for i in Type if i.isalpha()])
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Sorting...')
    sys.setrecursionlimit(2500)
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        if Type.upper() in 'QUICKSORT':
            new_list = quicksort(arr)
        elif Type.upper() in 'BUBBLESORT':
            new_list = bubblesort(arr)
        elif Type.upper() in 'INSERTIONSORT':
            new_list = bubblesort(arr)
        elif Type.upper() in 'MERGESORT':
            new_list = mergesort(arr)
        elif Type.upper() in 'JACOBSORT':
            new_list = JacobSort(arr)
        elif Type.upper() == 'X':
            new_list = sorted(arr)
        else:
            print('Invalid Input')
            time.sleep(20)
        os.system('cls' if os.name == 'nt' else 'clear')
        output_list(new_list)
    else:
        print('List is already sorted')
        time.sleep(5)
    



