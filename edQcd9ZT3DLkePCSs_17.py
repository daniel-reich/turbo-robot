"""


Given a list and an integer `n`, return the sum of the first `n` numbers in
the list.

### Worked Example

    sum_first_n_nums([9, 8, 7, 6], 3) ➞ 24
    # The parameter n is specified as 3.
    # The first 3 numbers in the list are 9, 8 and 7.
    # The sum of these 3 numbers is 24 (9 + 8 + 7).
    # Return the answer.

### Examples

    sum_first_n_nums([1, 3, 2], 2) ➞ 4
    
    sum_first_n_nums([4, 2, 5, 7], 4) ➞ 18
    
    sum_first_n_nums([3, 6, 2], 0) ➞ 0

### Notes

If `n` is larger than the length of the list, return the sum of the whole
list.

"""

def sum_first_n_nums(lst, n):
  return sum(lst[0:n])

