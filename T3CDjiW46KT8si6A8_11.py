"""


Create a function that takes a list and returns the product of the largest and
second largest number.

### Examples

    product([2, 3, 1, -1, 2]) ➞ 6
    # 2 * 3 = 6
    
    product([-2, -2, -1, -1]) ➞ 2
    # -2 * - 1 = 2
    # Not 1, because you can only use -1 one time.
    
    product([8, 8, 8]) ➞ 64
    # 8 * 8 = 64
    # You can repeat here because there is only one value.
    
    product([2, 8, 8, 8]) ➞ 16
    # 2 * 8 = 16
    # Not 64, because you can only use 8 one time.

### Notes

  * Numbers in the list are all integers.
  * Numbers can be both positive or negative.

"""

def product(lst):
  meh = sorted(set(lst))
  return meh[-1]*meh[-2] if len(meh)>1 else meh[-1]**2

