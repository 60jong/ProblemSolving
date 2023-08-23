def push_front(value):
    global head

    deque[head] = value
    head -= 1

def push_back(value):
    global tail

    tail += 1
    deque[tail] = value

def pop_front():
    global head

    head += 1
    return deque[head]

def pop_back():
    global tail

    tail -= 1
    return deque[tail]

def top_front():
    global head

    return deque[head + 1]


def top_front():
    global tail

    return deque[tail - 1]

def size():
    global head, tail

    return tail - head

MX = int(10)
deque = [0] * (2 * MX + 1)
head = MX
tail = MX

push_front(1)
push_back(2)
push_front(3)
push_front(4)
print(pop_front())
push_front(5)
print(deque)
print(size())
