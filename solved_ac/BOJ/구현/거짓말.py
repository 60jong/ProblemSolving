from collections import deque
import sys

N, M = map(int, sys.stdin.readline().strip().split())

line = list(map(int, sys.stdin.readline().strip().split()))

truth = deque()
party = []
canLie = [True] * M
used = [False] * (N + 1)

if len(line) == 1:
    print(M)
else:
    for m in line[1:]:
        truth.append(m)
        used[m] = True

    for m in range(M):
        partyLine = list(map(int, sys.stdin.readline().strip().split()))
        party.append(partyLine[1:])

    while len(truth) > 0:
        t = truth.popleft()

        for idx, p in enumerate(party):
            if canLie[idx]:
                if t in p:
                    canLie[idx] = False
                    for _p in p:
                        if not used[_p]:
                            used[_p] = True
                            truth.append(_p)

    count = 0
    for c in canLie:
        if c:
            count += 1
    print(count)