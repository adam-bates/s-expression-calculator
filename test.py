import unittest
from calc import SExpressionCalc


class TestNoFunction(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(SExpressionCalc.calc("TEST"), "TEST")


if __name__ == '__main__':
    unittest.main()
