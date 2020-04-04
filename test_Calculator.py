import unittest
from tkinter import Tk
from CalculatorFunctions import CalculateAnswer, PressCalculate


class TestStringMethods(unittest.TestCase):

    def test_CalculateOperation(self):
        self.assertEqual(CalculateAnswer('+', 45, 5), 50)
        self.assertEqual(CalculateAnswer('-', 45, 5), 40)
        self.assertEqual(CalculateAnswer('/', 45, 5), 9)
        self.assertEqual(CalculateAnswer('*', 5, 5), 25)
        self.assertEqual(CalculateAnswer('+', 4.5, 5), 9.5)
        self.assertEqual(CalculateAnswer('-', 5.5, 5), .5)
        self.assertEqual(CalculateAnswer('/', 4.5, 5), .9)
        self.assertEqual(CalculateAnswer('*', 5.5, 5), 27.5)
        self.assertEqual(CalculateAnswer('-', 10, 15), -5)

    def test_CalculateEquation(self):
        self.assertEqual(CalculateAnswer(), 50)


if __name__ == '__main__':
    unittest.main()
