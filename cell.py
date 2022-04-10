from __future__ import annotations


class Cell:
    """A cell in the maze.
    
    This class represents a cell in the maze. It has a position, a
    g, h and f value, a parent and a list of walls.

    Attributes
    ----------
    x : int
        The x coordinate of the cell.
    y : int
        The y coordinate of the cell.
    g : int
        Cost of the path from the start cell.
    h : int
        Estimated cost of the cheapest path from the cell to the goal.
    f : int
        The sum of the g and h values.
    parent : Cell
        The parent cell of the current cell.
    walls : dict
        A dictionary of the walls of the cell.
    
    Methods
    -------
    carve(wall: str)
        Carve a wall in the cell.
    """

    def __init__(self, x, y) -> None:
        """Initialize a cell.
        
        Parameters
        ----------
        x : int
            The x coordinate of the cell.
        y : int
            The y coordinate of the cell.
        """
        self.x = x
        self.y = y

        self.g = self.h = self.f = 0
        self.parent = None

        self.walls = {'n': True, 's': True, 'e': True, 'w': True}
    
    def carve(self, wall: str) -> None:
        """Carve a wall in the cell."""
        self.walls[wall] = False
    
    def __eq__(self, __o: object) -> bool:
        """Compare the cell to another object.
        
        Parameters
        ----------
        __o : object
            The object to compare the cell to.
        
        Returns
        -------
        bool
            True if the cell is equal to the object, False otherwise.
        """
        if not isinstance(__o, Cell):
            return False
        
        return self.x == __o.x and self.y == __o.y
    
    def __hash__(self) -> int:
        """Get the hash of the cell.
        
        Returns
        -------
        int
            The hash of the cell.
        """
        return hash((self.x, self.y))
