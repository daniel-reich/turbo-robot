"""


A billboard is an `m * n` list, where each list element consists of either one
letter or a blank space. You are given a phrase and the billboard dimensions.
Create a function that determines whether you can place the complete phrase on
the billboard.

There are two rules:

  1. If there is a space between two words:
    * If they are on the same row, you must put a space.
    * If they are two different rows, the space is optional.
  2. You can only put COMPLETE words on a row.

To illustrate, `can_put("GOOD MORN", [2, 4])` should yield `True`, since while
there is a space between "GOOD" and "MORN", it's not needed since both words
are on separate rows.

    [
      ["G", "O", "O", "D"],
      ["M", "O", "R", "N"]
    ]

On the other hand `can_put("GOOD MORN", [1, 8])` should yield `False`. Since
both words reside in the first row, we require nine spots, and eight would
yield the incomplete phrase "GOOD MOR".

    [
      ["G", "O", "O", "D", "_", "M", "O", "R"]
    ]

We would also return `False` if we could not fit a word on a row. So
`can_put("GOOD MORN", [3,3])` should yield `False`, since we can only fit
"GOO" on the first row.

    [
      ["G", "O", "O"],
      ["D", "_", "M"],
      ["O", "R", "N"]
    ]
    
    # No good!

### Examples

    can_put("HEY JUDE", [2, 4]) ➞ True
    
    can_put("HEY JUDE", [1, 8]) ➞ True
    
    can_put("HEY JUDE", [1, 7]) ➞ False
    
    can_put("HEY JUDE", [4, 3]) ➞ False

### Notes

It is okay to leave extra empty spaces on one line if you cannot fit two words
with a space. For example, in a 5 x 5 billboard, you can put "BE" on the first
row and "HAPPY" on the second row.

"""

def can_put(t,d):
  p,q = 0,0
  for i in t.split():
    if len(i) > d[1]:
      return False
    if len(i)+p > d[1]:
      p = len(i)+1
      q += 1
    else:
      p += len(i)+1
  return q < d[0]
