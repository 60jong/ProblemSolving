from itertools import combinations as cmb, product
from collections import defaultdict
import math


def remain_cmb(N, cmb):
    cmb_set = set(cmb)

    remain = []
    for n in range(N):
        if n not in cmb_set:
            remain.append(n)

    return tuple(remain)


def solution(dice):
    N = len(dice)
    combs = math.comb(N, N // 2)
    max_wins = 0
    max_comb = ()

    comb_count = 0
    # (10 C 5) * (6 ** 5 + 500 * 2)
    for c in cmb(range(N), N // 2):
        comb_count += 1

        rc = remain_cmb(N, c)

        count_c, count_rc = defaultdict(int), defaultdict(int)
        for p in product(*list(map(lambda x: dice[x], c))):
            count_c[sum(p)] += 1
        for p in product(*list(map(lambda x: dice[x], rc))):
            count_rc[sum(p)] += 1

        c_keys, rc_keys = sorted(list(count_c.keys())), sorted(list(count_rc.keys()))

        # 투 포인터로 승수 계산
        ci, ri = 0, 0
        wins, cumul = 0, 0
        while ci < len(c_keys):
            while ri < len(rc_keys) and rc_keys[ri] < c_keys[ci]:
                cumul += count_rc[rc_keys[ri]]
                ri += 1
            wins += count_c[c_keys[ci]] * cumul
            ci += 1

        if max_wins < wins:
            max_wins = wins
            max_comb = tuple(map(lambda x: x + 1, c))

    return sorted(list(max_comb))