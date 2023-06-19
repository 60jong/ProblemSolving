def solution(n,a,b):
    if a > b:
        temp = a
        a = b
        b = temp
    answer = 0;
    if abs(a-b)==1:
        return 1
    while ((n/2 - a) * (n/2 - b)) > 0:
        if (n/2 - a) > 0:
            n /= 2
            n += 0.1
        elif (n/2 - a) < 0:
            n /= 2
            a -= n
            b -= n
            n += 0.1
    n = int(n)
    while n != 1:
        n /= 2
        answer+=1
    return answer

    # if(a > n/2 and b > n/2) :
    #     solution(n/2, a - n/2, b - n/2)
    # elif (a <= n/2 and b <= n/2):
    #     solution(n/2, a, b)
    # else:
    #
    #     while n != 1:
    #         n /= 2
    #         answer+=1
    #     return answer

print(solution(8,6,7))














