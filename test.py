import unittest
import random

from calc import SExpression


class SExpressionCalculatorTest(unittest.TestCase):

    def test_no_function(self):
        # explicit checks
        self.assertEqual(SExpression.calc('0'), 0)
        self.assertEqual(SExpression.calc('1'), 1)
        self.assertEqual(SExpression.calc('2'), 2)
        self.assertEqual(SExpression.calc('3'), 3)
        self.assertEqual(SExpression.calc('4'), 4)
        self.assertEqual(SExpression.calc('5'), 5)
        self.assertEqual(SExpression.calc('8'), 8)
        self.assertEqual(SExpression.calc('16'), 16)
        self.assertEqual(SExpression.calc('32'), 32)
        self.assertEqual(SExpression.calc('64'), 64)
        self.assertEqual(SExpression.calc('128'), 128)
        self.assertEqual(SExpression.calc('256'), 256)

        # check 0 through 1,000
        for i in range(0, 1000):
            self.assertEqual(SExpression.calc(str(i)), i)

        # check random values between 0 through 10,000 (100 times)
        for i in range(0, 100):
            val = random.randrange(10001)
            self.assertEqual(SExpression.calc(str(val)), val)

    def test_single_add(self):
        # explicit checks
        self.assertEqual(SExpression.calc('(add 1 1)'), 2)
        self.assertEqual(SExpression.calc('(add 12 34)'), 46)
        self.assertEqual(SExpression.calc('(add 321 456)'), 777)

        # check 0 + 0 through 100 + 100
        for i in range(0, 100):
            for j in range(0, 100):
                self.assertEqual(SExpression.calc('(add ' + str(i) + ' ' + str(j) + ')'), i + j)

        # check random values between 0 through 10,000 (100 times)
        for i in range(0, 100):
            a = random.randrange(10001)
            b = random.randrange(10001)
            self.assertEqual(SExpression.calc('(add ' + str(a) + ' ' + str(b) + ')'), a + b)

    def test_single_multiply(self):
        # explicit checks
        self.assertEqual(SExpression.calc('(multiply 1 1)'), 1)
        self.assertEqual(SExpression.calc('(multiply 12 4)'), 48)
        self.assertEqual(SExpression.calc('(multiply 321 456)'), 146376)

        # check 0 * 0 through 100 * 100
        for i in range(0, 100):
            for j in range(0, 100):
                self.assertEqual(SExpression.calc('(multiply ' + str(i) + ' ' + str(j) + ')'), i * j)

        # check random values between 0 through 10,000 (100 times)
        for i in range(0, 100):
            a = random.randrange(10001)
            b = random.randrange(10001)
            self.assertEqual(SExpression.calc('(multiply ' + str(a) + ' ' + str(b) + ')'), a * b)

    def test_nested_functions(self):
        # Each combination of 1 layer of nested functions
        self.assertEqual(SExpression.calc('(add (add 1 2) 5)'), 8)
        self.assertEqual(SExpression.calc('(add (multiply 2 3) 7)'), 13)

        self.assertEqual(SExpression.calc('(add 3 (add 1 2))'), 6)
        self.assertEqual(SExpression.calc('(add 3 (multiply 1 2))'), 5)

        self.assertEqual(SExpression.calc('(add (add 1 2) (add 3 4))'), 10)
        self.assertEqual(SExpression.calc('(add (add 1 2) (multiply 1 2))'), 5)
        self.assertEqual(SExpression.calc('(add (multiply 5 3) (add 3 4))'), 22)
        self.assertEqual(SExpression.calc('(add (multiply 5 3) (multiply 3 4))'), 27)

        self.assertEqual(SExpression.calc('(multiply (add 1 2) 5)'), 15)
        self.assertEqual(SExpression.calc('(multiply (multiply 2 3) 7)'), 42)

        self.assertEqual(SExpression.calc('(multiply 3 (add 1 2))'), 9)
        self.assertEqual(SExpression.calc('(multiply 3 (multiply 1 2))'), 6)

        self.assertEqual(SExpression.calc('(multiply (add 1 2) (add 3 4))'), 21)
        self.assertEqual(SExpression.calc('(multiply (add 1 2) (multiply 1 2))'), 6)
        self.assertEqual(SExpression.calc('(multiply (multiply 5 3) (add 3 4))'), 105)
        self.assertEqual(SExpression.calc('(multiply (multiply 5 3) (multiply 3 4))'), 180)

        # More complex combinations
        self.assertEqual(SExpression.calc('(multiply (add (multiply 1 2) 3) (add 1 2))'), 15)
        self.assertEqual(SExpression.calc('(multiply (add (multiply 1 2) (add 3 4)) (multiply (add 5 6) (multiply 7 8)))'), 5544)


if __name__ == '__main__':
    unittest.main()
