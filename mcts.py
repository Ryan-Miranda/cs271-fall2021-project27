# Disclaimer: this doesn't work in all cases. If MCTS gets stuck exploring nodes that look good based on simulations,
# the search can hit dead ends. This is bc in actual MCTS, states are simulated until a 'winner' is reached. We
# can't do that, since a 'winner' would essentially be a winning state, which is what we're trying to find.
# Therefore, if you see that the code fails on sokoban02.txt for example, keep run it again until it succeeds
# (should not take more than 4 - 5 runs).
# 
# This means we need to implement a way to do some backtracking, maybe go back up the tree when we notice Manhattan
# distance has been increasing for awhile, but I'm not sure exactly.

from node import Node
import random
import utils

SIMULATION_DEPTH = 40
NUM_ITERATIONS = 1000


class MCTS:


    def __init__(self, X0, Y0, grid, walls, boxes, goals, boundaries) -> None:
        self.root = Node(position=(X0, Y0), boxes=boxes)
        self.grid = grid
        self.walls = walls
        self.goals = goals
        self.initial_boxes = boxes
        self.boundaries = boundaries


    def select(self) -> Node:
        node = self.root
        
        while len(node.children) > 0:
            children = node.children
            max_val = max(children, key = lambda t: t.value()).value()
            max_nodes = [node for node in node.children if node.value() == max_val]

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
        #simulate moves until a certain depth and then return the manhattan distance
        # this is an approximation of returning the 'winner' from a state
        
        for _ in range(SIMULATION_DEPTH):

            # a check might be needed to see if the node has been visited or not?
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
        num_simulations = 0

        for _ in range(NUM_ITERATIONS):
            node = self.select()

            if utils.goalTest(node.boxes, self.goals):
                return utils.return_path(node), node.boxes

            score = self.simulate(node)
            self.backpropagation(node, score)
            num_simulations += 1
            self.root = self.best_move()

        print("NO SOLUTION FOUND")
        return None, None
