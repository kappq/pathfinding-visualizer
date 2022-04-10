from cell import Cell
from helpers import reconstruct_path, get_neighbours, heuristic, are_connected


def astar(maze: list[list[Cell]], start_cell: Cell, end_cell: Cell) -> list[Cell]:
    """A* pathfinding algorithm.

    1. Add the start cell to the open list.
    2. While the open list is not empty.
        1. Get the cell with the lowest f score from the open list.
        2. Add the current cell to the closed list.
        3. If the current cell is the end cell, return the path.
        4. For each of the current cell's neighbours.
            1. If the neighbour is not walkable or is in the closed list, skip to the next neighbour.
            2. Calculate the new path to the neighbour through the current cell.
            3. If the neighbour is not in the open list or the new path to the neighbour is shorter than the old path.
                1. Set the neighbour's g score to the new path's g score.
                2. Calculate the neighbour's h score.
                3. Calculate the neighbour's f score.
                4. Set the neighbour's parent to the current cell.
                5. If the neighbour is not in the open list, add it to the open list.
    3. If no path is found, return an empty path.
    
    Parameters
    ----------
    maze : list[list[Cell]]
        The maze to find the path in.
    start_cell : Cell
        The cell to start the path from.
    end_cell : Cell
        The cell to end the path at.
    
    Returns
    -------
    list[Cell]
        The path from the start cell to the end cell.
    """
    open_cells = set()
    closed_cells = set()

    open_cells.add(start_cell)

    while len(open_cells) > 0:
        current_cell = min(open_cells, key=lambda cell: cell.f)

        open_cells.remove(current_cell)
        closed_cells.add(current_cell)

        if current_cell == end_cell:
            return reconstruct_path(current_cell)

        for neighbour in get_neighbours(maze, current_cell):
            if neighbour in closed_cells or not are_connected(current_cell, neighbour):
                continue

            new_g_score = current_cell.g + heuristic(neighbour, current_cell)

            if neighbour not in open_cells or new_g_score < neighbour.g:
                neighbour.g = new_g_score
                neighbour.h = heuristic(neighbour, end_cell)
                neighbour.f = neighbour.g + neighbour.h
                
                neighbour.parent = current_cell

                if neighbour not in open_cells:
                    open_cells.add(neighbour)
        
        yield maze, open_cells, closed_cells

    return []


def dijkstra(maze: list[list[Cell]], start_cell: Cell, end_cell: Cell) -> list[Cell]:
    """Dijkstra's algorithm.

    1. Add the start cell to the open list.
    2. While the open list is not empty.
        1. Get the cell with the lowest g score from the open list.
        2. Add the current cell to the closed list.
        3. If the current cell is the end cell, return the path.
        4. For each of the current cell's neighbours.
            1. If the neighbour is in the closed list or it is not walkable, skip to the next neighbour.
            2. If the neighbour is not in the open list or the new path to the neighbour is shorter than the old path.
                1. Set the neighbour's g score to the new path's g score.
                2. Set the neighbour's parent to the current cell.
                3. If the neighbour is not in the open list, add it to the open list.
    3. If no path is found, return an empty path.

    Parameters
    ----------
    maze : list[list[Cell]]
        The maze to find the path in.
    start_cell : Cell
        The cell to start the path from.
    end_cell : Cell
        The cell to end the path at.

    Returns
    -------
    list[Cell]
        The path from the start cell to the end cell.
    """
    open_cells = set()
    closed_cells = set()

    open_cells.add(start_cell)

    while len(open_cells) > 0:
        current_cell = min(open_cells, key=lambda cell: cell.g)

        open_cells.remove(current_cell)
        closed_cells.add(current_cell)

        if current_cell == end_cell:
            return reconstruct_path(current_cell)

        for neighbour in get_neighbours(maze, current_cell):
            if neighbour in closed_cells or not are_connected(current_cell, neighbour):
                continue
            
            new_g_score = current_cell.g + heuristic(neighbour, current_cell)

            if neighbour not in open_cells or new_g_score < neighbour.g:
                neighbour.g = new_g_score
                neighbour.parent = current_cell

                if neighbour not in open_cells:
                    open_cells.add(neighbour)

        yield maze, open_cells, closed_cells

    return []
