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

def check_pattern(lst, pat):
  c1 = all([len({tuple(lst[i]) for i in range(len(lst)) if pat[i]==l})==1 for l in set(pat)])
  c2 = len({tuple({tuple(lst[i]) for i in range(len(lst)) if pat[i]==l}) for l in set(pat)})==len(set(pat))
  return c1 and c2

