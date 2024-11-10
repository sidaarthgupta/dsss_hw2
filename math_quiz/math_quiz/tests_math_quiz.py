import unittest
from math_quiz import random_integers, random_operator, problem_question


class TestMathGame(unittest.TestCase):

    def test_random_integers(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integers(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operator = random_operator()
            self.assertIn(operator, operators)

    def test_problem_question(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 3, '-', '10 - 3', 7),
                (4, 6, '*', '4 * 6', 24),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = problem_question(num1, num2, operator)
                self.assertEqual(problem, expected_problem)  
                self.assertEqual(answer, expected_answer)  

if __name__ == "__main__":
    unittest.main()
