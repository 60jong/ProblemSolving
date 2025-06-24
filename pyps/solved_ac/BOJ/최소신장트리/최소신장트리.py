import sys

input = sys.stdin.readline

V, E = map(int, input().strip().split())

parent = [i for i in range(V + 1)]
def get_parent(a):
    if parent[a] == a:
        return a
    parent[a] = get_parent(parent[a])
    return parent[a]

def union(a, b):
    ap = get_parent(a)
    bp = get_parent(b)

    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp

def is_diff(a, b):
    return get_parent(a) != get_parent(b)

edges = []
for _ in range(E):
    a, b, c = map(int, input().strip().split())
    edges.append((c, a, b))

weight = 0
e = 0
edges.sort() # ElogE
for cost, v1, v2 in edges:
    if e == (V - 1):
        break
    if is_diff(v1, v2):
        union(v1, v2)
        weight += cost
        e += 1

print(weight)

