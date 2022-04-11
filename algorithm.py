from enum import Enum
from maze_generation import dfs, prim
from path_finding import astar, dijkstra


class AlgorithmType(Enum):
    """Algorithm Type.
    
    This is the type of algorithm to use.
    """
    MAZE_GENERATION = 1
    PATH_FINDING = 2


class MazeGenerationAlgorithm(Enum):
    """Maze generation algorithms.

    This enum contains the different maze generation algorithms.
    """
    DFS = dfs
    PRIM = prim


class PathFindingAlgorithm(Enum):
    """Path finding algorithms.

    This enum contains the different path finding algorithms.
    """
    ASTAR = astar
    DIJKSTRA = dijkstra
