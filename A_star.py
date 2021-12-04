import copy

class Node:

    # Node contains parent node, position in the grid, what move was taken to get here, 
    # list of box positions at that point in time, cost (g), manhattan dist (h), and 
    # f (g + h)

    def __init__(self, parent=None, position=None, move=None, boxes=None):
        self.parent = parent
        self.position = position
        self.move = move
        self.boxes = boxes

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position and self.f == other.f and self.move == other.move and self.boxes == other.boxes

    def __str__(self) -> str:
        return f'{self.position} g:{self.g} h:{self.h} f:{self.f} {self.move}'


def return_path(current, grid):
    path = []
    M, N = (len(grid), len(grid[0]))
    result = [[-1 for i in range(N)] for j in range(M)]

    while current is not None:
        path.append((current.position, current.move))
        current = current.parent
    
    path = path[::-1]
    return path

    # builds a grid based on the path? uneeded for now
    start_value = 0

    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1

    return result


def search(grid, cost, start, walls, boxes, goals):
    start_node = Node(position=tuple(start), boxes=boxes)

    frontier = [start_node]  
    visited = [] 

    outer_iterations = 0
    max_iterations = (len(grid) // 2) ** 10

    moves  =  {'U': [-1, 0 ], 'L': [ 0, -1], 'D': [ 1, 0 ], 'R': [ 0, 1 ]} 
    M, N = (len(grid), len(grid[0]))
    
    while len(frontier) > 0:
        outer_iterations += 1    

        if outer_iterations % 1000 == 0:
            print(outer_iterations)

        current_node = frontier[0]
        current_index = 0
        for index, item in enumerate(frontier):
            if item.f < current_node.f:
                current_node = item
                current_index = index
                
        if outer_iterations > max_iterations:
            print ("giving up on pathfinding, too many iterations")
            return return_path(current_node,grid), current_node.boxes

        frontier.pop(current_index)
        visited.append(current_node)

        if goalTest(current_node.boxes, goals):
            return return_path(current_node,grid), current_node.boxes

        children = []

        for move in moves: 
            new_position = moves[move]
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            newBoxes = current_node.boxes

            if inGrid(grid, node_position) and not isWall(walls, node_position):

                if isBox(newBoxes, node_position):

                    # the new position of the box is just new_position x 2 (in the same direction)
                    boxNewPosition = (node_position[0] + new_position[0], node_position[1] + new_position[1])

                    # if the box's new position is valid
                    if inGrid(grid, boxNewPosition) and not isWall(walls, boxNewPosition):

                        # if we push a box, the new position will be the same as current_position, but there will be a new g, f, h assoc with this state
                        newBoxes = updateBoxLocation(newBoxes, node_position, boxNewPosition)
                        node_position = current_node.position

                    else:
                        continue
                
                new_node = Node(current_node, node_position, move, newBoxes)
                children.append(new_node)

        for child in children:
            
            if child not in visited:

                child.g = current_node.g + cost
                child.h = manhattanDistance(goals, child.boxes)
                child.f = child.g + child.h

                if len([i for i in frontier if child == i and child.g > i.g]) > 0:
                    continue

                frontier.append(child)

    # if goalTest(boxes, goals):
    #     return return_path(current_node,grid)
    # else:
    #     print('ERROR: no goal found but exiting anyway??')


def goalTest(boxes, goals):
    # if the set of goal coords = set of box coords, every box is in some goal and the game is finished
    return set(boxes) == set(goals)


def updateBoxLocation(boxes, oldBoxPosition, newBoxPosition):
    copy_boxes = copy.deepcopy(boxes)
    copy_boxes.remove(oldBoxPosition)
    copy_boxes.add(newBoxPosition)
    return copy_boxes


def manhattanDistance(goals, boxes):
    boxes_copy = list(boxes)
    dist = 0

    for goal in goals: 
        box, d = min( [(b, calcManhattan(b, goal)) for b in boxes_copy], key=lambda t: t[1] )
        dist += d
        boxes_copy.remove(box)
    
    return dist

def calcManhattan(box, goal):
    return abs(box[0] - goal[0]) + abs(box[1] - goal[1])


def inGrid(grid, position):
    return position[0] > -1 and position[0] < len(grid) and position[1] > -1 and position[1] < len(grid[0])

def isWall(walls, position):
    return position in walls

def isBox(boxes, position):
    return position in boxes

def isStorage(goals, position):
    return position in goals


def euclid(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def printPath(path):
    for i in range(len(path)):
        for j in range(len(path[0])):
            print(f'{path[i][j]: 02}', end = ' ')
        print()


def doSearch(grid, walls, boxes, goals, X0, Y0):
    start = [X0, Y0]
    cost = 1 # cost per movement

    boxes = set(boxes)
    goals = set(goals)
    walls = set(walls)

    path, boxes = search(grid, cost, start, walls, boxes, goals)

    print(f'Final location of boxes: {boxes}')
    print(f'Goal locations: {goals}')
    print(f'Path: {path}')
    print()