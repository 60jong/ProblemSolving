import sys

sentence = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()

stack = []
len_target = len(target)
for s in sentence:
    stack.append(s)
    if len(stack) >= len_target and ''.join(stack[-len_target:]) == target:
        for _ in range(len_target):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")