"""


Write a **sudoku validator**. This function should return `True` if the 2-D
array represents a valid sudoku and `False` otherwise. To be a valid sudoku:

  1. Each row must have the digits from 1 to 9 exactly once.
  2. Each column must have the digits from 1 to 9 exactly once.
  3. Each 3x3 box must have the digits from 1 to 9 exactly once.

### Examples

    sudoku_validator([
      [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
      [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
      [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
      [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
      [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
      [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
      [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
      [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
      [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
    ]) ➞ True
    
    sudoku_validator([
      [ 1, 1, 2, 4, 8, 9, 3, 7, 6 ],
      [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
      [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
      [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
      [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
      [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
      [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
      [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
      [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
    ]) ➞ False

### Notes

N/A

"""

def sudoku_validator(lst: list) -> bool:
    k, box_score = len(lst), sum(range(1, 10))
    # checking rows
    if sum(0 if len(set(i)) != k or sum(i) != box_score else 1 for i in lst) != k:
        return False
​
    # checking columns
    transformed = list(zip(*lst))
    if sum(0 if len(set(i)) != k or sum(i) != box_score else 1 for i in transformed) != k:
        return False
​
    # checking boxes 3x3
    n = k // 3
    for i in range(n):
        for j in range(n):
            sub_L = []
            sub_L.extend(lst[3*i][3*j:3*(j+1)])
            sub_L.extend(lst[3 *i+1][3*j:3*(j + 1)])
            sub_L.extend(lst[3 *i+2][3 * j:3*(j + 1)])
            if sum(sub_L) != box_score:
                return False
    return True

