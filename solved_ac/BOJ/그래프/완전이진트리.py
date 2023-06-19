K = int(input())
nums = input().split()

result = [[] for _ in range(K)]
# LNR
for i in range(len(nums)):
    for j in range(len(nums)):
        if ((i + 1) + 2 ** j) % 2 ** (j + 1) == 0:
            result[j].append(nums[i])


for i in range(K - 1, -1, -1):
    layerNodes = result[i]
    for n in layerNodes:
        print(n, end=' ')
    print()