import unittest
from entity.direction_of_movement import DirectionOfMovement


class TestUnitMovement(unittest.TestCase):
    def test_all_movement_directions(self):
        test_case = DirectionOfMovement()
        self.assertEqual(test_case.all_movement(), [0, 1, 2,
                                                    3, 4, 5,
                                                    6, 7, 8])

    def test_x_axis_movement_directions(self):
        test_case = DirectionOfMovement()
        self.assertEqual(test_case.x_movement(), [3, 4, 5])

    def test_y_axis_movement_directions(self):
        test_case = DirectionOfMovement()
        self.assertEqual(test_case.y_movement(), [1, 4, 7])

    def test_z_axis_movement_directions(self):
        test_case = DirectionOfMovement()
        self.assertEqual(test_case.z_movement(), [0, 2, 4, 6, 8])
