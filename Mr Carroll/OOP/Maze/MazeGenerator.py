import numpy,FileIO,math,heapq
from numpy.random import randint as rand
def generate(width=81, height=51, complexity=.75, density=.75):
    # Only odd dimensions
    dimension = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    complexity = int(complexity * (5 * (dimension[0] + dimension[1])))  # No. of blocks
    density = int(density * ((dimension[0] // 2) * (dimension[1] // 2)))  # Size of blocks
    Z = numpy.zeros(dimension, dtype = int)
    Z[0, :] = 1
    Z[-1, :] = 1
    Z[:, 0] = 1
    Z[:, -1] = 1
    for i in range(density):
        y = 2 * rand(0, dimension[0] // 2)
        x = 2 * rand(0, dimension[1] // 2) 
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:
                neighbours.append((y, x - 2))
            #end if
            if x < dimension[1] - 2:
                neighbours.append((y, x + 2))
            #endif
            if y > 1:
                neighbours.append((y - 2, x))
            #endif
            if y < dimension[0] - 2:
                neighbours.append((y + 2, x))
            #endif
            if len(neighbours):
                y_, x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
                #endif
            #endif
        #next j
    return Z

def getNodes(Maze):
    Node_List = []
    for y in range(len(Maze)):
        for x in range(len(Maze[y])):
            if Maze[y][x] == 0:
                neighbours = [0,0,0,0]                   #left,right,above,below
                if y > 0 and y < len(Maze)-1:
                    if Maze[y-1][x]== 0: neighbours[2] = 1
                    if Maze[y+1][x]== 0: neighbours[3] = 1
                if x > 0 and x < len(Maze[y])-1:
                    if Maze[y][x-1]== 0: neighbours[0] = 1
                    if Maze[y][x+1] == 0: neighbours[1] = 1
                if neighbours.count(1) > 2:
                    Node_List.append([x,y])
                elif neighbours[0] ^ neighbours[1] and neighbours[2] ^ neighbours[3]:
                    Node_List.append([x,y])
    return Node_List
    
def getConnections(Maze,Nodes):
    Adjacency_Vector = [[] for i in range(len(Nodes))]   #Adjacency_Vector is a list of lists of coordinates and weights
    for i in range(len(Nodes)):
        x = Nodes[i][0]
        y = Nodes[i][1]
        if Maze[y-1][x]== 0:
            Found = False
            count = 0
            while Maze[y][x] != 1 and Found == False:
                y -= 1
                count += 1
                if [x,y] in Nodes:
                    Adjacency_Vector[i].append([x,y,count])
                    Found = True
            y = Nodes[i][1]
            x = Nodes[i][0]
        if Maze[y+1][x]== 0:
            Found = False
            count = 0
            while Maze[y][x] != 1 and Found == False:
                y += 1
                count += 1
                if [x,y] in Nodes:
                    Adjacency_Vector[i].append([x,y,count])
                    Found = True
            y = Nodes[i][1]
            x = Nodes[i][0]
        if Maze[y][x-1]== 0:
            Found = False
            count = 0
            while Maze[y][x] != 1 and Found == False:
                x -= 1
                count += 1
                if [x,y] in Nodes:
                    Adjacency_Vector[i].append([x,y,count])
                    Found = True
            x = Nodes[i][0]
            y = Nodes[i][1]
        if Maze[y][x+1] == 0:
            Found = False
            while Maze[y][x] != 1 and Found == False:
                x += 1
                count += 1
                if [x,y] in Nodes:
                    Adjacency_Vector[i].append([x,y,count])
                    Found = True
            x = Nodes[i][0]
            y = Nodes[i][1]
    return Adjacency_Vector


maze = FileIO.input_list('Block15.json')
Node_List = getNodes(maze)
Connection_List = getConnections(maze,Node_List)
Connection_Dict = {tuple(i):[] for i in Node_List}
for i in range(len(Connection_List)):
    for j in Connection_List[i]:
        temp = tuple(Node_List[i])
        Connection_Dict[temp].append({(j[0],j[1]):j[2]})
print(Dijkstra(Connection_Dict,3))
