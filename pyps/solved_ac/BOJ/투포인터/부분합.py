import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

numbers = list(map(int, input().strip().split()))

sum = numbers[0]
h = 0
t = 1

result = N + 1
while h < t:
    if sum >= M:
        result = min(result, t - h)

        sum -= numbers[h]
        h += 1
    else:
        if t >= N:
            break
        sum += numbers[t]
        t += 1

if result > N:
    print(0)
else:
    print(result)