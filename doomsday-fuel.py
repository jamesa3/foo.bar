from fractions import Fraction


def zero_matrix(n, m=None):
    m = m if m else n
    return [[0 for x in range(m)] for y in range(n)]


def subtract_from_identity_matrix(m):
    result = zero_matrix(len(m))
    for i, row in enumerate(m):
        for j, cell in enumerate(row):
            identity_cell = 1 if i == j else 0
            result[i][j] = identity_cell - cell
    return result


def identity_matrix(m):
    result = zero_matrix(m)
    for i in range(m):
        result[i][i] = 1
    return result


def copy_matrix(m):
    len_m = len(m)
    result = zero_matrix(len_m)

    for i in range(len_m):
        for j in range(len_m):
            result[i][j] = m[i][j]
    return result


# def invert_matrix(m):
def invert_matrix(m):
    # # Section 1: Make sure A can be inverted.
    # check_squareness(m)
    # check_non_singular(m)

    # Section 2: Make copies of A & I, AM & IM, to use for row ops
    n = len(m)
    AM = copy_matrix(m)
    I = identity_matrix(n)
    IM = copy_matrix(I)

    # Section 3: Perform row operations
    indices = list(range(n))  # to allow flexible row referencing ***
    for fd in range(n):  # fd stands for focus diagonal
        # fd_scaler = 1.0 / AM[fd][fd]
        fd_scaler = Fraction(1, AM[fd][fd])
        # FIRST: scale fd row with fd inverse.
        for j in range(n):  # Use j to indicate column looping.
            AM[fd][j] *= fd_scaler
            IM[fd][j] *= fd_scaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd + 1:]:
            # *** skip row with fd in it.
            cr_scaler = AM[i][fd]  # cr stands for "current row".
            for j in range(n):
                # cr - cr_scaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - cr_scaler * AM[fd][j]
                IM[i][j] = IM[i][j] - cr_scaler * IM[fd][j]

    return IM


def matrix_multiply(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    C = zero_matrix(rows_a, cols_b)
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            C[i][j] = total

    return C


def solution(m):
    # STEP 1
    state_count = len(m)
    zero_count = [0] * state_count
    totals = [0] * state_count

    transient_states = []
    terminal_states = []
    unreachable_states = []

    for i, row in enumerate(m):
        for j, cell in enumerate(row):
            totals[i] += cell
            if cell == 0:
                zero_count[j] += 1
        if totals[i] > 0:
            transient_states.append(i)
        elif totals[i] == 0:
            terminal_states.append(i)

    for i, count in enumerate(zero_count):
        if count == state_count:
            unreachable_states.append(i)

    all_terminal_states = terminal_states
    terminal_states = list(set(terminal_states) - set(unreachable_states))
    transient_states = list(set(transient_states) - set(unreachable_states))

    # STEP 2
    Q = []  # t * t matrix transient states
    R = []  # t * r matrix transient by terminal states
    for i, row in enumerate(m):
        if i in transient_states:
            total = sum(row)
            Q.append([Fraction(cell, total)
                      for j, cell in enumerate(row) if j in transient_states])
            R.append([Fraction(cell, total)
                      for j, cell in enumerate(row) if j in terminal_states])

    N = invert_matrix(subtract_from_identity_matrix(Q))
    B = matrix_multiply(N, R)

    print(B)

    first_row_b = B[0]

    result = [0 for x in range(len(all_terminal_states) + 1)]

    for i in range(len(result)):
        if i in terminal_states:
            result[i] = first_row_b[i.numerator]
        elif i in all_terminal_states:
            result[i] = 0

    # TODO: LCD
    # result[len(result - 1)] =

def main():
    print(solution([
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]))


if __name__ == '__main__':
    main()
