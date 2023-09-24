arr = [5, 3, 7, 4, 1, 10, 9, 6]
tmp = [-1] * len(arr)


def merge(start, end):
    mid = (start + end) // 2
    idx, sidx, eidx = start, start, mid + 1

    for _ in range(end - start + 1):
        if sidx > mid:
            tmp[idx] = arr[eidx]
            eidx += 1
        elif eidx > end:
            tmp[idx] = arr[sidx]
            sidx += 1
        elif arr[sidx] <= arr[eidx]:
            tmp[idx] = arr[sidx]
            sidx += 1
        else:
            tmp[idx] = arr[eidx]
            eidx += 1
        idx += 1

    # 반영
    for i in range(start, end + 1): arr[i] = tmp[i]


def merge_sort(start, end):
    if start >= end: return

    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    merge(start, end)


merge_sort(0, len(arr) - 1)
print(tmp)
