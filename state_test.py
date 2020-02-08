from life import random_state, get_next_state
import numpy as np

if __name__ == "__main__":
    test_state = np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1]])
    print(test_state)
    next_state = get_next_state(test_state)
    print(next_state)
    third_state = get_next_state(next_state)
    print(third_state)

