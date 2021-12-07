def from_stdin():
    M, N = [int(num) for num in input().split(' ')]

    wallSquares = get_coordinates(input().split(' '))
    boxes = get_coordinates(input().split(' '))
    storageLocations = get_coordinates(input().split(' '))

    X0, Y0 = [int(num)-1 for num in input().split(' ')]

    return M, N, wallSquares, boxes, storageLocations, X0, Y0


def from_file(fileNum=None):
    directory = 'input_files/sokoban'

    if fileNum:
        file = open(directory + fileNum + '.txt')
    else:
        file = open(directory + '02.txt')

    M, N = [int(num) for num in file.readline().split(' ')]

    wallSquares = get_coordinates(file.readline().split(' '))
    boxes = get_coordinates(file.readline().split(' '))
    storageLocations = get_coordinates(file.readline().split(' '))

    X0, Y0 = [int(num)-1 for num in file.readline().split(' ')]

    file.close()

    return M, N, wallSquares, boxes, storageLocations, X0, Y0


def get_coordinates(inputList):
    inputList = [int(coord) for coord in inputList]
    coords = []
    for i in range(1, inputList[0] * 2, 2):
        coords.append((inputList[i] - 1, inputList[i+1] - 1))
    return coords


def build_grid(M, N, wallSquares=0, boxes=0, storageLocations=0, X0=0, Y0=0):
    grid = [[' ' for j in range(N)] for i in range(M)]

    # (1, 1) at top left of grid, we do a simple conversion by subtracting 1 from every index

    for i, j in wallSquares:
        grid[i][j] = '#'
    for i, j in boxes:
        grid[i][j] = '$'
    for i, j in storageLocations:
        grid[i][j] = '.'
    grid[X0][Y0] = '@'

    return grid


def print_grid(grid):
    print()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=' ')
        print()
    print()


def find_boundaries(walls):
    sorted_walls = sorted(walls, key=lambda t: t[1])
    left_bound = sorted_walls[0][1]
    right_bound = sorted_walls[-1][1]

    sorted_walls = sorted(walls, key=lambda t: t[0])
    top_bound = sorted_walls[0][0]
    bottom_bound = sorted_walls[-1][0]

    return (left_bound, right_bound, top_bound, bottom_bound)
