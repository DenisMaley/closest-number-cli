import numpy as np
from tqdm import tqdm

from .models import Game
from .lib import MatrixA, MatrixB


class Controller:
    def __init__(self, players_num):
        self.players_num = players_num

    def make_experiment(self, samples_num):
        win_statistics = [0] * len(self.get_optimal_points())

        with tqdm(total=samples_num) as pbar:
            for i in range(samples_num):
                pbar.update(1)
                win_statistics[self.get_game_winner()] += 1

        return [round(x / samples_num, 2) for x in win_statistics]

    def get_game_winner(self):
        points = self.get_optimal_points()
        sample = np.random.uniform()

        game = Game(points, sample)

        return game.get_winner()

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
