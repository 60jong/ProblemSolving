def get_primes(N):
    import math

    end = int(math.sqrt(N))
    prime_candidates = [False, False] + [True] * N
    primes = []

    for c in range(2, end + 1):
        if prime_candidates[c]:
            for _c in range(c ** 2, N + 1, c):
                prime_candidates[_c] = False

    for i in range(N + 1):
        if prime_candidates[i]:
            primes.append(i)
    return primes


def get_result(N, primes):
    np = len(primes)

    if np == 0:
        return 0

    count = 0
    a, b = 0, 0
    sum = primes[0]

    while a < np - 1 or b < np - 1:
        if sum <= N:
            if b < np - 1:
                b += 1
                if sum == N:
                    count += 1
                sum += primes[b]
        else:
            sum -= primes[a]
            a += 1

    if primes[-1] == N:
        count += 1
    return count

N = int(input())
primes = get_primes(N)
print(get_result(N, primes))