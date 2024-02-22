import numpy as np

class Conway:
    grid = np.random.randint(0, 2, 10)

    @staticmethod
    def live_cell(neighborhood):
        if (np.sum(neighborhood) - 1) < 2 or (np.sum(neighborhood) - 1) > 3:
            return False
        return True

    @staticmethod
    def dead_cell(neighborhood: list[list[int]]):
        if np.sum(neighborhood) == 3:
            return True
        return False