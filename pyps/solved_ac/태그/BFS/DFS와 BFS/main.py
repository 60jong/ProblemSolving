from collections import deque

n, l, start = map(int,input().split())
graph = [[] for _ in range(n+1)]
bfs_visited = [False] * (n+1)
dfs_visited = bfs_visited[:]

for i in range(l):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

minNode = 0
for i in range(1,len(graph)):
    if len(graph[i]) != 0:
        minNode = i
        break

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while len(queue) > 0:
        nextNode = queue.popleft()
        print(nextNode, end=' ')
        for i in graph[nextNode]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i,visited)

dfs(graph,start,dfs_visited)
print()
bfs(graph,start,bfs_visited)

