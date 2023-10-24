import sys

input = sys.stdin.readline

max_len = 0
max_case = []

def dfs(cur, i, s, used):
    global max_len, max_case

    # base condition
    if i == len(s):
        if len(cur) > max_len:
            max_len = len(cur)
            max_case = cur[:]
        return

    for n in s[i]:
        if n == -1:
            dfs(cur, i + 1, s, used)
        # use n
        if not used[n]:
            if len(cur) == 0 or (len(cur) > 0 and n > cur[-1]):
                used[n] = True
                cur.append(n)
                dfs(cur, i + 1, s, used)
                cur.pop()
                used[n] = False
        # not use n
        dfs(cur, i + 1, s, used)


A = input().strip()
B = input().strip()

idxes = []
for a in A:
    tmp = []
    for bi in range(len(B)):
        if a == B[bi]:
            tmp.append(bi)
    if len(tmp) == 0:
        tmp.append(-1)
    idxes.append(tmp)

dfs([], 0, idxes, [False] * len(B))

print(max_len)
for c in max_case:
    print(B[c], end='')

# 시간 초과