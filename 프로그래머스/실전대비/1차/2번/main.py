def solution(want, number, discount):
    answer = 0

    for day in range(0, len(discount) - 9):
        wantDict = dict(zip(want, [0 for _ in range(len(want))]))

        isTheDay = True
        for i in want:
            if i not in discount[day:day + 10]:
                isTheDay = False
                break
        if isTheDay == True:
            for item in discount[day:day + 10]:
                if item in wantDict:
                    wantDict[item] += 1

            for a, b in zip(number, wantDict.values()):
                if b < a:
                    isTheDay = False

        if isTheDay == True:
            answer += 1

    return answer