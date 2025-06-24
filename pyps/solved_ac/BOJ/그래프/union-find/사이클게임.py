import sys

input = sys.stdin.readline

def find(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x
def union(parent, a, b):
    p_a, p_b = find(parent, a), find(parent, b)
    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b

def solution():
    N, M = map(int, input().split())
    parent = [i for i in range(N)]
    for m in range(M):
        a, b = map(int, input().split())
        if find(parent, a) == find(parent, b):
            return m + 1
        else:
            union(parent, a, b)
    return 0

print(solution())