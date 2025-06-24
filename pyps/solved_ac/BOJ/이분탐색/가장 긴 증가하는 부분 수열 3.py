import sys

N = int(sys.stdin.readline().strip())
nums = map(int, sys.stdin.readline().strip().split())

def lower_bound(arr, num):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > num:
            end = mid
        elif arr[mid] < num:
            start = mid + 1
        else:
            return mid
    return end

arr = []
for n in nums:
    if len(arr) == 0:
        arr.append(n)
        continue
    if arr[-1] < n:
        arr.append(n)
    elif arr[-1] > n:
        idx = lower_bound(arr, n)
        arr[idx] = n

print(arr)
