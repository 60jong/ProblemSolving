from collections import deque

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(land, visited, count_by_col, i, j):
    count = 1
    col_set = set()
    q = deque()

    q.append((i, j))
    visited[i][j] = True
    col_set.add(j)
    while q:
        r, c = q.popleft()

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(visited) and 0 <= nc < len(visited[0]) and not visited[nr][nc] and land[nr][nc] == 1:
                count += 1
                q.append((nr, nc))
                visited[nr][nc] = True
                col_set.add(nc)
    # Increase count for each col
    for c in col_set:
        count_by_col[c] += count


def solution(land):
    count_by_col = [0] * len(land[0])

    visited = [[False] * len(land[0]) for _ in range(len(land))]

    for j in range(len(land[0])):
        for i in range(len(land)):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(land, visited, count_by_col, i, j)

    return max(count_by_col)


land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1]]
print(solution(land))

## Programmers 아날로그 시계
def get_hour_position(hour, minute, second):
    return 3600 * (hour % 12) + 1 * (minute * 60 + second)


def get_minute_position(hour, minute, second):
    return 720 * minute + 12 * second


def get_second_position(hour, minute, second):
    return 720 * second


def get_duration_seconds(h1, m1, s1, h2, m2, s2):
    return 3600 * (h2 - h1) + 60 * (m2 - m1) + s2 - s1


def solution(h1, m1, s1, h2, m2, s2):
    total_ticks = 43_200

    # get init position
    init_h = get_hour_position(h1, m1, s1)
    init_m = get_minute_position(h1, m1, s1)
    init_s = get_second_position(h1, m1, s1)

    answer = 0
    if init_h == init_s or init_m == init_s:
        answer += 1

    # check position transition
    dur = get_duration_seconds(h1, m1, s1, h2, m2, s2)
    while dur > 0:
        init_s += 720
        init_m += 12
        init_h += 1

        add = 0

        if 0 <= (init_s - init_h) < (720 - 1):
            add += 1
        if 0 <= (init_s - init_m) < (720 - 12):
            add += 1
        if add == 2 and init_m == init_h:
            add = 1

        answer += add
        dur -= 1
        init_s %= total_ticks
        init_m %= total_ticks
        init_h %= total_ticks

    return answer
