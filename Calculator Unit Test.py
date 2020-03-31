import unittest
from CalculatorScript import CalculateAnswer, PressCalculate


class TestStringMethods(unittest.TestCase):

    # def setUpClass(self):
    #     print('Test')
    #
    # def tearDown(self):
    #     print('Test')

    def test_CalculateAnswer(self):
        self.assertEqual(CalculateAnswer('+', 45, 5), 50)
        self.assertEqual(CalculateAnswer('-', 45, 5), 40)
        self.assertEqual(CalculateAnswer('/', 45, 5), 50)
        self.assertEqual(CalculateAnswer('*', 5, 5), 25)

    def test_PressCalculate(self):
        self.assertEqual(PressCalculate('+', 45, 5), 50)


if __name__ == '__main__':
    unittest.main()
