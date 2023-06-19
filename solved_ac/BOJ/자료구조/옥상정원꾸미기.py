import sys
N = int(sys.stdin.readline())

heights = [int(sys.stdin.readline()) for _ in range(N)]

# (높이, 누적) 리스트
stack = []
result = 0

for i in range(N - 1, -1, -1):
    cumul = 0
    while len(stack) > 0 and heights[i] > stack[-1][0]:
        h, c = stack.pop()
        result += c
        cumul += 1 + c

    stack.append((heights[i], cumul))

while len(stack) > 0 :
    h, c = stack.pop()
    result += c

print(result)




