# Conway's Game of Life Program
# A system of cells that liv on a grid,
# where they live and die, and also evolve
# based on rules that dictate their world.

import numpy as np
from os import name, system


def dead_state(width=5, height=5):
    # Create a board of declared width and height
    # with all cells initialized to dead.
    state = np.zeros((height, width), dtype=int)
    return state


def random_state(width=5, height=5):
    # state = dead_state(width, height)
    s = (height, width)
    state = np.random.sample(size=s)
    for row in state:
        for i, num in enumerate(row):
            if num >= 0.5:
                num = 0
            else:
                num = 1
            row[i] = int(num)
    return state


# take a grid of cell states & render a board with ascii chars
def render(state, on_str="#", off_str=" "):
    border = "-" * len(state[0])
    print("-" + border + "-")
    for row in state:
        row = [on_str if n == 1 else off_str for n in row]
        row = "".join(str(n) for n in row)
        print("|" + row + "|")
    print("-" + border + "-")
    return


def live_neighbors(state):
    live_count = 0
    cell = state[1][1]
    for row in range(3):
        for col in range(3):
            if state[row][col] == 1:
                live_count += 1
    if cell == 1:
        return live_count - 1
    else:
        return live_count


width = 5
height = 5
board_state = random_state(width, height)
system("cls" if name == "nt" else "clear")
# render(board_state)
# print(board_state)
