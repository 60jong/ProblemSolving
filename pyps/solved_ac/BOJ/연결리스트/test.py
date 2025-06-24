N = 10
data = [-1] * N
pre = [-1] * N
next = [-1] * N
unused = 1


# 0번지는 dummmy

# 13(2) - 65(1) - 21(4) - 17(5)

# setup
data[0] = -1
pre[0] = -1
next[0] = 2

data[2] = 13
pre[2] = 0
next[2] = 1

data[1] = 65
pre[1] = 2
next[1] = 4

data[4] = 21
pre[4] = 1
next[4] = 5

data[5] = 17
pre[5] = 4

unused = 6

def traverse():
    print('------')
    start = next[0]
    while start != -1:
        print(data[start])
        start = next[start]
    print('------')

def insert(idx, value):
    global unused

    # next node 설정
    if next[idx] != -1: pre[next[idx]] = unused

    # target node 설정
    data[unused] = value
    pre[unused] = idx
    next[unused] = next[idx]

    # pre node 설정
    next[idx] = unused

    unused += 1

def erase(idx):
    # pre node 설정
    next[pre[idx]] = next[idx]

    # next node 설정
    if next[idx] != -1: pre[next[idx]] = pre[idx]

print(next)
traverse()

erase(4)
print(next)
traverse()


# 두 연결 리스트가 만나는 점을 구하는 방법?? - 공간/시간 복잡도
# 한 연결리스트에 사이클이 존재하는지 확인하는 법?? - 공간/시간 복잡도 -> 두 실행 흐름(하나씩 / 두개씩) -> 둘은 언젠가 반드시 만남(사이클 있으면)