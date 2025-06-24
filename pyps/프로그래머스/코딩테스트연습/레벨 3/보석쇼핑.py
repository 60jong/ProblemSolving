def solution(gems):
    answer = [1, len(gems)]
    types = set(gems)
    count = {}

    start = 0
    i = 0
    while i < len(gems):
        if i - start == 0:
            start = i
            count[gems[i]] = 1
        # 맨 앞이 중복이면 맨 앞 idx 옮기기
        elif i - start == 1 and gems[start] == gems[i]:
            start = i
        else:
            addCount(count, gems[i])

        if foundAll(count, len(types)):
            if i - start == len(types) - 1:
                answer = [start + 1, i + 1]
                break
            # answer 조정
            elif i - start < answer[1] - answer[0]:
                answer = [start + 1, i + 1]
            # start 조정 후 새로운 시작
            subCount(count, gems[start])
            subCount(count, gems[i])
            start += 1
        else:
            i += 1

    return answer


def foundAll(count, size):
    return len(count) == size


def addCount(count, gem):
    if gem in count:
        count[gem] += 1
    else:
        count[gem] = 1


def subCount(count, gem):
    count[gem] -= 1

    if count[gem] == 0:
        del count[gem]