import numpy as np

from .services import MatrixA, MatrixB


class Controller:
    def __init__(self, players_num):
        self.players_num = players_num

    def get_optimal_points(self):
        return self.get_solution().tolist()

    def get_optimal_point(self):
        x = self.get_solution()

        random_index = np.random.randint(x.size)

        return x.item(random_index)

    def get_solution(self):
        n = self.players_num - 1

        # check the theory of the method here:
        # https://en.wikipedia.org/wiki/System_of_linear_equations#Matrix_solution
        a = np.array(MatrixA(n).get_matrix())
        b = np.array(MatrixB(n).get_matrix())
        x = np.linalg.solve(a, b)

        return x
