"""


An **ice cream sandwich** is a string that is formed by two identical ends and
a different middle.

#### Some examples of ice cream sandwiches:

    "AABBBAA"
    
    "3&&3"
    
    "yyyyymmmmmmmmyyyyy"
    
    "hhhhhhhhmhhhhhhhh"

Notice how **left** and **right** ends of the sandwich are identical in both
**length** and in **repeating character** ). The **middle** section is
distinctly different.

#### Not ice cream sandwiches:

    "BBBBB"
    // You can't have just plain icecream.
    
    "AAACCCAA"
    // You can't have unequal sandwich ends.
    
    "AACDCAA"
    // You can't have more than one filling.
    
    "A"
    // You can't have fewer than 3 characters.

Write a function that returns `True` if a string is an **ice cream sandwich**
and `False` otherwise.

### Examples

    is_icecream_sandwich("CDC") ➞ True
    
    is_icecream_sandwich("AAABB") ➞ False
    
    is_icecream_sandwich("AA") ➞ False

### Notes

An ice cream sandwich must have a **minimum length of 3 characters** , and at
least **two of these characters must be distinct** (you can't only have the
filling!).

"""

import numpy as np
def is_icecream_sandwich(txt):
  text = np.unique([x for x in txt])
  if len(txt) < 3:
    return False
  elif len(text) != 2:
    return False
  elif txt[0] != txt[-1]:
    return False
  elif txt == txt[::-1]:
    return True
  else:
    return False

