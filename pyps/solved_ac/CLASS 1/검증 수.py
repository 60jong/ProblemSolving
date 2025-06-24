numList = list(map(int,input().split()))
sum = 0
for i in numList:
    sum += i ** 2
print(sum%10)