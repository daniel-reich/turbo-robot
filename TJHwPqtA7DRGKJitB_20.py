"""


In probability theory, a _probability matrix_ is a matrix such that:

  * The matrix is a square matrix (same number of rows as columns).
  * All entries are probabilities, i.e. numbers between 0 and 1.
  * All rows add up to 1.

The following is an example of a probability matrix:

    [
      [0.5, 0.5, 0.0],
      [0.2, 0.5, 0.3],
      [0.1, 0.2, 0.7]
    ]

Note that though all rows add up to 1, there is no restriction on the columns,
which may or may not add up to 1.

Write a function that determines if a matrix is a probability matrix or not.

### Examples

    is_prob_matrix([
      [0.5, 0.5, 0.0],
      [0.2, 0.5, 0.3],
      [0.1, 0.2, 0.7]
    ]) ➞ True
    
    is_prob_matrix([
      [0.5, 0.5, 0.0],
      [0.2, 0.5, 0.3]
    ]) ➞ False
    
    # Not a square matrix.
    
    is_prob_matrix([
      [2, -1],
      [-1, 2]
    ]) ➞ False
    
    # Entries not between 0 and 1.
    
    is_prob_matrix([
      [0, 1],
      [1, 0]
    ]) ➞ True
    
    is_prob_matrix([
      [0.5, 0.4],
      [0.5, 0.6]
    ]) ➞ False
    
    # Rows do not add to 1.

### Notes

Fun fact: for most probability matrices M (for example, if M has no zero
entries), the matrix powers M^n converge (as n increases) to a matrix where
_all rows are identical_.

"""

def is_prob_matrix(arr):
​
    condition_1 = True
    for raw in arr:
      if len(raw) != len(arr):
        condition_1 = False
        break
​
    condition_2 = True
    for raw in arr:
      for item in raw:
        if item < 0 or item > 1:
          condition_2 = False
          break
​
    condition_3 = True
    for raw in arr:
      if sum(raw) != 1:
        condition_3 = False
        break
​
    if condition_1 is True and condition_2 is True and condition_3 is True:
      return True
    else:
      return False

