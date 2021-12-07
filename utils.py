from node import Node

MOVES = {'U': [-1, 0], 'L': [0, -1], 'D': [1, 0], 'R': [0, 1]}

def generateChildren(current_node, boundaries, walls):
    children = []

    for move in MOVES:
        new_position = MOVES[move]
        node_position = (
            current_node.position[0] + new_position[0],
            current_node.position[1] + new_position[1]
        )
        newBoxes = current_node.boxes

        if inGrid(node_position, boundaries) and not isWall(node_position, walls):

            if isBox(node_position, newBoxes):

                boxNewPosition = (
                    node_position[0] + new_position[0],
                    node_position[1] + new_position[1]
                )

                # if the box's new position is valid
                if inGrid(boxNewPosition, boundaries) and not isWall(boxNewPosition, walls):

                    # if we push a box, the new position will be the same as current_position, but there will be a new g, f, h assoc with this state
                    newBoxes = updateBoxLocation(newBoxes, node_position, boxNewPosition)
                    node_position = current_node.position

                else:
                    continue

            new_node = Node(current_node, node_position, move, newBoxes)
            children.append(new_node)

    return children


def inGrid(position, boundaries):
    return position[1] >= boundaries[0] and position[1] <= boundaries[1] and position[0] >= boundaries[2] \
        and position[0] <= boundaries[3]


def isBox(position, boxes):
    return position in boxes


def isWall(position, walls):
    return position in walls


def isStorage(position, goals):
    return position in goals


def updateBoxLocation(boxes, oldBoxPosition, newBoxPosition):
    copy_boxes = set(boxes)
    copy_boxes.remove(oldBoxPosition)
    copy_boxes.add(newBoxPosition)
    return copy_boxes


def euclid(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def goalTest(boxes, goals):
    # if the set of goal coords = set of box coords, every box is in some goal and the game is finished
    return set(boxes) == set(goals)


def manhattanDistance(goals, boxes):
    boxes_copy = list(boxes)
    dist = 0

    for goal in goals:
        box, d = min([(b, calcManhattan(b, goal))
                    for b in boxes_copy], key=lambda t: t[1])
        dist += d
        boxes_copy.remove(box)

    return dist


def calcManhattan(box, goal):
    return abs(box[0] - goal[0]) + abs(box[1] - goal[1])


def return_path(node):
    path = []

    while node is not None:
        path.append((node.position, node.move))
        node = node.parent

    path = path[::-1]
    return path


def printPath(path):
    for i in range(len(path)):
        for j in range(len(path[0])):
            print(f'{path[i][j]: 02}', end=' ')
        print()
