from cell import Cell
from helpers import get_neighbours, carve_wall
from random import choice, randint


def dfs(width: int, height: int) -> list[list[Cell]]:
    """Generate a maze using depth-first search.
    
    1. Choose the initial cell, mark it as visited and push it to the stack.
    2. While the stack is not empty.
        1. Pop a cell from the stack and make it a current cell.
        2. If the current cell has any neighbours which have not been visited.
            1. Push the current cell to the stack.
            2. Choose one of the unvisited neighbours.
            3. Remove the wall between the current cell and the chosen cell.
            4. Mark the chosen cell as visited and push it to the stack.
    
    Parameters
    ----------
    width : int
        The width of the maze.
    height : int
        The height of the maze.
    cell : Cell
        The current cell.
    
    Returns
    -------
    list[list[Cell]]
        The maze.
    """
    maze = [[Cell(x, y) for x in range(width)] for y in range(height)]

    visited = set()
    stack = []

    initial_cell = maze[randint(0, height - 1)][randint(0, width - 1)]
    
    visited.add(initial_cell)
    stack.append(initial_cell)

    while stack:
        current_cell = stack.pop()
        neighbours = [neighbour for neighbour in get_neighbours(maze, current_cell) if neighbour not in visited]

        if neighbours:
            stack.append(current_cell)

            neighbour = choice(neighbours)
            carve_wall(current_cell, neighbour)
            
            visited.add(neighbour)
            stack.append(neighbour)
        
        yield maze, stack
    
    return maze


def prim(width: int, height: int) -> list[list[Cell]]:
    """Generate a maze using Prim's algorithm.
    
    1. Choose the initial cell, mark it as visited and add it's neighbours to the frontier.
    2. While the frontier set is not empty.
        1. Pop a cell from the frontier.
        2. Choose a random "in" neighbour.
        3. Carve a wall from the current cell to the neighbour.
        4. Mark the current cell as visited.
        5. Add any of it's "out" neighbours to the frontier.
    
    Parameters
    ----------
    width : int
        The width of the maze.
    height : int
        The height of the maze.
    cell : Cell
        The current cell.
    
    Returns
    -------
    list[list[Cell]]
        The maze.
    """
    maze = [[Cell(x, y) for x in range(width)] for y in range(height)]

    visited = set()
    frontier = set()

    initial_cell = maze[randint(0, height - 1)][randint(0, width - 1)]

    visited.add(initial_cell)
    frontier.update(get_neighbours(maze, initial_cell))

    while frontier:
        current_cell = choice(list(frontier))
        frontier.remove(current_cell)

        in_neighbours = [in_neighbour for in_neighbour in get_neighbours(maze, current_cell) if in_neighbour in visited]

        if in_neighbours:
            in_neighbour = choice(in_neighbours)
            carve_wall(current_cell, in_neighbour)
            
            visited.add(current_cell)
            frontier.update([out_neighbour for out_neighbour in get_neighbours(maze, current_cell) if out_neighbour not in visited])
        
        yield maze, frontier
    
    return maze
