import unittest
import random

from calc import SExpressionCalc


class SExpressionCalculatorTest(unittest.TestCase):

    def test_no_function(self):
        # explicit checks
        self.assertEqual(SExpressionCalc.calc('0'), 0)
        self.assertEqual(SExpressionCalc.calc('1'), 1)
        self.assertEqual(SExpressionCalc.calc('2'), 2)
        self.assertEqual(SExpressionCalc.calc('3'), 3)
        self.assertEqual(SExpressionCalc.calc('4'), 4)
        self.assertEqual(SExpressionCalc.calc('5'), 5)
        self.assertEqual(SExpressionCalc.calc('8'), 8)
        self.assertEqual(SExpressionCalc.calc('16'), 16)
        self.assertEqual(SExpressionCalc.calc('32'), 32)
        self.assertEqual(SExpressionCalc.calc('64'), 64)
        self.assertEqual(SExpressionCalc.calc('128'), 128)
        self.assertEqual(SExpressionCalc.calc('256'), 256)

        # check 0 through 1,000
        for i in range(0, 1000):
            self.assertEqual(SExpressionCalc.calc(str(i)), i)

        # check random values between 0 through 10,000 (100 times)
        for i in range(0, 100):
            val = random.randrange(10001)
            self.assertEqual(SExpressionCalc.calc(str(val)), val)

    def test_single_add(self):
        # explicit checks
        self.assertEqual(SExpressionCalc.calc('(add 1 1)'), 2)
        self.assertEqual(SExpressionCalc.calc('(add 12 34)'), 46)
        self.assertEqual(SExpressionCalc.calc('(add 321 456)'), 777)

        # check 0 + 0 through 100 + 100
        for i in range(0, 100):
            for j in range(0, 100):
                self.assertEqual(SExpressionCalc.calc('(add ' + str(i) + ' ' + str(j) + ')'), i+j)

        # check random values between 0 through 10,000 (100 times)
        for i in range(0, 100):
            a = random.randrange(10001)
            b = random.randrange(10001)
            self.assertEqual(SExpressionCalc.calc('(add ' + str(a) + ' ' + str(b) + ')'), a+b)


if __name__ == '__main__':
    unittest.main()
