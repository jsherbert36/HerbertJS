from FileIO import input_list
index = -1
i = 0
found = False
Elem_Sought = input('Enter the item you wish to find: ')
if Elem_Sought.isalpha():
    Elem_Sought = Elem_Sought.lower()
Search_List = input_list()
while i < len(Search_List) and not found:
    if str(Search_List[i]) == Elem_Sought:
        index = i
        found = True
    #end if
    i += 1
#end while
if found == False:
    print(Elem_Sought,'was not found',sep=' ')
else:
    print(Elem_Sought,'is at index:',index,sep=' ')
