"""


A **fulcrum** of a list is an integer such that all elements to the left of it
and all elements to the right of it sum to the same value. Write a function
that finds the **fulcrum** of a list.

To illustrate:

    find_fulcrum([3, 1, 5, 2, 4, 6, -1]) ➞ 2
    // Since [3, 1, 5] and [4, 6, -1] both sum to 9

### Examples

    find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]) ➞ 4
    
    find_fulcrum([9, 1, 9]) ➞ 1
    
    find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]) ➞ 0
    
    find_fulcrum([8, 8, 8, 8]) ➞ -1

### Notes

  * If the fulcrum does not exist, return `-1` (see example #4).
  * Exclude the leftmost and rightmost elements when computing the fulcrum (it doesn't make sense to sum zero values).
  * If a list has multiple fulcrums, return the one that occurs first.

"""

def find_fulcrum(lst):
  l=lst
  n=len(l)
  pre=[0]*n
  suf=[0]*n
  pre[0]=l[0]
  suf[n-1]=l[n-1]
  for i in range(1,n,1):
    pre[i]=pre[i-1]+l[i]
  for j in range(n-2,-1,-1):
    suf[j]=suf[j+1]+l[j]
  for i in range(1,n,1):
    if pre[i]==suf[i]:
      return l[i]
  return -1

