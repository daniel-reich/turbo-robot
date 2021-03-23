"""


Maxie is the largest number that can be obtained by **swapping two digits** ,
Minnie is the smallest. Write a function that takes a number and returns Maxie
and Minnie. Leading zeros are not permitted.

### Examples

    maxmin(12340) ➞ (42310, 10342)
    
    maxmin(98761) ➞ (98761, 18769)
    
    maxmin(9000) ➞ (9000, 9000)
    # Sometimes no swap needed.
    
    maxmin(11321) ➞ (31121, 11123)

### Notes

N/A

"""

def maxmin(n):
  ns = [n] + [int(swap(list(str(n)), i, j)) for i in range(len(str(n))) for j in range(i)]
  ns = [x for x in ns if len(str(x)) == len(str(n))]
  return max(ns), min(ns)
def swap(L, i, j):
  L[i], L[j] = L[j], L[i]
  return "".join(L)

