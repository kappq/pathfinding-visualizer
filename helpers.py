from cell import Cell


def carve_wall(cell: Cell, neighbour: Cell) -> None:
    """Carve a wall between two cells.
    
    Parameters
    ----------
    cell : Cell
        The cell to carve a wall from.
    neighbour : Cell
        The cell to carve a wall to.
    """
    if neighbour.x > cell.x:
        cell.walls['e'] = False
        neighbour.walls['w'] = False
    elif neighbour.x < cell.x:
        cell.walls['w'] = False
        neighbour.walls['e'] = False
    elif neighbour.y > cell.y:
        cell.walls['s'] = False
        neighbour.walls['n'] = False
    elif neighbour.y < cell.y:
        cell.walls['n'] = False
        neighbour.walls['s'] = False


def add_wall(cell: Cell, neighbour: Cell) -> None:
    """Add a wall between two cells.
    
    Parameters
    ----------
    cell : Cell
        The cell to add a wall from.
    neighbour : Cell
        The cell to add a wall to.
    """
    if neighbour.x > cell.x:
        cell.walls['e'] = True
        neighbour.walls['w'] = True
    elif neighbour.x < cell.x:
        cell.walls['w'] = True
        neighbour.walls['e'] = True
    elif neighbour.y > cell.y:
        cell.walls['s'] = True
        neighbour.walls['n'] = True
    elif neighbour.y < cell.y:
        cell.walls['n'] = True
        neighbour.walls['s'] = True


def are_connected(cell: Cell, neighbour: Cell) -> bool:
    """Check if two cells are connected.
    
    Parameters
    ----------
    cell : Cell
        The cell to check if it is connected to the neighbour.
    neighbour : Cell
        The neighbour to check if it is connected to the cell.
    
    Returns
    -------
    bool
        True if the two cells are connected, False otherwise.
    """
    if neighbour.x > cell.x:
        return not neighbour.walls['w']
    elif neighbour.x < cell.x:
        return not neighbour.walls['e']
    elif neighbour.y > cell.y:
        return not neighbour.walls['n']
    elif neighbour.y < cell.y:
        return not neighbour.walls['s']


def get_neighbours(maze: list[list[Cell]], cell: Cell) -> list[Cell]:
    """Get a list of the neighbours of a cell.
    
    Parameters
    ----------
    cell : Cell
        The cell to get the neighbours of.
    
    Returns
    -------
    list[Cell]
        A list of the neighbours of the cell.
    """
    neighbours = []
    
    if cell.x > 0:
        neighbours.append(maze[cell.y][cell.x - 1])
    if cell.x < len(maze[0]) - 1:
        neighbours.append(maze[cell.y][cell.x + 1])
    if cell.y > 0:
        neighbours.append(maze[cell.y - 1][cell.x])
    if cell.y < len(maze) - 1:
        neighbours.append(maze[cell.y + 1][cell.x])
    
    return neighbours


def reconstruct_path(current_cell: Cell) -> list[Cell]:
    """Reconstruct the path from the current cell to the start cell.
    
    Parameters
    ----------
    current_cell : Cell
        The current cell to reconstruct the path from.
    
    Returns
    -------
    list[Cell]
        The path from the current cell to the start cell.
    """
    path = []

    while current_cell:
        path.append(current_cell)
        current_cell = current_cell.parent
    
    return path[::-1]


def heuristic(a: Cell, b: Cell) -> int:
    """Calculate the heuristic between two cells.
    
    Parameters
    ----------
    a : Cell
        The first cell.
    b : Cell
        The second cell.
    
    Returns
    -------
    int
        The heuristic between the two cells.
    """
    return abs(a.x - b.x) + abs(a.y - b.y)
