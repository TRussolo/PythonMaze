##########################
# Version: 0.1 29.11.2019#
##########################
#
# 29.11.2019 - v0.1 - TRussolo
#                     First version
#
#

import random

class Cell:
    """A cell in the maze.

    A maze "Cell" is a point in the grid which may be surrounded by walls to
    the north, east, south or west.

    """

    # A wall separates a pair of cells in the N-S or W-E directions.
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        """Initialize the cell at (x,y). At first it is surrounded by walls."""

        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def has_all_walls(self):
        """Does this cell still have all its walls?"""

        return all(self.walls.values())

class Maze:
    """A Maze, represented as a grid of cells."""

    def __init__(self, nx, ny, ix=0, iy=0):
        """Initialize the maze grid.
        The maze consists of nx x ny cells and will be constructed starting
        at the cell indexed at (ix, iy).

        """
        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy
        self.maze_map = [[Cell(x, y) for y in range(ny)] for x in range(nx)]
    
    # Return the area of the maze
    def calculate_area(self):
        return(self.nx*self.ny)
        
    def choose_dir():
        listOfDirs=['N','S','E','W']
        return random.choice(listOfDirs)
    
    def backtrack(self):
        coordOfDirections={'N':-1,'S':1,'E':-1,'W':1}
        # Choose random direction to test
        direction=choose_dir()
        
        # Check if the cell is allowed
        
        
        # Check if the chosen cell has been visited
        
        # Remove the wall
        
        # Move to new cell and mark it as visited
        
        # Add the cell to the list of moves
        
        

m=Maze(6,4)
