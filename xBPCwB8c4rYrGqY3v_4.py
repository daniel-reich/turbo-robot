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
  new_lst = [m * 100 for m in lst]
  i = int((new_lst[len(new_lst)-1]-new_lst[0])/len(new_lst))
  new_list = []
  new_list_int = []
  for c in new_lst:
    new_list_int.append(int(c))
  for n in range(new_list_int[0],new_list_int[len(new_list_int)-1],i):
    new_list.append(n)
  for w in new_list:
    if w not in new_list_int:
      if isinstance(lst[0], float):
        return w/100
      else:
        return(int(w/100))

