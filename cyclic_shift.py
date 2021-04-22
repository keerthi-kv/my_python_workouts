import sys


def cyclic_shift(x, y, z):
    cn = 0
    cnt = 0
    l = []
    while True:
        x = x[1:len(x)] + x[0]
        if int(x, 2) == y:
            l.append(cn)
            cnt = cnt + 1
            if cnt == z:
                break
        cn = cn + 1
    print(l[-1])


if __name__ == '__main__':

    t = int(input())

    for t in range(t):
        # a='10101'
        a = ''
        len_str, mc = map(int, input().split())
        # len_str=int(input('Enter length of string'))
        # mc=int(input('Enter match count'))
        a = input()
        if len(a) != len_str:
            sys.exit(-1)
        # for i in range(len_str):
        #   a=a+input()
        b = int(a, 2)
        cyclic_shift(a, b, mc)