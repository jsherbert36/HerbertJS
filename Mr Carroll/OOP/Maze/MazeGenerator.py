import numpy,FileIO
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
                    Node_List.append((x,y))
                elif neighbours[0] ^ neighbours[1] and neighbours[2] ^ neighbours[3]:
                    Node_List.append((x,y))
    return Node_List


def move(direction,plane):
    while Maze[y][x] != 1:
        if plane == 'vertical':
            y += direction
        else:
            x += direction
        CurrentNode = [x,y]
        if CurrentNode in Nodes:
            Node_Dict[Node].append(CurrentNode)
    y = Node[1]
    x = Node[0]
    CurrentNode = Node
    
def getConnections(Maze,Nodes):
    Nodes = [tuple(i) for i in Nodes]
    Node_Dict = [[] for i in range(len(Nodes))]   #Node_Dict is a dictionary of list of lists of coordinates, keys are also lists of coordinates
    for i in range(len(Nodes)):
        CurrentNode = Nodes[i]
        x = Nodes[i][0]
        y = Nodes[i][1]
        if Maze[y-1][x]== 0:
            while Maze[y][x] != 1:
                y -= 1
                CurrentNode = [x,y]
                if CurrentNode in Nodes:
                    Node_Dict[i].append(CurrentNode)
            y = Nodes[i][1]
            CurrentNode = Nodes[i]
        if Maze[y+1][x]== 0: 
            while Maze[y][x] != 1:
                y += 1
                CurrentNode = [x,y]
                if CurrentNode in Nodes:
                    Node_Dict[i].append(CurrentNode)
            y = Nodes[i][1]
            CurrentNode = Nodes[i]
        if Maze[y][x-1]== 0: 
            while Maze[y][x] != 1:
                x -= 1
                CurrentNode = [x,y]
                if CurrentNode in Nodes:
                    Node_Dict[i].append(CurrentNode)
            x = Nodes[i][0]
            CurrentNode = Nodes[i]
        if Maze[y][x+1] == 0:
            while Maze[y][x] != 1:
                x += 1
                CurrentNode = [x,y]
                if CurrentNode in Nodes:
                    Node_Dict[i].append(CurrentNode)
            x = Nodes[i][0]
            CurrentNode = Nodes[i]
    return Node_Dict
maze = FileIO.input_list('test_maze.json')
nodes = FileIO.input_list('nodes.json')
FileIO.output_list(getConnections(maze,nodes))
