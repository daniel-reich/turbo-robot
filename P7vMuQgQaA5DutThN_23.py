"""


Given a list of numbers, negate all elements contained within.

  * Negating a positive value `-+n` will return `-n`, because all `+`'s are removed.
  * Negating a negative value `--n` will return `n`, because the first `-` turns the second minus into a `+`.

### Examples

    negate([1, 2, 3, 4]) ➞ [-1, -2, -3, -4]
    
    negate([-1, 2, -3, 4]) ➞ [1, -2, 3, -4]
    
    negate([]) ➞ []

### Notes

If you get an empty list, return an empty list: `[]`

"""

def negate(lst):
  return [-i for i in lst]

