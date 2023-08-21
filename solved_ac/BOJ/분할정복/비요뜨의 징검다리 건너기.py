import sys

input = sys.stdin.readline
divide = 10 ** 9 + 7

def fpow(a, b):
    if b == 1:
        return a % divide

    x = fpow(a, b // 2)
    if b & 1:
        return x * x * a % divide
    else:
        return x * x % divide

T = int(input())


for _ in range(T):
    N = int(input())
    print(fpow(2, N - 2))