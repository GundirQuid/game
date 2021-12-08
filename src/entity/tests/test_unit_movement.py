import unittest
from entity.direction_of_movement import DirectionOfMovement


class TestUnitMovement(unittest.TestCase):
    def test_all_movement_directions(self):
        test_case = DirectionOfMovement()
        self.assertEqual(test_case.all_movement(), [(-1, 1),  (0, 1),  (1, 1),
                                                    (-1, 0),  (0, 0),  (1, 0),
                                                    (-1, -1), (0, -1), (1, -1)])

    def test_x_axis_movement_directions(self):
        test_case = DirectionOfMovement()
        self.assertEqual(test_case.x_movement(), [(-1, 0), (0, 0), (1, 0)])

    def test_y_axis_movement_directions(self):
        test_case = DirectionOfMovement()
        self.assertEqual(test_case.y_movement(), [(0, 1),
                                                  (0, 0),
                                                  (0, -1)])

    def test_z_axis_movement_directions(self):
        test_case = DirectionOfMovement()
        self.assertEqual(test_case.z_movement(), [(-1, 1), (1, 1),
                                                  (0, 0),
                                                  (-1, -1), (1, -1)])
