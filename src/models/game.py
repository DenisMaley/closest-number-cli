class Game:
    def __init__(self, points, sample):
        self.points = points
        self.sample = sample

    def get_winner(self):
        winner_value = min(self.points, key=lambda x: abs(x - self.sample))

        return self.points.index(winner_value)
