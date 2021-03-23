"""


In this challenge, you must verify the equality of two different values given
the parameters `a` and `b`.

Both the _value_ and _type_ of the parameters need to be equal. The possible
types of the given parameters are:

  * Numbers
  * Strings
  * Booleans (`False` or `True`)
  * Special values: `None`

What have you learned so far that will permit you to do two different checks
(value **and** type) with a single statement?

Implement a function that returns `True` if the parameters are equal, and
`False` if they are not.

### Examples

    check_equality(1, true) ➞ False
    # A number and a boolean: the value and type are different.
    
    check_equality(0, "0") ➞ False
    # A number and a string: the type is different.
    
    check_equality(1,  1) ➞ True
    # A number and a number: the type and value are equal.

### Notes

  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

check_equality=lambda a,b:type(a)==type(b)and a==b

