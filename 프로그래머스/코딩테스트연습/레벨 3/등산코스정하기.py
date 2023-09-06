def mount(p_per_n, summits, gates, intensity):
    for s in summits:
        stack = [s]
        visited = [False] * len(p_per_n)
        visited[s] = True
        
        while stack:
            node = stack.pop()
            
            if node in gates:
                return (True, s)
            
            for n, w in p_per_n[node]:
                if w <= intensity and not visited[n] and not n in summits:
                    stack.append(n)
                    visited[n] = True
    return (False, None)

def solution(n, paths, gates, summits):
    hash_summits = dict(zip(sorted(summits), [0]*len(summits)))
    hash_gates = dict(zip(gates,[0]*len(gates)))
    p_per_n = [[] * (n + 1) for _ in range(n + 1)]
    w_set = set()
    for a, b, w in paths:
        p_per_n[a].append((b, w))
        p_per_n[b].append((a, w))
        w_set.add(w)
    
    weights = sorted(list(w_set))
    
    start = 0
    end = len(weights) - 1
    while start <= end:
        mid = (start + end) // 2
        success, summit = mount(p_per_n, hash_summits, hash_gates, weights[mid])
        if success:
            end = mid - 1
            answer_summit = summit
        else:
            start = mid + 1
    return [answer_summit, weights[start if start > end else end]]
