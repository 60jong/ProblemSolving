import math

def isSosu(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
m,n = map(int,input().split())

for num in range(m,n+1):
    if num in [2,3,5]:
        print(num)
    elif str(num)[-1] in ['0','2','4','5','6','8']:
        continue
    else:
        if num == 1:
            continue
        if isSosu(num):
            print(num)
