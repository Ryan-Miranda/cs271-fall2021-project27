class Node:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self) -> str:
        return f'{self.pos} g:{self.g} h:{self.h} f:{self.f}'


def return_path(current, grid):
    path = []
    M, N = (len(grid), len(grid[0]))
    result = [[-1 for i in range(N)] for j in range(M)]

    while current is not None:
        path.append(current.position)
        current = current.parent
    
    path = path[::-1]
    start_value = 0

    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1

    return result


def search(grid, cost, start, end):
    start_node = Node(position=tuple(start))
    end_node = Node(position=tuple(end))

    frontier = [start_node]  
    visited = [] 

    outer_iterations = 0
    max_iterations = (len(grid) // 2) ** 10

    move  =  [[-1, 0 ], # up
              [ 0, -1], # left
              [ 1, 0 ], # down
              [ 0, 1 ]] # right

    M, N = (len(grid), len(grid[0]))
    
    while len(frontier) > 0:
        outer_iterations += 1    

        current_node = frontier[0]
        current_index = 0
        for index, item in enumerate(frontier):
            if item.f < current_node.f:
                current_node = item
                current_index = index
                
        if outer_iterations > max_iterations:
            print ("giving up on pathfinding, too many iterations")
            return return_path(current_node,grid)

        frontier.pop(current_index)
        visited.append(current_node)

        if current_node == end_node:
            return return_path(current_node,grid)

        children = []

        for new_position in move: 
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if inGrid(grid, node_position[0], node_position[1]) and not isWall(grid, node_position[0], node_position[1]):
                new_node = Node(current_node, node_position)
                children.append(new_node)

        for child in children:
            
            if child not in visited:

                child.g = current_node.g + cost
                child.h = euclid(child.position[0], child.position[1], end_node.position[0], end_node.position[1])
                child.f = child.g + child.h

                if len([i for i in frontier if child == i and child.g > i.g]) > 0:
                    continue

                frontier.append(child)


def euclid(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def inGrid(grid, i, j):
    return i > -1 and i < len(grid) and j > -1 and j < len(grid[0])

def isWall(grid, i, j):
    return grid[i][j] == '#'

def isBox(grid, i, j):
    return grid[i][j] == '$'
    
def isStorage(grid, i, j):
    return grid[i][j] == '.'

def printPath(path):
    for i in range(len(path)):
        for j in range(len(path[0])):
            print(f'{path[i][j]: 02}', end = ' ')
        print()


if __name__ == '__main__':
    grid = [[0, '#', 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, '#', 0, '#', 0, 0],
            [0, '#', 0, 0, '#', 0],
            [0, 0, 0, 0, '#', 0]]
    
    start = [0, 0] # starting position
    end = [4,5] # ending position
    cost = 1 # cost per movement

    path = search(grid,cost, start, end)
    printPath(path)