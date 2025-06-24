from collections import deque

N = int(input())

visited = [False for _ in range(10**6 + 1)]
count = 0
queue = deque()
queue.append((N, count))
while True:
    num, c = queue.popleft()
    if num == 1:
        count = c
        break

    divOf3 = num // 3
    if num % 3 == 0 and not visited[divOf3]:
        visited[divOf3] = True
        queue.append((divOf3, c + 1))

    divOf2 = num // 2
    if num % 2 == 0 and not visited[divOf2]:
        visited[divOf2] = True
        queue.append((divOf2, c + 1))

    if not visited[num - 1]:
        visited[num - 1] = True
        queue.append((num - 1, c + 1))
print(count)