"""


A "truthy" value is a value that translates to `True` when evaluated in a
Boolean context. All values are truthy unless they're defined as falsy.

All falsy values are as follows:

  * `False`
  * `None`
  * `0`
  * `[]`
  * `{}`
  * `""`

Create a function that takes an argument of any data type and returns `1` if
it's truthy and `0` if it's falsy.

### Examples

    is_truthy(0) ➞ 0
    
    is_truthy(False) ➞ 0
    
    is_truthy("") ➞ 0
    
    is_truthy("False") ➞ 1

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

is_truthy=lambda v:(0,1)[bool(v)]

