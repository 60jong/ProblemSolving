trials = int(input())

brackets = [input() for _ in range(trials)]
results = list()


def getResult(elems):
    stack = list()
    for element in elems:
        if element == '(':
            stack.append('(')
        else:
            if len(stack) < 1:
                return "NO"
            else:
                stack.pop()
    if len(stack) != 0:
        return "NO"
    else:
        return "YES"


for bracket in brackets:
    elements = list(bracket)

    results.append(getResult(elements))

for result in results:
    print(result)
