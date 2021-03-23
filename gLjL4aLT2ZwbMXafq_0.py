"""


Find all swap pairs between two lists such that the sums of lists after the
swap are equal. The input is two lists of integers, not necessarily of the
same length. The output is a set of tuples `{(num_from_l1, num_from_l2), ..}`.
If there is no pair found return an empty set.

### Examples

    fair_swap([1, 1], [2, 2]) ➞ {(1, 2)}
    
    fair_swap([1, 2], [2, 3]) ➞ {(1, 2), (2, 3)}
    
    fair_swap([2], [1, 3]) ➞ {(2, 3)}
    
    fair_swap([2, 3, 4], [11, 4, 1]) ➞ set()

### Notes

N/A

"""

def fair_swap(l1, l2):
  swaps = set()
  l1_sum = sum(l1)
  l2_sum = sum(l2)
  for num1 in set(l1):
    for num2 in set(l2):
      if l1_sum - num1 + num2 == l2_sum - num2 + num1:
        swaps.add((num1, num2))
  return swaps

