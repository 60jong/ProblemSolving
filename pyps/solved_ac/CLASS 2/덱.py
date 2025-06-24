import sys
from collections import deque

lines = int(sys.stdin.readline())

queue = deque()
for _ in range(lines):
    command = sys.stdin.readline()

    if command.startswith('push_front'):
        queue.appendleft(command.split()[1])

    if command.startswith('push_back'):
        queue.append(command.split()[1])

    if command.startswith('pop_back'):
        if len(queue) > 0:
            print(queue.pop())
        else:
            print(-1)

    if command.startswith('pop_front'):
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)

    if command.startswith('size'):
        print(len(queue))

    if command.startswith('front'):
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)

    if command.startswith('empty'):
        if len(queue) > 0:
            print(0)
        else:
            print(1)

    if command.startswith('back'):
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
