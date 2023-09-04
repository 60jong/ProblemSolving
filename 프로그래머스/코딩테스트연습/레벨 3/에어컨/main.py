stack = []
dirs = [(-1, 0, 'u'), (0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l')]
visit_count = []
answer = ''

def func(stack, visit_count, N, M, R, C, K):
    global answer
    if len(stack) == K + 1:
        if stack[-1][0] == R and stack[-1][1] == C:
            route = ''.join(map(lambda x : x[2], stack))
            answer = min(route, answer)
        return

    for d in dirs:
        nx, ny = stack[-1][0] + d[0], stack[-1][1] + d[1]
        if 1 <= nx <= N and 1 <= ny <= M and visit_count[nx][ny] > 0:
            visit_count[nx][ny] = visit_count[nx][ny] - 1
            stack.append((nx, ny, d[2]))

            func(stack, visit_count, N, M, R, C, K)

            visit_count[nx][ny] = visit_count[nx][ny] + 1
            stack.pop()


def solution(n, m, x, y, r, c, k):
    global answer

    answer = 'z' * k
    visit_count = [[1 + (k - (abs(x - r) + abs(y - c))) // 2] * (m + 1) for _ in range(n + 1)]
    stack = [(x, y, '')]
    func(stack, visit_count, n, m, r, c, k)

    return answer

print(solution(2,2,1,1,2,2,2))