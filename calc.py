import sys


class SExpressionCalc:
    @staticmethod
    def calc(string):
        expression = string.split()
        if len(expression) == 1:
            return int(expression[0].replace('(', '').replace(')', ''))
        elif expression[0] == '(add':
            return SExpressionCalc.calc(expression[1]) + SExpressionCalc.calc(expression[2])


def main():
    print(SExpressionCalc.calc(sys.argv[1]))


if __name__ == '__main__':
    main()
