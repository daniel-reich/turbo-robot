"""


Create a function that takes an integer `n` and returns **multiplication
table** of 1 to `n` numbers up to `n`th multiple.

### Examples

    mult_table(2) ➞ [
      [1, 2],
      [2, 4]
    ]
    
    mult_table(3) ➞ [
      [1, 2, 3],
      [2, 4, 6],
      [3, 6, 9]
    ]
    
    mult_table(5) ➞ [
      [1, 2, 3, 4, 5],
      [2, 4, 6, 8, 10],
      [3, 6, 9, 12, 15],
      [4, 8, 12, 16, 20],
      [5, 10, 15, 20, 25]
    ]

### Notes

N/A

"""

def mult_table(n):
  t = [list(range(1, n+1))]
  # for x in range(2, n+1):
    # l = [x]
    # for y in t[0][1:]:
      # l += [x * y]
    # t += [l]
  # return t
  
  return t + [[x] + [y * x for y in t[0][1:]] for x in range(2, n+1)]
