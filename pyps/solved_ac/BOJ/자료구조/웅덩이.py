import sys
N, L = map(int, sys.stdin.readline().split(' '))

stack = list()
for _ in range(N):
    stack.append(list(map(int, sys.stdin.readline().split(" "))))

stack = sorted(stack, key=lambda x:-1 * x[0])
count = 0
while len(stack) > 0:
    if stack[-1][0] >= stack[-1][1]:
        popped = stack.pop()
        if len(stack) > 0:
            if popped[0] > stack[-1][0]:
                stack[-1][0] = popped[0]
                continue
        else:
            break

    # 웅덩이 수
    halls = stack[-1][1] - stack[-1][0]
    plates = (halls // L) + 1 if halls % L > 0 else halls // L
    stack[-1][0] = stack[-1][0] + plates * L
    count += plates

print(count)