"""


Create a function that checks if the sub-lists in a list adhere to the
specified pattern.

### Examples

    check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True
    
    check_pattern([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA") ➞ True
    
    check_pattern([[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]], "AABB") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA") ➞ True

### Notes

  * The length of the pattern will always be the same as the length of the (main) list.
  * The pattern does not necessarily have to be alphabetically ordered (see last example).

"""

def check_pattern(lst, pattern):
  lst = tuple(tuple(item) for item in lst)
  dict1, dict2 = {lst[i]:i for i in range(len(lst))},{l:i for i, l in enumerate(pattern)}
  lst1, lst2 = [dict1[ch] for ch in lst], [dict2[ch] for ch in pattern]
  return lst1 == lst2

