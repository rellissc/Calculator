import unittest
from tkinter import Tk
from CalculatorScript import CalculateAnswer, PressCalculate


class TestStringMethods(unittest.TestCase):

    def test_CalculateAnswer(self):
        self.assertEqual(CalculateAnswer('+', 45, 5), 50)
        self.assertEqual(CalculateAnswer('-', 45, 5), 40)
        self.assertEqual(CalculateAnswer('/', 45, 5), 50)
        self.assertEqual(CalculateAnswer('*', 5, 5), 25)
        self.assertEqual(CalculateAnswer('+', 4.5, 5), ?)
        self.assertEqual(CalculateAnswer('-', 4.5, 5), ?)
        self.assertEqual(CalculateAnswer('/', 4.5, 5), ?)
        self.assertEqual(CalculateAnswer('*', 5.5, 5), ?)

    def test_PressCalculate(self):
        self.assertEqual(PressCalculate())


if __name__ == '__main__':
    unittest.main()
