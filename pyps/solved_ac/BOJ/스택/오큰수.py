import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().strip().split()))

s = []
result = [0] * N
for i in range(N):
    while len(s) > 0 and s[-1] <= nums[N - 1 - i]:
        s.pop()

    if len(s) == 0:
        result[N - 1 - i] = -1
    else:
        result[N - 1 - i] = s[-1]
    s.append(nums[N - 1 - i])

print(' '.join(list(map(str, result))))
