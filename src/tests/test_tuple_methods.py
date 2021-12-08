import unittest
import operator


class TestTupleMethods(unittest.TestCase):
    # (0, 0) is a tuple, true
    def test_0_0_is_a_tuple(self):
        self.assertTrue(type((0, 0)), tuple)

    def test_tuple_math_add(self):
        self.assertEqual(tuple(map(operator.add, (0, 0), (0, 0))), (0, 0))

        self.assertEqual(tuple(map(operator.add, (0, 1), (0, 0))), (0, 1))
        self.assertEqual(tuple(map(operator.add, (0, 0), (0, 1))), (0, 1))

        self.assertEqual(tuple(map(operator.add, (1, 0), (0, 0))), (1, 0))
        self.assertEqual(tuple(map(operator.add, (0, 0), (1, 0))), (1, 0))

        self.assertEqual(tuple(map(operator.add, (1, 1), (0, 0))), (1, 1))
        self.assertEqual(tuple(map(operator.add, (1, 0), (0, 1))), (1, 1))
        self.assertEqual(tuple(map(operator.add, (0, 1), (1, 0))), (1, 1))
        self.assertEqual(tuple(map(operator.add, (0, 0), (1, 1))), (1, 1))

    def test_tuple_math_subtract(self):
        self.assertEqual(tuple(map(operator.sub, (0, 0), (0, 0))), (0, 0))

        self.assertEqual(tuple(map(operator.sub, (0, 1), (0, 0))), (0, 1))
        self.assertEqual(tuple(map(operator.sub, (0, 0), (0, 1))), (0, -1))

        self.assertEqual(tuple(map(operator.sub, (1, 0), (0, 0))), (1, 0))
        self.assertEqual(tuple(map(operator.sub, (0, 0), (1, 0))), (-1, 0))

        self.assertEqual(tuple(map(operator.sub, (1, 1), (0, 0))), (1, 1))
        self.assertEqual(tuple(map(operator.sub, (1, 0), (0, 1))), (1, -1))
        self.assertEqual(tuple(map(operator.sub, (0, 1), (1, 0))), (-1, 1))
        self.assertEqual(tuple(map(operator.sub, (0, 0), (1, 1))), (-1, -1))