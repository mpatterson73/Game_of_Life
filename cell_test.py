from life import live_neighbors, new_cell_state
import numpy as np

if __name__ == "__main__":

    test1 = np.array([[1, 0, 0], [0, 0, 0], [1, 1, 0]])
    test2 = np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1]])
    test3 = np.array([[0, 1, 0], [0, 1, 0], [0, 0, 0]])
    test4 = np.array([[1, 1, 0], [0, 1, 0], [0, 1, 0]])

    answer1 = (3, 1)
    answer2 = (7, 0)
    answer3 = (1, 0)
    answer4 = (3, 1)

    test_list = [test1, test2, test3, test4]
    ans_list = [answer1, answer2, answer3, answer4]
    for test, ans in zip(test_list, ans_list):
        x = live_neighbors(test)
        y = new_cell_state(test)
        if (x, y) == ans:
            print("true")
        else:
            print("false")

