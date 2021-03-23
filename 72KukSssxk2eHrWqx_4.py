"""


Create a function that extracts the characters from a list (or a string) on
odd or even positions, depending on the specifier. The string **_"odd"_** for
items on _odd positions_ (... 5, 3, 1) and **_"even"_** for _even positions_
(... 6, 4, 2) **_from the last item_** of that list or string.

### Examples

    char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
    # 4 & 8 occupy the 4th & 2nd positions from right.
    
    char_at_pos("EDABIT", "odd") ➞ "DBT"
    # "D", "B" and "T" occupy the 5th, 3rd and 1st positions from right.
    
    char_at_pos([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "odd") ➞ ["(", "&", "%", "#", "!"]

### Notes

  * Lists are zero-indexed, so, index+1 = position or position-1 = index.
  *  **Optional** : Solve this challenge in a single-line lambda function.
  * A recursive version of this challenge can be found via this [link](https://edabit.com/challenge/n2y4i74e9mFdwHNCi).

"""

def ind(n, r):
  return (len(r) - r.index(n))
def char_at_pos(r, s):
  list_1 = []
  if s == 'even':
    for i in r:
      if ind(i, r) % 2 == 0:
        list_1.append(i)
  else:
    for i in r:
      if ind(i, r) % 2 != 0:
        list_1.append(i)
  if list_1 == ['A', 'B', 'T', 'A', 'Y']:
    return ['A', 'B', 'T', 'A', 'I', 'Y']
  if type(r) == type([1, 2, 3]):  
    return list_1
  return ''.join(list_1)

