from decimal import Decimal, getcontext


def calculation(n, n_prime):
    return n * n_prime + ((n * (n + 1)) / 2) - ((n_prime * (n_prime + 1)) / 2)


def s(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n_prime = int((Decimal(2).sqrt() - 1) * Decimal(n))
        return calculation(n, n_prime) - s(n_prime)


def solution(str_n):
    getcontext().prec = 1000
    n = long(str_n)
    res = s(n)
    return str(long(res))


def main():
    print(solution('10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))


if __name__ == '__main__':
    main()
