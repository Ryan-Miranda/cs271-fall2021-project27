import sys

import process_input
import a_star
import mcts


if __name__ == '__main__':
    file_num = None
    benchmark = False
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == 'all':
            benchmark = True
        else:
            file_num = sys.argv[1]


    if benchmark:

        for i in range(1, 5):
            if i < 10:
                file_num = '0' + str(i)
            else:
                file_num = str(i)
            
            # M, N, wallSquares, boxes, storageLocations, X0, Y0 = process_input.from_stdin()
            M, N, walls, boxes, goals, X0, Y0 = process_input.from_file(file_num, 'input_files/benchmarks/sokoban-')

            grid = process_input.build_grid(M, N, walls, boxes, goals, X0, Y0)
            print('\nInitial grid: ')
            process_input.print_grid(grid)

            boundaries = process_input.find_boundaries(walls)

            agent = a_star.A_Star(X0, Y0, grid, set(walls), set(boxes), set(goals), boundaries, max_time=180)
            # agent = mcts.MCTS(X0, Y0, grid, set(walls), set(boxes), set(goals), boundaries, max_time=180)

            path, time_taken, end_node = agent.search()

            print(f'Final location of boxes: {end_node.setBoxes.union(end_node.boxes)}')
            print(f'Goal locations: {goals}')
            print(f'Path: {path if len(path) < 30 else set()}')
            print(f'Time elapsed: {time_taken}')
            print()
    
    else:
        M, N, walls, boxes, goals, X0, Y0 = process_input.from_file(file_num)

        grid = process_input.build_grid(M, N, walls, boxes, goals, X0, Y0)
        print('\nInitial grid: ')
        process_input.print_grid(grid)

        boundaries = process_input.find_boundaries(walls)

        agent = a_star.A_Star(X0, Y0, grid, set(walls), set(boxes), set(goals), boundaries)
        # agent = mcts.MCTS(X0, Y0, grid, set(walls), set(boxes), set(goals), boundaries)

        path, time_taken, end_node = agent.search()

        print(f'Final location of boxes: {boxes}')
        print(f'Goal locations: {goals}')
        print(f'Path: {path if len(path) < 30 else set()}')
        print(f'Time elapsed: {time_taken}')
        print()
