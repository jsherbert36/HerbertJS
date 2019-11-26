import numpy,FileIO
from numpy.random import randint as rand
def generate_maze(width=81, height=51, density=.75, complexity=.75):
    # Only odd dimensions
    dimension = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (dimension[0] + dimension[1])))  # Number of components
    density = int(density * ((dimension[0] // 2) * (dimension[1] // 2)))  # Size of components
    Z = numpy.zeros(dimension, dtype=bool)
    # Make paths/walls
    for i in range(density):
        x = rand(0, dimension[1] // 2) * 2
        y = rand(0, dimension[0] // 2) * 2 
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
width = 1000//15
height = 700//15
Maze_List = (generate_maze(width,height,10)).tolist()
FileIO.output_list(Maze_List)
