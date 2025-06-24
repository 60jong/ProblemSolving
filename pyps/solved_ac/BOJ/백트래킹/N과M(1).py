N, M = map(int, input().strip().split())

def solution(made):
    if len(made) == M:
        print(' '.join(list(made)))
        return

    for n in range(1, N + 1):
        str_n = str(n)
        if str_n not in made:
            solution(made + str_n)

used = [False] * (N + 1)
arr = [0] * (M + 1)
def function(k):
    if k == M + 1:
        for a in arr[1:]:
            print(a, end=' ')
        print()
        return

    for n in range(1, N + 1):
        if not used[n]:
            used[n] = True
            arr[k] = n
            function(k + 1)
            used[n] = False

# solution('')
function(1)