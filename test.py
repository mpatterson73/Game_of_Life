from life import live_neighbors

if __name__ == "__main__":

    state = [[1, 1, 0], [0, 1, 0], [1, 1, 0]]
    cell = (1, 1)

    print(live_neighbors(state))
