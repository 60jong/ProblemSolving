board = [input() for _ in range(5)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

result = 0
arr = []
visited = [[False] * 5 for _ in range(5)]
def solution(k):
    global result
    # base condition
    if k == 8:
        count = 0
        for r, c in arr:
            if board[r][c] == 'S':
                count += 1
        if count >= 4:
            result += 1
        print('count', count, [board[ar][ac] for ar, ac in arr])
        return

    # recursion
    if k == 1:
        for r in range(5):
            for c in range(5):
                visited[r][c] = True
                arr.append((r, c))
                solution(2)
                arr.pop()
                visited[r][c] = False
    else:
        for d in dirs:
            nr, nc = arr[-1][0] + d[0], arr[-1][1] + d[1]
            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                visited[nr][nc] = True
                arr.append((nr, nc))
                solution(k + 1)
                arr.pop()
                visited[nr][nc] = False

solution(1)