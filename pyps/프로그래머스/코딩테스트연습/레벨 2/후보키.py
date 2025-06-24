from collections import defaultdict
from itertools import combinations

def is_candidate(relation, combi):
    row_dict = defaultdict(int)
    for r in relation:
        key = ""
        for c in combi:
            key += r[c]
        row_dict[key] += 1
    return len(row_dict) == len(relation)

def is_unique(combi, candidates):
    combi_set = {*combi}

    for cd in candidates:

        if len(combi_set.union({*cd})) == len(combi_set):
            return False
    return True

def solution(relation):

    count = 0
    candidates = []
    cols = len(relation[0])
    for i in range(1, cols + 1):
        for combi in combinations(range(cols), i):
            print(combi, candidates)
            if is_unique(set(combi), candidates) and is_candidate(relation, combi):
                candidates.append(combi)
                print(combi, candidates)
                count += 1
    return count