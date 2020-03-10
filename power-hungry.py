from functools import reduce


def solution(xs):
    if not xs:
        return str(0)

    if len(xs) == 1:
        return str(xs[0])

    negatives = [x for x in xs if (x < 0)]
    positives = [x for x in xs if (x > 0)]
    zeroes = [x for x in xs if (x == 0)]

    if (len(negatives) == 1 and len(zeroes)):
        return str(0)

    if len(negatives) % 2 != 0:
        negatives.remove(max(negatives))

    result = reduce(lambda x, y: x * y, positives + negatives)
    return str(result)


def main():
    print(solution([-2,-3,4,-5]))

if __name__ == '__main__':
    main()