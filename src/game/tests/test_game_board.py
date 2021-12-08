import unittest
from game.game_board import GameBoard


def helper_loop(helper_board: GameBoard, helper_test_case: tuple, helper_change: tuple) -> tuple:
    import operator

    x_axis, y_axis = helper_board.get_board_size()

    for _ in range(x_axis * y_axis * 2 + 1):
        helper_old_location = helper_test_case
        helper_test_case = tuple(map(operator.add, helper_test_case, helper_change))

        # Default, we go from (0, 0) to (-20, 0), but (-20, 0) is not a valid spot,
        # Since we have (-5, 5) to (4, -4), we need to figure out what to do to keep bounds
        # To solve this, we will use a Wrap-around method, located inside GameBoard
        if not helper_board.verify_location(helper_test_case):

            helper_test_case = helper_board.wrap_around_location(helper_old_location, helper_change)

    return helper_test_case


class TestGameBoard(unittest.TestCase):
    def test_board_size(self):
        # Testing default game board size
        test_case = GameBoard()
        self.assertEqual(test_case.get_board_size(), (3, 3))

        # Testing hard-coded board size
        test_case = GameBoard(500, 500)
        self.assertEqual(test_case.get_board_size(), (500, 500))

        # Testing hard-coded board size larger then maximum size
        test_case = GameBoard(2000, 2000)
        self.assertEqual(test_case.get_board_size(), (1000, 1000))

    def test_board_x_axis(self):
        test_board = GameBoard(10, 10)
        test_case = (0, 2)

        # Testing a 10x10 game board, starting at (0, 2) and continue heading West, wrap around to East
        test_case = helper_loop(test_board, test_case, (-1, 0))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (-1, 2))

        # Testing a 10x10 game board, starting at (0, 0) and continue heading East, wrap around to West
        test_case = helper_loop(test_board, test_case, (1, 0))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (0, 2))

    def test_board_y_axis(self):
        test_board = GameBoard(10, 10)
        test_case = (-2, 3)

        # Testing a 10x10 game board, starting at (-2, 3) and continue heading South, wrap around to North
        test_case = helper_loop(test_board, test_case, (0, -1))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (-2, 2))

        # Testing a 10x10 game board, starting at (0, 0) and continue heading North, wrap around to South
        test_case = helper_loop(test_board, test_case, (0, 1))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (-2, 3))

    def test_board_x_and_y_axis(self):
        test_board = GameBoard(10, 10)
        test_case = (2, -3)

        # Testing a 10x10 game board, starting at (2, -3) and continue heading South-West, wrap around to North-East
        test_case = helper_loop(test_board, test_case, (-1, -1))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (1, -4))

        # Testing a 10x10 game board, starting at (1, -4) and continue heading North, wrap around to South
        test_case = helper_loop(test_board, test_case, (1, 1))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (2, -3))

