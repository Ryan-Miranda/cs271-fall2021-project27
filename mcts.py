from node import Node
import random
import utils
import time

SIMULATION_DEPTH = 60


class MCTS:


    def __init__(self, X0, Y0, grid, walls, boxes, goals, boundaries, max_time=300) -> None:
        print('MCTS')
        self.root = Node(position=(X0, Y0), boxes=boxes, goals=goals, setBoxes=set())
        self.grid = grid
        self.walls = walls
        self.goals = goals
        self.initial_boxes = boxes
        self.boundaries = boundaries
        self.max_time = max_time


    def select(self, iter_count) -> Node:
        node = self.root
        explore = 0.5

        if iter_count > 10000:
            explore -= 0.1
        elif iter_count > 20000:
            explore -= 0.2
    
        while len(node.children) > 0:
            children = node.children
            max_val = max(children, key = lambda t: t.value(explore)).value(explore)
            max_nodes = [node for node in node.children if node.value(explore) == max_val]

            node = random.choice(max_nodes)

            if node.N == 0:
                return node

        if self.expand(node):
            node = random.choice(node.children)
        
        return node


    def expand(self, parent) -> bool:
        if utils.goalTest(parent.boxes, self.goals):
            return False
        else:
            parent.add_children(utils.generateChildren(parent, self.boundaries, self.walls))
            return True

    
    def simulate(self, node) -> int:
        # simulate moves until a certain depth and then return the manhattan distance
        # this is an approximation of returning the 'winner' from a state
        
        for _ in range(SIMULATION_DEPTH):

            if len(node.children) > 0:
                node = random.choice(node.children)

            else:
                break
        
        return utils.manhattanDistance(self.goals, node.boxes)


    def backpropagation(self, node, score) -> None:
        while node is not None:
            node.N += 1
            node.Q += score
            node = node.parent


    def best_move(self):
        max_val = max(self.root.children, key = lambda t: t.N).N
        max_nodes = [node for node in self.root.children if node.N == max_val]
        return random.choice(max_nodes)

    
    def search(self):
        start_time = time.time()
        num_simulations = 0
        node = self.root
        iter_count = 0

        while (time.time() - start_time) < self.max_time:
            iter_count += 1
            if iter_count % 5000 == 0:
                print(iter_count)

            node = self.select(iter_count)

            if utils.goalTest(node.boxes, self.goals):
                path, end_time = utils.return_path(node)
                return path, end_time - start_time, node
    
            score = self.simulate(node)
            self.backpropagation(node, score)
            num_simulations += 1
            self.root = self.best_move()

        print(f"Exiting after {(time.time() - start_time)/60}min. Iterations: {iter_count}")
        path, end_time = utils.return_path(node)
        return path, end_time - start_time, node
