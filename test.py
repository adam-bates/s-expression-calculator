import unittest
import random

from calc import SExpression


class SExpressionCalculatorTest(unittest.TestCase):

    def test_no_function(self):
        s_expression_calc = SExpression()
        
        # explicit checks
        self.assertEqual(s_expression_calc.calc('0'), 0)
        self.assertEqual(s_expression_calc.calc('1'), 1)
        self.assertEqual(s_expression_calc.calc('2'), 2)
        self.assertEqual(s_expression_calc.calc('3'), 3)
        self.assertEqual(s_expression_calc.calc('4'), 4)
        self.assertEqual(s_expression_calc.calc('5'), 5)
        self.assertEqual(s_expression_calc.calc('8'), 8)
        self.assertEqual(s_expression_calc.calc('16'), 16)
        self.assertEqual(s_expression_calc.calc('32'), 32)
        self.assertEqual(s_expression_calc.calc('64'), 64)
        self.assertEqual(s_expression_calc.calc('128'), 128)
        self.assertEqual(s_expression_calc.calc('256'), 256)

        # check 0 through 1,000
        for i in range(0, 1000):
            self.assertEqual(s_expression_calc.calc(str(i)), i)

        # check random values between 0 through 10,000 (100 times)
        for i in range(0, 100):
            val = random.randrange(10001)
            self.assertEqual(s_expression_calc.calc(str(val)), val)

    def test_single_add(self):
        s_expression_calc = SExpression()
        
        # explicit checks
        self.assertEqual(s_expression_calc.calc('(add 1 1)'), 2)
        self.assertEqual(s_expression_calc.calc('(add 12 34)'), 46)
        self.assertEqual(s_expression_calc.calc('(add 321 456)'), 777)

        # check 0 + 0 through 100 + 100
        for i in range(0, 100):
            for j in range(0, 100):
                self.assertEqual(s_expression_calc.calc('(add ' + str(i) + ' ' + str(j) + ')'), i + j)

        # check random values between 0 through 10,000 (100 times)
        for i in range(0, 100):
            a = random.randrange(10001)
            b = random.randrange(10001)
            self.assertEqual(s_expression_calc.calc('(add ' + str(a) + ' ' + str(b) + ')'), a + b)

    def test_single_multiply(self):
        s_expression_calc = SExpression()
        
        # explicit checks
        self.assertEqual(s_expression_calc.calc('(multiply 1 1)'), 1)
        self.assertEqual(s_expression_calc.calc('(multiply 12 4)'), 48)
        self.assertEqual(s_expression_calc.calc('(multiply 321 456)'), 146376)

        # check 0 * 0 through 100 * 100
        for i in range(0, 100):
            for j in range(0, 100):
                self.assertEqual(s_expression_calc.calc('(multiply ' + str(i) + ' ' + str(j) + ')'), i * j)

        # check random values between 0 through 10,000 (100 times)
        for i in range(0, 100):
            a = random.randrange(10001)
            b = random.randrange(10001)
            self.assertEqual(s_expression_calc.calc('(multiply ' + str(a) + ' ' + str(b) + ')'), a * b)

    def test_nested_functions(self):
        s_expression_calc = SExpression()
        
        # Each combination of 1 layer of nested functions
        self.assertEqual(s_expression_calc.calc('(add (add 1 2) 5)'), 8)
        self.assertEqual(s_expression_calc.calc('(add (multiply 2 3) 7)'), 13)

        self.assertEqual(s_expression_calc.calc('(add 3 (add 1 2))'), 6)
        self.assertEqual(s_expression_calc.calc('(add 3 (multiply 1 2))'), 5)

        self.assertEqual(s_expression_calc.calc('(add (add 1 2) (add 3 4))'), 10)
        self.assertEqual(s_expression_calc.calc('(add (add 1 2) (multiply 1 2))'), 5)
        self.assertEqual(s_expression_calc.calc('(add (multiply 5 3) (add 3 4))'), 22)
        self.assertEqual(s_expression_calc.calc('(add (multiply 5 3) (multiply 3 4))'), 27)

        self.assertEqual(s_expression_calc.calc('(multiply (add 1 2) 5)'), 15)
        self.assertEqual(s_expression_calc.calc('(multiply (multiply 2 3) 7)'), 42)

        self.assertEqual(s_expression_calc.calc('(multiply 3 (add 1 2))'), 9)
        self.assertEqual(s_expression_calc.calc('(multiply 3 (multiply 1 2))'), 6)

        self.assertEqual(s_expression_calc.calc('(multiply (add 1 2) (add 3 4))'), 21)
        self.assertEqual(s_expression_calc.calc('(multiply (add 1 2) (multiply 1 2))'), 6)
        self.assertEqual(s_expression_calc.calc('(multiply (multiply 5 3) (add 3 4))'), 105)
        self.assertEqual(s_expression_calc.calc('(multiply (multiply 5 3) (multiply 3 4))'), 180)

        # More complex combinations
        self.assertEqual(s_expression_calc.calc('(multiply (add (multiply 1 2) 3) (add 1 2))'), 15)
        self.assertEqual(s_expression_calc.calc('(multiply (add (multiply 1 2) (add 3 4)) (multiply (add 5 6) (multiply 7 8)))'), 5544)


if __name__ == '__main__':
    unittest.main()
