from FileIO import input_list, output_list
num_list = input_list()
n = len(num_list)
if n > 1000:
    print('Elements Sorted:',end='')
for i in range(n- 1):
    if i % 1000 == 0:
        print(i,' ',end='')
    for j in range(n - i -1):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j+1] = num_list[j+1],num_list[j]
        #endif
    #next j
#next i
print()
output_list(num_list)
