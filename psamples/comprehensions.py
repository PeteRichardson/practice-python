''' comprehensions.py - test of list, dict and set comprehensions '''

import sys
from pprint import pprint


def main():
    square_dict = {x: x**2 for x in xrange(6)}
    reverse_square_dict = { y:x for (x,y) in square_dict.items()}
    pprint(square_dict)
    pprint(reverse_square_dict)
    return 1


if __name__ == "__main__":
    sys.exit(main())
