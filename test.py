import unittest
from calc import SExpressionCalc


class SExpressionCalculatorTest(unittest.TestCase):

    def test_no_function(self):
        for i in range(0, 10000):
            self.assertEqual(SExpressionCalc.calc(str(i)), i)


if __name__ == '__main__':
    unittest.main()
