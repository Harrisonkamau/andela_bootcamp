import unittest

class MethodTests(unittest.TestCase):
    def test_multiplication_of_two_numbers(self):
        self.assertEqual(2,2)

    def test_multiplication_of_a_string_with_anumber(self):
        self.assertFalse(True)
        self.assertGreater(2,5)
        self.assertIn('Hello', 'Hey there!')

        # this will not run because tests must start with a keyword test_
    def add_test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
