from life import random_state, get_next_state
import numpy as np

if __name__ == "__main__":
    test_state1 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    test_state2 = [[1, 1, 1], [0, 0, 1], [1, 1, 1]]
    test_state3 = np.array([[1, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0]])

    correct_state1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    correct_state2 = [[0, 1, 1], [0, 0, 0], [0, 1, 1]]
    correct_state3 = [[0, 1, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0]]

    # test for shape & state from get_next_state to match
    test_list = [test_state1, test_state2, test_state3]
    correct_list = [correct_state1, correct_state2, correct_state3]
    print(type(test_state1))
    for t, c in zip(test_list, correct_list):
        next_state = get_next_state(np.array(t))
        if np.array_equal(next_state, c):
            print("Correct")
        else:
            print("Incorrect!!")
            print("Expected: " + c)
            print("Returned: " + next_state)

