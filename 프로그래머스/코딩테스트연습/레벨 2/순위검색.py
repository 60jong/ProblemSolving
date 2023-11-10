import re
from collections import defaultdict
from bisect import bisect_left

hash = defaultdict(list)
def solution(info, query):
    result = []
    for idx, i in enumerate(info):
        options = i.split()
        key = []
        for o in options[:4]:
            key.append([o[0], '-'])

        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        k = key[0][a] + key[1][b] + key[2][c] + key[3][d]
                        hash[k].append(int(options[4]))
    for h in hash:
        hash[h].sort()

    for q in query:
        a = re.split(' and ', q)
        score = int(a[3].split()[1])
        key = ""
        for _a in a:
            key += _a[0]

        result.append(len(hash[key]) - bisect_left(hash[key], score))
    return result