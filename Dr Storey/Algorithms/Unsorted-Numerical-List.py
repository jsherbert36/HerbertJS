from FileIO import output_list
from random import randint
Num = int(input('How many numbers: '))
List = []
for i in range(Num):
    List.append(randint(0,10000))
output_list(List)
