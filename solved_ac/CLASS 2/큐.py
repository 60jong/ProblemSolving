import sys
from collections import deque

head = 0
tail = -1
lines = int(sys.stdin.readline())

queue = deque()
for _ in range(lines):
    command = sys.stdin.readline()

    if command.startswith('push'):
        queue.append(command.split()[1])
        tail = tail + 1

    if command.startswith('pop'):
        if tail - head >= 0:
            print(queue[head])
            head = head + 1
        else:
            print(-1)

    if command.startswith('size'):
        print(tail - head + 1)

    if command.startswith('front'):
        if tail - head >= 0:
            print(queue[head])
        else:
            print(-1)

    if command.startswith('empty'):
        if tail - head >= 0:
            print(0)
        else:
            print(1)

    if command.startswith('back'):
        if tail - head >= 0:
            print(queue[-1])
        else:
            print(-1)