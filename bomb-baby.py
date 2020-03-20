def solution(M, F):
    steps = 0
    M = int(M)
    F = int(F)
    while True:
        if M <= 0 or F <= 0:
            return "impossible"
        if M > F:
            if F == 1:
                M -= F
                steps += 1
            else:
                m_div_f = M // F
                M = M - F * m_div_f
                steps += m_div_f
        elif F > M:
            if M == 1:
                F -= M
                steps += 1
            else:
                f_div_m = F // M
                F = F - M * f_div_m
                steps += f_div_m
        elif F == M == 1:
            break
        else:
            return "impossible"
    if steps == 0:
        return "impossible"
    return str(steps)


def main():
    print(solution('100', '100'))


if __name__ == '__main__':
    main()