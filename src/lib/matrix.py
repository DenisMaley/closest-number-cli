from abc import ABC, abstractmethod


class Matrix(ABC):
    def __init__(self, n):
        self.n = n

    @abstractmethod
    def get_matrix(self):
        pass


class MatrixA(Matrix):
    def get_matrix(self):
        matrix_a = []

        matrix_a.append(self.get_first_row())

        for i in range(1, self.n - 1):
            matrix_a.append(self.get_middle_row(i))

        matrix_a.append(self.get_last_row())

        return matrix_a

    def get_first_row(self):
        first_row = [0] * self.n
        first_row[0] = 3
        first_row[1] = -1

        return first_row

    def get_middle_row(self, i):
        middle_row = [0] * self.n
        middle_row[0] = 2
        middle_row[i] = 1
        middle_row[i + 1] = -1

        return middle_row

    def get_last_row(self):
        last_row = [0] * self.n
        last_row[0] = 1
        last_row[self.n - 1] = 1

        return last_row


class MatrixB(Matrix):
    def get_matrix(self):
        matrix_b = [0] * self.n
        matrix_b[self.n - 1] = 1

        return matrix_b
