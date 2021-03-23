"""
Write a function that accepts the width and height (`m, n`) and an optional
**proc** `s` and generates a list with `m` elements. Each element is a string
consisting of either:

  * The default character (hash `#`) repeating `n` times (if no **proc** is given).
  * The character passed in through the proc repeating `n` times.

### Examples

    make_rug(3, 5) ➞ [
      "#####",
      "#####",
      "#####"
    ]
    
    make_rug(3, 5, '$')  ➞ [
      "$$$$$",
      "$$$$$",
      "$$$$$"
    ]
    
    make_rug(2, 2, 'A')  ➞ [
      "AA"
      "AA"
    ]

### Notes

You can set a value for the parameter when creating the function e.g. `def
func(x = 3)`

"""

def make_rug(m, n, s="#"):
  return [s * n for x in range(m)]

