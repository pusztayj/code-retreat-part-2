import numpy as np
import pytest

from conway import Conway

class TestConway:

    @pytest.mark.parametrize(
        "input_array,expected",
        [
            ([(1, 0, 0), (0, 1, 0), (0, 0, 0)], False),
            ([(1, 1, 1), (0, 1, 0), (0, 0, 1)], False),
            ([(1, 1, 1), (0, 1, 0), (0, 0, 0)], True),
            ([(1, 1, 0), (0, 1, 0), (0, 0, 0)], True),
         ]
    )
    def test_live_cell_death(self, input_array, expected):
        assert Conway.live_cell(np.asarray(input_array)) == expected


    @pytest.mark.parametrize(
        "input_array, expected",
        [
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], False),
            ([[1, 0, 0], [1, 0, 0], [1, 0, 0]], True),
            ([[1, 0, 1], [1, 0, 0], [1, 0, 0]], False),
        ]
    )
    def test_dead_cell_birth(self, input_array, expected):
        assert Conway.dead_cell(np.asarray(input_array)) == expected

