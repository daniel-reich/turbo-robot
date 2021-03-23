"""


Create a function that always returns `True` for every item in a given list.
However, if an element is the word `"flick"`, switch to always returning the
opposite boolean value.

### Examples

    flick_switch(["edabit", "flick", "eda", "bit"]) ➞ [True, False, False, False]
    
    flick_switch(["flick", 11037, 3.14, 53]) ➞[False, False, False, False]
    
    flick_switch([False, False, "flick", "sheep", "flick"]) ➞ [True, True, False, False, True]

### Notes

  * `"flick"` will always be given in lowercase.
  * A list may contain multiple flicks.
  * Switch the boolean value on the same element as the flick itself.

"""

def flick_switch(lst):
  r = []
  s = True
  for x in lst:
    if x == "flick":
      s = not s
    r.append(s)
  return r

