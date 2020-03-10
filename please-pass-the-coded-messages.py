def format_string(l):
    zeroes = [x for x in l if x == 0]
    if len(zeroes) == len(l):
        return str(0)
    return ''.join(str(x) for x in l)


def remove(l, bucket_1, bucket_2):
    if not bucket_1:
        to_remove = None
    else:
        to_remove = min(bucket_1)
    if to_remove in l:
        l.remove(to_remove)
        return format_string(l)
    else:
        to_remove = min(bucket_2)
        bucket_2.remove(to_remove)
        l.remove(to_remove)
        to_remove = min(bucket_2)
        l.remove(to_remove)
        return format_string(l)


def solution(l):
    l_sorted = sorted(l, reverse=True)

    bucket_1 = [x for x in l_sorted if x % 3 == 1]
    bucket_2 = [x for x in l_sorted if x % 3 == 2]

    total = sum(l)

    if total % 3 == 0:
        return format_string(l_sorted)
    elif total % 3 == 1:
        return remove(l_sorted, bucket_1, bucket_2)
    else:
        return remove(l_sorted, bucket_2, bucket_1)


def main():
    print(solution([3,1,4,1,5,9]))


if __name__ == '__main__':
    main()
