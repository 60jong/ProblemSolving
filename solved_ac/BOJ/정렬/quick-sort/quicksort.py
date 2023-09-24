def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def partiton(arr, start, end):
    pivot = arr[start]

    low, high = start, end
    while low < high:
        while arr[high] > pivot and low < high:
            high -= 1

        while arr[low] <= pivot and low < high:
            low += 1

        swap(arr, low, high)

    swap(arr, start, low)
    return low

def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = partiton(arr, start, end)

    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)

arr = [5, 12, 3, 7, 2, 11, 4, 9]

quick_sort(arr, 0, len(arr) - 1)
print(arr)