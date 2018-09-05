import sys


class SExpression:

    @staticmethod
    def calc(str_input):
        while ')' in str_input:
            # Start with the first expression to close (ie. first index of ')')
            right_bound = str_input.index(')')
            left_bound = str_input[:right_bound].rindex('(')

            # Note: Because we're getting the first expression to close,
            #       it is guaranteed not to have nested functions inside
            value = SExpression._evaluate_single(str_input[left_bound + 1:right_bound])

            # If evaluated final function
            if left_bound == 0:
                return value

            # Else update str_input, replacing expression with calculated value
            else:
                str_input = str_input[:left_bound] + str(value) + str_input[right_bound+1:]

        return int(str_input)

    @staticmethod
    # Evaluates simple expression with no nested values
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
