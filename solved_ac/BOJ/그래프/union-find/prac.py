parent = [x for x in range(6)]

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    if parent_x < parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y

seq = [(0, 1), (1, 2), (1, 3), (0, 3)]

for a, b in seq:
    print(parent)
    if find(a) == find(b):
        print("cycle")
        break
    union(a, b)
