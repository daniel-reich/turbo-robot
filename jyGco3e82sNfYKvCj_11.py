"""


Create a function that takes an integer `n` and reverses it.

### Examples

    rev(5121) ➞ "1215"
    
    rev(69) ➞ "96"
    
    rev(-122157) ➞ "751221"

### Notes

  * This challenge is about using two operators that are related to division.
  * If the number is negative, treat it like it's positive.

"""

def rev(n):
  x = abs(n)
  y = str(x)
  rev = y[::-1]
  return rev

