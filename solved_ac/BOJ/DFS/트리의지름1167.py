import sys
def findFarthest(start):
    global conn

    maxNode = 0
    maxDist = 0
    stack = [(start, 0)]
    visited = [False for _ in range(len(conn))]
    visited[start] = True

    distances = []
    while len(stack) > 0:
        cur, dist = stack.pop()

        isEndpoint = True
        for i, j in conn[cur]:
            if not visited[i]:
                visited[i] = True
                isEndpoint = False
                stack.append((i, dist + j))
        if isEndpoint:
            if dist > maxDist:
                maxDist = dist
                maxNode = cur
    return maxNode, maxDist


V = int(sys.stdin.readline().strip())

conn = [[] for v in range(V + 1)]
for v in range(1, V + 1):
    row = list(map(int, sys.stdin.readline().strip().split()))
    rowDiv = (len(row) - 2) // 2
    for i in range(1, rowDiv + 1):
        conn[row[0]].append((row[2 * i - 1], row[2 * i]))

randStart = 0
for i in range(len(conn)):
    if len(conn[i]) > 0:
        randStart = i
        break

farthest, dist = findFarthest(randStart)
print(findFarthest(farthest)[1])
