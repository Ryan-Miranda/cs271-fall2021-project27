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


if __name__ == '__main__':
    M, N, wallSquares, boxes, storageLocations, X0, Y0 = readInput()
    grid = buildGrid(M, N, wallSquares, boxes, storageLocations, X0, Y0)
    printGrid(grid)