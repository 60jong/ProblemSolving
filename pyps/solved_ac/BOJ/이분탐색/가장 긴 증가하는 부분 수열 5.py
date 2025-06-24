import sys

N = int(sys.stdin.readline().strip())
nums = map(int, sys.stdin.readline().strip().split())

def lower_bound(arr, num):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid][-1][0] > num:
            end = mid
        elif arr[mid][-1][0] < num:
            start = mid + 1
        else:
            return mid
    return end

arr = []
for idx, n in enumerate(nums):
    if len(arr) == 0:
        arr.append([(n, idx)])
        continue
    if arr[-1][-1][0] < n:
        arr.append([(n, idx)])
    elif arr[-1][-1][0] > n:
        target_idx = lower_bound(arr, n)
        arr[target_idx].append((n, idx))

print(len(arr))

result = [0] * len(arr)

priorIdx = arr[-1][-1][1] + 1
for i in range(len(arr)):
    idx = len(arr) - 1 - i

    while arr[idx][-1][1] >= priorIdx:
        arr[idx].pop()

    result[idx] = arr[idx][-1][0]
    priorIdx = arr[idx][-1][1]
print(' '.join(map(str, result)))

