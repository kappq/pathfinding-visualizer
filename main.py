"""Main Script.

This is the main file and allows the user to run the program. Here you
can change the maze generation algorithm, the pathfinding algorithm,
and the size of the maze.
"""

import pygame
from cell import Cell
from algorithm import AlgorithmType, MazeGenerationAlgorithm, PathFindingAlgorithm


pygame.init()

MAZE_GENERATION_ALGORITHM = MazeGenerationAlgorithm.DFS
PATH_FINDING_ALGORITHM = PathFindingAlgorithm.ASTAR

BLACK = 0x0A0908
WHITE = 0xF1FFE7
RED = 0xC1292E
GREEN = 0x63A46C
BLUE = 0x0E6BA8
YELLOW = 0xF1D302
CYAN = 0x5CC8FF
PINK = 0xEAC4D5
GREY = 0x596475

COLS = 25
ROWS = 15

SIZE = 20

WIDTH, HEIGHT = (COLS * SIZE, ROWS * SIZE)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pathfinding Visualizer')


def draw_maze(
    maze: list[list[Cell]],
    start_cell: Cell = None,
    end_cell: Cell = None,
    path: list[Cell] = [],
    special_cells: Cell = set(),
    open_cells: set[Cell] = set(),
    closed_cells: set[Cell] = set(),
) -> None:
    """Draw the maze.
    
    Parameters
    ----------
    maze : list[list[Cell]]
        The maze to draw.
    path : list[Cell], optional
        The path to draw.
    current_cell : Cell, optional
        The current cell to draw.
    open_cells : set[Cell], optional
        The open cells to draw.
    closed_cells : set[Cell], optional
        The closed cells to draw.
    start_cell : Cell, optional
        The start cell to draw.
    end_cell : Cell, optional
        The end cell to draw.
    """
    for row in maze:
        for cell in row:
            if all(cell.walls.values()):
                pygame.draw.rect(window, GREY, (cell.x * SIZE, cell.y * SIZE, SIZE, SIZE))
            else:
                pygame.draw.rect(window, WHITE, (cell.x * SIZE, cell.y * SIZE, SIZE, SIZE))
            
            if cell == start_cell:
                pygame.draw.rect(window, RED, (cell.x * SIZE, cell.y * SIZE, SIZE, SIZE))
            elif cell == end_cell:
                pygame.draw.rect(window, GREEN, (cell.x * SIZE, cell.y * SIZE, SIZE, SIZE))
            elif cell in special_cells:
                pygame.draw.rect(window, PINK, (cell.x * SIZE, cell.y * SIZE, SIZE, SIZE))
            elif cell in path:
                pygame.draw.rect(window, YELLOW, (cell.x * SIZE, cell.y * SIZE, SIZE, SIZE))
            elif cell in open_cells:
                pygame.draw.rect(window, CYAN, (cell.x * SIZE, cell.y * SIZE, SIZE, SIZE))
            elif cell in closed_cells:
                pygame.draw.rect(window, BLUE, (cell.x * SIZE, cell.y * SIZE, SIZE, SIZE))
            
            if cell.walls['n']:
                pygame.draw.line(window, BLACK, (cell.x * SIZE, cell.y * SIZE), (cell.x * SIZE + SIZE, cell.y * SIZE))
            if cell.walls['s']:
                pygame.draw.line(window, BLACK, (cell.x * SIZE, cell.y * SIZE + SIZE), (cell.x * SIZE + SIZE, cell.y * SIZE + SIZE))
            if cell.walls['e']:
                pygame.draw.line(window, BLACK, (cell.x * SIZE + SIZE, cell.y * SIZE), (cell.x * SIZE + SIZE, cell.y * SIZE + SIZE))
            if cell.walls['w']:
                pygame.draw.line(window, BLACK, (cell.x * SIZE, cell.y * SIZE), (cell.x * SIZE, cell.y * SIZE + SIZE))


def main() -> None:
    """Main function.
    
    This is the main function of the program. It is the entry point of
    the program. It is responsible for the main loop of the program.
    It starts the pygame window and generates the maze. It then runs the
    pathfinding algorithm and draws the path.
    """
    algorithm = None
    algorithm_type = None

    maze = [[Cell(x, y) for x in range(COLS)] for y in range(ROWS)]
    path = []

    start_cell = Cell(0, 0)
    end_cell = Cell(COLS - 1, ROWS - 1)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_m:
                            algorithm = MAZE_GENERATION_ALGORITHM(COLS, ROWS)
                            algorithm_type = AlgorithmType.MAZE_GENERATION
                        case pygame.K_p:
                            algorithm = PATH_FINDING_ALGORITHM(COLS, ROWS)
                            algorithm_type = AlgorithmType.PATH_FINDING

        if algorithm and algorithm_type == AlgorithmType.MAZE_GENERATION:
            try:
                maze, special_cells = next(algorithm)
                draw_maze(maze, special_cells=special_cells)
            except StopIteration as e:
                maze = e.value
                algorithm = None
        elif algorithm and algorithm_type == AlgorithmType.PATH_FINDING:
            try:
                maze, open_cells, closed_cells = next(algorithm)
                draw_maze(maze, open_cells=open_cells, closed_cells=closed_cells, start_cell=start_cell, end_cell=end_cell)
            except StopIteration as e:
                path = e.value
                algorithm = None
        else:
            draw_maze(maze, start_cell, end_cell, path)
        
        pygame.display.update()


if __name__ == '__main__':
    main()
