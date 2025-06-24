from heapq import heappop, heappush, heapify


def dijkstra(start):
    if calculated[start]:
        return

    distance = distances[start]
    pq = []

    distance[start] = 0
    heappush(pq, (0, start))

    while pq:
        w, v = heappop(pq)

        if distance[v] < w:
            continue

        for nv in adjacents[v]:
            new_dist = w + cities[v][nv]
            if new_dist < distance[nv]:
                distance[nv] = new_dist
                heappush(pq, (distance[nv], nv))
    calculated[start] = True


def cell_product():
    if len(products) == 0 or products[0][0] > 0:
        print(-1)
    else:
        value, id, r, d = heappop(products)
        if removed[id]:
            cell_product()
        else:
            print(id)


Q = int(input())

INF = int(1e9)
cities = [[INF] * 2000 for _ in range(2000)]
for c in range(2000):
    cities[c][c] = 0
adjacents = dict(zip(range(2000), [dict() for _ in range(2000)]))

distances = [[INF] * 2000 for _ in range(2000)]
for i in range(2000):
    distances[i][i] = 0

calculated = [False] * 2000

land_elements = list(map(int, input().strip().split()))
N, M = land_elements[1], land_elements[2]
for i in range(M):
    v1, v2, w = land_elements[3 * (i + 1)], land_elements[3 * (i + 1) + 1], land_elements[3 * (i + 1) + 2]
    if v1 == v2:
        continue

    cities[v1][v2] = min(cities[v1][v2], w)
    cities[v2][v1] = min(cities[v2][v1], w)

    adjacents[v1][v2] = 0
    adjacents[v2][v1] = 0

# Find shortest distance
products = []
removed = [True] * 30001
s = 0
dijkstra(s)

for _ in range(Q - 1):
    row = list(map(int, input().strip().split()))

    if row[0] == 200:
        # create_product
        id, revenue, dest = row[1], row[2], row[3]
        value = revenue - distances[s][dest]

        heappush(products, (-1 * value, id, revenue, dest))
        removed[id] = False

    elif row[0] == 300:
        removed[row[1]] = True
    elif row[0] == 400:
        cell_product()
    else:  # 500
        if s == row[1]:
            continue

        s = row[1]
        dijkstra(s)

        # update product pq
        temp = []
        for value, id, revenue, dest in products:
            new_value = revenue - distances[s][dest]
            temp.append((-1 * new_value, id, revenue, dest))

        heapify(temp)
        products = temp