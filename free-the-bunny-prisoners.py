from itertools import combinations


def solution(num_buns, num_required):
    copies_of_each_key = num_buns - num_required + 1
    combos = list(combinations(range(num_buns), copies_of_each_key))
    result = [[] for i in range(num_buns)]

    for i, combo in enumerate(combos):
        for j in combo:
            result[j].append(i)

    return result


def main():
    print(solution(3, 1))


if __name__ == '__main__':
    main()