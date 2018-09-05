import sys


class SExpressionCalc:
    @staticmethod
    def calc(string):
        return int(string)


def main():
    print(SExpressionCalc.calc(sys.argv[1]))


if __name__ == '__main__':
    main()
