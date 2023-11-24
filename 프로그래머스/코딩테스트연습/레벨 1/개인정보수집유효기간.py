def expired(today, date, dur):
    y, m, d = date.split('.')

    total_m = int(m) + dur
    y_o = 0
    while total_m >= 13:
        total_m -= 12
        y_o += 1

    target_date = str(int(y) + y_o) + "." + str(total_m).zfill(2) + "." + d
    return target_date <= today


def solution(today, terms, privacies):
    answer = []

    # terms -> dict
    term_dict = dict(zip(list(map(lambda x: x.split()[0], terms)), list(map(lambda x: int(x.split()[1]), terms))))

    for idx, p in enumerate(privacies):
        date, t = p.split()

        if expired(today, date, term_dict[t]):
            answer.append(idx + 1)

    return answer