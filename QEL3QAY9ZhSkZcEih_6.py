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

## Use Bitwise Operator (% modulo operator disallowed.)
def is_odd(n):
    if n & 1 == 1:
        return 'Yes'
    else:
        return 'No'
  
​
## Use Regular Expression (% modulo operator disallowed.)
def is_even(n):
    import re
    if re.match(r"(-?\d*[02468]$)", str(n)):
        return 'Yes'
    else:
        return 'No'

