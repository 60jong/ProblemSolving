def check_decreasing_number(number : int) -> bool:
    prior_mod = -1
    while number > 0:
        div, mod = divmod(number, 10)
        if mod > prior_mod:
            number = div
            prior_mod = mod
            continue
        return False
    return True

def get_next_decreasing_number(number : int) -> int:
    if number == 9876543210:
        return -1

    str_number = str(number)
    str_nums = list(str_number)
    digits = len(str_nums)
    for i in range(digits):

        if str_nums[-1 - i] == '9':
            continue

        temp = str_nums[:]

        temp[-1 - i] = str(int(temp[-1 - i]) + 1)
        for _i in range(i):
            temp[-1 - _i] = str(_i)

        new_number = int(''.join(temp))
        if check_decreasing_number(new_number):
            return new_number
    # 자릿 수 올려야 하는 상황
    return int(''.join(map(str,range(digits, -1, -1))))

init_number = 0
N = int(input())
while N > 0:
    N -= 1
    init_number = get_next_decreasing_number(init_number)
    if init_number == -1:
        break

print(init_number)