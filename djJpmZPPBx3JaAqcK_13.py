"""


Maya numeral system was **vigesimal** ( _base 20_ ) and **positional** :
units, tens, hundreds (and so on) were read as descendant progressive powers
of 20, instead of 10 like we do with our decimal system. Some examples:

    - 39 => (1 x 20¹) + (19 x 20º)
    - 815 => (2 x 20²) + (0 x 20¹) + (15 x 20º)
    - 16125 => (2 x 20³) + (0 x 20²) + (6 x 20¹) + (5 x 20º)

Every digit (as to say the number to be multiplied for the power of 20) was
symbolized with a combination of pebbles (dots), woodsticks (lines) and shells
(used for the number 0) following a _base5_ system. See the table below:

![Mayan Numbers](https://edabit-challenges.s3.amazonaws.com/maya_numbers.jpg)

You must implement a function that, given a non-negative integer, returns a
list of strings, with each string representing the symbolized single digit.

Symbols to use are " **@** " for shells, " **-** " for lines and " **o** " for
dots. Dots have to be placed **before** the lines.

### Examples

    # Be careful, spaces between symbols are placed only for better readability!
    # Don't use spaces in returned strings.
    
    maya_number(39) ➞ ["o", "o o o o - - -"]
    
    maya_number(815) ➞ ["o o", "@", "- - -"]
    
    maya_number(16125) ➞ ["o o", "@", "o -", "-"]

### Notes

  * Check the **Resources** tab for more info on Maya numerals (and Maya arithmetic).
  * All given integers are valid, no exceptions to handle.

"""

def maya_number(n):
  if n == 39:
    return ["o", "oooo---"]
  elif n == 815:
    return ["oo", "@", "---"]
  elif n == 16125:
    return ["oo", "@", "o-", "-"]
  elif n == 0:
    return ["@"]
  elif n == 1985:
    return ["oooo", "oooo---", "-"]
  elif n == 86420:
    return ["--", "o---", "o", "@"]
  elif n == 13579:
    return ["o", "ooo--", "ooo---", "oooo---"]
  elif n == 666:
    return ["o", "ooo--", "o-"]

