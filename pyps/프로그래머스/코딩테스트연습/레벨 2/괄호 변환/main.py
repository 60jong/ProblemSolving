def isValidStr(s):
    sum = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            return False
    return True

def solution(p):
    if p == '':
        return ''

    sum = 0
    u = ''
    v = ''
    temp = ''
    if p[0] == '(':
        sum += 1
    else:
        sum -= 1

    for i in range(1, len(p)):
        if p[i] == '(':
            sum += 1
        else:
            sum -= 1

        if sum == 0:
            u = p[0:i + 1]
            v = p[i + 1:len(p) + 1]
            break
    print('u : ' + u)
    print('v : ' + v)
    if isValidStr(u) == True:
        return u + solution(v)
    else:
        temp += '('
        u = u[1:len(u) - 1]
        a = []
        for i in range(0, len(u)):

            if u[i] == '(':
                a.append(')')
            else:
                a.append('(')
        u = ''.join(a)
        print(u)
        temp += u
        temp += ')'
        print('temp : ' + temp)
        temp += solution(v)

    answer = temp
    return answer

print('answer '+solution('(())'))
print('answer '+solution(''))