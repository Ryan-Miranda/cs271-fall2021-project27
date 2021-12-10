from node import Node
import utils
import time

class A_Star:

    def __init__(self, X0, Y0, grid, walls, boxes, goals, boundaries, cost=1, max_time=300) -> None:
        print('A* Search')
        self.start = (X0, Y0)
        self.grid = grid
        self.walls = walls
        self.boxes = boxes
        self.goals = goals
        self.boundaries = boundaries
        self.cost = cost
        self.max_time = max_time


    def search(self):
        start_time = time.time()

        start_node = Node(position=tuple(self.start), boxes=self.boxes, goals=self.goals, setBoxes=set())

        frontier = [start_node]  
        visited = [] 

        outer_iterations = 0
        max_iterations = (len(self.grid) // 2) ** 10
        
        while len(frontier) > 0:
            outer_iterations += 1    

            if outer_iterations % 5000 == 0:
                print(outer_iterations)

            current_node = frontier[0]
            current_index = 0
            for index, item in enumerate(frontier):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
                    
            if outer_iterations > max_iterations:
                print (f"giving up on pathfinding, too many iterations: {outer_iterations}")
                path, end_time = utils.return_path(current_node)
                return path, end_time - start_time, current_node

            if time.time() - start_time > self.max_time:
                print(f"giving up on pathfinding, longer than {self.max_time / 60}min. iterations: {outer_iterations}")
                path, end_time = utils.return_path(current_node)
                return path, end_time - start_time, current_node

            frontier.pop(current_index)
            visited.append(current_node)

            if utils.goalTest(current_node.boxes, self.goals):
                path, end_time = utils.return_path(current_node)
                return path, end_time - start_time, current_node.boxes

            children = utils.generateChildren(current_node, self.boundaries, self.walls)

            for child in children:
                
                if child not in visited:

                    child.g = current_node.g + self.cost
                    child.h = utils.manhattanDistance(child.goals, child.boxes)
                    child.f = child.g + child.h

                    if len([i for i in frontier if child == i and child.g > i.g]) > 0:
                        continue

                    frontier.append(child)
