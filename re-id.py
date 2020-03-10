def gen_primes(min_str_len):
    D = {}
    q = 2
    primes = []

    while True:
        if len(''.join(x for x in primes)) >= min_str_len:
            break
        if q not in D:
            primes.append(str(q))
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

    return ''.join(x for x in primes)


def solution(i):
    min_str_len = i + 5
    prime_string = gen_primes(min_str_len)
    return prime_string[i:min_str_len]


def main():
    print(solution(10000))

if __name__ == '__main__':
    main()