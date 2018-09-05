import sys


class SExpressionCalc:
    @staticmethod
    def calc(str_input):
        if str_input[0] == '(' and str_input[-1] == ')':
            str_input = str_input[1:-1]

        pieces = str_input.split()
        if len(pieces) == 1:
            return int(pieces[0])

        while ')' in str_input:
            right_bound = str_input.index(')') + 1
            left_bound = str_input[:right_bound].rindex('(')

            str_input = str_input[:left_bound] + str(SExpressionCalc.calc(str_input[left_bound:right_bound])) + str_input[right_bound:]
            pieces = str_input.split()

        if pieces[0] == 'add':
            return SExpressionCalc.calc(pieces[1]) + SExpressionCalc.calc(pieces[2])
        elif pieces[0] == 'multiply':
            return SExpressionCalc.calc(pieces[1]) * SExpressionCalc.calc(pieces[2])


def main():
    print(SExpressionCalc.calc(sys.argv[1]))


if __name__ == '__main__':
    main()
