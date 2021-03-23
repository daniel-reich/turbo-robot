"""


Python has a logical operator `and`. The `and` operator takes two boolean
values, and returns `True` if both values are `True`.

Consider `a and b`:

  * `a` is checked if it is `True` or `False`.
  * If `a` is `False`, `False` is returned.
  * `b` is checked if it is `True` or `False`.
  * If `b` is `False`, `False` is returned.
  * Otherwise, `True` is returned (as both `a` and `b` are therefore `True` ).

The `and` operator will only return `True` for `True and True`.

Make a function using the `and` operator.

### Examples

    And(True, False) ➞ False
    
    And(True, True) ➞ True
    
    And(False, True) ➞ False
    
    And(False, False) ➞ False

### Notes

N/A

"""

def And(a, b):
  return (a and b)

