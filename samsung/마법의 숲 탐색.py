from collections import deque

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def move_golem(cur_r, cur_c, cur_d):
    global forest

    # South
    s1, s2, s3 = (cur_r + 1, cur_c - 1), (cur_r + 2, cur_c), (cur_r + 1, cur_c + 1)
    if s2[0] < len(forest) and forest[s1[0]][s1[1]][0] == -1 and forest[s2[0]][s2[1]][0] == -1 and forest[s3[0]][s3[1]][0] == -1:
        return True, cur_r + 1, cur_c, cur_d

    # West & South
    w1, w2, w3 = (cur_r - 1, cur_c - 1), (cur_r, cur_c - 2), (cur_r + 1, cur_c - 1)

    if w2[1] >= 0 and forest[w1[0]][w1[1]][0] == -1 and forest[w2[0]][w2[1]][0] == -1 and forest[w3[0]][w3[1]][0] == -1:
        ws1, ws2, ws3 = (w1[0] + 1, w1[1]), (w2[0] + 1, w2[1]), (w3[0] + 1, w3[1])
        if ws3[0] < len(forest) and forest[ws1[0]][ws1[1]][0] == -1 and forest[ws2[0]][ws2[1]][0] == -1 and forest[ws3[0]][ws3[1]][0] == -1:
            return True, cur_r + 1, cur_c - 1, (cur_d - 1) % 4

    # East & South
    e1, e2, e3 = (cur_r - 1, cur_c + 1), (cur_r, cur_c + 2), (cur_r + 1, cur_c + 1)
    if e2[1] < len(forest[0]) and forest[e1[0]][e1[1]][0] == -1 and forest[e2[0]][e2[1]][0] == -1 and forest[e3[0]][e3[1]][0] == -1:
        es1, es2, es3 = (e1[0] + 1, e1[1]), (e2[0] + 1, e2[1]), (e3[0] + 1, e3[1])
        if es3[0] < len(forest) and forest[es1[0]][es1[1]][0] == -1 and forest[es2[0]][es2[1]][0] == -1 and forest[es3[0]][es3[1]][0] == -1:
            return True,  cur_r + 1, cur_c + 1, (cur_d + 1) % 4
    return False, cur_r, cur_c, cur_d


def solution(c, d, idx):
    global forest
    cur_r, cur_c, cur_d = 1, c, d # Center positions of a golem

    ## Move ##
    while True:
        moved, cur_r, cur_c, cur_d = move_golem(cur_r, cur_c, cur_d)
        if not moved:
            # Checks whether golem is entered into forest
            if cur_r < 4:
                forest = [[[-1, False] for _c in range(C)] for _r in range(R + 3)]
                return 0
            else:
                break

    # Fills golem to forest - n, e, s, w, c
    cells = [(cur_r - 1, cur_c), (cur_r, cur_c + 1), (cur_r + 1, cur_c), (cur_r, cur_c - 1), (cur_r, cur_c)]
    for cell in cells:
        forest[cell[0]][cell[1]][0] = idx

    door_cell = cells[cur_d]
    forest[door_cell[0]][door_cell[1]][1] = True

    # Find path to most southern row
    southern = cur_r

    q = deque()
    visited = [[False] * len(forest[0]) for _ in range(len(forest) + 3)]

    q.append((cur_r, cur_c, idx))
    visited[cur_r][cur_c] = True

    count = 1
    while q:
        count += 1
        r_, c_, gi = q.popleft()
        southern = max(southern, r_)

        # Base condition
        if southern == len(forest) - 1:
            return southern - 2

        for dr, dc in dirs:
            nr, nc = r_ + dr, c_ + dc
            if 3 <= nr < len(forest) and 0 <= nc < len(forest[0]) and forest[nr][nc][0] > -1:
                if not visited[nr][nc]:
                    if forest[nr][nc][0] == gi:
                        q.append((nr, nc, gi))
                        visited[nr][nc] = True
                    else:
                        # Transfer to another golem
                        if forest[r_][c_][1]:
                            q.append((nr, nc, forest[nr][nc][0]))
                            visited[nr][nc] = True
    return southern - 2 # (-3 + 1)


R, C, K = map(int, input().strip().split())
forest = [[[-1, False] for _c in range(C)] for _r in range(R + 3)] # [golem_id, is_door] & 0th row is start point

answer = 0

for k in range(K):
    c, d = map(int, input().strip().split())
    answer += solution(c - 1, d, k)

print(answer)
