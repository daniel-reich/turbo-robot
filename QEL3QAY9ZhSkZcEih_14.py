"""


Create two functions:

  1. The first is `is_odd()` to check if a given number is odd using **bitwise operator**.
  2. The second is `is_even()` to check if a given input is even using **regular expressions**.

Use of `%` operator is disallowed.

### Examples

    is_odd(3) ➞ "Yes"
    # Use Bitwise Operator
    
    is_odd(58) ➞ "No"
    # Use Bitwise Operator
    
    is_even("0") ➞ "Yes"
    # Use Regular Expression
    
    is_even("-99") ➞ "No"
    # Use Regular Expression

### Notes

  * Input will only be integers (positive/negative/zero).
  * For the second function, input will be numbers in string.
  * For more info on regular expressions, check the **Resources** tab.

"""

import re
​
def is_odd(n):
  return "Yes" if n^1==n-1 else "No"
​
def is_even(n):
  return "Yes" if re.search("[13579]$", n) is None else "No"

