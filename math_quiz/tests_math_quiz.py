import unittest
from math_quiz import generate_random_integer, get_random_operator, create_math_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, "Random integer should be within range")

    def test_get_random_operator(self):
        # Test if the operator returned is one of the expected operators
        for _ in range(1000):  # Test a large number of random operators
            operator = get_random_operator()
            self.assertIn(operator, ['+', '-', '*'], "Operator should be '+', '-', or '*'")

    def test_create_math_problem(self):
        # Test cases for create_math_problem
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 3, '*', '4 * 3', 12),
            (7, 5, '+', '7 + 5', 12),
            (9, 3, '-', '9 - 3', 6),
            (6, 6, '*', '6 * 6', 36),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Problem should be '{expected_problem}'")
            self.assertEqual(answer, expected_answer, f"Answer should be '{expected_answer}'")

if __name__ == "__main__":
    unittest.main()