import sys

init = sys.stdin.readline().strip()
class Node:
    def __init__(self):
        self.p = None
        self.c = None
        self.n = None

nodes = [Node() for _ in range(len(init) + 1)]

for i in range(len(init)):
    if i == 0:
        nodes[i].p = None
        nodes[i].c = init[i]
        nodes[i].n = nodes[i + 1]
    elif i == len(init) - 1:
        nodes[i].p = nodes[i - 1]
        nodes[i].c = init[i]
        # 마지막 노드는 특별
        nodes[i].n = nodes[-1]
    else:
        nodes[i].p = nodes[i - 1]
        nodes[i].c = init[i]
        nodes[i].n = nodes[i + 1]

nodes[-1].p = nodes[-2]
nodes[-1].c = None
nodes[-1].n = None

# position은 커서 뒤 노드
position = nodes[-1]
first = nodes[0]

N = int(sys.stdin.readline())

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'L':
        if position.p is not None:
            position = position.p
    elif cmd[0] == 'D':
        if position.n is not None:
            position = position.n
    elif cmd[0] == 'B':
        if position.p is not None:
            temp = position.p.p
            if temp is not None:
                position.p.c = None # 삭제 노드의 c를 None으로
                position.p = temp
                temp.n = position

                if temp.p is None:
                    first = temp
            else:
                position.p.c = None
                position.p = temp
                first = position
    else:
        newNode = Node()
        newNode.c = cmd[1]
        if position.p is None:
            first = newNode
            newNode.p = None
            newNode.n = position
            position.p = newNode
        else:
            temp = position.p
            temp.n = newNode
            newNode.n = position
            newNode.p = temp
            position.p = newNode
while first.n is not None:
    print(first.c, end='')
    first = first.n

