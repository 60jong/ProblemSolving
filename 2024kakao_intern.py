# 1
from itertools import combinations as cmb


def solution(friends, gifts):
    F = len(friends)

    # 선물 지수
    gs = dict(zip(friends, [0] * F))
    # 선물 관계
    t = [dict(zip(friends, [0] * F)) for _ in range(F)]
    gr = dict(zip(friends, t))

    for g in gifts:
        a, b = g.split()
        # 선물 지수
        gs[a] += 1
        gs[b] -= 1

        # 선물 관계
        gr[a][b] += 1
        gr[b][a] -= 1

    takes = [0] * F
    for A, B in cmb(range(F), 2):
        fa, fb = friends[A], friends[B]
        # A <- B
        if gr[fa][fb] > 0:
            takes[A] += 1
        # A -> B
        elif gr[fa][fb] < 0:
            takes[B] += 1
        # 같은 갯수 -> 선물 지수 비교
        else:
            # A <- B
            if gs[fa] > gs[fb]:
                takes[A] += 1
            # A -> B
            elif gs[fa] < gs[fb]:
                takes[B] += 1

    return max(takes)


# 2
from collections import defaultdict


def solution(edges):
    graph = defaultdict(list)
    idg, odg = defaultdict(int), defaultdict(int)

    for a, b in edges:
        idg[a] += 0
        odg[a] += 1

        idg[b] += 1
        odg[b] += 0

        graph[a].append(b)

    # new_v, 8자 찾기 -> N
    new_v = -1
    for v in idg:
        if odg[v] >= 2:
            if idg[v] == 0:
                new_v = v

    donuts, sticks, eights = 0, 0, 0
    for v in graph[new_v]:
        real_idg = idg[v] - 1
        # 막대 시작
        if real_idg == 0:
            sticks += 1
        # 8자 중앙
        elif real_idg == 2:
            eights += 1
        # 원래 idg가 1이면
        # 막대 중간 (계속 가면 끝) or
        # 도넛 중간 (돌아서 자기 자신 + 모두 odg 1) or
        # 8자 중간  (돌아서 자기 자신 + 중간에 odg 2)
        else:
            # 막대 끝
            if v not in graph:
                sticks += 1
                continue

            visited = {v}
            while True:
                v = graph[v][0]
                if v not in graph:
                    sticks += 1
                    break
                # 8자 중앙
                if odg[v] >= 2:
                    eights += 1
                    break
                # 도넛
                if v in visited:
                    donuts += 1
                    break
    return [new_v, donuts, sticks, eights]


# 3


# 4 8
answer = 1


def dfs(r, cards, oh, coin, target):
    global answer

    # print(r, cards, oh, coin)
    # 카드 부족 -> 종료
    if len(cards) == 0:
        answer = max(answer, r)
        return

    remain = oh[1]

    # case 1, 뽑은 2장 버림 -> on_hand에서

    c1, c2 = cards.pop(), cards.pop()

    if oh[0] > 0:
        oh[0] -= 1

        dfs(r + 1, cards, oh, coin, target)

        oh[0] += 1
    else:
        answer = max(answer, r)

    cards.extend([c2, c1])

    if coin > 0:
        c1, c2 = cards.pop(), cards.pop()
        # case 2, c1 get
        coin -= 1

        if (target - c1) in remain:
            oh[0] += 1
            remain.remove(target - c1)

            oh[0] -= 1
            dfs(r + 1, cards, oh, coin, target)
            oh[0] += 1

            remain.add(target - c1)
            oh[0] -= 1
        else:
            if oh[0] > 0:
                oh[0] -= 1
                remain.add(c1)

                dfs(r + 1, cards, oh, coin, target)

                remain.remove(c1)
                oh[0] += 1
            else:
                answer = max(answer, r)

        coin += 1

        cards.extend([c2, c1])
        # case 3, c2 get
        c1, c2 = cards.pop(), cards.pop()
        coin -= 1

        if (target - c2) in remain:
            oh[0] += 1
            remain.remove(target - c2)

            oh[0] -= 1
            dfs(r + 1, cards, oh, coin, target)
            oh[0] += 1

            remain.add(target - c2)
            oh[0] -= 1
        else:
            if oh[0] > 0:
                oh[0] -= 1
                remain.add(c2)

                dfs(r + 1, cards, oh, coin, target)

                remain.remove(c2)
                oh[0] += 1
            else:
                answer = max(answer, r)
        coin += 1
        cards.extend([c2, c1])
        # case 4, c1, c2 get
        if coin >= 2:
            c1, c2 = cards.pop(), cards.pop()
            coin -= 2

            if (target - c1) in remain:
                oh[0] += 1
                remain.remove(target - c1)
            else:
                remain.add(c1)

            if (target - c2) in remain:
                oh[0] += 1
                remain.remove(target - c2)
            else:
                remain.add(c2)

            if oh[0] > 0:
                oh[0] -= 1

                dfs(r + 1, cards, oh, coin, target)

                oh[0] += 1
            else:
                answer = max(answer, r)

            # 복구
            if c2 in remain:
                remain.remove(c2)
            else:
                oh[0] -= 1
                remain.add(target - c2)

            if c1 in remain:
                remain.remove(c1)
            else:
                oh[0] -= 1
                remain.add(target - c1)

            coin += 2
            cards.extend([c2, c1])


def solution(coin, cards):
    global answer

    N = len(cards)
    target = N + 1

    avail = 0
    remain = set()
    for c in cards[: N // 3]:
        if (target - c) in remain:
            remain.remove(target - c)
            avail += 1
        else:
            remain.add(c)
    # print(avail, remain)

    cards = cards[N // 3:]
    cards.reverse()

    dfs(1, cards, [avail, remain], coin, target)

    return answer