"""


Make a function that takes a integer, `size`, returns 2D list that is a Magic
Square with side lengths of `size`

A Magic Square is an arrangement of numbers in a square in such a way that the
sum of each row, column, and diagonal is one constant number, the "magic
constant." For this challenge I will be testing with the assumption that your
magic squares are made with whole numbers from 1 - n^2

### Example

    make_magic(3) ➞ [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    # Rows: 2+7+6 = 9+5+1 = 4+3+8 = 15
    # Columns: 2+9+4 = 7+5+3 = 6+1+8 = 15
    # Diagonals: 2+5+8 = 6+5+4 = 15

### Notes

For this challenge I will only be testing with sizes >= 3 as there are no
Magic Squares of size 2 at least as I have described them.

"""

def odd_magic(start, size):
    res = [[0] * size for _ in range(size)]
    r, c = 0, size // 2
    res[r][c] = start
    for i in range(start + 1, size * size + start):
        r_new = (r - 1) % size
        c_new = (c + 1) % size
        if res[r_new][c_new]:
            r_new = (r + 1) % size
            c_new = c
        res[r_new][c_new] = i
        r, c = r_new, c_new
    return res
​
def make_magic(n):
    if n % 2:
        res = odd_magic(1, n)
    elif not n % 2 and n % 4:
        q_size = n // 2
        q_square = q_size * q_size
        a = odd_magic(1, q_size)
        b = odd_magic(1 + q_square, q_size)
        cc = odd_magic(1 + 2 * q_square, q_size)
        d = odd_magic(1 + 3 * q_square, q_size)
        left_swap_len = q_size // 2
        for r in range(q_size):
            if r == q_size // 2:
                for c in range(1, left_swap_len + 1):
                    a[r][c], d[r][c] = d[r][c], a[r][c]
            else:
                for c in range(left_swap_len):
                    a[r][c], d[r][c] = d[r][c], a[r][c]
        right_swap_len = left_swap_len - 1
        if right_swap_len:
            for r in range(q_size):
                for c in range(q_size - right_swap_len, q_size):
                    b[r][c], cc[r][c] = cc[r][c], b[r][c]
        res = []
        for r in range(q_size):
            res.append(a[r][:] + cc[r][:])
        for r in range(q_size):
            res.append(d[r][:] + b[r][:])
    else:
        q_s = n // 4
        val = 0
        res = [[0] * n for _ in range(n)]
        subs = []
        for r in range(n):
            for c in range(n):
                val += 1
                if ((r < q_s and c < q_s) or
                    (r < q_s and c >= 3 * q_s) or
                    (q_s <= r < 3 * q_s and q_s <= c < 3 * q_s) or
                    (r >= 3 * q_s and c < q_s) or
                    (r >= 3 * q_s and c >= 3 * q_s)):
                    res[r][c] = val
                else:
                    subs.append(val)
        subs = subs[::-1]
        idx_sub = -1
        for r in range(n):
            for c in range(n):
                if not ((r < q_s and c < q_s) or
                        (r < q_s and c >= 3 * q_s) or
                        (q_s <= r < 3 * q_s and q_s <= c < 3 * q_s) or
                        (r >= 3 * q_s and c < q_s) or
                        (r >= 3 * q_s and c >= 3 * q_s)):
                    idx_sub += 1
                    res[r][c] = subs[idx_sub]
    return res

