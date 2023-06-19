import sys
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

result = [0]

def dfs(i,j,prev,result):
    if i == n-1 and j == m-1:
        result[0] += 1
        return True
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    if graph[i][j] >= prev:
        return False
    dfs(i-1,j,graph[i][j],result)
    dfs(i+1,j,graph[i][j],result)
    dfs(i,j-1,graph[i][j],result)
    dfs(i,j+1,graph[i][j],result)
dfs(0,0,graph[0][0]+1,result)
print(result[0])