from collections import deque

def bfs(myQueue):
    global k, visited

    while len(myQueue) > 0:
        num, layer = myQueue.popleft()
        if num == k:
            return layer
        else:
            canGo = [num - 1, num + 1, 2 * num]
            for c in canGo:
                if 0 <= c <= 200000 and (not visited[c]):
                    visited[c] = True
                    myQueue.append((c, layer + 1))

n, k = map(int, input().split())
if n == k:
    print(0)
else:
    visited = [False] * 200001
    layer = 1

    myQueue = deque()

    visited[n] = True
    canGo = [n - 1, n + 1, 2 * n]
    for c in canGo:
        if not visited[c]:
            myQueue.append((c, layer))

    print(bfs(myQueue))


