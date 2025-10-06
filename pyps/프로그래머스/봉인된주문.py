alphabet = {
    "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6,
    "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13,
    "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19,
    "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26
}

alphabet_num = {}
for k in alphabet.keys():
    alphabet_num[alphabet[k]] = k
    
def solution(n, bans):
    answer = ''
    
    num_bans = []
    for b in bans:
        len_b = len(b)
        
        order = 0
        for i in range(len_b):
            order += (26 ** i) * alphabet[b[len_b - 1 - i]]
        
        num_bans.append(order)

    num_bans.sort()
    
    cnt = 0
    ci = 0
    for i, b in enumerate(num_bans):
        if b <= n:
            cnt += 1
            ci += 1
        else:
            break
    while cnt > 0:
        n += cnt
        cnt = 0
        ii = ci
        for i in range(ii, len(num_bans)):
            if num_bans[i] <= n:
                cnt += 1
                ci += 1
            else:
                break
    answer = []
    
    while n > 0:
        m = n % 26
        n //= 26
        
        if m == 0:
            m += 26
            n -= 1
        answer.append(m)
        
    result = ""
    for a in answer:
        result = alphabet_num[a] + result
        
    return result
