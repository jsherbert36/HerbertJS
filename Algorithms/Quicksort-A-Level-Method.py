def swap(j,p,list):
    temp = list[p]
    list[p] = list[j]
    list[j] = temp
    return p,j,list

def partition(list):
    p = 0
    j = len(list) -1
    while j != p:
        if j > p:
            if list[j] < list[p]:
                j,p,list = swap(j,p,list)
                j+=2
            j-=1
        elif j < p:
            if list[j] > list[p]:
                j,p,list = swap(j,p,list)
                j-=2
            j+=1
    return j,list
  
def quicksort(list):
    if len(list) > 1:
        P,list = partition(list) 
        return quicksort(list[:P]) + [list[P]] + quicksort(list[P+1:]) 
    else:
        return list

if __name__ == "__main__":
    arr = [6710, 4428, 4867, 6562, 1342, 9715, 1466, 2280, 8201]
    print(quicksort(arr))
    


