import sys

input = sys.stdin.readline

# union-find
def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union(a, b):
    pa = get_parent(a)
    pb = get_parent(b)

    if pa < pb:
        parent[pb] = pa
    elif pa > pb:
        parent[pa] = pb

V, E = map(int, input().strip().split())

edges = []
parent = [i for i in range(V + 1)]

# input
for _ in range(E):
    a, b, c = map(int, input().strip().split())
    edges.append((c, a, b))

# edge sorting
edges = sorted(edges, key=lambda x: x[0], reverse=True)

conn_edges = 0
weights = 0
while edges and conn_edges < (V - 2):  # V - 1 개 -> stop
    cost, v1, v2 = edges.pop()
    if get_parent(v1) != get_parent(v2):
        union(v1, v2)
        conn_edges += 1
        weights += cost

print(weights)
