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
  solutionOdd = []
  solutionEven = []
  if s == "odd":
    for i in range(0,len(r),2):
      solutionOdd.append(r[i])
    if type(r) == str: 
      return "".join(solutionOdd)
    else:
      return solutionOdd
  else: 
    for i in range(1,len(r),2):
      solutionEven.append(r[i])
    if type(r) == str: 
      return "".join(solutionEven)
    else:
      return solutionEven

