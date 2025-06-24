from collections import deque

N = int(input())

for n in range(N):
    num = int(input())
    queue = deque()
    queue.append((num))

    methods = 0
    while len(queue) > 0:
        poppedNum = queue.popleft()
        if poppedNum < 0:
            continue
        if poppedNum == 0:
            methods += 1

        queue.append(poppedNum - 1)
        queue.append(poppedNum - 2)
        queue.append(poppedNum - 3)
    print(methods)