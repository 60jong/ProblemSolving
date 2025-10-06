from collections import deque

def solution(edges):
    ind = {}
    outd = {}
    vis = {}
    for f, t in edges:
        if f not in outd:
            outd[f] = []
        if t not in outd:
            outd[t] = []

        if f not in ind:
            ind[f] = []
        if t not in ind:
            ind[t] = []
        
        if f not in vis:
            vis[f] = False
        if t not in vis:
            vis[t] = False
            
        outd[f].append(t)
        ind[t].append(f)
        
    cand = []
    tar_num = 0
    
    for n in ind.keys():
        if len(ind[n]) == 0 and len(outd[n]) > 0:
            if len(outd[n]) > 1:
                tar_num = n
                break
            else:
                cand.append(n)
    
    if tar_num == 0:
        if len(cand) == 1:
            tar_num = cand[0]
            return [tar_num, 0, 1, 0]

        for c in cand:
            next_n = outd[c][0]
            if len(ind[next_n]) == 2:
                tar_num = c
                break
    
    # 순환
    answer = [tar_num, 0, 0, 0]
    for n in outd[tar_num]:
        ind[n].remove(tar_num)
        
        q = deque()
        q.append(n)
        vis[n] = True
        
        min_in = len(ind[n])
        max_in = len(ind[n])
        
        min_out = len(outd[n])
        max_out = len(outd[n])
        
        while q:
            cn = q.popleft()
            
            for nn in outd[cn]:
                if not vis[nn]:
                    vis[nn] = True
                    q.append(nn)
                    
                    min_in = min(len(ind[nn]), min_in)
                    min_out = min(len(outd[nn]), min_out)
                    max_in = max(len(ind[nn]), max_in)
                    max_out = max(len(outd[nn]), max_out)
        
        if max_in == 2 and max_out == 2:
            # 8자
            answer[3] += 1
        elif min_out == 0:
            # 막대
            answer[2] += 1
        else:
            # 도넛
            answer[1] += 1
    return answer