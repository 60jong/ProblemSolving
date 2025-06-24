import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

stack = []

result = [0] * N
for i in range(N - 1, -1, -1):
    if stack:
        while stack and stack[-1][0] < nums[i]:
            num, idx = stack.pop()
            result[idx] = i + 1
        stack.append((nums[i], i))
    else:
        stack.append((nums[i], i))

while stack:
    num, idx = stack.pop()
    result[idx] = 0

print(' '.join(map(str, result)))