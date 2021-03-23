"""


Write a function that takes two numbers and returns if they should be added,
subtracted, multiplied or divided to get 24. If none of the operations can
give 24, return `None`.

### Examples

    operation(15, 9) ➞ "added"
    
    operation(26, 2) ➞ "subtracted"
    
    operation(11, 11) ➞ None

### Notes

  * Only integers are used as test input.
  * Numbers should be added, subtracted, divided or multiplied in the order they appear in the parameters.
  * The function should return either `"added"`, `"subtracted"`, `"divided"`, `"multiplied"` or `None`.

"""

def operation(a, b):
  return {a+b: "added", a-b: "subtracted", a*b: "multiplied", a/b: "divided"}.get(24)

