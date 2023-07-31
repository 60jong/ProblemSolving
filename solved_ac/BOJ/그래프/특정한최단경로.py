from heapq import heapify, heappushpop
import sys

# def findDist(a, b, graph):

N, E = map(int, sys.stdin.readline().strip().split())

graph = [[1e9] * (N + 1) for _ in range(N + 1)]

for e in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = c
    graph[b][a] = c

d1, d2 = map(int, sys.stdin.readline().strip().split())


distance = [1e9] * (N + 1)
distance[N] = 0
visited = [False] * (N + 1)
heap = []
# N / d1 / d2 / E
# N / d2 / d1 / E-