def getUpper(num):
    upper = 0
    while 2 ** upper <= num:
        upper += 1
    return upper - 1

def solution(r, c):
    if r <= 1 and c <= 1:
        return 2 * r + c

    r_upper = getUpper(r)
    c_upper = getUpper(c)

    plus = (2 * (2 ** (2 * r_upper)) if r_upper > 0 else 0) + (2 ** (2 * c_upper) if c_upper > 0 else 0)
    next_r = r - 2 ** r_upper if r_upper > 0 else r
    next_c = c - 2 ** c_upper if c_upper > 0 else c
    return solution(next_r, next_c) + plus

N, r, c = map(int, input().strip().split())

print(solution(r, c))
