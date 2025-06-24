from collections import deque

n, k = map(int, input().split())

if n >= k:
    print(n - k)
    print(1)
else:
    visited = [False] * 100001
    store = [[0, 0] for _ in range(100001)] # [layer, duplicates]

    answer = 0

    myQ = deque()
    # start
    layer = 1
    visited[n] = True
    canGo = [n - 1, n + 1, 2 * n]
    for c in canGo:
        if 0 < c <= 100000:
            if not visited[c]:
                visited[c] = True
                store[c][0] = layer
                store[c][1] += 1
                myQ.append((c, layer))
            else:
                if store[c][0] == layer:
                    store[c][1] += 1
    # next layer
    while len(myQ) > 0:
        num, layer = myQ.popleft()

        if num == k:
            answer = store[num][0]
            break
        else:
            canGo = [num - 1, num + 1, 2 * num]
            for c in canGo:
                if 0 < c <= 100000:
                    if not visited[c]:
                        visited[c] = True
                        store[c][0] = layer + 1
                        store[c][1] = store[num][1]
                        myQ.append((c, layer + 1))
                    else:
                        if store[c][0] == layer + 1:
                            store[c][1] += store[num][1]
    print(store[k][0])
    print(store[k][1])
