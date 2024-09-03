count = 0


def dfs(h, v, l, r, row, stack):
    global count
    N = len(h)

    # End of board
    if row == N:
        count += 1
        return

    for n in range(N):
        nr, nc = row, n
        if h[nr] == 0 and v[nc] == 0 and l[N - (nc - nr) - 1] == 0 and r[nr + nc] == 0:
            stack.append((nr, nc))
            h[nr] = 1
            v[nc] = 1
            l[N - (nc - nr) - 1] = 1
            r[nr + nc] = 1

            dfs(h, v, l, r, row + 1, stack)

            h[nr] = 0
            v[nc] = 0
            l[N - (nc - nr) - 1] = 0
            r[nr + nc] = 0
            stack.pop()


N = int(input())

grid = [[0] * N for _ in range(N)]

horiz = [0] * N
vert = [0] * N
l_diag = [0] * (2 * N - 1)
r_diag = [0] * (2 * N - 1)

dfs(horiz, vert, l_diag, r_diag, 0, [])
print(count)