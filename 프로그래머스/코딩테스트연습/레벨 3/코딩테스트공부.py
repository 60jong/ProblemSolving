
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
def get_usables(a, c, p):
    u = []
    for _p in p:
        if a >= _p[0] and c >= _p[1]:
            u.append(_p)
    return u

def solution(alp, cop, problems):
    ma, mc = alp, cop
    for p in problems:
        ma = max(ma, p[0])
        mc = max(mc, p[1])

    store = [[ma + mc - alp - cop] * (mc + 1) for _ in range(ma + 1)]

    store[alp][cop] = 0
    for a in range(alp, ma + 1):
        for c in range(cop, mc + 1):
            usables = [[a, c, 1, 0, 1], [a, c, 0, 1, 1]]
            usables.extend(get_usables(a, c, problems))

            for u in usables:
                store[min(ma, a + u[2])][min(mc, c + u[3])] = min(store[min(ma, a + u[2])][min(mc, c + u[3])], store[a][c] + u[4])
    return store[ma][mc]