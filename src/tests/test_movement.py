import unittest
from entity.entity import Entity


# Actually move to a new location
class TestMovement(unittest.TestCase):
    def test_get_current_location(self):
        test_case = Entity()
        self.assertEqual(test_case.get_location(), (0, 0))

    def test_change_y_position(self):
        test_case = Entity()

        # Testing moving North 1 spot
        test_case.move_y_axis(1)
        self.assertEqual(test_case.get_location(), (0, 1))

        # Testing moving North 2 spots
        test_case.move_y_axis(2)
        self.assertEqual(test_case.get_location(), (0, 3))

        # Testing moving South 1 spot
        test_case.move_y_axis(-1)
        self.assertEqual(test_case.get_location(), (0, 2))

        # Testing moving South 2 spots
        test_case.move_y_axis(-2)
        self.assertEqual(test_case.get_location(), (0, 0))

    def test_change_x_position(self):
        test_case = Entity()

        # Test moving West 1 spot
        test_case.move_x_axis(-1)
        self.assertEqual(test_case.get_location(), (-1, 0))

        # Test moving West 2 spots
        test_case.move_x_axis(-2)
        self.assertEqual(test_case.get_location(), (-3, 0))

        # Test moving East 1 spot
        test_case.move_x_axis(1)
        self.assertEqual(test_case.get_location(), (-2, 0))

        # Test moving East 2 spots
        test_case.move_x_axis(2)
        self.assertEqual(test_case.get_location(), (0, 0))

    def test_change_z_position(self):
        test_case = Entity()

        # Test moving North-West 1 spot
        test_case.move_z_axis(-1, 1)
        self.assertEqual(test_case.get_location(), (-1, 1))

        # Test moving North-West 2 spots
        test_case.move_z_axis(-2, 2)
        self.assertEqual(test_case.get_location(), (-3, 3))

        # Test moving North-East 1 spot
        test_case.move_z_axis(1, 1)
        self.assertEqual(test_case.get_location(), (-2, 4))

        # Test moving North-East 2 spots
        test_case.move_z_axis(2, 2)
        self.assertEqual(test_case.get_location(), (0, 6))

        # Test moving South-West 1 spot
        test_case.move_z_axis(-1, -1)
        self.assertEqual(test_case.get_location(), (-1, 5))

        # Test moving South-West 2 spots
        test_case.move_z_axis(-2, -2)
        self.assertEqual(test_case.get_location(), (-3, 3))

        # Test moving South-East 1 spot
        test_case.move_z_axis(1, -1)
        self.assertEqual(test_case.get_location(), (-2, 2))

        # Test moving South-East 2 spots
        test_case.move_z_axis(2, -2)
        self.assertEqual(test_case.get_location(), (0, 0))
