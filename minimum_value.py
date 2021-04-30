# Minimum start value
# start with a given array of integers an an arbitrary initial value x.
# calculate the sum of x plus each array element from left to right.
# The running sum must never get below 1. Determine the minimum value of x.

import functools as f


class MinimumStartValue:

    def __init__(self, l: list, a: int):
        self.l = l
        self.a = a

    def minVal(self):
        print('list passed:', self.l)
        self.l[0] = self.l[0] + self.a
        rs = f.reduce(lambda x, y: x + y, self.l)
        print(rs)


if __name__ == '__main__':
    n = int(input('length of list'))

    a = MinimumStartValue([int(input()) for i in range(n)], int(input('Enter arbitrary value')))

    a.minVal()