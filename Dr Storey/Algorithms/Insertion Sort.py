from FileIO import input_list,output_list
num_list = input_list()
n = len(num_list)
if n > 1000:
    print('Elements Sorted: ',end='')
for j in range(1,n):
    next = num_list[j]
    i = j-1
    if j % 1000 == 0:
        print(j,' ',end='')
    while i >= 0 and num_list[i] > next:
        num_list[i + 1] = num_list[i]
        i = i-1
    #endwhile
    num_list[i+1] = next
#next j 
print()
output_list(num_list)
