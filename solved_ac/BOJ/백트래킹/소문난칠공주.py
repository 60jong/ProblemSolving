from collections import deque

def check_dasom(arr):
    count = 0
    for i, j in arr:
        if board[i][j] == 'S':
            count += 1
    if count >= 4:
        return True
    else:
        return False

def check_adjacent(arr):
    count = 0
    used = [[False] * 5 for _ in range(5)]
    q = deque()
    q.append(arr[0])
    used[arr[0][0]][arr[0][1]] = True
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        r, c = q.popleft()
        count += 1
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if (nr, nc) in arr and not used[nr][nc]:
                used[nr][nc] = True
                q.append((nr, nc))
    return True if count == 7 else False

def get_after_sets(a, b):
    sets = []
    for i in range(5):
        for j in range(5):
            if i == a:
                if j > b:
                    sets.append((i, j))
            elif i > a:
                sets.append((i, j))
    return sets
def solution(k):
    global result

    # base condition
    if k == 8:
        if check_adjacent(arr) and check_dasom(arr):
            result += 1
        return

    # recursion
    if k == 1:
        afterSets = [(i, j) for i in range(5) for j in range(5)]
    else:
        afterSets = get_after_sets(arr[-1][0], arr[-1][1])
    for i, j in afterSets:
        if not visited[i][j]:
            visited[i][j] = True
            arr.append((i, j))
            # print(k, i, j, arr)
            solution(k + 1)
            arr.pop()
            visited[i][j] = False

board = [input() for _ in range(5)]

visited = [[False] * 5 for _ in range(5)]
result = 0
arr = []

solution(1)
print(result)