def solution(X, Y):
    answer = ''
    # Y = list(map(str,Y))

    # dupList = []
    # for i in range(len(X)):
    #     a = X[i]
    #     for j in range(len(Y)):
    #         if Y[j] == a:
    #             dupList.append(a)
    #             Y[j] = ' '
    #             break;
    # dupList.sort(reverse=True)
    # setDupList = set(dupList)

    # if len(dupList) == 0:
    #     answer = '-1'
    # elif setDupList == {'0'}:
    #     answer = '0'
    # else:
    #     answer = ''.join(dupList)
    Xdict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    Ydict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

    for x in X:
        Xdict[x] += 1
    for y in Y:
        Ydict[y] += 1

    dupList = []
    idxList = []
    for idx, (x, y) in enumerate(zip(Xdict.values(), Ydict.values())):
        if x > 0 and y > 0:
            dupList.append(min(x, y))
            idxList.extend([str(idx) for _ in range(min(x, y))])

    idxList.sort(reverse=True)
    setList = set(idxList)
    if len(idxList) == 0:
        answer = '-1'
    elif setList == {'0'}:
        answer = '0'
    else:
        answer = ''.join(idxList)
    return answer
