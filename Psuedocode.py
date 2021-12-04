class Node:

    """
        move: move taken by Agent to arrive here
        parent: parent Node

        fields:
        N: number of times this position was visited
        Q: average reward from this position
        children: list of child Nodes
    """

    def __init__(self, move, parent):
        pass

    def UCB1(C: float) -> float:
        return UCB1 with the inputted exploration/exploitation term C




def selection():
    node = root

    while not is not leaf:
        node = node with max UCB1

    expand node
    if node is not terminal:
        return one of the node's children
    
    return node


def expand(parent: Node, state: GameState) -> bool:
    """
    Generate the children of the passed "parent" node based on the available
    moves in the passed gamestate and add them to the tree.
    Returns:
        bool: returns false If node is leaf (the game has ended).
    """
    children = []
    if state.winner != GameMeta.PLAYERS['none']:
        # game is over at this node so nothing to expand
        return False

    for move in state.moves():
        children.append(Node(move, parent))

    parent.add_children(children)
    return True


def simulate(state) -> bool:
    get the available moves in the current state
    while state is not terminal:
        select a random move
        execute the move
        remove the move from the list of current moves
    
    return state is terminal


    moves = state.moves()  # Get a list of all possible moves in current state of the game

    while state.winner == GameMeta.PLAYERS['none']:
        move = choice(moves)
        state.play(move)
        moves.remove(move)

    return state.winner



@staticmethod
def backpropagate(node: Node, turn: int, outcome: int) -> None:
    while node is not None:
        node.N += 1
        node.Q += 1 if player 1 else 0
        node = node.parent


def search(self, time_budget: int) -> None:
    """
    Search and update the search tree for a
    specified amount of time in seconds.
    """
    start_time = clock()
    num_rollouts = 0

    # do until we exceed our time budget
    while we have not exceeded our time bound:
        node, state = self.select_node()
      
        winOrLoss = self.roll_out(state)
        self.backp(node, turn, outcome)
        num_rollouts += 1


    run_time = clock() - start_time
    node_count = self.tree_size()
    self.run_time = run_time
    self.node_count = node_count
    self.num_rollouts = num_rollouts