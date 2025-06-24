dict124 = {'1' : 1, '2' : 2, '3' : 4}

def make124pattern(num):
    if str(num) in dict124: 
        return str(dict124[str(num)])

    div, mod = divmod(num,3)
    if mod == 0:
        return make124pattern(div-1) + "4"
    else:
        return make124pattern(div)+ str(mod)

def solution(n):

    return make124pattern(n)