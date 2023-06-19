dictSize = int(input())

a = list(map(int,input().split()))

a_dict = dict()
for a_ in a:
    try:
        a_dict[a_] = a_dict[a_] + 1
    except:
        a_dict[a_] = 1

findSize = int(input())
b = list(map(int,input().split()))

c = list(a_dict.keys())
c.sort()

result = list()
for e in b:
    start = 0
    end = len(c) - 1
    result.append(0)
    while start <= end:
        index = (start + end) // 2
        if e < c[index]:
            end = index - 1
        elif e > c[index]:
            start = index + 1
        else:
            result[-1] = result[-1] + a_dict[c[index]]
            break

print(' '.join(map(str,result)))

