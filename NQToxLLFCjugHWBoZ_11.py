"""


Write a function that sorts a list of characters alphabetically in ascending
order **(a-z)** by the character at the **n-th character**.

### Examples

    sort_by_character(["az16", "by35", "cx24"], 2) ➞ ["cx24", "by35", "az16"]
    // By 2nd character: ["x", "y", "z"] is in alphabetical order.
    
    sort_by_character(["mayor", "apple", "petal"], 5) ➞ ["apple", "petal", "mayor"]
    # By 5th character: ["e", "l", "r"] is in alphabetical order
    
    sort_by_character(["mate", "team", "bade"], 3) ➞ ["team", "bade", "mate"]

### Notes

All inputs will be of same length.

"""

def sort_by_character(lst, n):
  a = []
  for x in lst:
    a.append(x[n-1])
  print(a)
  a.sort()
  print(a)
  b = []
  for x in a:
    for y in lst:
      if y[n-1] == x:
        b.append(y)
  print(b)
  return b

