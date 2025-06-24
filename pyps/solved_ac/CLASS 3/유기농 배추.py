import sys
sys.setrecursionlimit(10**6)

trials = int(input())
for i in range(trials):
    m, n ,k= map(int,input().split())

    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int,input().split())
        graph[j][i] = 1

    visited = [[False] * m for j in range(n)]

    def dfs(i,j):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        if visited[i][j] == True:
            return False
        visited[i][j] = True
        if graph[i][j] == 1:
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            return True
        else:
            return False

    result  = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1

    print(result)

