from FileIO import input_list
import time
found = False
index = -1
Search_List = input_list()
first = 0
last = len(Search_List)
Elem_Sought = input('Enter the item you wish to find: ')
if Elem_Sought.isalpha():
    Elem_Sought = Elem_Sought.lower()
while first <= last and not found:
        midpoint = ((first + last)//2)
        if str(Search_List[midpoint]) == Elem_Sought:
            found = True
            index = midpoint
        elif str(Search_List[midpoint]) < Elem_Sought:
            first = midpoint + 1 
        else:
            last = midpoint - 1
        #endif
#endwhile
if found == False:
    print(Elem_Sought,'was not found',sep=' ')
else:
    print(Elem_Sought,'is at index:',index,sep=' ')
time.sleep(3)
