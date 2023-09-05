from collections import deque


def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    if k < dist or (k - dist) % 2 == 1: return 'impossible'

    answer = 'z' * k
    dirs = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]

    q = deque()
    q.append((x, y, ''))
    while q:
        x, y, route = q.popleft()

        if x == r and y == c and len(route) == k:
            answer = min(answer, route)
            continue

        for d in dirs:
            nx, ny = x + d[0], y + d[1]

            if 1 <= nx <= n and 1 <= ny <= m:
                if (k - len(route)) >= (abs(nx - r) + abs(ny - c)):
                    q.append((nx, ny, route + d[2]))
                    break

    return answer

print(solution(2,2,1,1,2,2,2))