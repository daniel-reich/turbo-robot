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
  if not lst: return []
  a = [True if lst[0]!="flick" else False]
  b = lst[1:]
  while b:
      if b[0]=="flick":
          a.append(not a[-1])
      else:
          a.append(a[-1])
      b.pop(0)
  return a

