def isOk(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                for t in range(i, 5):
                    for s in range(5):
                        if t == i:
                            if s <= j:
                                continue
                        if place[t][s] == 'P':
                            if abs(i - t) + abs(j - s) == 1:
                                return 0
                            if abs(i - t) + abs(j - s) == 2:
                                if i == t:
                                    if place[i][j + 1] != 'X':
                                        return 0
                                elif j == s:
                                    if place[i + 1][j] != 'X':
                                        return 0
                                else:
                                    if s > j:
                                        if not (place[i][j + 1] == 'X' and place[i + 1][j] == 'X'):
                                            return 0
                                    if s < j:
                                        if not (place[i][j - 1] == 'X' and place[i + 1][j] == 'X'):
                                            return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(isOk(place))

    return answer