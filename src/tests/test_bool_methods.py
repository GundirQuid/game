import unittest


class TestBoolMethods(unittest.TestCase):
    # True == True
    def test_true_is_true(self):
        test_case = True
        self.assertTrue(test_case)

    # True != False
    def test_true_is_not_false(self):
        test_case = True
        self.assertFalse(not test_case)

    # False != True
    def test_false_is_not_true(self):
        test_case = False
        self.assertTrue(not test_case)

    # False == False
    def test_false_is_false(self):
        test_case = False
        self.assertFalse(test_case)

    # Testing bool() methods
    def test_bool_function_with_integer(self):
        self.assertTrue(bool(1))
        self.assertFalse(bool(0))

    def test_bool_function_with_string(self):
        self.assertTrue(bool('a'))
        self.assertFalse(bool(''))

    def test_bool_function_with_list(self):
        self.assertTrue(bool([0]))
        self.assertTrue(bool([1]))

        self.assertTrue(bool([0, 1]))
        self.assertTrue(bool([1, 1]))

        self.assertFalse(bool([]))

    def test_bool_function_with_tuple(self):
        self.assertTrue(bool((0,)))
        self.assertTrue(bool((1,)))

        self.assertTrue(bool((0, 0)))
        self.assertTrue(bool((0, 1)))

        self.assertTrue(bool((1, 0)))
        self.assertTrue(bool((1, 1)))

        self.assertFalse(bool(()))

    def test_bool_function_with_dict(self):
        self.assertTrue(bool({0: 0}))
        self.assertTrue(bool({0: 1}))

        self.assertTrue(bool({0: 0, 1: 0}))
        self.assertTrue(bool({0: 0, 1: 1}))

        self.assertTrue(bool({0: 1, 1: 0}))
        self.assertTrue(bool({0: 1, 1: 1}))

        self.assertFalse(bool({}))

    def test_bool_math(self):
        self.assertFalse(False + 0)
        self.assertTrue(False + 1)

        self.assertTrue(True + 0)
        self.assertTrue(True + 1)

        self.assertEqual(False + 1, 1)
        self.assertEqual(True + 1, 2)

        self.assertFalse(False * 70)
        self.assertEqual(False * 75, 0)

        self.assertTrue(True * 75)
        self.assertEqual(True * 75, 75)

