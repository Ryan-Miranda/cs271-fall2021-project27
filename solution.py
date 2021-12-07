import sys

import process_input
import a_star
import mcts


if __name__ == '__main__':
    file_num = None
    if len(sys.argv) > 1:
        file_num = sys.argv[1]
        
    # M, N, wallSquares, boxes, storageLocations, X0, Y0 = process_input.from_stdin()
    M, N, walls, boxes, goals, X0, Y0 = process_input.from_file(file_num)

    grid = process_input.build_grid(M, N, walls, boxes, goals, X0, Y0)
    print('\nInitial grid: ')
    process_input.print_grid(grid)

    boundaries = process_input.find_boundaries(walls)

    # agent = a_star.A_Star(X0, Y0, grid, set(walls), set(boxes), set(goals), boundaries)
    agent = mcts.MCTS(X0, Y0, grid, set(walls), set(boxes), set(goals), boundaries)

    path, boxes = agent.search()

    print(f'Final location of boxes: {boxes}')
    print(f'Goal locations: {goals}')
    print(f'Path: {path}')
    print()
