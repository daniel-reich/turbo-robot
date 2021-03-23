"""


Given two non-empty lists, write a function that determines whether the second
list is a subsequence of the first list.

For instance, the numbers `[1, 3, 4]` form a subsequence of the list `[1, 2,
3, 4]`, and so do the numbers `[2, 4]`.

### Examples

    is_valid_subsequence([1, 1, 6, 1],[1, 1, 1, 6]) ➞ False
    
    is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]) ➞ True
    
    is_valid_subsequence([1, 2, 3, 4], [2, 4]) ➞ True

### Notes

N/A

"""

def is_valid_subsequence(array, sequence):
  seqindex = 0
  for i in array:
    if seqindex == len(sequence):
         break
    if sequence[seqindex] == i:
      seqindex+=1
  return seqindex == len(sequence)

