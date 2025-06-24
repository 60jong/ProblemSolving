def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    total_memo = [[0] * (M + 1) for _ in range(N + 1)]

    memo = [[0] * (M + 1) for _ in range(N + 1)]

    for t, r1, c1, r2, c2, degree in skill:
        m = 1 if t == 2 else -1
        memo[r1][c1] += m * degree
        memo[r1][c2 + 1] -= m * degree
        memo[r2 + 1][c1] -= m * degree
        memo[r2 + 1][c2 + 1] += m * degree

    for m in range(M + 1):
        holder = 0
        for n in range(N + 1):
            holder += memo[n][m]
            total_memo[n][m] += holder

    holder = 0
    for n in range(N):
        for m in range(M + 1):
            holder += total_memo[n][m]
            if m != M:
                board[n][m] += holder
                if board[n][m] > 0:
                    answer += 1
    return answer
