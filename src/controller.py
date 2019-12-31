import numpy as np
from .services import MatrixA, MatrixB


class Controller:
    def __init__(self, players_num):
        self.players_num = players_num

    def calculate_optimal_points(self):
        n = self.players_num - 1

        a = np.array(MatrixA(n).get_matrix())
        b = np.array(MatrixB(n).get_matrix())
        x = np.linalg.solve(a, b)
        return x
