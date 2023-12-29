import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())

in_degree = [0] * (N + 1)
out_node = [[] for _ in range(N + 1)]
for _ in range(M):

    row = list(map(int, input().strip().split()))
    for r in range(1, len(row)):

        if r > 1:
            in_degree[row[r]] += 1

        if r < (len(row) - 1):
            out_node[row[r]].append(row[r + 1])

q = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)

count = 0
result = []
while q:
    n = q.popleft()

    # save result
    result.append(str(n))
    count += 1

    for on in out_node[n]:

        in_degree[on] -= 1
        if in_degree[on] == 0:
            q.append(on)

if count < N:
    print(0)
else:
    for r in result:
        print(r)