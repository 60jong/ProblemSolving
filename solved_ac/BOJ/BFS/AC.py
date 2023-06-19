import sys
from collections import deque

def doAC():
    commands = sys.stdin.readline().strip()
    nums = int(sys.stdin.readline().strip())
    numList = deque(sys.stdin.readline().strip()[1:-1].split(','))
    if nums == 0:
        numList = deque()

    order = 1
    for c in commands:
        if c == 'R':
            order *= -1
        if c == 'D':
            if len(numList) == 0:
                return 'error'
            elif order == 1:
                numList.popleft()
            else:
                numList.pop()

    if order == -1:
        numList.reverse()

    result = ','.join(numList)
    return '[' + result + ']'

T = int(sys.stdin.readline().strip())

while T > 0:
    print(doAC())
    T -= 1