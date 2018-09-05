import sys


class SExpression:

    @staticmethod
    def calc(str_input):
        # 1. Remove surrounding parenthesis
        if str_input[0] == '(' and str_input[-1] == ')':
            str_input = str_input[1:-1]

        # 2. Loop through nested expressions and evaluate each
        while ')' in str_input:
            # Start with the first expression to close (ie. first index of ')')
            right_bound = str_input.index(')')
            left_bound = str_input[:right_bound].rindex('(')

            # Update str_input, replacing expression with calculated value
            value = SExpression._evaluate_single(str_input[left_bound + 1:right_bound])
            str_input = str_input[:left_bound] + str(value) + str_input[right_bound+1:]

        # 3. Evaluate out-most expression
        return SExpression._evaluate_single(str_input)

    @staticmethod
    def _evaluate_single(str_input):
        pieces = str_input.split()

        if pieces[0] == 'add':
            return int(pieces[1]) + int(pieces[2])

        elif pieces[0] == 'multiply':
            return int(pieces[1]) * int(pieces[2])

        else:
            return int(str_input)


def main():
    print(SExpression.calc(sys.argv[1]))


if __name__ == '__main__':
    main()
