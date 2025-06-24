from collections import deque

def D(register):
    register = register * 2 % 10000
    return register

def S(register):
    register = register - 1 if register > 0 else 9999
    return register

def L(register):
    tail = register // 1000
    head = (register % 1000) // 100
    return head * 1000 + (register * 10 + tail) % 1000
def R(register):
    head = register % 10
    return head * 1000 + register // 10

T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    visited = [False for _ in range(10000)]

    queue = deque()
    queue.append((A, ''))
    visited[A] = True

    command = ''
    while len(queue) > 0:
        register, accumCommand = queue.popleft()

        if register == B:
            command = accumCommand
            break
        #D
        dr = D(register)
        if not visited[dr]:
            queue.append((dr, accumCommand + 'D'))
            visited[dr] = True
        #S
        sr = S(register)
        if not visited[sr]:
            queue.append((sr, accumCommand + 'S'))
            visited[sr] = True
        #L
        lr = L(register)
        if not visited[lr]:
            queue.append((lr, accumCommand + 'L'))
            visited[lr] = True
        #R
        rr = R(register)
        if not visited[rr]:
            queue.append((rr, accumCommand + 'R'))
            visited[rr] = True

    print(command)