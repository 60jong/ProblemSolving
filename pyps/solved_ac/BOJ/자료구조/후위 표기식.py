# [ 괄호, 곱셈, 나눗셈 ]  (A+B) -> AB+ -> 한 덩어리로 생각
# D*(A*(B+C)-E)
# seq = '(A+(B+F)*G)*C-D/E'
seq = '(A+(B+F)*G)'
def getInner(sequence):
    for s in sequence:
        if s == '(':
            getInner()

i = 0
while True:
    if seq[i] == '(':
        temp = ['(']
        chars = []
        i += 1
        while len(temp) > 0:
            if seq[i] == '(':
                temp.append('(')
            if seq[i] == ')':
                temp.pop();
            else:
                chars.append(seq[i])
            i += 1
    break
print(chars)