# Conway's Game of Life Program
# A system of cells that liv on a grid,
# where they live and die, and also evolve
# based on rules that dictate their world.

import numpy as np

def dead_state(width=5, height=5):
    # Create a board of declared width and height
    # with all cells initialized to dead.
    board = np.zeros((height,width),dtype=int)
    return board


print(dead_state(10,5))

