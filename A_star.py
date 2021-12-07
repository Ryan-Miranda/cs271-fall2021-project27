from node import Node
import utils

class A_Star:

    def __init__(self, X0, Y0, grid, walls, boxes, goals, boundaries, cost=1) -> None:
        self.start = (X0, Y0)
        self.grid = grid
        self.walls = walls
        self.boxes = boxes
        self.goals = goals
        self.boundaries = boundaries
        self.cost = cost


    def search(self):
        start_node = Node(position=tuple(self.start), boxes=self.boxes)

        frontier = [start_node]  
        visited = [] 

        outer_iterations = 0
        max_iterations = (len(self.grid) // 2) ** 10
        
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
                return utils.return_path(current_node), current_node.boxes

            frontier.pop(current_index)
            visited.append(current_node)

            if utils.goalTest(current_node.boxes, self.goals):
                return utils.return_path(current_node), current_node.boxes

            children = utils.generateChildren(current_node, self.boundaries, self.walls)

            for child in children:
                
                if child not in visited:

                    child.g = current_node.g + self.cost
                    child.h = utils.manhattanDistance(self.goals, child.boxes)
                    child.f = child.g + child.h

                    if len([i for i in frontier if child == i and child.g > i.g]) > 0:
                        continue

                    frontier.append(child)
