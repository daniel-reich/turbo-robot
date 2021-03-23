"""


Create a function that takes an array of numbers, and returns the size of the
biggest square patch of odd numbers. See examples for a clearer picture.

### Examples

    odd_square_patch([
      [1, 2, 4, 9],
      [4, 5, 5, 7],
      [3, 6, 1, 7]
    ]) ➞ 2
    
    # The 2x2 square at the lower right
    # ([5, 7] on the 2nd row, [1, 7] on the third).
    
    odd_square_patch([[1, 2, 4, 9]]) ➞ 1
    
    # An array with a single row can only have a square patch of
    # maximum size 1x1 containing a single odd element.
    
    odd_square_patch([[2, 4, 6]]) ➞ 0

### Notes

N/A

"""

def odd_square_patch(lst): 
    mss = -float('inf')
    for i, x in enumerate(lst):
        indexes, start, count = [], 0, 0
​
        for ind, num in enumerate(x):
            if not num % 2:
                start = ind + 1
                count = 0 
            else:
                count += 1
                indexes.extend([(a, b) for a, b in enumerate(range(count, 0, -1), start) if i + b - 1 < len(lst)])
​
        for a, b in indexes:
            if all(all(item % 2 for item in lst[i+r][a:a+b]) for r in range(b)):
                mss = max(mss, b)
                        
    return max(mss, 0)

