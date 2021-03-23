"""


Your function will get a list with a number sequence. However, one item will
be missing. It's your job to find out which one is not in the list.

To illustrate, given the list `[1, 3, 4, 5]`, `2` is missing so the output
must be `2`.

### Examples

    missing([1, 3, 4, 5]) ➞ 2
    
    missing([2, 4, 6, 8, 10, 14, 16]) ➞ 12
    
    missing([1.5, 2, 3]) ➞ 2.5

### Notes

  * The missing item will never be the smallest or largest number in the list.
  * In every list, exactly one item is missing.

"""

def missing(lst):
  lst2=[]
  a=min(lst[1]-lst[0],lst[-1]-lst[-2])
  for i in range(len(lst)-1):
    if lst[i+1]-lst[i]!=a:
      return lst[i]+a

