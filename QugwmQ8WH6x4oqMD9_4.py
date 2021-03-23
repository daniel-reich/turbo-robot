"""


Create a function that takes four lists as arguments and returns a count of
the total number of identical lists.

### Examples

    count_identical_lists([0, 0, 0], [0, 1, 2], [0, 0, 0], [2, 1, 0]) ➞ 2
    
    count_identical_lists([0, 1, 0], [0, 1, 2], [0, 2, 0], [2, 1, 0]) ➞ 0
    
    count_identical_lists([0, 1, 2], [0, 1, 2], [0, 1, 2], [2, 1, 0]) ➞ 3

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're really stuck, unlock solutions in the **Solutions** tab.

"""

count_identical_lists=lambda*l:sum(l.count(e)>1for e in l)

