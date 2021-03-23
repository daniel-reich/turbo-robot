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
  if (sum(l1) + sum(l2)) % 2 == 1:
    return set()
  avg = (sum(l1) + sum(l2))//2
  pair2 = lambda x: avg - (sum(l1)-x)
  pairs = [(el,pair2(el)) for el in list(set(l1)) if pair2(el) in l2]
  sorted_pairs = sorted(pairs)
  return set(sorted_pairs)

