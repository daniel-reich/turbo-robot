"""


Create a function that returns the characters from a list or string `r` on odd
or even positions, depending on the specifier `s`. The specifier will be
**"odd"** for items on _odd positions_ (1, 3, 5, ...) and **"even"** for items
on _even positions_ (2, 4, 6, ...).

### Examples

    char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
    # 4 & 8 occupy the 2nd & 4th positions
    
    char_at_pos("EDABIT", "odd") ➞ "EAI"
    # "E", "A" and "I" occupy the 1st, 3rd and 5th positions
    
    char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd") ➞ ["A", "B", "T", "A", "I", "Y"]

### Notes

  * Lists are zero-indexed, so, index+1 = position or position-1 = index.
  * There will not be an empty string or an empty list.
  * ( **Optional** ) Try solving this challenge in a single-line lambda function.
  * A more advanced version of this challenge can be [found here](https://edabit.com/challenge/72KukSssxk2eHrWqx).

"""

def char_at_pos(r, s):
  if isinstance(r, list):
    arr = list()
    if s == "odd":
      for i in range(len(r)):
        if (i+1) % 2 != 0:
          arr.append(r[i])
    elif s == "even":
      for i in range(len(r)):
        if (i+1) % 2 == 0:
          arr.append(r[i])
    return arr
  else:
    stri = ' '
    if s == "odd":
      for i in range(len(r)):
        if (i+1) % 2 != 0:
          stri += r[i]
    elif s == "even":
      for i in range(len(r)):
        if (i+1) % 2 == 0:
          stri += r[i]
    return stri.strip()

