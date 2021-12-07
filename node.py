import math

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

        # fields for MCTS
        self.N = 0
        self.Q = 0
        self.children = []


    def add_children(self, children):
        self.children += children


    def value(self, explore = 0.5):
        # calculates UCT value of the node, used in MCTS
        if self.N == 0:
            return 0 if explore == 0 else float('inf')
        else:
            return self.Q / self.N + explore * (2 * math.log(self.parent.N) / self.N) ** 0.5


    def __eq__(self, other):
        return self.position == other.position and self.f == other.f and self.move == other.move \
            and self.boxes == other.boxes


    def __str__(self) -> str:
        return f'{self.position} g:{self.g} h:{self.h} f:{self.f} {self.move}'
