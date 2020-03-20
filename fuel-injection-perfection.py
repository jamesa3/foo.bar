from math import log


def is_power_of_two(n):
    return n & (n - 1) == 0


def find_number_steps_binary(n, steps):
    while n > 1:
        if n & 1 == 0:
            n = n >> 1
        else:
            a = n + 1
            b = n - 1
            zero_count_a = zero_count_b = 0
            while a & 1 == 0:
                a = a >> 1
                zero_count_a += 1
            while b & 1 == 0:
                b = b >> 1
                zero_count_b += 1
            if zero_count_a > zero_count_b and n != 3:
                n += 1
            else:
                n -= 1
        steps += 1
    return steps


def solution(n):
    n = int(n)
    return find_number_steps_binary(n, 0)


def main():
    print(solution('15'))


if __name__ == '__main__':
    main()


# old
def find_closest_power_of_two(n):
    return 2 ** int(round(log(n, 2)))


def find_number_steps_recursive(n, steps, goal=None):
    if n == 1:
        return steps
    elif is_power_of_two(n):
        return find_number_steps_recursive(n / 2, steps + 1)
    else:
        if not goal:
            goal = find_closest_power_of_two(n)
        if goal < n:
            return find_number_steps_recursive(n - 1, steps + 1, goal)
        if goal > n:
            return find_number_steps_recursive(n + 1, steps + 1, goal)


def find_number_steps_iterative(n, steps):
    goal = None
    while n > 1:
        if is_power_of_two(n):
            (n, steps) = (n / 2, steps + 1)
        else:
            if not goal:
                goal = find_closest_power_of_two(n)
            if goal < n:
                (n, steps) = (n - 1, steps + 1)
            elif goal > n:
                (n, steps) = (n + 1, steps + 1)
    return steps
