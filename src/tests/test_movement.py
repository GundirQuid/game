import unittest
import operator
from entity.entity import Entity
from entity.direction_of_movement import DirectionOfMovement


# Actually move to a new location
class TestMovement(unittest.TestCase):
    def test_get_current_location(self):
        test_case = Entity()
        self.assertEqual(test_case.get_location(), (0, 0))

    def test_change_all_positions(self):
        test_case = Entity()
        test_movement = DirectionOfMovement().all_movement()

        # Test all possible movement combinations according to DirectionOfMovement().y_movement()
        for movement in test_movement:
            previous_position = test_case.get_location()

            # Test moving 1 spot
            test_case.move_axis(movement)
            self.assertEqual(test_case.get_location(), tuple(map(operator.add, previous_position, movement)))

            # Test moving 2 spots
            test_case.move_axis(movement)
            self.assertEqual(test_case.get_location(),
                             tuple(map(operator.add, tuple(map(operator.add, previous_position, movement)), movement)))

    def test_change_y_position(self):
        test_case = Entity()
        test_movement = DirectionOfMovement().y_movement()

        # Test all possible movement combinations according to DirectionOfMovement().y_movement()
        for movement in test_movement:
            previous_position = test_case.get_location()

            # Test moving 1 spot
            test_case.move_axis(movement)
            self.assertEqual(test_case.get_location(), tuple(map(operator.add, previous_position, movement)))

            # Test moving 2 spots
            test_case.move_axis(movement)
            self.assertEqual(test_case.get_location(),
                             tuple(map(operator.add, tuple(map(operator.add, previous_position, movement)), movement)))

    def test_change_x_position(self):
        test_case = Entity()
        test_movement = DirectionOfMovement().x_movement()

        # Test all possible movement combinations according to DirectionOfMovement().x_movement()
        for movement in test_movement:
            previous_position = test_case.get_location()

            # Test moving 1 spot
            test_case.move_axis(movement)
            self.assertEqual(test_case.get_location(), tuple(map(operator.add, previous_position, movement)))

            # Test moving 2 spots
            test_case.move_axis(movement)
            self.assertEqual(test_case.get_location(),
                             tuple(map(operator.add, tuple(map(operator.add, previous_position, movement)), movement)))

    def test_change_z_position(self):
        test_case = Entity()
        test_movement = DirectionOfMovement().z_movement()

        # Test all possible movement combinations according to DirectionOfMovement().z_movement()
        for movement in test_movement:
            previous_position = test_case.get_location()

            # Test moving 1 spot
            test_case.move_axis(movement)
            self.assertEqual(test_case.get_location(), tuple(map(operator.add, previous_position, movement)))

            # Test moving 2 spots
            test_case.move_axis(movement)
            self.assertEqual(test_case.get_location(),
                             tuple(map(operator.add, tuple(map(operator.add, previous_position, movement)), movement)))

