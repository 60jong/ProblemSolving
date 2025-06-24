import sys
import math

def calShape1(scores): # [ㅡ] -> 2개 존재
    maxScore = 0
    count = 0
    #[ㅡ]
    for y in range(len(scores)):
        for x in range(len(scores[0]) - 3):
            score = scores[y][x] + scores[y][x + 1] + scores[y][x + 2] + scores[y][x + 3]
            if score > maxScore:
                maxScore = score

    #[|]
    for y in range(len(scores) - 3):
        for x in range(len(scores[0])):
            score = scores[y][x] + scores[y + 1][x] + scores[y + 2][x] + scores[y + 3][x]
            if score > maxScore:
                maxScore = score
    return maxScore


def calShape2(scores): # [ㅁ] -> 1개 존재
    maxScore = 0
    for y in range(len(scores) - 1):
        for x in range(len(scores[0]) - 1):
            score = scores[y][x] + scores[y + 1][x] + scores[y][x + 1] + scores[y + 1][x + 1]
            if score > maxScore:
                maxScore = score
    return maxScore

def calShape3(scores): # [ㄴ] -> 8개 존재
    maxScore = 0
    # [ㄴ]
    for y in range(len(scores) - 1):
        for x in range(len(scores[0]) - 2):
            score = scores[y][x] + scores[y + 1][x] + scores[y + 1][x + 1] + scores[y + 1][x + 2]
            if score > maxScore:
                maxScore = score
    # [ㄴ] 90도 회전
    for y in range(len(scores) - 2):
        for x in range(len(scores[0]) - 1):
            score = scores[y][x] + scores[y][x + 1] + scores[y + 1][x] + scores[y + 2][x]
            if score > maxScore:
                maxScore = score
    # [ㄴ] 180도 회전 ㄱ
    for y in range(len(scores) - 1):
        for x in range(len(scores[0]) - 2):
            score = scores[y][x] + scores[y][x + 1] + scores[y][x + 2] + scores[y + 1][x + 2]
            if score > maxScore:
                maxScore = score
    # [ㄴ] 270도 회전
    for y in range(2, len(scores)):
        for x in range(len(scores[0]) - 1):
            score = scores[y][x] + scores[y][x + 1] + scores[y - 1][x + 1] + scores[y - 2][x + 1]
            if score > maxScore:
                maxScore = score
    # [ㄴ] 대칭
    for y in range(1, len(scores)):
        for x in range(len(scores[0]) - 2):
            score = scores[y][x] + scores[y][x + 1] + scores[y][x + 2] + scores[y - 1][x + 2]
            if score > maxScore:
                maxScore = score
    # [ㄴ] 대칭 90도 회전
    for y in range(len(scores) - 2):
        for x in range(len(scores[0]) - 1):
            score = scores[y][x] + scores[y + 1][x] + scores[y + 2][x] + scores[y + 2][x + 1]
            if score > maxScore:
                maxScore = score
    # [ㄴ] 대칭 180도 회전
    for y in range(len(scores) - 1):
        for x in range(len(scores[0]) - 2):
            score = scores[y][x] + scores[y + 1][x] + scores[y][x + 1] + scores[y][x + 2]
            if score > maxScore:
                maxScore = score
    # [ㄴ] 대칭 270도 회전
    for y in range(len(scores) - 2):
        for x in range(len(scores[0]) - 1):
            score = scores[y][x] + scores[y][x + 1] + scores[y + 1][x + 1] + scores[y + 2][x + 1]
            if score > maxScore:
                maxScore = score
    return maxScore

def calShape4(scores): # [ㅜ] -> 4개 존재
    maxScore = 0
    # [ㅜ]
    for y in range(len(scores) - 1):
        for x in range(len(scores[0]) - 2):
            score = scores[y][x] + scores[y][x + 1] + scores[y + 1][x + 1] + scores[y][x + 2]
            if score > maxScore:
                maxScore = score
    # [ㅜ] 90도 회전 ㅓ
    for y in range(1, len(scores) - 1):
        for x in range(len(scores[0]) - 1):
            score = scores[y][x] + scores[y][x + 1] + scores[y - 1][x + 1] + scores[y + 1][x + 1]
            if score > maxScore:
                maxScore = score
    # [ㅜ] 180도 회전 ㅗ
    for y in range(1, len(scores)):
        for x in range(len(scores[0]) - 2):
            score = scores[y][x] + scores[y][x + 1] + scores[y][x + 2] + scores[y - 1][x + 1]
            if score > maxScore:
                maxScore = score
    # [ㅜ] 270도 회전 ㅏ
    for y in range(len(scores) - 2):
        for x in range(len(scores[0]) - 1):
            score = scores[y][x] + scores[y + 1][x] + scores[y + 1][x + 1] + scores[y + 2][x]
            if score > maxScore:
                maxScore = score
    return maxScore

def calShape5(scores): # [z] -> 4개 존재
    maxScore = 0
    # [z]
    for y in range(len(scores) - 1):
        for x in range(len(scores[0]) - 2):
            score = scores[y][x] + scores[y][x + 1] + scores[y + 1][x + 1] + scores[y + 1][x + 2]
            if score > maxScore:
                maxScore = score
    # [z] 90도 회전 N
    for y in range(1, len(scores) - 1):
        for x in range(len(scores[0]) - 1):
            score = scores[y][x] + scores[y + 1][x] + scores[y][x + 1] + scores[y - 1][x + 1]
            if score > maxScore:
                maxScore = score
    # [z] 대칭
    for y in range(1, len(scores)):
        for x in range(len(scores[0]) - 2):
            score = scores[y][x] + scores[y][x + 1] + scores[y - 1][x + 1] + scores[y - 1][x + 2]
            if score > maxScore:
                maxScore = score
    # [z] 90도 회전 대칭
    for y in range(len(scores) - 2):
        for x in range(len(scores[0]) - 1):
            score = scores[y][x] + scores[y + 1][x] + scores[y + 1][x + 1] + scores[y + 2][x + 1]
            if score > maxScore:
                maxScore = score
    return maxScore

N, M = map(int, sys.stdin.readline().strip().split())
scores = [list(map(int, sys.stdin.readline().strip().split())) for n in range(N)]

score1 = calShape1(scores)
score2 = calShape2(scores)
score3 = calShape3(scores)
score4 = calShape4(scores)
score5 = calShape5(scores)

maxScore = max(score1, score2, score3, score4, score5)
print(maxScore)