from collections import deque


def find_stuffs(grid):
    value = 0
    stuffs = []
    visited = [[False] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                history = [(i, j)]

                while q:
                    r, c = q.popleft()

                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and grid[nr][nc] == grid[r][c]:
                            visited[nr][nc] = True
                            history.append((nr, nc))
                            q.append((nr, nc))
                if len(history) >= 3:
                    value += len(history)
                    stuffs.extend(history)
    return stuffs


def rotate(grid, r, c, degree):
    if degree < 1:
        return

    tmp1, tmp2 = grid[r - 1][c], grid[r - 1][c - 1]

    grid[r - 1][c] = grid[r][c - 1]
    grid[r - 1][c - 1] = grid[r + 1][c - 1]
    grid[r][c - 1] = grid[r + 1][c]
    grid[r + 1][c - 1] = grid[r + 1][c + 1]
    grid[r + 1][c] = grid[r][c + 1]
    grid[r + 1][c + 1] = grid[r - 1][c + 1]
    grid[r][c + 1] = tmp1
    grid[r - 1][c + 1] = tmp2
    rotate(grid, r, c, degree - 1)


def get_stuff_values(grid, wi):
    init = 0
    values = 0

    while True:
        stuffs = find_stuffs(grid)

        if init == 0:
            init = len(stuffs)

        if len(stuffs) == 0:
            break
        values += len(stuffs)

        # fill
        stuffs.sort(key=lambda x: (x[1], -x[0]))
        for r, c in stuffs:
            grid[r][c] = wall_num[wi % M]
            wi += 1

    return init, values


K, M = map(int, input().strip().split())

grid = [list(map(int, input().strip().split())) for _ in range(5)]
wall_num = list(map(int, input().strip().split()))
wi = 0

centers = [(j, i) for i in range(1, 4) for j in range(1, 4)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

answer = []
for k in range(K):
    max_values = [0, 0, []]

    for d in range(1, 4):
        for r, c in centers:
            origin_grid = [[i for i in grid[j]] for j in range(5)]

            rotate(grid, r, c, d)
            init, value = get_stuff_values(grid, wi)

            if init > max_values[0]:
                max_values[0] = init
                max_values[1] = value
                max_values[2] = [[i for i in grid[j]] for j in range(5)]
            grid = origin_grid

    grid = max_values[2]
    wi = wi + max_values[1]
    if max_values[0] > 0:
        answer.append(str(max_values[1]))
    else:
        break

print(' '.join(answer))