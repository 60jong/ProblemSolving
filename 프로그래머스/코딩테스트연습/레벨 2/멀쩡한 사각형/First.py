# import math
# def solution(w,h):
#     gcd = 1
#     for i in range(min(w,h),0,-1):
#         if w%i==0 and h%i==0:
#             gcd = i
#             break
#     w = int(w/gcd)
#     h = int(h/gcd)
#
#     inclination = h/w
#
#     bRecCnt = 0
#     temp = 0
#
#     for i in range(1,w+1):
#         tar = i * inclination
#         bRecCnt += math.ceil(tar) - temp
#         temp = math.floor(tar)
#
#     answer = (w*gcd) * (h*gcd) - bRecCnt*gcd
#
#     return answer

import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))



print(solution(8,12))
