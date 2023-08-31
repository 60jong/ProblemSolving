def solution(k):
    global max_count, N
    # print(k, eggs)
    # base condition
    if k == N:
        broken = 0
        for a, b in eggs:
            if a <= 0:
                broken += 1
        max_count = max(max_count, broken)
        return

    # recursion
    if eggs[k][0] > 0:
        found = False
        for i in range(N):
            if i != k and eggs[i][0] > 0:
                found = True
                eggs[i][0] = eggs[i][0] - eggs[k][1]
                eggs[k][0] = eggs[k][0] - eggs[i][1]
                solution(k + 1)
                eggs[k][0] = eggs[k][0] + eggs[i][1]
                eggs[i][0] = eggs[i][0] + eggs[k][1]
        if not found:
            solution(k + 1)
    else:
        solution(k + 1)


N = int(input())

eggs = [list(map(int, input().strip().split())) for _ in range(N)]
max_count = 0
solution(0)
print(max_count)
