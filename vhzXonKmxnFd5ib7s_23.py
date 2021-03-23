"""


Create a function that multiplies two matrices (n x m) and (p x q) and
returns:

  * `"invalid"` if the matrices are not multiplicable (i.e. if m is not equal to p).
  * The multiplication matrix (n x q) otherwise.

### Examples

    matrix_multiply([[1, 2]], [[3], [4]]) ➞ [[11]]
    
    matrix_multiply([[0, 0], [0, 1]], [[1, 2], [3, 4], [5, 6]]) ➞ "invalid"
    
    matrix_multiply([[4, 2], [3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]

### Notes

This challenge is a generalized version of [Matrix
Multiplication](https://edabit.com/challenge/dfep4NR2twAFTdt9k).

"""

def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0]);
    rows_b, cols_b = len(b), len(b[0]);
    if cols_a != rows_b:
        return 'invalid';
​
    result_matrix = []
    
    for r in range(rows_a):
        result_row = []
        for c in range(cols_b):
            row_vals = a[r]
            col_vals = [row[c] for row in b]
            s = sum([l * r for l,r in zip(row_vals, col_vals)])
            result_row.append(s)
        result_matrix.append(result_row)
    return result_matrix

