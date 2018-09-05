import sys


class SExpressionCalc:

    @staticmethod
    def calc(str_input):
        # 1. Remove surrounding parenthesis
        if str_input[0] == '(' and str_input[-1] == ')':
            str_input = str_input[1:-1]

        # 2. Base Case: Check if str_input is alone (it. just an integer)
        pieces = str_input.split()
        if len(pieces) == 1:
            return int(pieces[0])

        # 3. Loop through nested expressions and calculate each
        while ')' in str_input:
            # Start with first expression to close (ie. first index of ')')
            right_bound = str_input.index(')') + 1
            left_bound = str_input[:right_bound].rindex('(')

            # Update str_input and pieces, replacing expression with calculated value
            str_input = str_input[:left_bound] + str(SExpressionCalc.calc(str_input[left_bound:right_bound])) + str_input[right_bound:]
            pieces = str_input.split()

        # 4. Evaluate
        if pieces[0] == 'add':
            return SExpressionCalc.calc(pieces[1]) + SExpressionCalc.calc(pieces[2])

        elif pieces[0] == 'multiply':
            return SExpressionCalc.calc(pieces[1]) * SExpressionCalc.calc(pieces[2])


def main():
    print(SExpressionCalc.calc(sys.argv[1]))


if __name__ == '__main__':
    main()
