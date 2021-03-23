"""


The ternary operator (sometimes called Conditional Expressions) in python is
an alternative to the if... else... statement.

It is written in the format:

    result_if_true if condition else result_if_false

Ternary operators are often more compact than multi-line `if` statements, and
are useful for simple conditional tests.

For example:

    is_nice = True
    
    # Using ternary operator.
    state = "nice" if is_nice else "not nice"
    
    # Equivalent code using multi-line if statements.
    if is_nice:
        state = "nice"
    else:
        state = "not nice"

Write a function that uses the ternary operator to return `"yeah"` if `b` is
`True`, and `"nope"` otherwise.

### Examples

    yeah_nope(True) ➞ "yeah"
    
    yeah_nope(False) ➞ "nope"

### Notes

N/A

"""

def yeahNope(b):
  return "yeah" if b else "nope"

