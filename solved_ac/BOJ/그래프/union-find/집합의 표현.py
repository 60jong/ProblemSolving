import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().strip().split())


def find(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]

def union(parent, a, b):
    if a == b:
        return
    p_a, p_b = find(parent, a), find(parent, b)
    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b

parent = [n for n in range(N + 1)]
for _ in range(M):
    op, a, b = map(int, input().strip().split())

    if op == 1:
        if find(parent, a) == find(parent, b):
            print('YES')
        else:
            print('NO')
    else: # 합치기
        union(parent, a, b)