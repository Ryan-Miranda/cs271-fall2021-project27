import A_star
import sys

def readInputFromStdIn():
    M, N = [int(num) for num in input().split(' ')]

    wallSquares = getCoordinates( input().split(' ') )
    boxes = getCoordinates( input().split(' ') )
    storageLocations = getCoordinates( input().split(' ') )

    X0, Y0 = [int(num)-1 for num in input().split(' ')]

    return M, N, wallSquares, boxes, storageLocations, X0, Y0


def readInputFromFile(fileNum=None):
    directory = 'input_files/sokoban'

    if fileNum:
        file = open(directory + fileNum + '.txt')
    else:
        file = open(directory + '00.txt')

    M, N = [int(num) for num in file.readline().split(' ')]

    wallSquares = getCoordinates( file.readline().split(' ') )
    boxes = getCoordinates( file.readline().split(' ') )
    storageLocations = getCoordinates( file.readline().split(' ') )

    X0, Y0 = [int(num)-1 for num in file.readline().split(' ')]

    file.close()

    return M, N, wallSquares, boxes, storageLocations, X0, Y0


def getCoordinates(inputList):
    inputList = [int(coord) for coord in inputList]
    coords = []
    for i in range(1, inputList[0] * 2, 2 ):
        coords.append( (inputList[i] - 1, inputList[i+1] - 1) )
    return coords


def buildGrid(M, N, wallSquares=0, boxes=0, storageLocations=0, X0=0, Y0=0): 
    grid = [ [' ' for j in range(N)] for i in range(M) ]

    # (1, 1) at top left of grid, we do a simple conversion by subtracting 1 from every index
    
    for i, j in wallSquares:
        grid[i][j] = '#'
    for i, j in boxes:
        grid[i][j] = '$'
    for i, j in storageLocations:
        grid[i][j] = '.'
    grid[X0][Y0] = '@'

    return grid


def printGrid(grid):
    print()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = ' ')
        print()
    print()


if __name__ == '__main__':
    fileNum = None
    if len(sys.argv) > 1:
        fileNum = sys.argv[1]
        
    # M, N, wallSquares, boxes, storageLocations, X0, Y0 = readInputFromStdIn()

    M, N, wallSquares, boxes, storageLocations, X0, Y0 = readInputFromFile(fileNum)

    grid = buildGrid(M, N, wallSquares, boxes, storageLocations, X0, Y0)
    print('\nInitial grid: ')
    printGrid(grid)

    A_star.doSearch(grid, wallSquares, boxes, storageLocations, X0, Y0)