answer = int(1e9)
inject_dir = (-1, 0, 1)

def is_valid(grid, inject_grid, K):
    for w in range(len(grid[0])):
        cell_type = grid[0][w] if inject_grid[0] == -1 else inject_grid[0]
        cell_idx = 0
        max_seq = 1

        for i in range(1, len(grid)):
            cur_cell_type = grid[i][w] if inject_grid[i] == -1 else inject_grid[i]
            if cur_cell_type != cell_type:
                max_seq = max(max_seq, i - cell_idx)

                cell_type = cur_cell_type
                cell_idx = i
        max_seq = max(max_seq, len(grid) - cell_idx)
        if max_seq < K:
            return False
    return True


def dfs(grid, inject, stack, K):
    global answer

    d, inject_type, inject_cnt = stack.pop()

    # Base condition
    if d >= len(grid) or inject_cnt >= K:
        if is_valid(grid, inject, K):
            answer = min(answer, inject_cnt)
        return

    for i_d in inject_dir:
        next_inject_cnt = inject_cnt
        if i_d != -1:
            next_inject_cnt += 1

        stack.append((d + 1, i_d, next_inject_cnt))

        inject_hold = inject[d]
        inject[d] = i_d

        dfs(grid, inject, stack, K)

        # Rollback
        inject[d] = inject_hold


def solution():
    global answer

    D, W, K = map(int, input().strip().split())
    answer = K

    grid = [list(map(int, input().strip().split())) for _ in range(D)]
    inject = [-1] * D # -1 : empty / 0 : A / 1 : B

    # Early returns
    if K == 1:
        return 0
    if K == D:
        if is_valid(grid, inject, K):
            return 0

    # DFS
    for i_d in inject_dir:
        inject_cnt = 0
        if i_d != -1:
            inject_cnt += 1

        stack = [(0, i_d, inject_cnt)]
        inject[0] = i_d

        dfs(grid, inject, stack, K)

        inject[0] = -1

    return answer


T = int(input())

for t in range(1, T + 1):
    print('#{} {}'.format(t, solution()))
