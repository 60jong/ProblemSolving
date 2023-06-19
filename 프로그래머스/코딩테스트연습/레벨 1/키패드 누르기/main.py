leftPad = [1, 4, 7]
rightPad = [3, 6, 9]
middlePad = [2, 5, 8, 0]

pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]


def calDist(a, b):
    aLoc = tuple()
    bloc = tuple()
    for i in range(4):
        for j in range(3):
            if pad[i][j] == a:
                aLoc = tuple((i, j))
            if pad[i][j] == b:
                bLoc = tuple((i, j))

    return abs(aLoc[0] - bLoc[0]) + abs(aLoc[1] - bLoc[1])


def solution(numbers, hand):
    answer = ''

    Llist = ['*']
    Rlist = ['#']

    for num in numbers:
        if num in leftPad:
            Llist.append(num)
            answer += 'L'
        elif num in rightPad:
            Rlist.append(num)
            answer += 'R'
        else:
            rDist = calDist(num, Rlist[-1])
            lDist = calDist(num, Llist[-1])

            if rDist < lDist:
                Rlist.append(num)
                answer += 'R'
            elif rDist > lDist:
                Llist.append(num)
                answer += 'L'
            else:
                if hand == 'right':
                    Rlist.append(num)
                    answer += 'R'
                else:
                    Llist.append(num)
                    answer += 'L'

    return answer
