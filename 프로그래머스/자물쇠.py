def rotate(key, offset):
    M = len(key)
    r_key = [k[:] for k in key]
    if offset == 0:
        return r_key
    elif offset == 1:
        for r in range(M):
            for c in range(M):
                r_key[r][c] = key[M - 1 - c][r]
    elif offset == 2:
        for r in range(M):
            for c in range(M):
                r_key[r][c] = key[M - 1 - r][M - 1 - c]
    elif offset == 3:
        for r in range(M):
            for c in range(M):
                r_key[r][c] = key[c][M - 1 - r]
    return r_key


def fill_lock(i, j, key, lock):
    M = len(key)
    W = len(lock)
    for r in range(i, i + M):
        for c in range(j, j + M):
            lock[r][c] = lock[r][c] + key[r - i][c - j]
    for r in range(M - 1, W - (M - 1)):
        for c in range(M - 1, W - (M - 1)):
            if lock[r][c] != 1:
                return False
    return True


def solution(key, lock):
    M = len(key)
    N = len(lock)
    W = N + 2 * (M - 1)

    exp_lock = [[0] * W for _ in range(W)]
    for r in range(M - 1, W - (M - 1)):
        for c in range(M - 1, W - (M - 1)):
            exp_lock[r][c] = lock[r - (M - 1)][c - (M - 1)]

    for o in range(4):
        r_key = rotate(key, o)
        for i in range(W - (M - 1)):
            for j in range(W - (M - 1)):
                cp_exp_lock = [l[:] for l in exp_lock]
                if fill_lock(i, j, r_key, cp_exp_lock):
                    return True

    return False