from collections import deque
import sys

input = sys.stdin.readline
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().strip().split())

def count_waters(board, r, c):
    count = 0
    for d in dirs:
        nr, nc = r + d[0], c + d[1]
        if (0 <= nr < N and 0 <= nc < M) and board[nr][nc] == 0:
            count += 1
    return count

def is_all_connected(board, elements, total):
    q = deque()
    visited = [[False] * M for _ in range(N)]
    for r, c in elements:
        if board[r][c] > 0:
            visited[r][c] = True
            q.append((r, c))
            break

    visit_count = 0
    while q:
        visit_count += 1
        r, c = q.popleft()
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if (0 <= nr < N and 0 <= nc < M) and board[nr][nc] > 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))

    return True if visit_count == total else False

def solution():
    elements = []
    board = []
    for n in range(N):
        row = list(map(int, input().strip().split()))
        board.append(row)
        for m in range(M):
            if row[m] > 0:
                elements.append((n, m))
    total = len(elements)

    years = 0
    while total > 0 and is_all_connected(board, elements, total):
        years += 1
        minuses = []
        for r, c in elements:
            if board[r][c] > 0:
                minuses.append(count_waters(board, r, c))
            else:
                minuses.append(0)
        for i in range(len(minuses)):
            r, c = elements[i]
            if board[r][c] > 0 and board[r][c] <= minuses[i]:
                board[r][c] = 0
                total -= 1
            else:
                board[r][c] -= minuses[i]

    return years if total > 0 else 0

print(solution())