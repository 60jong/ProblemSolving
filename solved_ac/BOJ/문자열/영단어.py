import sys
N, L = map(int, sys.stdin.readline().split())
dicts = []

for _ in range(N):
    d = sys.stdin.readline().strip()
    if len(d) >= L:
        dicts.append(d)

dictSet = set(dicts)
diction = dict(zip(dictSet, [0] * len(dictSet)))

for d in dicts:
    diction[d] += 1

result = sorted(diction.items(), key=lambda x: (-1 * x[1], -1 * len(x[0]), x[0]))

for i in result:
    print(i[0])