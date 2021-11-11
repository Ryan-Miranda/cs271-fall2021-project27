def readInput():
    M, N = [int(num) for num in input().split(' ')]

    wallSquares = getCoordinates( input().split(' ') )
    boxes = getCoordinates( input().split(' ') )
    storageLocations = getCoordinates( input().split(' ') )

    X0, Y0 = [int(num) for num in input().split(' ')]

    return M, N, wallSquares, boxes, storageLocations, X0, Y0


def getCoordinates(inputList):
    inputList = [int(coord) for coord in inputList]
    coords = []
    for i in range(1, inputList[0] * 2, 2 ):
        coords.append( (inputList[i], inputList[i+1]) )
    return coords


def buildGrid(M, N, wallSquares=0, boxes=0, storageLocations=0, X0=0, Y0=0): 
    grid = [ [' ' for j in range(N)] for i in range(M) ]

    # (1, 1) at top left of grid, we do a simple conversion by subtracting 1 from every index
    
    for i, j in wallSquares:
        grid[i-1][j-1] = '#'
    for i, j in boxes:
        grid[i-1][j-1] = '$'
    for i, j in storageLocations:
        grid[i-1][j-1] = '.'
    grid[X0-1][Y0-1] = '@'

    return grid

def printGrid(grid):
    print()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = ' ')
        print()
    print()

def dfs_iterative(grid, start):
    stack = []
    stack.append(start)
    visited = set()
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.extend(grid[v] - visited)
            #for neighbor in v.neighbors:
            #for neighbor in grid[v]:
                #stack.append(neighbor)

def find_path(row_i, col_j, grid):
    """"
    Maze-finding algorithm:
    Push all paths from the point on which you are standing on a stack.
    While the stack is not empty
        Pop a path from the stack.
        Follow the path until you reach an exit, intersection, or dead end.
        If you found an exit
            Congratulations!
        Else if you found an intersection
            Push all paths meeting at the intersection, except the current one, onto the stack.
    """
    # If cell is out of bounds
    stack, path = ([] for i in range(2))
    grid_size = sum(len(row) for row in grid)
    # TODO

def is_out_of_bounds(row_i, col_j, M, N):
    if (row_i < 1 or row_i > M or col_j < 1 or col_j > N):
        return True
    return False

if __name__ == '__main__':
    M, N, wallSquares, boxes, storageLocations, X0, Y0 = readInput()
    grid = buildGrid(M, N, wallSquares, boxes, storageLocations, X0, Y0)
    printGrid(grid)
    #printGrid(grid[X0 - 1][Y0 - 1])

       