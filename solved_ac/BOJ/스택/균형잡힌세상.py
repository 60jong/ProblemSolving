def is_pair(another, bracket):
    if another == '(':
        if bracket == ')':
            return True
    elif another == '[':
        if bracket == ']':
            return True
    return False

def solution(brackets):
    stack = []
    for b in brackets:
        if b in ['(', '[']:
            stack.append(b)
        else:
            if not stack:
                return False
            else:
                if is_pair(stack[-1], b):
                    stack.pop()
                else:
                    return False

    if stack:
        return False
    else:
        return True

while True:
    sentence = input()
    if sentence == '.': break
    elems = []
    for s in sentence:
        if s in ['(', ')', '[', ']']:
            elems.append(s)

    print('yes' if solution(elems) else 'no')
