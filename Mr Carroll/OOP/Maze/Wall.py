import FileIO,random,sys
def generate_wall(size,block_width):
    Wall_List = []
    Choose_List = [1,0,0]
    for i in range(0,size[1],block_width):
        Temp_List = []
        for j in range(0,size[0],block_width):
            Temp_List.append(random.choice(Choose_List))
        #endfor
        Wall_List.append(Temp_List)
    #endfor
    FileIO.output_list(Wall_List)

size = input('Enter the size of the blocks: ')
generate_wall((1000,700),int(size))
