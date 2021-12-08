import unittest
from entity.entity import Entity
from entity.direction_of_movement import DirectionOfMovement


# Actually move to a new location
class TestMovement(unittest.TestCase):
    def test_get_current_location(self):
        test_case = Entity()
        self.assertEqual(test_case.get_location(), (0, 0))

    def test_change_y_position(self):
        test_case = Entity()

        test_movement = DirectionOfMovement()
        test_movement = test_movement.y_movement()
        test_move_north = test_movement[0]
        test_move_center = test_movement[1]
        test_move_south = test_movement[2]

        self.assertEqual(test_move_north, (0, 1))
        self.assertEqual(test_move_center, (0, 0))
        self.assertEqual(test_move_south, (0, -1))

        # Test moving North 1 spot
        test_case.move_axis(test_move_north)
        self.assertEqual(test_case.get_location(), (0, 1))

        # Test moving North 2 spots
        test_case.move_axis(test_move_north)
        test_case.move_axis(test_move_north)
        self.assertEqual(test_case.get_location(), (0, 3))

        # Test moving South 1 spot
        test_case.move_axis(test_move_south)
        self.assertEqual(test_case.get_location(), (0, 2))

        # Test moving South 2 spots
        test_case.move_axis(test_move_south)
        test_case.move_axis(test_move_south)
        self.assertEqual(test_case.get_location(), (0, 0))

        # Test moving center 1 spot (should have no impact as we are not actually moving)
        test_case.move_axis(test_move_center)
        self.assertEqual(test_case.get_location(), (0, 0))

        # Test moving center 2 spots (should have no impact as we are not actually moving)
        test_case.move_axis(test_move_center)
        test_case.move_axis(test_move_center)
        self.assertEqual(test_case.get_location(), (0, 0))

    def test_change_x_position(self):
        test_case = Entity()

        test_movement = DirectionOfMovement()
        test_movement = test_movement.x_movement()
        test_move_west = test_movement[0]
        test_move_center = test_movement[1]
        test_move_east = test_movement[2]

        self.assertEqual(test_move_west, (-1, 0))
        self.assertEqual(test_move_center, (0, 0))
        self.assertEqual(test_move_east, (1, 0))

        # Test moving West 1 spot
        test_case.move_axis(test_move_west)
        self.assertEqual(test_case.get_location(), (-1, 0))

        # Test moving West 2 spots
        test_case.move_axis(test_move_west)
        test_case.move_axis(test_move_west)
        self.assertEqual(test_case.get_location(), (-3, 0))

        # Test moving East 1 spot
        test_case.move_axis(test_move_east)
        self.assertEqual(test_case.get_location(), (-2, 0))

        # Test moving East 2 spots
        test_case.move_axis(test_move_east)
        test_case.move_axis(test_move_east)
        self.assertEqual(test_case.get_location(), (0, 0))

        # Test moving center 1 spot (should have no impact as we are not actually moving)
        test_case.move_axis(test_move_center)
        self.assertEqual(test_case.get_location(), (0, 0))

        # Test moving center 2 spots (should have no impact as we are not actually moving)
        test_case.move_axis(test_move_center)
        test_case.move_axis(test_move_center)
        self.assertEqual(test_case.get_location(), (0, 0))

    def test_change_z_position(self):
        test_case = Entity()

        test_movement = DirectionOfMovement()
        test_movement = test_movement.z_movement()
        test_move_north_west = test_movement[0]
        test_move_north_east = test_movement[1]
        test_move_center = test_movement[2]
        test_move_south_west = test_movement[3]
        test_move_south_east = test_movement[4]

        self.assertEqual(test_move_north_west, (-1, 1))
        self.assertEqual(test_move_north_east, (1, 1))
        self.assertEqual(test_move_center, (0, 0))
        self.assertEqual(test_move_south_west, (-1, -1))
        self.assertEqual(test_move_south_east, (1, -1))

        # Test moving North-West 1 spot
        test_case.move_axis(test_move_north_west)
        self.assertEqual(test_case.get_location(), (-1, 1))

        # Test moving North-West 2 spots
        test_case.move_axis(test_move_north_west)
        test_case.move_axis(test_move_north_west)
        self.assertEqual(test_case.get_location(), (-3, 3))

        # Test moving North-East 1 spot
        test_case.move_axis(test_move_north_east)
        self.assertEqual(test_case.get_location(), (-2, 4))

        # Test moving North-East 2 spots
        test_case.move_axis(test_move_north_east)
        test_case.move_axis(test_move_north_east)
        self.assertEqual(test_case.get_location(), (0, 6))

        # Test moving South-West 1 spot
        test_case.move_axis(test_move_south_west)
        self.assertEqual(test_case.get_location(), (-1, 5))

        # Test moving South-West 2 spots
        test_case.move_axis(test_move_south_west)
        test_case.move_axis(test_move_south_west)
        self.assertEqual(test_case.get_location(), (-3, 3))

        # Test moving South-East 1 spot
        test_case.move_axis(test_move_south_east)
        self.assertEqual(test_case.get_location(), (-2, 2))

        # Test moving South-East 2 spots
        test_case.move_axis(test_move_south_east)
        test_case.move_axis(test_move_south_east)
        self.assertEqual(test_case.get_location(), (0, 0))

        # Test moving center 1 spot (should have no impact as we are not actually moving)
        test_case.move_axis(test_move_center)
        self.assertEqual(test_case.get_location(), (0, 0))

        # Test moving center 2 spots (should have no impact as we are not actually moving)
        test_case.move_axis(test_move_center)
        test_case.move_axis(test_move_center)
        self.assertEqual(test_case.get_location(), (0, 0))
