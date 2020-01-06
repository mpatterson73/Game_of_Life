# Conway's Game of Life Program
# A system of cells that liv on a grid,
# where they live and die, and also evolve
# based on rules that dictate their world.

import numpy as np

def get_state

def dead_state(width=5, height=5):
    # Create a board of declared width and height
    # with all cells initialized to dead.
    state_grid = np.zeros((height,width),dtype=int)
    return state_grid

def random_state(width=10, height=5):
    #board = dead_state(width, height)
    s = (height, width)
    state_grid = np.random.sample(size=s)
    state_grid[]
    return state_grid
    
def render(state):
    # take a grid of cell states & render a board

    return


print(random_state(10,5))

