import unittest
import operator
from game.game_board import GameBoard


def helper_validate_move(helper_game_board: GameBoard,
                         helper_location_current: tuple,
                         helper_location_change: tuple) -> tuple:
    """
    :param helper_game_board: GameBoard instance
    :param helper_location_current: Current location
    :param helper_location_change: Direction of movement
    :return: Valid next location
    """
    x_axis, y_axis = helper_game_board.get_board_size()

    for _ in range(x_axis * y_axis * 2 + 1):
        helper_location_current = helper_game_board.move_location(helper_location_current, helper_location_change)

    return helper_location_current


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

        # Test passing non-int to GameBoard, it should raise a TypeError
        with self.assertRaises(TypeError):
            test_case = GameBoard(100, '100')

        with self.assertRaises(TypeError):
            test_case = GameBoard('100', 100)

        with self.assertRaises(TypeError):
            test_case = GameBoard('100', '100')

    def test_board_x_axis(self):
        test_board = GameBoard(10, 10)
        test_case = (0, 2)

        # Testing a 10x10 game board, starting at (0, 2) and continue heading West, wrap around to East
        test_case = helper_validate_move(test_board, test_case, (-1, 0))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (-1, 2))

        # Testing a 10x10 game board, starting at (0, 0) and continue heading East, wrap around to West
        test_case = helper_validate_move(test_board, test_case, (1, 0))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (0, 2))

    def test_board_y_axis(self):
        test_board = GameBoard(10, 10)
        test_case = (-2, 3)

        # Testing a 10x10 game board, starting at (-2, 3) and continue heading South, wrap around to North
        test_case = helper_validate_move(test_board, test_case, (0, -1))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (-2, 2))

        # Testing a 10x10 game board, starting at (0, 0) and continue heading North, wrap around to South
        test_case = helper_validate_move(test_board, test_case, (0, 1))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (-2, 3))

    def test_board_x_and_y_axis(self):
        test_board = GameBoard(10, 10)
        test_case = (2, -3)

        # Testing a 10x10 game board, starting at (2, -3) and continue heading South-West, wrap around to North-East
        test_case = helper_validate_move(test_board, test_case, (-1, -1))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (1, -4))

        # Testing a 10x10 game board, starting at (1, -4) and continue heading North, wrap around to South
        test_case = helper_validate_move(test_board, test_case, (1, 1))

        # Validate our x-axis movements match what we expect it to match, on a 10x10 board
        self.assertEqual(test_case, (2, -3))

