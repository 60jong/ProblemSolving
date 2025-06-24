import sys

input = sys.stdin.readline

N = int(input())
if N == 1:
    print(input())
else:
    steps = [0]
    steps.extend([int(input()) for _ in range(N)])
    d = [0] * (N + 1)

    # init
    d[0], d[1], d[2] = 0, steps[1], steps[1] + steps[2]

    if N < 3:
        print(d[N])
    else:
        for n in range(3, N + 1):
            d[n] = max(d[n-2], d[n-3] + steps[n-1]) + steps[n]

        print(d[N])
    # 테이블 정의
    ## d[i] = i까지 얻을 수 있는 최대 값