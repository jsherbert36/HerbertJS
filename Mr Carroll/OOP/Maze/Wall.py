import FileIO,random,sys
def generate_wall(size,block_width):
    Wall_List = []
    Choose_List = ['P','W']
    for i in range(0,size[1],block_width):
        Wall_List.append([])
        for j in range(0,size[0],block_width):
            Wall_List[i].append(random.choice(Choose_List))
        #endfor
    #endfor
    FileIO.output_list()


