N = int(input())

used_col = [False] * (N + 1)
used_diag1 = [False] * (2 * N)
used_diag2 = [False] * (2 * N)


def solution(k):
    global count, N

    # base condition
    if k == N + 1:
        count += 1
        return
    # 재귀
    for i in range(1, N + 1):
        if used_col[i] or used_diag1[N - (k - i)] or used_diag2[k + i - 1]:
            continue
        used_col[i] = True
        used_diag1[N - (k - i)] = True
        used_diag2[k + i - 1] = True
        solution(k + 1)
        used_col[i] = False
        used_diag1[N - (k - i)] = False
        used_diag2[k + i - 1] = False

count = 0
solution(1)
print(count)