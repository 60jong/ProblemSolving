from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n
    visitCount = 0

    queue = deque()
    while visitCount < n:
        for i in range(n):
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                visitCount += 1
                break
        while len(queue) > 0:

            node = queue.popleft()

            for i in range(n):
                if computers[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    visitCount += 1
                    queue.append(i)

        answer += 1

    return answer