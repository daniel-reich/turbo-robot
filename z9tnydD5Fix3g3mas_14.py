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

def check_pattern(lst,pat):
 dic=[(j,i) for i,j in zip(lst,pat)]
 if len([i for i in lst if lst.count(i)>1]) == len([i for i in pat if pat.count(i)>1]):
    if len([i for i in dic if dic.count(i)>1]) == len([i for i in pat if pat.count(i)>1]):
     return all([i for i in dic if dic.count(i)>1])
    else:
     return len([i for i in pat if pat.count(i)>1])==0
 else:
     return False

