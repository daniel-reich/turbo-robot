"""


Imagine a messaging device with only one button. For the letter **A** , you
press the button **one time** , for **E** , you press it **five times** , for
**G** , it's pressed **seven times** , etc, etc.

Write a function that takes a string (the message) and returns the total
number of times the button is pressed.

### Examples

    how_many_times("abde") ➞ 12
    
    how_many_times("azy") ➞ 52
    
    how_many_times("qudusayo") ➞ 123

### Notes

  * Ignore spaces.
  * The given string argument will be in lower case.

"""

import string
def how_many_times(msg):
  dicto = {}
  total = 0 
  num = 0
  asc = list(list(string.ascii_lowercase))
  for x in range(1,27):
    dicto[asc[num]] = x
    num += 1 
  for a in msg:
    total += dicto[a]
  return total

