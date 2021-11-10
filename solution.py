def read_input():
    M, N = input().split(' ')

    wallSquares = getCoordinates( input().split(' ') )
    boxes = getCoordinates( input().split(' ') )
    storageLocations = getCoordinates( input().split(' ') )

    X0, Y0 = input().split(' ')

    return M, N, wallSquares, boxes, storageLocations, X0, Y0


def getCoordinates(inputList):
    inputList = [int(coord) for coord in inputList]
    coords = []
    for i in range(1, inputList[0] * 2, 2 ):
        coords.append( (inputList[i], inputList[i+1]) )
    return coords


if __name__ == '__main__':
    M, N, wallSquares, boxes, storageLocations, X0, Y0 = read_input()

    print(M, N)
    print(wallSquares)
    print(storageLocations)
    print(boxes)
    print(X0, Y0)
