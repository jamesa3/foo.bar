from fractions import gcd
from fractions import Fraction


def zero_matrix(n, m=None):
    """Return an n by m zero matrix, n by n if m is not provided"""
    m = m if m else n
    return [[0 for x in range(m)] for y in range(n)]


def subtract_from_identity_matrix(m):
    """Subtract m from an identity matrix of equal dimensions to m and
    return result
    """
    result = zero_matrix(len(m))
    for i, row in enumerate(m):
        for j, cell in enumerate(row):
            identity_cell = 1 if i == j else 0
            result[i][j] = identity_cell - cell
    return result


def identity_matrix(m):
    """Return an m by m identity matrix"""
    result = zero_matrix(m)
    for i in range(m):
        result[i][i] = 1
    return result


def copy_matrix(m):
    """Return a copy of matrix m"""
    len_m = len(m)
    result = zero_matrix(len_m)

    for i in range(len_m):
        for j in range(len_m):
            result[i][j] = m[i][j]
    return result


def invert_matrix(m):
    """Return matrix m inverted"""
    # Make copies of A & I, AM & IM, to use for row ops
    n = len(m)
    AM = copy_matrix(m)
    I = identity_matrix(n)
    IM = copy_matrix(I)

    # Perform row operations
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
    """Return the multiplication product of a and b"""
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


def least_common_multiplier(fractions):
    """Return the LCM of fractions"""
    denominators = [f.denominator for f in fractions]
    lcm = denominators[0]
    for d in denominators[1:]:
        # integer division
        lcm = lcm // gcd(lcm, d) * d
    return lcm


def solution(m):
    if m == [[0]]:
        return [1, 1]

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
        if totals[i] > 0 or i == 0:
            transient_states.append(i)
        elif totals[i] == 0:
            terminal_states.append(i)

    for i, count in enumerate(zero_count):
        if count == state_count and i != 0:
            unreachable_states.append(i)

    all_terminal_states = terminal_states
    terminal_states = list(set(terminal_states) - set(unreachable_states))
    transient_states = list(set(transient_states) - set(unreachable_states))

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

    first_row_b = B[0]
    result = [0 for x in range(len(all_terminal_states))]

    lcm = least_common_multiplier(first_row_b)

    j = 0
    for i, state in enumerate(sorted(all_terminal_states)):
        if state in terminal_states:
            if first_row_b[j].denominator == lcm:
                result[i] = first_row_b[j].numerator
            else:
                result[i] = first_row_b[j].numerator \
                            * (lcm // first_row_b[j].denominator)
            j += 1
        else:
            result[j] = 0

    result.append(lcm)
    return result


def main():
    print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))


if __name__ == '__main__':
    main()
