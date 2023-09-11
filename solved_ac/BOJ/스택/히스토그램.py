import sys

input = sys.stdin.readline

N = int(input())

square = 0

stack = []
for i in range(N):
    h = int(input())

    if h == 0:
        while stack:
            ph, idx = stack.pop()
            square = max(square, ph * (i - idx))
        continue

    store_idx = i
    while stack and stack[-1][0] > h:
        ph, idx = stack.pop()
        store_idx = idx
        square = max(square, ph * (i - idx))

    if stack:
        if stack[-1][0] < h:
            stack.append((h, store_idx))
    else:
        stack.append((h, store_idx))

while stack:
    ph, idx = stack.pop()
    square = max(square, ph * (N - idx))

print(square)