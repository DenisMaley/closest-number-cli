import numpy as np
from tqdm import tqdm

from .lib import MatrixA, MatrixB
from .models import Game


class Controller:
    def __init__(self, players_num):
        self.players_num = players_num

    def make_experiment(self, samples_num):
        points = self.get_game_points()
        win_counts = [0] * len(points)

        with tqdm(total=samples_num) as pbar:
            for i in range(samples_num):
                pbar.update(1)
                game = self.get_game(points)
                win_counts[game.get_winner()] += 1

        return points, [x / samples_num for x in win_counts]

    def get_game_points(self):
        # optimal points for the first (players_num - 1) players
        points = self.get_optimal_points()
        # point for the last player
        # Could be any number between any two strategies: np.random.uniform(points[i], points[i + 1])
        # where 0 < i < players_num - 1
        # For the last player it doesn't matter
        # For the simplicity but without loss of generality let's choose in the middle of the two last points
        last_player_point = np.average(points[-2:])
        points.insert(self.players_num - 2, last_player_point)

        return points

    @staticmethod
    def get_game(points):
        sample = np.random.uniform()

        return Game(points, sample)

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
