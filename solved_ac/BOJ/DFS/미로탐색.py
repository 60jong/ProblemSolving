from collections import deque

N, M = map(int,input().split())

board = []
for n in range(N):
    line = input()
    temp = [l for l in line]
    board.append(temp)

visited = [[False for m in range(M)] for n in range(N)]

# init
queue = deque()
queue.append((0, 0, 1))
count = 1
visited[0][0] = True

while len(queue) > 0:
    y, x, c = queue.popleft()

    if y == N - 1 and x == M - 1:
        count = c
        break
    #상
    if y - 1 >= 0 and board[y - 1][x] == '1' and not visited[y - 1][x]:
        visited[y - 1][x] = True
        queue.append((y - 1, x, c + 1))
    #하
    if y + 1 < N and board[y + 1][x] == '1' and not visited[y + 1][x]:
        visited[y + 1][x] = True
        queue.append((y + 1, x, c + 1))
    #좌
    if x - 1 >= 0 and board[y][x - 1] == '1' and not visited[y][x - 1]:
        visited[y][x - 1] = True
        queue.append((y, x - 1, c + 1))
    #우
    if x + 1 < M and board[y][x + 1] == '1' and not visited[y][x + 1]:
        visited[y][x + 1] = True
        queue.append((y, x + 1, c + 1))

print(count)