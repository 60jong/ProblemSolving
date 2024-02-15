class Stack:

    def __init__(self):
        self._numbers = []

    def push(self, num):
        self._numbers.append(num)


    def pop(self):
        return self._numbers.pop()


    def top(self):
        return self._numbers[-1]

    def get_max(self):
        pass


s = Stack()
s.push(1)
s.push(3)
s.push(2)

print(s.pop())
print(s.pop())